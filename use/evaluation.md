# Evaluation

[English](./judgment-validation.md) | [简体中文](./judgment-validation.zh-CN.md)

> Scope: A cross-domain **evaluation method for judgments, forecasts, and observed effects**, not a seventh working lens, foundational axiom, universal scoring rule, or substitute for domain validation and governance.

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

Normative questions need not have a single numerical ground truth. Assess factual premises, logical consistency, applicable norms, and procedure separately; do not promote a score into legitimacy.

## 3. Minimal testable claim

Where judgments or forecasts materially affect action, retain enough to reconstruct the following. These are **semantic responsibilities**, not requirements for one global database entity.

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

Check formal claims using proofs, counterexamples, or reproducible computations within their models. When applicability conditions change, requalify the claim before reusing it. Failure to find a counterexample is not a proof.

For empirical forecasts, specify a baseline, loss, evaluation population, and split strategy beforehand. For a binary outcome y in {0,1} with forecast probability p, one option is the Brier loss (p-y)², lower being better. For continuous targets, MAE may be appropriate. When applicable, also report calibration, subgroup behavior, interval coverage, and uncertainty. Do not silently double-count events.

- Separate training, tuning, and evaluation chronologically when time matters; prevent future information leakage.
- Compare against simple baselines and earlier versions on the same population, metric, and independently observed outcomes.
- Report limits from small samples, selective reporting, distribution shift, strategic adaptation, or unreliable labels; avoid spurious precision.
- If abstention is allowed, report both coverage and accuracy conditional on answering. Abstention is not a correct prediction.
- Observing the predicted result after an intervention does not, by itself, identify the intervention's causal effect.

## 5. Error attribution and reopening

Distinguish errors in facts/evidence, subject/framing, derivation, model/identification assumptions, time/population transport, objectives/scoring rules, measurements, stochastic variation, other actors' adaptation, and changing environments.

Procedure:

1. Check whether the outcome is due and independently observable; otherwise retain unknown status.
2. Reconstruct the ex ante claim, boundary, scope, sources, and model version.
3. Compare under the predeclared standard; test counterexamples, alternatives, and changing conditions where material.
4. Revise the particular fact, model, rule, or scope implicated by falsifiable errors. Do not rebuild a model from one random miss.
5. Retain immutable history while requalifying current validity. Reopen exploration, sufficiency, or decision when warranted; reopening never grants execution authority.

## 6. Multi-actor checks

Reported bids and observable behavior do not directly reveal internal preferences; rules and proposing rights can alter outcomes; individual optimality does not imply collective optimality; equilibrium need not be unique or fair; publishing a model may change actors' strategies.

Conditional game-theoretic predictions must specify repetition horizon, information, move order, preferences/utilities, and meaningful counterfactual changes.

See formal cases in [prediction](prediction.md) and [leverage](leverage.md).

## 7. Completion criteria and limits

- **Formal cases**: Reproduce the result, identify counterexamples, distinguish no solution from no solution found, and re-evaluate when key conditions change.
- **Empirical forecasts**: Require ex ante records, independent observations, fixed baselines, and repeatable errors. Do not claim measured improvement without actual outcomes.
- **Deployment**: Keep validation separate from authority, effect verification, and recovery in the [action chain](https://github.com/xiongweilin/aios/blob/main/docs/reference/guide/action-chain.md).
- **Proportionality**: Match verification effort to risk and irreversibility, rather than requiring complex persistence for every minor transition.

This protocol can make errors more detectable and improvements more falsifiable. It does not prove high accuracy or a unique universal judgment theory.
