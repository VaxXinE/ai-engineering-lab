"""Read and validate small, deliberately synthetic text-classification datasets."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

LABELS = ("normal", "warning", "fault")
MAX_TEXT_LENGTH = 500


@dataclass(frozen=True)
class Example:
    text: str
    label: str


def normalize_text(text: str) -> str:
    """Normalize whitespace and case for duplicate detection (not for storage)."""
    return " ".join(text.casefold().split())


def read_examples(path: Path) -> list[Example]:
    """Fail closed on invalid labels, bad schemas, empty fields, or duplicates."""
    examples: list[Example] = []
    seen: set[str] = set()
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != ["text", "label"]:
            raise ValueError("CSV columns must be exactly: text,label")
        for row_number, row in enumerate(reader, start=2):
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"Invalid CSV shape at row {row_number}")
            text = row["text"].strip()
            label = row["label"].strip()
            if not text or len(text) > MAX_TEXT_LENGTH:
                raise ValueError(f"Invalid text length at row {row_number}")
            if label not in LABELS:
                raise ValueError(f"Unknown label at row {row_number}: {label!r}")
            key = normalize_text(text)
            if key in seen:
                raise ValueError(f"Duplicate device event at row {row_number}")
            seen.add(key)
            examples.append(Example(text=text, label=label))
    if not examples:
        raise ValueError("Dataset is empty")
    return examples


def check_train_test_leakage(train: list[Example], test: list[Example]) -> None:
    """Reject exact normalized overlap between training and held-out evaluation."""
    training = {normalize_text(example.text) for example in train}
    overlap = training & {normalize_text(example.text) for example in test}
    if overlap:
        raise ValueError(f"Training/test leakage: {len(overlap)} duplicate text(s)")
