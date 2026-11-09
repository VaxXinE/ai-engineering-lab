"""Transparent per-class evaluation; never evaluate on training examples."""

from __future__ import annotations

from .dataset import LABELS


def evaluate(y_true: list[str], y_pred: list[str]) -> dict:
    if len(y_true) != len(y_pred) or not y_true:
        raise ValueError("Evaluation requires nonempty, equally sized arrays")
    if any(label not in LABELS for label in y_true) or any(label not in (*LABELS, "abstain") for label in y_pred):
        raise ValueError("Unknown class label in evaluation")
    matrix = {
        actual: {predicted: 0 for predicted in (*LABELS, "abstain")} for actual in LABELS
    }
    for actual, predicted in zip(y_true, y_pred):
        matrix[actual][predicted] += 1
    metrics = {}
    for label in LABELS:
        tp = matrix[label][label]
        fp = sum(matrix[actual][label] for actual in LABELS if actual != label)
        fn = sum(matrix[label][pred] for pred in (*LABELS, "abstain") if pred != label)
        precision = tp / (tp + fp) if (tp + fp) else 0.0
        recall = tp / (tp + fn) if (tp + fn) else 0.0
        f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) else 0.0
        metrics[label] = {
            "precision": round(precision, 4),
            "recall": round(recall, 4),
            "f1": round(f1, 4),
            "support": sum(matrix[label].values()),
        }
    return {
        "accuracy": round(sum(a == b for a, b in zip(y_true, y_pred)) / len(y_true), 4),
        "macro_f1": round(sum(metrics[label]["f1"] for label in LABELS) / len(LABELS), 4),
        "per_class": metrics,
        "confusion_matrix": matrix,
        "test_size": len(y_true),
        "abstention_count": y_pred.count("abstain"),
        "abstention_rate": round(y_pred.count("abstain") / len(y_true), 4),
    }
