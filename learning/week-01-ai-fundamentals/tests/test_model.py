import unittest
from pathlib import Path

from week01.dataset import read_examples
from week01.model import NaiveBayesClassifier, tokenize


class ModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data = Path(__file__).resolve().parents[1] / "data" / "train.csv"
        cls.model = NaiveBayesClassifier(read_examples(data))

    def test_unicode_tokenizer(self):
        self.assertEqual(tokenize("Halo, DÜNIA! 123"), ["halo", "dünia"])

    def test_rejects_missing_labels(self):
        from week01.dataset import Example
        with self.assertRaisesRegex(ValueError, "every label"):
            NaiveBayesClassifier([Example("paket harga", "sales")])

    def test_predict_sales_example(self):
        predicted = self.model.predict("saya ingin membeli paket langganan")
        self.assertEqual(predicted.label, "sales")
        self.assertGreaterEqual(predicted.relative_score, 0.0)
        self.assertLessEqual(predicted.relative_score, 1.0)

    def test_predict_support_example(self):
        self.assertEqual(self.model.predict("tidak bisa login aplikasi error").label, "support")

    def test_predict_general_example(self):
        self.assertEqual(self.model.predict("alamat kantor perusahaan di mana").label, "general")

    def test_rejects_empty_or_too_long(self):
        for text in ("   ", "x" * 501, "1234"):
            with self.subTest(text=text[:8]):
                with self.assertRaises(ValueError):
                    self.model.predict(text)

    def test_abstains_when_vocabulary_has_no_match(self):
        result = self.model.predict("zzzzzzqqq")
        self.assertEqual(result.label, "abstain")
        self.assertEqual(result.relative_score, 0.0)


if __name__ == "__main__":
    unittest.main()
