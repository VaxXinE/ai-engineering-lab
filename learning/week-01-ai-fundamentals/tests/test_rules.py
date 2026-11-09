import unittest

from week01.rules import classify_by_rules


class RuleBaselineTests(unittest.TestCase):
    def test_normal_keyword(self):
        self.assertEqual(classify_by_rules("pembacaan meter stabil"), "normal")

    def test_warning_keyword(self):
        self.assertEqual(classify_by_rules("konsumsi energi meningkat"), "warning")

    def test_no_keyword_abstains(self):
        self.assertEqual(classify_by_rules("halo halo dunia"), "abstain")

    def test_tie_abstains(self):
        self.assertEqual(classify_by_rules("sensor stabil tapi offline"), "abstain")


if __name__ == "__main__":
    unittest.main()
