"""Minimal CLI for train / inference / evaluation of the Week 01 baseline."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .dataset import MAX_TEXT_LENGTH, check_train_test_leakage, read_examples
from .metrics import evaluate
from .model import NaiveBayesClassifier
from .rules import classify_by_rules

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TRAIN = ROOT / "data" / "train.csv"
DEFAULT_TEST = ROOT / "data" / "test.csv"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Week 01: introductory AI classification lab")
    parser.add_argument("--train", type=Path, default=DEFAULT_TRAIN)
    subparsers = parser.add_subparsers(dest="command", required=True)

    predict_parser = subparsers.add_parser("predict", help="Classify one synthetic device event")
    predict_parser.add_argument("--text", required=True)
    eval_parser = subparsers.add_parser("evaluate", help="Evaluate on separate held-out CSV")
    eval_parser.add_argument("--test", type=Path, default=DEFAULT_TEST)
    args = parser.parse_args(argv)

    try:
        train = read_examples(args.train)
        model = NaiveBayesClassifier(train)
        if args.command == "predict":
            if len(args.text) > MAX_TEXT_LENGTH:
                raise ValueError("Maximum input size: 500 characters")
            result = model.predict(args.text)
            print(json.dumps({
                "label": result.label,
                "relative_score": round(result.relative_score, 4),
                "note": "relative_score is NOT a calibrated confidence or certainty",
            }, ensure_ascii=False, indent=2))
        else:
            test = read_examples(args.test)
            check_train_test_leakage(train, test)
            results = evaluate([example.label for example in test], [model.predict(example.text).label for example in test])
            results["rule_based_baseline"] = evaluate(
                [example.label for example in test],
                [classify_by_rules(example.text) for example in test],
            )
            print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError) as exc:
        # Do not echo raw device event text or whole rows in errors.
        print(f"Validation or file error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
