"""Check that current educational materials use the active energy-monitoring domain."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = [
    re.compile(r"\b" + "c" + "rm" + r"\b", re.I),
    re.compile("live" + r"[\s-]?" + "chat", re.I),
    re.compile("cus" + "tomer", re.I),
    re.compile("pelang" + "gan", re.I),
    re.compile("ai-" + "customer-" + "intelligence", re.I),
]

def check() -> list[str]:
    errors: list[str] = []
    for folder in ("README.md", "docs", "learning", "projects", "datasets", "certification"):
        target = ROOT / folder
        paths = [target] if target.is_file() else list(target.rglob("*"))
        for path in paths:
            if not path.is_file() or path.suffix.lower() not in {".md", ".py", ".csv", ".yml"}:
                continue
            content = path.read_text(encoding="utf-8")
            for pattern in PATTERNS:
                if match := pattern.search(content):
                    line = content.count("\n", 0, match.start()) + 1
                    errors.append(f"{path.relative_to(ROOT)}:{line}: stale domain reference")
    return errors

if __name__ == "__main__":
    failures = check()
    for item in failures:
        print("ERROR:", item, file=sys.stderr)
    if failures:
        raise SystemExit(1)
    print("Use-case text scan OK: energy-monitoring domain")
