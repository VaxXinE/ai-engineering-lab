import tempfile
import unittest
from pathlib import Path

from week01.dataset import Example, check_train_test_leakage, read_examples


class DatasetTests(unittest.TestCase):
    def test_loads_synthetic_train_data(self):
        path = Path(__file__).resolve().parents[1] / "data" / "train.csv"
        rows = read_examples(path)
        self.assertEqual(len(rows), 54)
        self.assertEqual({row.label for row in rows}, {"sales", "support", "general"})

    def test_rejects_unknown_label(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.csv"
            path.write_text("text,label\nhello,secret\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Unknown label"):
                read_examples(path)

    def test_rejects_duplicate_rows_even_different_spacing_case(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "dup.csv"
            path.write_text("text,label\nHello World,sales\n hello   WORLD ,support\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Duplicate"):
                read_examples(path)

    def test_rejects_bad_headers(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.csv"
            path.write_text("message,label\nhello,sales\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "columns"):
                read_examples(path)

    def test_rejects_overlapping_training_and_test_set(self):
        with self.assertRaisesRegex(ValueError, "leakage"):
            check_train_test_leakage([Example("Hello world", "sales")], [Example("  HELLO  WORLD", "support")])


if __name__ == "__main__":
    unittest.main()
