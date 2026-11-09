"""Static curriculum contract checks; not an AI application."""
from __future__ import annotations

import csv
import io
import math
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COLUMNS = (
    "site_id", "meter_id", "source_event_id", "interval_start_utc",
    "interval_minutes", "energy_kwh", "voltage_v", "current_a",
)
CONTRACT = Path("docs/architecture/energy-data-contract.md")
FORBIDDEN = re.compile(
    r"\bInquir(?:y|ies)\b|\bInquiryCreate\b|\bEventNote\b|"
    r"\bevent_note\b|\breceived_at\b|/meter readings\b|"
    r"UNIQUE\(\s*tenant_id\b|\b77\.78%",
    re.IGNORECASE,
)
MODULES = (
    "03-data-ingestion", "04-data-validation", "05-data-structures",
    "06-ux-design", "07-ui-implementation", "08-database-design",
    "09-software-architecture", "10-scalability", "11-model-evaluation",
    "12-ai-integration",
)


def validate_row(row: dict[str, str]) -> None:
    if set(row) != set(COLUMNS) or any(v is None or not v.strip() for v in row.values()):
        raise ValueError("Invalid canonical columns or missing value")
    if int(row["interval_minutes"]) != 15:
        raise ValueError("Expected exactly 15-minute interval")
    dt = datetime.fromisoformat(row["interval_start_utc"].replace("Z", "+00:00"))
    if dt.utcoffset() != timedelta(0) or dt.minute % 15 or dt.second or dt.microsecond:
        raise ValueError("Timestamp must be UTC and aligned to 15 minutes")
    for key in ("energy_kwh", "voltage_v", "current_a"):
        value = float(row[key])
        if not math.isfinite(value) or value < 0:
            raise ValueError("Invalid numeric: " + key)


def read_csv_example(text: str) -> list[dict[str, str]]:
    fence = chr(96) * 3
    pattern = re.escape(fence) + r"csv\s*\n(.*?)\n" + re.escape(fence)
    match = re.search(pattern, text, re.DOTALL)
    if not match:
        raise ValueError("Missing fenced CSV example")
    reader = csv.DictReader(io.StringIO(match.group(1)))
    if tuple(reader.fieldnames or ()) != COLUMNS:
        raise ValueError("CSV header does not match canonical contract")
    rows = list(reader)
    if not rows:
        raise ValueError("Empty CSV example")
    for row in rows:
        validate_row(row)
    return rows


def energy_to_average_kw(kwh: float, minutes: int) -> float:
    if not math.isfinite(kwh) or kwh < 0 or minutes <= 0:
        raise ValueError("Invalid energy or duration")
    return kwh / (minutes / 60)


def check(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    path = root / CONTRACT
    if not path.is_file():
        return ["Missing canonical energy contract"]
    body = path.read_text(encoding="utf-8")
    for fragment in ("UNIQUE (site_id, meter_id, source_event_id)", "interval_start_utc", "interval_minutes", "scoring_unavailable"):
        if fragment not in body:
            errors.append("Canonical contract missing: " + fragment)
    try:
        rows = read_csv_example(body)
        keys = [(r["site_id"], r["meter_id"], r["source_event_id"]) for r in rows]
        if len(set(keys)) != len(keys):
            errors.append("Duplicate composite event keys in example")
    except (ValueError, TypeError) as exc:
        errors.append("Bad canonical CSV example: " + str(exc))

    for rel in ("docs/domain-casebook.md", "datasets/synthetic/README.md",
                "projects/ai-energy-intelligence/docs/requirements.md"):
        p = root / rel
        if not p.is_file():
            errors.append("Missing: " + rel)
        else:
            txt = p.read_text(encoding="utf-8")
            if not all(key in txt for key in ("interval_start_utc", "interval_minutes", "energy_kwh")):
                errors.append("Outdated schema reference: " + rel)

    for module in MODULES:
        for filename in ("theory.md", "deep-dive.md", "lab-guide.md", "worked-examples.md"):
            p = root / "learning" / ("week-" + module) / filename
            if not p.is_file():
                errors.append("Missing: " + str(p.relative_to(root)))
                continue
            txt = p.read_text(encoding="utf-8")
            for match in FORBIDDEN.finditer(txt):
                number = txt.count("\n", 0, match.start()) + 1
                errors.append(f"Old schema/terminology {p.relative_to(root)}:{number}: {match.group()}")
    return errors


if __name__ == "__main__":
    problems = check()
    for problem in problems:
        print("ERROR:", problem, file=sys.stderr)
    if problems:
        raise SystemExit(1)
    print("Energy data/lesson schema integrity: OK")
