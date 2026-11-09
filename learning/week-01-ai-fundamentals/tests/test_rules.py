import unittest

from week01.rules import classify_by_rules


class RuleBaselineTests(unittest.TestCase):
    def test_sales_keyword(self):
        self.assertEqual(classify_by_rules("berapa harga paket"), "sales")

    def test_support_keyword(self):
        self.assertEqual(classify_by_rules("login error"), "support")

    def test_no_keyword_falls_back_to_general(self):
        self.assertEqual(classify_by_rules("halo selamat pagi"), "general")

    def test_ties_fall_back_to_general(self):
        self.assertEqual(classify_by_rules("harga error"), "general")


if __name__ == "__main__":
    unittest.main()
