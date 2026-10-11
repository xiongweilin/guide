"""Regression fixtures for allocation consistency; no human data."""
from __future__ import annotations
import csv
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "use/studies"

def load(file):
    spec = importlib.util.spec_from_file_location(file.removesuffix(".py"), ROOT / file)
    assert spec and spec.loader
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj

freeze = load("freeze_allocation.py")
checker = load("audit_frozen_allocation.py")


class LockedAllocationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        root = Path(self.directory.name)
        cases = [
            {"case_id": f"fixture-{i}", "case_version": f"sha-{i}",
             "information_cutoff": "frozen", "source_ref": f"src-{i}"}
            for i in range(4)
        ]
        self.rows, manifest = freeze.freeze(cases, seed=13)
        self.allocation = root / "allocation.csv"
        self.manifest = root / "manifest.json"
        self.reviews = root / "reviews.csv"
        self.manifest.write_text(json.dumps(manifest), encoding="utf-8")
        self.review_rows = [
            {**row, "reviewer_id": row["case_id"] + "-" + row["slot"]}
            for row in self.rows
        ]
        self.save()

    def write_csv(self, path, keys, rows):
        with path.open("w", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(stream, fieldnames=keys)
            writer.writeheader()
            writer.writerows(rows)

    def save(self):
        self.write_csv(self.allocation, freeze.FIELDS, self.rows)
        self.write_csv(self.reviews, checker.REVIEW_FIELDS, self.review_rows)

    def audit(self):
        return checker.audit(self.allocation, self.manifest, self.reviews)

    def test_passes_well_formed_fixture(self):
        result = self.audit()
        self.assertEqual(result["frozen_cases"], 4)
        self.assertEqual(result["review_rows"], 8)

    def test_allocation_fingerprint_detects_changes(self):
        self.rows[0]["slot"] = "B" if self.rows[0]["slot"] == "A" else "A"
        self.save()
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            self.audit()

    def test_reviewer_id_cannot_repeat_in_pair(self):
        pair = [x for x in self.review_rows if x["case_id"] == "fixture-0"]
        pair[1]["reviewer_id"] = pair[0]["reviewer_id"]
        self.save()
        with self.assertRaisesRegex(ValueError, "same reviewer"):
            self.audit()

    def test_cannot_drop_assigned_review(self):
        self.review_rows.pop()
        self.save()
        with self.assertRaisesRegex(ValueError, "omit"):
            self.audit()

    def test_cannot_rebind_review_slot(self):
        self.review_rows[0]["slot"] = "other"
        self.save()
        with self.assertRaisesRegex(ValueError, "does not match"):
            self.audit()


if __name__ == "__main__":
    unittest.main()
