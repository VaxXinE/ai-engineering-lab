import contextlib
import io
import json
import unittest

from week01.cli import main


class CliTests(unittest.TestCase):
    def test_evaluate_returns_machine_readable_metrics(self):
        with io.StringIO() as output, contextlib.redirect_stdout(output):
            code = main(["evaluate"])
            result = json.loads(output.getvalue())
        self.assertEqual(code, 0)
        self.assertEqual(result["test_size"], 18)
        self.assertIn("macro_f1", result)

    def test_prediction_has_uncertainty_notice(self):
        with io.StringIO() as output, contextlib.redirect_stdout(output):
            code = main(["predict", "--text", "meter melaporkan tegangan stabil normal"])
            result = json.loads(output.getvalue())
        self.assertEqual(code, 0)
        self.assertEqual(result["label"], "normal")
        self.assertIn("NOT", result["note"])

    def test_invalid_user_text_returns_nonzero(self):
        with io.StringIO() as errors, contextlib.redirect_stderr(errors):
            code = main(["predict", "--text", " "])
            err = errors.getvalue()
        self.assertEqual(code, 2)
        self.assertIn("Validation", err)


if __name__ == "__main__":
    unittest.main()
