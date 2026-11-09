import contextlib
import io
import json
import unittest

from week01.cli import main


class CliTests(unittest.TestCase):
    def test_evaluate_returns_machine_readable_metrics(self):
        with io.StringIO() as output, contextlib.redirect_stdout(output):
            exit_code = main(["evaluate"])
            result = json.loads(output.getvalue())
        self.assertEqual(exit_code, 0)
        self.assertEqual(result["test_size"], 18)
        self.assertIn("macro_f1", result)

    def test_prediction_has_uncertainty_notice(self):
        with io.StringIO() as output, contextlib.redirect_stdout(output):
            exit_code = main(["predict", "--text", "berapa harga paket baru"])
            result = json.loads(output.getvalue())
        self.assertEqual(exit_code, 0)
        self.assertEqual(result["label"], "sales")
        self.assertIn("NOT", result["note"])

    def test_invalid_user_text_returns_nonzero(self):
        with io.StringIO() as errors:
            with contextlib.redirect_stderr(errors):
                exit_code = main(["predict", "--text", " "])
            error_message = errors.getvalue()
        self.assertEqual(exit_code, 2)
        self.assertIn("Validation", error_message)


if __name__ == "__main__":
    unittest.main()
