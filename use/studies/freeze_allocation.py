"""Freeze blinded, balanced assignment slots BEFORE gathering human outcomes.

Input is an independently sourced JSON list of case descriptors (no results).
This prepares a reproducible allocation, not participants, adjudication or an
empirical study. Keep the seed, complete case set and CSV locked before ratings.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
from pathlib import Path

REQUIRED = ("case_id", "case_version", "information_cutoff", "source_ref")
PROHIBITED = {"outcome", "answer", "correct", "score", "result", "judgment"}
FIELDS = ("case_id", "case_version", "information_cutoff", "source_ref", "slot", "arm")


def freeze(cases: list[dict[str, str]], *, seed: int) -> tuple[list[dict[str, str]], dict]:
    if not cases:
        raise ValueError("case set is empty")
    seen: set[str] = set()
    for case in cases:
        if not isinstance(case, dict):
            raise ValueError("case descriptor must be an object")
        if PROHIBITED & {str(k).lower() for k in case}:
            raise ValueError("case descriptors must not contain outcomes or ratings")
        # Fail closed on other fields too; a benign-looking 'truth_label'
        # can otherwise leak an answer through allocation inputs.
        if set(case) != set(REQUIRED):
            raise ValueError("case descriptors must contain exactly the provenance fields")
        if not all(isinstance(case.get(key), str) and case[key].strip() for key in REQUIRED):
            raise ValueError("case descriptor must have nonempty provenance fields")
        if case["case_id"] in seen:
            raise ValueError("duplicate case_id")
        seen.add(case["case_id"])
    source = json.dumps(cases, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    source_sha256 = hashlib.sha256(source).hexdigest()
    rng = random.Random(seed)
    order = list(range(len(cases)))
    rng.shuffle(order)
    # Balanced study order; each case is reviewed in both arms by different
    # blinded persons assigned to A/B slots. Actual people are not invented.
    first = ["guide"] * ((len(cases) + 1) // 2) + ["checklist"] * (len(cases) // 2)
    rng.shuffle(first)
    rows: list[dict[str, str]] = []
    for index, first_arm in zip(order, first):
        case = cases[index]
        for slot, arm in (
            ("A", first_arm),
            ("B", "checklist" if first_arm == "guide" else "guide"),
        ):
            rows.append({**{k: case[k] for k in REQUIRED}, "slot": slot, "arm": arm})
    assignment = json.dumps(rows, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    manifest = {
        "status": "allocation_only_no_human_data",
        "seed": seed,
        "case_count": len(cases),
        "source_descriptors_sha256": source_sha256,
        "assignment_sha256": hashlib.sha256(assignment).hexdigest(),
        "guide_first": sum(row["arm"] == "guide" and row["slot"] == "A" for row in rows),
        "checklist_first": sum(row["arm"] == "checklist" and row["slot"] == "A" for row in rows),
        "not_established": ["independent sourcing", "consent", "blinding", "ratings", "benefit"],
    }
    return rows, manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cases_json", type=Path)
    parser.add_argument("output_prefix", type=Path)
    parser.add_argument("--seed", type=int, required=True,
                        help="Freeze this randomization seed before data collection")
    args = parser.parse_args()
    cases = json.loads(args.cases_json.read_text(encoding="utf-8"))
    if not isinstance(cases, list):
        raise ValueError("case descriptors must be a JSON list")
    rows, manifest = freeze(cases, seed=args.seed)
    csv_path = args.output_prefix.with_suffix(".csv")
    json_path = args.output_prefix.with_suffix(".manifest.json")
    if csv_path.exists() or json_path.exists():
        raise FileExistsError("refuse to overwrite an existing frozen allocation")
    with csv_path.open("x", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    json_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    print(json.dumps(manifest, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
