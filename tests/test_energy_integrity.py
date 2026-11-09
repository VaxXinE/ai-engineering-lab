"""Tests for the educational domain contract, not the future capstone."""
import unittest

from scripts.check_energy_integrity import (
    ROOT, CONTRACT, read_csv_example, validate_row,
    energy_to_average_kw, check,
)


class CurriculumEnergyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = read_csv_example((ROOT / CONTRACT).read_text(encoding="utf-8"))

    def test_example_has_three_unique_events(self):
        self.assertEqual(len(self.rows), 3)
        keys = [(r["site_id"], r["meter_id"], r["source_event_id"]) for r in self.rows]
        self.assertEqual(len(keys), len(set(keys)))

    def test_kwh_to_average_kw_15min(self):
        self.assertEqual(energy_to_average_kw(1.5, 15), 6.0)

    def test_kwh_to_average_kw_60min(self):
        self.assertEqual(energy_to_average_kw(1.5, 60), 1.5)

    def test_invalid_kwh(self):
        for val in (-1.0, float("nan"), float("inf")):
            with self.subTest(val=val):
                with self.assertRaises(ValueError):
                    energy_to_average_kw(val, 15)

    def test_zero_duration_invalid(self):
        with self.assertRaises(ValueError):
            energy_to_average_kw(1.0, 0)

    def test_missing_timezone_invalid(self):
        row = dict(self.rows[0])
        row["interval_start_utc"] = "2026-01-01T00:00:00"
        with self.assertRaises(ValueError):
            validate_row(row)

    def test_wrong_interval_invalid(self):
        row = dict(self.rows[0])
        row["interval_minutes"] = "60"
        with self.assertRaises(ValueError):
            validate_row(row)

    def test_nan_reading_invalid(self):
        row = dict(self.rows[0])
        row["energy_kwh"] = "NaN"
        with self.assertRaises(ValueError):
            validate_row(row)

    def test_course_docs_have_consistent_domain(self):
        self.assertEqual(check(), [])


if __name__ == "__main__":
    unittest.main()
