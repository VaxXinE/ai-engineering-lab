"""Hand-written decision rules: deterministic, requires no ML training."""

from .model import tokenize

RULES = {
    "sales": {"harga", "biaya", "beli", "membeli", "diskon", "langganan", "paket", "penawaran"},
    "support": {"error", "gagal", "bug", "gangguan", "masalah", "login", "password", "terkunci"},
    "general": {"alamat", "kantor", "kontak", "panduan", "profil", "faq", "informasi", "tutorial"},
}


def classify_by_rules(text: str) -> str:
    """Choose class with most keyword matches. Ties/no match fall back to general."""
    words = set(tokenize(text))
    scores = {label: len(words & keywords) for label, keywords in RULES.items()}
    best_score = max(scores.values())
    winners = [label for label, score in scores.items() if score == best_score]
    return winners[0] if len(winners) == 1 and best_score > 0 else "general"
