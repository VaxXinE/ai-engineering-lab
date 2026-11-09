"""Educational bag-of-words Multinomial Naive Bayes, not a production model."""

from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass

from .dataset import Example, LABELS

_TOKEN = re.compile(r"[^\W\d_]+", flags=re.UNICODE)


def tokenize(text: str) -> list[str]:
    """Lowercase Unicode words, ignoring punctuation and numbers."""
    return _TOKEN.findall(text.casefold())


@dataclass(frozen=True)
class Prediction:
    label: str
    relative_score: float


class NaiveBayesClassifier:
    """Tiny teaching model. Relative scores are *not* calibrated probabilities."""

    def __init__(self, examples: list[Example]):
        if not examples:
            raise ValueError("Training set must not be empty")
        self.document_counts: Counter[str] = Counter(row.label for row in examples)
        if any(self.document_counts[label] == 0 for label in LABELS):
            raise ValueError("Training set must include every label")
        self.word_counts: dict[str, Counter[str]] = {label: Counter() for label in LABELS}
        self.vocabulary: set[str] = set()
        for row in examples:
            tokens = tokenize(row.text)
            if not tokens:
                raise ValueError("Training row has no words")
            self.word_counts[row.label].update(tokens)
            self.vocabulary.update(tokens)
        self.total_docs = len(examples)
        self.total_words = {
            label: sum(self.word_counts[label].values()) for label in LABELS
        }

    def predict(self, text: str) -> Prediction:
        if not text.strip() or len(text) > 500:
            raise ValueError("Input must contain 1–500 characters")
        tokens = tokenize(text)
        if not tokens:
            raise ValueError("Input has no words")
        # Only score vocabulary seen during training. Out-of-vocabulary words
        # carry no information in this tiny baseline.
        known_tokens = [token for token in tokens if token in self.vocabulary]
        if not known_tokens:
            # Abstain rather than silently guessing from class priors alone.
            return Prediction(label="abstain", relative_score=0.0)
        log_scores: dict[str, float] = {}
        for label in LABELS:
            log_score = math.log(self.document_counts[label] / self.total_docs)
            denominator = self.total_words[label] + len(self.vocabulary)
            for token in known_tokens:
                log_score += math.log((self.word_counts[label][token] + 1) / denominator)
            log_scores[label] = log_score
        best = max(LABELS, key=lambda item: log_scores[item])
        top = max(log_scores.values())
        weights = {label: math.exp(score - top) for label, score in log_scores.items()}
        relative_score = weights[best] / sum(weights.values())
        return Prediction(label=best, relative_score=relative_score)
