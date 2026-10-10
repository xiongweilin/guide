# Interpretive sufficiency: rater study protocol draft

[English](sufficiency-raters-v1.md) | [简体中文](sufficiency-raters-v1.zh-CN.md)

**Status:** design draft; not preregistered; no cases have been frozen and no ratings have been collected.

## Question and scope

Can independent reviewers apply the three interpretive classifications consistently when the purpose, current boundary, evidence cutoff, and proposed transition are fixed?

The study concerns interpretive sufficiency only. Explicit prescriptive cases, including the formal observation/commitment special case, may be reported separately as rule anchors; they are not observations in the main sample. Permission and authority must be recorded separately and must not substitute for an epistemic rating.

Agreement would establish reproducibility under the studied materials and reviewer population. It would not establish that a rating is true, that the boundary is adequate in reality, or that using guide improves decisions.

## Case record to freeze

Each case must provide, using only information available at the decision time:

~~~text
case_id
source_and_version
domain
information_cutoff
purpose_P
current_boundary_B
proposed_transition_T
evidence_and_counterevidence
known_unknowns
material_competing_explanations
invalidation_conditions
outcome_observability
~~~

Use independently sourced historical audits, incident records, and newly written authorization or maintenance cases. Do not turn a synthetic example into an empirical case. Freeze the case set, presentation, scoring guide, exclusions, and analysis before main-sample ratings. Keep later outcomes hidden unless they were available at the recorded cutoff.

## Rating and missingness

For each fixed (B, P, T), record one nominal category:

- **insufficient:** a material support gap is identified as relevant to the proposed transition;
- **materially uncertain:** whether a gap changes the next transition cannot currently be determined;
- **sufficient:** the available support is proportionate for this transition while residual unknowns remain explicit.

Materially uncertain is a substantive category, not missing data. A case that cannot be rated because the packet is incomplete or unreadable receives a separate not_rateable status and a reason. Record permission, authority, and organizational policy in separate fields.

## Reviewers and analysis

The proposed pilot uses six reviewers who are not co-authors, with experience spanning relevant domain practice and method review. Six is a resource choice for a pilot, not evidence of adequate precision or a representative sample. After the pilot, determine the main-sample size from a predeclared interval-precision target before collecting its ratings.

Report nominal Krippendorff's alpha, its preselected uncertainty interval, the sufficient versus not-sufficient agreement, the full confusion matrix, and the main sources of disagreement. Do not merge categories or select easier cases after seeing results. If the project retains alpha = 0.80 as a release criterion, label it a provisional project decision and confirm it before the main sample against the consequences of misclassification; it is not a general safety threshold.

An interval wholly below a confirmed criterion would count against reproducibility for this operation. An interval crossing it remains inconclusive. An interval wholly above it supports reproducibility only, not correctness or benefit.

## Reopening conditions

If reviewers disagree because the purpose, boundary, or transition was underspecified, repair case construction and rerun on a new frozen set. If they disagree despite fixed cases and instructions, narrow or revise this operationalization. Neither result by itself rejects guide's broader objective of accountable, context-sensitive judgment.

The protocol remains a draft until the case sources, reviewer recruitment, analysis code, precision target, and decision criterion are fixed. No empirical conclusion is available now.
