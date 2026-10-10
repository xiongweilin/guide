# Judgment benefit: comparison protocol draft

[English](judgment-benefit-v1.md) | [简体中文](judgment-benefit-v1.zh-CN.md)

**Status:** design draft; not preregistered; no comparison or outcome data exist.

## Question

Under equal information, review time, and training, does guide-assisted review improve independently verifiable decisions over a simple checklist?

This is separate from the rater reproducibility study. Agreement between reviewers is not an outcome for this comparison and cannot stand in for decision quality.

## Design requirements

- Choose tasks whose relevant outcome can be independently established; define the target, population, decision time, and outcome before assignment.
- Compare guide-assisted review with a simple checklist using the same case information, time allowance, and training effort. Record deviations rather than assuming the inputs remained equal.
- Freeze allocation, primary outcomes, baseline, missing/outcome-unknown handling, and analysis before outcomes are available. Do not choose cases after seeing which method performs better.
- Report decision errors, appropriate retention of unknowns, task coverage, and human time separately. Select the primary outcome and the smallest worthwhile difference from task costs before the main comparison; no numeric threshold is set here.
- Use an outcome assessor who is independent of the reviewers and does not see method assignment where feasible. Document any shared labels or sources that limit independence.

## Interpretation and reversal

A gain under unequal time, information, or training does not identify a guide-specific effect. If the checklist performs equivalently under equal inputs, remove the claim that guide adds measurable benefit for this task; that result does not invalidate the conceptual framework as a whole. No benefit claim is currently supported because the study has not been run.

## Allocation freeze tool (no participants or outcomes)

Before recruitment or rating, use `python use/studies/freeze_allocation.py independent-case-descriptors.json frozen-allocation --seed <precommitted-integer>`. The JSON must contain a list of records with `case_id`, `case_version`, `information_cutoff`, and `source_ref`, sourced independently and fixed before assignment. The script produces a two-arm A/B allocation CSV and a manifest with SHA-256 fingerprints and balanced arm order; it refuses to overwrite an existing freeze. Assignment *slots* are not reviewers, blinding evidence or human outcomes. Two distinct actual reviewers must later be assigned per paired case, with true assessor independence verified externally. Record the seed and complete case pool in the external preregistration before collecting outcomes; the tool alone is not preregistration.

### Verify allocation-to-review integrity

Before running the outcome analyzer, run `python use/studies/audit_frozen_allocation.py frozen-allocation.csv frozen-allocation.manifest.json review-records-with-slots.csv`. Its additional review columns `slot` (A or B) and `reviewer_id` must match the frozen case/arm/slot rows; paired arms cannot share a reviewer ID. The check rejects changed allocation hashes, missing assignments, duplicated or rebound rows and same-ID paired reviewers. This is **not** authentication of individuals, independent judges, anonymization, preregistration or masking; those require external safeguards. Treat manifest and CSV as independently archived before review, because a self-rewritten manifest and allocation can both pass local hash checks.

## Reproducible analysis gate (no study data yet)

`python use/studies/analyze_judgment_benefit.py locked-review-records.csv` checks for exactly one guide and one checklist row per case, matched case version, evidence cutoff, source reference, training and allowed review time, separately recorded actual seconds, and independent adjudication status. Its exact two-sided sign calculation uses only adjudicated discordant pairs; unknown outcomes remain unknown and enter a conservative full-sample bound rather than being scored as success or failure.

The input columns are `case_id, arm, case_version, information_cutoff, source_ref, training_seconds, budget_seconds, elapsed_seconds, outcome_status, adjudicated_correct, assessor_blinded`. Allowed values are `arm=guide|checklist`, `outcome_status=known|unknown`, and `adjudicated_correct=0|1` only when known; otherwise blank or `NA`. `assessor_blinded=yes` is an attestation, **not a machine proof of independence**. Each case's provenance and true cutoff still require external audit. Synthetic unit fixtures are never study observations.

The analysis tool deliberately does not infer causal benefit, a sampling population, protocol preregistration, or cross-domain generalization. Before use with real data, freeze the independent outcome rubric and recruitment/allocation protocol separately and publish failure and missingness counts.
