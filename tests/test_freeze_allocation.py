"""Synthetic protocol-tool tests; zero human observations."""
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "use/studies/freeze_allocation.py"
SPEC = importlib.util.spec_from_file_location("freeze_allocation", PATH)
assert SPEC and SPEC.loader
script = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(script)


class FreezeAllocationTests(unittest.TestCase):
    @staticmethod
    def cases(n=5):
        return [
            {
                "case_id": f"independent-source-case-{i}",
                "case_version": f"sha256:case{i}",
                "information_cutoff": "2026-10-10T00:00:00Z",
                "source_ref": f"source:{i}",
            }
            for i in range(n)
        ]

    def test_reproducible_balanced_two_arm_allocation(self):
        rows, manifest = script.freeze(self.cases(), seed=101)
        rows2, manifest2 = script.freeze(self.cases(), seed=101)
        self.assertEqual((rows, manifest), (rows2, manifest2))
        self.assertEqual(manifest["status"], "allocation_only_no_human_data")
        self.assertEqual(manifest["case_count"], 5)
        self.assertEqual(manifest["guide_first"] + manifest["checklist_first"], 5)
        self.assertLessEqual(abs(manifest["guide_first"] - manifest["checklist_first"]), 1)
        by_case = {}
        for row in rows:
            by_case.setdefault(row["case_id"], []).append((row["slot"], row["arm"]))
        self.assertEqual(len(by_case), 5)
        self.assertTrue(all(
            set(pair) in (
                {("A", "guide"), ("B", "checklist")},
                {("A", "checklist"), ("B", "guide")},
            ) for pair in by_case.values()
        ))

    def test_reject_outcome_leakage_duplicates_and_empty_sources(self):
        with self.assertRaisesRegex(ValueError, "outcomes"):
            script.freeze([{**self.cases(1)[0], "score": "1"}], seed=1)
        with self.assertRaisesRegex(ValueError, "duplicate"):
            script.freeze(self.cases(1) * 2, seed=1)
        with self.assertRaisesRegex(ValueError, "provenance"):
            script.freeze([{**self.cases(1)[0], "source_ref": ""}], seed=1)
        with self.assertRaisesRegex(ValueError, "provenance fields"):
            script.freeze([{**self.cases(1)[0], "truth_label": "1"}], seed=1)
        with self.assertRaisesRegex(ValueError, "empty"):
            script.freeze([], seed=1)


if __name__ == "__main__":
    unittest.main()
