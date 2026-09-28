# Sufficiency operator

[English](./sufficiency.md) | [简体中文](./sufficiency.zh-CN.md)

Sufficiency is the **operator** of this framework, not a seventh dimension.

It asks:

> Is the current boundary sufficient for the current purpose and next transition?

Abstractly:

`S(B, P, T) → {insufficient, materially uncertain, sufficient}`

where:

- (B): the current six-dimensional boundary and its epistemic status;
- (P): the current purpose;
- (T): the next transition, such as continued exploration, candidate exclusion, decision, authorization, execution, verification, or completion.

Sufficiency is not a property of reality itself. It is a relation among current boundary, purpose, and transition.

## 1. Minimal states

`unmet → accumulating → sufficient → enter`

"Unmet" may mean a condition is known false, evidence is missing, state is unknown, required grounds are absent, or applicability of a rule remains disputed. These causes must not collapse into one boolean.

"Accumulating" does not require numerical increase. Grounds may include:

- necessary conditions being met;
- evidence and counterevidence being distinguished;
- dependencies becoming valid;
- permissions, approvals, or commitments being established;
- verification completed;
- risk, cost, and residual unknowns acceptable for the current purpose.

## 2. Two basic mechanisms

### Interpretive sufficiency

When "what counts as enough" cannot be fully specified in advance, a finite system forms an accountable judgment over context, evidence, counterevidence, competing interpretations, purpose, and residual unknowns.

Open problems, diagnosis, strategy, design, exception handling, and novel cases commonly require interpretive sufficiency.

At minimum preserve:

- object and transition under judgment;
- scope, purpose, and time scale;
- evidence and counterevidence;
- assumptions and default distinctions;
- competing interpretations that could materially change the result;
- residual unknowns and accepted risk;
- reason for provisional closure;
- accountable judgment;
- review and reopening conditions.

`reasoned judgment != criteria were fully specified in advance`

`interpretive sufficiency != universal truth`

### Specified sufficiency

When relevant conditions are explicit enough to check, use a rule, predicate, threshold, state-machine guard, protocol, test, contract, or approval set.

At minimum preserve:

- rule / contract identity and version;
- authority or source;
- applicability and validity interval;
- inputs and versions;
- predicates, thresholds, or necessary conditions;
- evaluator and result;
- exceptions, overrides, and reopening conditions.

`rule explicit != rule applicable to the current object`

`predicate true != transition automatically authorized`

### Combination and conversion

Real activity can combine both mechanisms, for example interpreting whether a rule applies before running the specified check.

`repeated interpretation → explicit rulemaking → specified checking`

`novel case / ambiguity / changed grounds → reopen → interpretive judgment`

Past interpretation must not silently become a deterministic rule. Rule satisfaction must not erase questions of applicability, freshness, or authority.

## 3. Sufficiency slice

A concrete sufficiency judgment only needs context proportionate to the transition:

- transition under judgment;
- current boundary version;
- purpose, scope, and time scale;
- supporting grounds;
- remaining unknowns;
- excluded or frozen candidates;
- rule maker, judge, decider, and authorizer where relevant;
- invalidation, review, and reopening conditions.

"Enough" is not one global boolean shared by all transitions.

`enough to answer != enough to authorize action`

`enough to execute != enough to confirm effect`

`enough to confirm effect != enough to declare all goals complete`

## 4. Sufficiently grounded contraction

When a system excludes candidates, stops search, freezes standards, or turns a provisional arrangement into commitment, it narrows possibility space.

Only when it actually claims "there are sufficient grounds to exclude or freeze" is this a sufficiency contraction:

`open space → sufficiently grounded contraction → provisional closure`

`fewer options != automatically sufficient`

"Not generated," "currently invisible," or "not found under current resources" cannot silently become "impossible."

## 5. Definition, judgment, and decision power

At minimum distinguish:

1. **definition power**: defining problem boundary, candidate space, evidence, criteria, thresholds, verification standards, and completion conditions;
2. **judgment power**: deciding whether current grounds meet the conditions or are sufficient;
3. **decision power**: deciding whether that judgment becomes commitment, resource allocation, rule adoption, action, continuation, pause, or termination.

`definition power != judgment power != decision power`

The same participant may occupy several positions in low-risk activity, but increasing scope, irreversibility, dependency, or power asymmetry increases the need for independent evidence, constrained rule-change authority, review, appeal, veto, or stopping paths.

A failure pattern to prevent is:

`define rule → judge own compliance → decide consequence → change rule when inconvenient`

Sufficiency itself does not create authority.

## 6. Responsibility and sufficiency are orthogonal

Responsibility asks "who is responsible?" Sufficiency asks "are the grounds enough?"

`responsible role exists != grounds are sufficient`

`grounds sufficient != authority automatically granted`

A role cannot manufacture missing evidence, conditions, or authority.

## 7. No silent shortcut

If moving from (X) to (Y) materially depends on an intermediate responsibility or evidentiary position (R), it cannot be silently omitted:

`X → R → Y`, not `X → Y`.

A missing position should be established explicitly, handed off, kept open, or stopped rather than replaced by an adjacent state.

## 8. Composition does not automatically hold

`S(C1) + S(C2) + ... != S(C1 ∘ C2 ∘ ...)`

Local components being sufficient does not establish joint compatibility. A composition-level sufficiency basis is needed when composition introduces new scope, assumptions, authority, dependencies, side effects, feedback, or failure propagation.

## 9. Handoff completeness

A consequential handoff should preserve enough context to prevent downstream overclaiming:

- current conclusion and scope;
- purpose and time scale;
- supporting grounds;
- key assumptions;
- residual unknowns;
- important alternatives;
- invalidation, review, and reopening conditions;
- authority boundary.

`handoff complete != downstream automatically has stronger sufficiency`

A handoff does not create broader scope, stronger evidence, new authority, or permanent validity.

## 10. Provisional closure and reopening

A finite system needs:

`open → converge → provisional closure → act → reality-side feedback → retain / reopen`

Closure is local to the current object, scope, purpose, time scale, and grounds. It is not permanent truth.

Material changes in facts, scope, relations, causal assumptions, dependencies, authority, value, cost, risk, or environment can trigger reevaluation.

`provisional closure != absolute foundation`

`revisable != requires infinite meta-review`

## 11. State and transition

A result state can be acceptable while the path that produced it was invalid.

Sufficiency can therefore apply both to a target state and to the transition itself.

`valid endpoint != valid path`

## 12. Cross-domain transfer

Cross-domain reuse should distinguish:

- common problem;
- formal similarity;
- mechanism similarity.

`formal similarity != mechanism-level sufficiency`

Success in domain A does not automatically establish sufficiency in domain B. Transfer itself requires proportionate grounds.
