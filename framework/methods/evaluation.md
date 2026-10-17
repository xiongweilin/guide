# Evaluation

[English](evaluation.md) | [简体中文](evaluation.zh-CN.md)

## 1. Separate four questions

- **Transition sufficiency**: Is the current boundary adequately supported for a particular purpose and next transition? Sufficiency does not guarantee future correctness.
- **Judgment correctness**: Is the claim supported by suitable evidence and methods, under a specified standard, subject, and applicability conditions?
- **Predictive quality**: How well do time-stamped, ex ante claims correspond to subsequently obtained independent outcomes, over the stated population and horizon?
- **Legitimacy of action**: Correct computation or prediction does not grant normative legitimacy, consent, or execution authority.

```text
sufficiency != truth
valid formal derivation != empirical applicability of assumptions
forecast hit != identified causal effect
calibrated probabilities != certainty for individual events
higher evaluation score != improvement in external objectives
```

## 2. Select the validation type before judging

| Type | Conditions to specify | Appropriate validation | Does not establish |
| --- | --- | --- | --- |
| Formal or rule-derived | Axioms, payoffs, preferences, constraints, quantifiers, rule version | Proof, enumeration, counterexample, independent implementation, conformance test | Empirical applicability |
| Empirical fact or interpretation | Subject, source, time, definitions, competing explanations | Independent sources, reliable measurements, cross-checks, explicit disputes | Absence of unobserved states |
| Empirical forecast | Target population, issuance time, horizon, outcome definition, baseline | Freeze predictions, then obtain independent outcomes; evaluate errors and calibration | Causation or action authority |
| Intervention / causal prediction | Intervention, comparator, outcome, identification assumptions, interference, setting | Suitable experiments, quasi-experiments, causal identification and transport checks | Causal effects from correlation alone |

- **Normative claims**: Check factual premises, logical consistency, applicable norms, and procedure independently. A score alone does not establish legitimacy.

## 3. Minimal testable claim

```text
claim_id
claim_type: formal | empirical | forecast | causal | normative
target / population / outcome_definition
purpose / scope / applicable_conditions
created_at / evaluation_horizon
boundary_version / evidence_refs / model_or_rule_version
assumptions / competing_explanations / residual_unknowns
claim / prediction / uncertainty_representation
verification_method / independent_source / baseline
observation_status / observed_at / observed_result
error_or_counterexample / disposition / reopen_conditions
```

- **Ex ante freeze**: Lock empirical predictions, versions, and horizons before outcomes are available. Revisions create new records, never rewrite the original forecast.
- **Outcome qualification**: Pending, unavailable, mismatched, or insufficiently verified outcomes remain unknown, neither hits nor misses.
- **Coverage**: A probability covers only the stated outcome space; ungenerated alternatives and out-of-scope cases remain visible unknowns.
- **Independence**: Reviewers sharing the same data, labels, rules, or upstream sources are not automatically independent evidence.

## 4. Comparing accuracy

- **Formal claims**: Verify with proofs, counterexamples, or reproducible computations. Recheck applicability when assumptions change; failure to find a counterexample is not a proof.

- **Empirical forecasts**: Fix baseline, loss, evaluation population, and split strategy in advance. For binary outcomes, use Brier loss `(p-y)²` when appropriate; for continuous targets, consider MAE. Report calibration, subgroup behavior, coverage, and uncertainty as applicable. Do not double-count events.

- Separate training, tuning, and evaluation chronologically when time matters; prevent future information leakage.
- Compare against simple baselines and earlier versions on the same population, metric, and independently observed outcomes.
- Report limits from small samples, selective reporting, distribution shift, strategic adaptation, or unreliable labels; avoid spurious precision.
- If abstention is allowed, report both coverage and accuracy conditional on answering. Abstention is not a correct prediction.
- Observing the predicted result after an intervention does not, by itself, identify the intervention's causal effect.

## 5. Error attribution and reopening

- **Error categories**: Evidence, framing, derivation, model assumptions, transport, objectives, measurement, stochastic variation, strategic adaptation, and environment change.

1. Check whether the outcome is due and independently observable; otherwise retain unknown status.
2. Reconstruct the ex ante claim, boundary, scope, sources, and model version.
3. Compare under the predeclared standard; test counterexamples, alternatives, and changing conditions where material.
4. Revise the particular fact, model, rule, or scope implicated by falsifiable errors. Do not rebuild a model from one random miss.
5. Retain immutable history while requalifying current validity. Reopen exploration, sufficiency, or decision when warranted; reopening never grants execution authority.

## 6. Multi-actor checks

- **Strategic behavior**: Observed bids do not establish internal preferences; proposing rights affect matching, individual and collective objectives differ, equilibria need not be unique or fair, and published models can alter strategies.

- **Game assumptions**: Specify horizon, information, move order, preferences, payoffs, and material counterfactual changes.

## 7. Completion criteria and limits

- **Formal cases**: Reproduce the result, identify counterexamples, distinguish no solution from no solution found, and re-evaluate when key conditions change.
- **Empirical forecasts**: Require ex ante records, independent observations, fixed baselines, and repeatable errors. Do not claim measured improvement without actual outcomes.
- **Deployment**: Keep validation separate from authority, effect verification, and recovery in the [action chain](https://github.com/xiongweilin/aios/blob/main/docs/reference/guide/action-chain.md).
- **Proportionality**: Match verification effort to risk and irreversibility, rather than requiring complex persistence for every minor transition.

## 8. Research proposals

- [Sufficiency rater study](studies/sufficiency-raters-v1.md) is a draft for testing reproducibility of interpretive classifications. It has no collected ratings and is not preregistered.
- [Judgment benefit study](studies/judgment-benefit-v1.md) is a draft comparison with an equal-input checklist baseline. It has no outcome data and establishes no guide-specific benefit.
- The [impact pathway](studies/impact-pathway.md) separates bounded execution evidence from unmeasured claims about total labor and human benefit.
