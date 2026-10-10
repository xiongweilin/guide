"""Analyze a *frozen*, paired guide-vs-checklist CSV without inventing outcomes.

The analyst must separately verify source provenance, allocation and assessor independence.
CLI output is a descriptive audit, not a causal-effect certification.
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from math import comb
from pathlib import Path

ARMS = ("guide", "checklist")
REQUIRED = (
    "case_id",
    "arm",
    "case_version",
    "information_cutoff",
    "source_ref",
    "training_seconds",
    "budget_seconds",
    "elapsed_seconds",
    "outcome_status",
    "adjudicated_correct",
    "assessor_blinded",
)
SHARED = ("case_version", "information_cutoff", "source_ref", "training_seconds", "budget_seconds")


def _nonnegative_number(value: str, label: str) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{label} must be numeric") from exc
    if not (0 <= number < float("inf")):
        raise ValueError(f"{label} must be finite and nonnegative")
    return number


def _read(path: Path) -> dict[str, dict[str, dict[str, str]]]:
    pairs: dict[str, dict[str, dict[str, str]]] = defaultdict(dict)
    with path.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or len(set(reader.fieldnames)) != len(reader.fieldnames):
            raise ValueError("CSV requires unique header names")
        missing = set(REQUIRED) - set(reader.fieldnames)
        if missing:
            raise ValueError(f"CSV missing columns: {sorted(missing)}")
        for line, row in enumerate(reader, start=2):
            if not all((row.get(k) or "").strip() for k in REQUIRED if k != "adjudicated_correct"):
                raise ValueError(f"row {line}: required identity/provenance field is blank")
            arm, case_id = row["arm"], row["case_id"]
            if arm not in ARMS:
                raise ValueError(f"row {line}: unknown arm {arm!r}")
            if arm in pairs[case_id]:
                raise ValueError(f"row {line}: duplicate case/arm")
            if row["assessor_blinded"] != "yes":
                raise ValueError(f"row {line}: assessor blinding not attested")
            for key in ("training_seconds", "budget_seconds", "elapsed_seconds"):
                _nonnegative_number(row[key], f"row {line} {key}")
            if float(row["elapsed_seconds"]) > float(row["budget_seconds"]):
                raise ValueError(f"row {line}: exceeds recorded budget")
            if row["outcome_status"] == "known":
                if row["adjudicated_correct"] not in {"0", "1"}:
                    raise ValueError(f"row {line}: known outcome requires independently adjudicated 0/1")
            elif row["outcome_status"] == "unknown":
                if row["adjudicated_correct"] not in {"", "NA"}:
                    raise ValueError(f"row {line}: unknown outcome must not be imputed")
            else:
                raise ValueError(f"row {line}: invalid outcome_status")
            pairs[case_id][arm] = row
    if not pairs:
        raise ValueError("empty dataset")
    for case_id, arms in pairs.items():
        if set(arms) != set(ARMS):
            raise ValueError(f"case {case_id}: comparison arm missing")
        a, b = (arms[x] for x in ARMS)
        for key in SHARED:
            if a[key] != b[key]:
                raise ValueError(f"case {case_id}: unequal case information/budget/training ({key})")
    return pairs


def _exact_sign_p_value(wins: int, losses: int) -> float | None:
    discordant = wins + losses
    if discordant == 0:
        return None
    return min(1.0, 2 * sum(comb(discordant, i) for i in range(min(wins, losses) + 1)) / (2**discordant))


def analyze(path: Path) -> dict[str, object]:
    pairs = _read(path)
    wins = losses = ties = unknown = 0
    elapsed = {"guide": 0.0, "checklist": 0.0}
    for arms in pairs.values():
        guide, checklist = (arms[x] for x in ARMS)
        for arm in ARMS:
            elapsed[arm] += float(arms[arm]["elapsed_seconds"])
        if guide["outcome_status"] == "unknown" or checklist["outcome_status"] == "unknown":
            unknown += 1
            continue
        delta = int(guide["adjudicated_correct"]) - int(checklist["adjudicated_correct"])
        if delta > 0:
            wins += 1
        elif delta < 0:
            losses += 1
        else:
            ties += 1
    n = len(pairs)
    return {
        "status": "descriptive_audit_only_not_independent_validation",
        "paired_cases": n,
        "fully_adjudicated_pairs": n - unknown,
        "outcome_unknown_pairs": unknown,
        "guide_only_correct": wins,
        "checklist_only_correct": losses,
        "same_correctness": ties,
        "paired_accuracy_delta_known_only": (wins - losses) / (n - unknown) if n > unknown else None,
        "accuracy_delta_bounds_including_unknown": [
            (wins - losses - unknown) / n,
            (wins - losses + unknown) / n,
        ],
        "two_sided_discordance_sign_p": _exact_sign_p_value(wins, losses),
        "mean_elapsed_seconds": {arm: elapsed[arm] / n for arm in ARMS},
        "caveat": "Cannot validate source independence, randomization, assessor masking or external generalization from CSV fields.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()
    print(json.dumps(analyze(args.csv_path), indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
