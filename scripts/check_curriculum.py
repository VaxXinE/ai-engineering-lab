"""Validate course documents and local Markdown links (Python 3.11+; stdlib only)."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
MODULES = [
    "01-ai-fundamentals", "02-technology-assessment", "03-data-ingestion",
    "04-data-validation", "05-data-structures", "06-ux-design",
    "07-ui-implementation", "08-database-design", "09-software-architecture",
    "10-scalability", "11-model-evaluation", "12-ai-integration",
    "13-ai-installation", "14-maintenance-planning",
    "15-maintenance-execution", "16-assessment",
]
REQUIRED = ("README.md", "theory.md", "lab-guide.md", "exercises.md", "assessment.md")
MD_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+[\"'][^\"']+[\"'])?\)")
FENCE = re.compile(r"^\s*(?:~{3}|\x60{3})")


def check() -> list[str]:
    errors: list[str] = []
    for folder in MODULES:
        module_path = ROOT / "learning" / f"week-{folder}"
        for filename in REQUIRED:
            target = module_path / filename
            if not target.is_file():
                errors.append(f"Missing module: {target.relative_to(ROOT)}")

    for path in sorted(ROOT.rglob("*.md")):
        if any(name in {".git", "node_modules", ".venv", ".next"} for name in path.parts):
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        fence_lines = sum(bool(FENCE.match(line)) for line in lines)
        if fence_lines % 2:
            errors.append(f"Unbalanced code fences: {path.relative_to(ROOT)}")
        outside_fence: list[str] = []
        inside = False
        for line in lines:
            if FENCE.match(line):
                inside = not inside
                continue
            if not inside:
                outside_fence.append(line)
        for match in MD_LINK.finditer("\n".join(outside_fence)):
            raw = match.group(1)
            if raw.startswith(("#", "mailto:", "data:")):
                continue
            parsed = urlparse(raw)
            if parsed.scheme or parsed.netloc or raw.startswith("//"):
                continue
            relative = unquote(parsed.path)
            if not relative:
                continue
            target = (path.parent / relative).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"Link escapes repository: {path.relative_to(ROOT)} -> {raw}")
                continue
            if not target.exists():
                errors.append(f"Broken link: {path.relative_to(ROOT)} -> {raw}")
    return errors


if __name__ == "__main__":
    issues = check()
    for issue in issues:
        print(f"ERROR: {issue}", file=sys.stderr)
    if issues:
        print(f"{len(issues)} curriculum checks failed.", file=sys.stderr)
        raise SystemExit(1)
    print("Curriculum OK: 16 modules complete; internal Markdown links and fences checked.")
