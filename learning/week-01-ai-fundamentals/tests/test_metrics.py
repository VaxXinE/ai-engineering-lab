import unittest

from week01.metrics import evaluate


class MetricsTests(unittest.TestCase):
    def test_perfect_prediction(self):
        report = evaluate(["normal", "warning", "fault"], ["normal", "warning", "fault"])
        self.assertEqual(report["accuracy"], 1.0)
        self.assertEqual(report["macro_f1"], 1.0)
        self.assertEqual(report["test_size"], 3)

    def test_misclassification(self):
        report = evaluate(["normal", "warning", "fault"], ["warning", "warning", "fault"])
        self.assertAlmostEqual(report["accuracy"], 0.6667, places=4)
        self.assertEqual(report["confusion_matrix"]["normal"]["warning"], 1)
        self.assertEqual(report["per_class"]["normal"]["recall"], 0.0)

    def test_abstention_counts_as_missed_prediction(self):
        report = evaluate(["normal", "warning"], ["abstain", "warning"])
        self.assertEqual(report["abstention_count"], 1)
        self.assertEqual(report["accuracy"], 0.5)
        self.assertEqual(report["per_class"]["normal"]["recall"], 0.0)

    def test_rejects_invalid_inputs(self):
        for truth, prediction in [([], []), (["normal"], []), (["made-up"], ["normal"])]:
            with self.subTest(truth=truth):
                with self.assertRaises(ValueError):
                    evaluate(truth, prediction)


if __name__ == "__main__":
    unittest.main()
