"""Deterministic educational rules for synthetic energy-device event notes."""

from .model import tokenize

RULES = {
    "normal": {"normal", "stabil", "lancar", "teratur", "konsisten", "sesuai", "valid"},
    "warning": {"lonjakan", "meningkat", "fluktuasi", "berlebih", "anomali", "peringatan", "ambang"},
    "fault": {"offline", "gagal", "rusak", "kerusakan", "putus", "error", "terputus", "berhenti"},
}


def classify_by_rules(text: str) -> str:
    """Use keyword votes. Ambiguous/no-match events require human review."""
    words = set(tokenize(text))
    scores = {label: len(words & keywords) for label, keywords in RULES.items()}
    peak = max(scores.values())
    winners = [label for label, value in scores.items() if value == peak]
    return winners[0] if peak > 0 and len(winners) == 1 else "abstain"
