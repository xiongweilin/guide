"""Unit fixtures are synthetic; they are not empirical guide results."""
from __future__ import annotations

import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "use/studies/analyze_judgment_benefit.py"
SPEC = importlib.util.spec_from_file_location("judgment_benefit_analysis", SCRIPT)
assert SPEC and SPEC.loader
analysis = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(analysis)


class PairedAnalysisTests(unittest.TestCase):
    def write(self, rows: list[dict[str, str]]) -> Path:
        self.addCleanup(lambda: self.directory.cleanup())
        self.directory = tempfile.TemporaryDirectory()
        path = Path(self.directory.name) / "synthetic-fixture.csv"
        with path.open("w", newline="", encoding="utf-8") as out:
            writer = csv.DictWriter(out, fieldnames=analysis.REQUIRED)
            writer.writeheader()
            writer.writerows(rows)
        return path

    @staticmethod
    def row(case: str, arm: str, correct: str, *, status: str = "known") -> dict[str, str]:
        return {
            "case_id": case,
            "arm": arm,
            "case_version": "sha256:synthetic-only",
            "information_cutoff": "synthetic-before-assignment",
            "source_ref": "unit-fixture-not-real-evidence",
            "training_seconds": "120",
            "budget_seconds": "60",
            "elapsed_seconds": "30" if arm == "guide" else "20",
            "outcome_status": status,
            "adjudicated_correct": correct,
            "assessor_blinded": "yes",
        }

    def test_descriptive_matched_pairs_and_unknown_bounds(self) -> None:
        rows = [
            self.row("A", "guide", "1"), self.row("A", "checklist", "0"),
            self.row("B", "guide", "0"), self.row("B", "checklist", "1"),
            self.row("C", "guide", "NA", status="unknown"),
            self.row("C", "checklist", "1"),
        ]
        result = analysis.analyze(self.write(rows))
        self.assertEqual(result["guide_only_correct"], 1)
        self.assertEqual(result["checklist_only_correct"], 1)
        self.assertEqual(result["outcome_unknown_pairs"], 1)
        self.assertEqual(result["accuracy_delta_bounds_including_unknown"], [-1/3, 1/3])
        self.assertEqual(result["two_sided_discordance_sign_p"], 1.0)
        self.assertEqual(result["mean_elapsed_seconds"], {"guide": 30.0, "checklist": 20.0})

    def test_rejects_unequal_information_and_training(self) -> None:
        rows = [self.row("A", "guide", "1"), self.row("A", "checklist", "0")]
        rows[1]["case_version"] = "changed"
        with self.assertRaisesRegex(ValueError, "unequal"):
            analysis.analyze(self.write(rows))

    def test_rejects_duplicates_and_missing_arm(self) -> None:
        rows = [self.row("A", "guide", "1"), self.row("A", "guide", "1")]
        with self.assertRaisesRegex(ValueError, "duplicate"):
            analysis.analyze(self.write(rows))
        with self.assertRaisesRegex(ValueError, "arm missing"):
            analysis.analyze(self.write([self.row("A", "guide", "1")]))

    def test_never_imputes_unknown_or_unblinded_outcome(self) -> None:
        rows = [self.row("A", "guide", "0", status="unknown"), self.row("A", "checklist", "1")]
        with self.assertRaisesRegex(ValueError, "not be imputed"):
            analysis.analyze(self.write(rows))
        rows[0]["adjudicated_correct"] = "NA"
        rows[0]["assessor_blinded"] = "no"
        with self.assertRaisesRegex(ValueError, "blinding"):
            analysis.analyze(self.write(rows))

    def test_discordance_sign_exact_small_n(self) -> None:
        self.assertEqual(analysis._exact_sign_p_value(0, 0), None)
        self.assertEqual(analysis._exact_sign_p_value(4, 0), 0.125)


if __name__ == "__main__":
    unittest.main()
