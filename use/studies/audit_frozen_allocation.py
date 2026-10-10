"""Cross-check frozen allocation, case-review records and reviewer separation.

This is a consistency check, NOT independent proof of masking, assignment,
assessor integrity, case provenance or participant identity.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

IDENTITY = ("case_id", "case_version", "information_cutoff", "source_ref")
ALLOC_FIELDS = (*IDENTITY, "slot", "arm")
REVIEW_FIELDS = (*ALLOC_FIELDS, "reviewer_id")


def _csv(path: Path, required: tuple[str, ...]) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if (not reader.fieldnames or len(reader.fieldnames) != len(set(reader.fieldnames))
                or not set(required) <= set(reader.fieldnames)):
            raise ValueError("missing or duplicated CSV header columns")
        rows = list(reader)
    if not rows:
        raise ValueError("empty allocation or review rows")
    for row in rows:
        if not all(row.get(key) and row[key].strip() for key in required):
            raise ValueError("blank required identity/allocation/reviewer field")
    return rows


def audit(alloc_path: Path, manifest_path: Path, reviews_path: Path) -> dict[str, object]:
    allocation = _csv(alloc_path, ALLOC_FIELDS)
    frozen = json.loads(manifest_path.read_text(encoding="utf-8"))
    if frozen.get("status") != "allocation_only_no_human_data":
        raise ValueError("unexpected frozen manifest status")
    canonical = json.dumps(
        [{key: row[key] for key in ALLOC_FIELDS} for row in allocation],
        ensure_ascii=False, sort_keys=True, separators=(",", ":"),
    ).encode()
    digest = hashlib.sha256(canonical).hexdigest()
    if digest != frozen.get("assignment_sha256"):
        raise ValueError("allocation rows do not match frozen SHA-256")
    cases: dict[str, dict[str, dict[str, str]]] = {}
    frozen_by_pair = {}
    for row in allocation:
        key = (row["case_id"], row["arm"])
        if (row["arm"] not in {"guide", "checklist"} or row["slot"] not in {"A", "B"}
                or key in frozen_by_pair):
            raise ValueError("duplicate or unsupported frozen allocation")
        frozen_by_pair[key] = row
        cases.setdefault(row["case_id"], {})[row["arm"]] = row
    if len(cases) != frozen.get("case_count"):
        raise ValueError("case count differs from frozen manifest")
    for cid, arms in cases.items():
        if set(arms) != {"guide", "checklist"}:
            raise ValueError(f"{cid}: missing frozen arm")
        a, d = arms["guide"], arms["checklist"]
        if a["slot"] == d["slot"] or any(a[k] != d[k] for k in IDENTITY):
            raise ValueError(f"{cid}: inconsistent paired assignment")
    reviews = _csv(reviews_path, REVIEW_FIELDS)
    seen: dict[tuple[str, str], dict[str, str]] = {}
    for row in reviews:
        key = (row["case_id"], row["arm"])
        frozen_row = frozen_by_pair.get(key)
        if key in seen or frozen_row is None:
            raise ValueError("duplicate or unassigned review row")
        if any(row[field] != frozen_row[field] for field in ALLOC_FIELDS):
            raise ValueError("review row does not match frozen case/arm/slot")
        seen[key] = row
    if set(seen) != set(frozen_by_pair):
        raise ValueError("review records omit frozen assigned rows")
    for cid, arms in cases.items():
        if seen[(cid, "guide")]["reviewer_id"] == seen[(cid, "checklist")]["reviewer_id"]:
            raise ValueError(f"{cid}: same reviewer filled both arms")
    return {
        "status": "matching_only_no_external_identity_validation",
        "frozen_cases": len(cases),
        "review_rows": len(reviews),
        "assignment_sha256": digest,
        "caveat": (
            "CSV consistency and distinct reviewer identifiers do not prove "
            "different human participants, genuine blinding, or independent adjudication."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("frozen_allocation_csv", type=Path)
    parser.add_argument("frozen_manifest_json", type=Path)
    parser.add_argument("review_records_csv", type=Path)
    args = parser.parse_args()
    result = audit(
        args.frozen_allocation_csv, args.frozen_manifest_json, args.review_records_csv,
    )
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
