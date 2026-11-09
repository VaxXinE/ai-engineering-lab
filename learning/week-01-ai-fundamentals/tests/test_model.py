import unittest
from pathlib import Path

from week01.dataset import Example, read_examples
from week01.model import NaiveBayesClassifier, tokenize


class ModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = Path(__file__).resolve().parents[1] / "data" / "train.csv"
        cls.model = NaiveBayesClassifier(read_examples(path))

    def test_unicode_tokenizer(self):
        self.assertEqual(tokenize("Halo, DÜNIA! 123"), ["halo", "dünia"])

    def test_rejects_missing_labels(self):
        with self.assertRaisesRegex(ValueError, "every label"):
            NaiveBayesClassifier([Example("tegangan stabil", "normal")])

    def test_predict_normal_example(self):
        prediction = self.model.predict("meter melaporkan tegangan stabil normal")
        self.assertEqual(prediction.label, "normal")
        self.assertGreaterEqual(prediction.relative_score, 0)
        self.assertLessEqual(prediction.relative_score, 1)

    def test_predict_warning_example(self):
        self.assertEqual(self.model.predict("konsumsi energi meningkat mendekati ambang").label, "warning")

    def test_predict_fault_example(self):
        self.assertEqual(self.model.predict("sensor offline tidak mengirim data").label, "fault")

    def test_rejects_empty_or_too_long(self):
        for value in ("   ", "x"*501, "1234"):
            with self.subTest(value=value[:9]):
                with self.assertRaises(ValueError):
                    self.model.predict(value)

    def test_unknown_vocabulary_abstains(self):
        result = self.model.predict("zzzzzzqqq")
        self.assertEqual(result.label, "abstain")
        self.assertEqual(result.relative_score, 0)


if __name__ == "__main__":
    unittest.main()
