# Qualification

[English](./qualification.md) | [简体中文](./qualification.zh-CN.md)

> Inspiration: the tension between rule by people and rule of law.

Qualification asks: **what conditions are sufficient for a candidate or state to enter the next state?**

It is not a universal score. It is the structure of grounds required for a state transition.

## Minimal state structure

`unmet → accumulating → sufficient → enter`

`Unmet` is a qualification state, not an epistemic negation. It may mean a condition is known false, evidence is missing, the state is unknown, or the required basis has simply not yet been established; those reasons should remain distinguishable.

“Accumulating” need not mean a numerical increase, and “sufficient” need not mean one scalar threshold. Conditions may include:

- necessary conditions becoming satisfied;
- evidence and counterevidence being distinguished;
- dependencies becoming valid;
- authority, approval, or commitment being established;
- verification completing;
- risk, cost, and residual unknowns becoming acceptable for the current purpose.

The core question is:

> Under the current object, scope, purpose, time scale, and conditions, what makes this transition valid now?

## Two qualification regimes

Reality does not always make sufficiency available in the same way. Keep at least two regimes distinct.

### Interpretive qualification

**Interpretive qualification** is used when the conditions for sufficiency cannot be completely fixed in advance. A participant must interpret the object, context, evidence, counterevidence, purpose, competing framings, and residual unknowns, then form an accountable judgment that the current basis is sufficient or insufficient.

This is common in open-ended questions, diagnosis, strategy, design, exception handling, novel cases, and judgments whose relevant variables or weights cannot be fully enumerated beforehand.

Interpretive qualification is not arbitrary. It should preserve at least:

- the object and transition being judged;
- scope, purpose, and time scale;
- evidence and counterevidence;
- assumptions and default distinctions;
- competing interpretations or candidates that materially matter;
- residual unknowns and accepted risk;
- reasons for closure;
- who is accountable for the judgment;
- review and reopening conditions.

So:

`judgment is reasoned != criterion was fully specified in advance`

`interpretive sufficiency != universal truth`

### Specified qualification

**Specified qualification** is used when the relevant conditions have already been made explicit enough to check: a rule, predicate, threshold, state-machine guard, protocol, test, contract, approval set, or equivalent specification defines what counts as sufficient for the current transition.

Examples include an age threshold, required signatures, a schema constraint, a test suite, a policy predicate, or a versioned authorization condition.

Specified qualification should preserve at least:

- the rule or contract identity and version;
- its authority or source;
- applicability scope and effective period;
- required inputs and their versions;
- predicates, thresholds, or required conditions;
- evaluator and evaluation result;
- exceptions, override rules, and reopening conditions.

A clear rule only makes evaluation more determinate. It does not establish the rule's own applicability, authority, current validity, or value.

So:

`rule is explicit != rule is qualified for this case`

`predicate evaluates true != transition is automatically authorized`

### Tension, combination, and conversion

The two regimes solve different problems and create a persistent tension:

- specified qualification increases determinacy, repeatability, and automation, but only inside the distinctions and conditions already encoded;
- interpretive qualification can handle ambiguity, novelty, and incomplete specification, but requires accountable judgment and leaves more room for disagreement and revision.

Many real activities are **hybrid**. Hybrid is not a third primitive regime; it is an explicit composition of interpretive and specified qualification slices. A transition may require specified gates plus an interpretive closure, or an interpretive judgment may first decide whether a specified rule applies.

They can also convert over time:

`repeated interpretation → explicit rule-making → specified qualification`

`novel case / rule ambiguity / changed basis → reopening → interpretive qualification`

But conversion must be explicit. A past interpretation does not silently become a deterministic rule, and a satisfied deterministic rule does not eliminate the need to interpret whether that rule still applies.

## Qualification slice

A concrete qualification slice should identify at least:

- the primitive qualification regime(s): interpretive and/or specified, whether they are composed, and why;
- the current object or state;
- the intended next state;
- scope, purpose, and time scale;
- conditions that must be satisfied and preserved;
- degrees of freedom that remain open;
- supporting basis;
- who proposes, evaluates or judges, authorizes, verifies, and reopens;
- conditions for invalidation, exit, review, and revalidation.

Different domains have different qualification conditions. One global `qualified = true` cannot preserve all of these meanings.

A shared status such as `sufficient` does not erase the regime that produced it. Two records with the same result but different qualification regimes do not carry the same semantics.

## Qualification contraction

Qualification is not only about the final moment of entry or closure. Many intermediate operations reduce the degrees of freedom that remain open:

- rejecting a candidate;
- stopping search;
- fixing an interpretation;
- freezing an interface or verification standard;
- narrowing scope;
- restricting action;
- turning a provisional arrangement into a commitment.

These are forms of **qualification contraction**.

`open space → qualified contraction → convergence → provisional closure`

Each contraction needs grounds proportional to what it excludes or freezes. “Not generated,” “not currently visible,” or “not found with current resources” cannot silently become “impossible.” A constraint or verification standard that has already been qualified for a slice also cannot be rewritten merely because the current implementation fails to satisfy it.

Closure is therefore not the first point where qualification matters; it is a special point reached after a sequence of qualified contractions.

## Responsibility and qualification are orthogonal

Responsibility asks **who** is accountable for defining, proposing, judging, authorizing, executing, verifying, stopping, repairing, recording, or reopening.

Qualification asks whether the **current basis is sufficient** for the transition under consideration.

Keep separate:

`responsible role exists != qualification conditions are satisfied`

`qualification conditions are satisfied != authority is automatically granted`

A role can own a judgment without being entitled to fabricate its evidence or prerequisites. Conversely, a basis can be sufficient while the relevant authority still belongs to someone else.

## Qualification does not silently inherit

The central rule is:

`valid at one layer != automatically valid at the next`

For example:

`default distinction != structure of the World`

`question can be asked != question is qualified`

`question is qualified != answer is reliable`

`evidence exists != judgment is sufficient`

`judgment is sufficient != goal is worth committing to`

`goal is worth committing to != someone has authority to decide`

`authority to decide != current execution permission`

`request succeeded != real-world effect occurred`

`effect occurred != goal is complete`

`goal complete != long-term validity continues`

Many serious failures are not total errors at one step. They are cases where qualification from one slice is silently promoted into another.

## Closure and reopening

Finite activity cannot keep all possibilities open forever. A common cycle is:

`open → converge → provisional closure → continue → conditions change → review / reopen`

Closure means only that support is sufficient for the current purpose. It does not mean permanent truth.

Material changes in facts, scope, dependencies, authority, value, cost, risk, or environment should trigger review, revalidation, or reopening.

Reopening restores candidate and choice space. It does not automatically create a new answer, decision, or authority.

## Finite closure and meta-qualification

A qualification judgment is itself a claim and may need review, but the framework does not require an infinite stack of meta-qualification judgments before anything can proceed.

Each qualification slice closes only locally: its object, scope, purpose, time scale, supporting basis, authority, residual unknowns, and reopening conditions must be sufficient for the transition currently being considered. If the validity of that basis later becomes material to another transition, it becomes an explicit object of review or revalidation.

So:

`provisional local closure != absolute foundation`

`qualification may be reviewed != every qualification requires an endless prior qualification`

## State and transition

A resulting state may be acceptable while the path used to reach it was invalid.

Qualification therefore checks both:

- whether the current state is acceptable;
- whether the transition from the previous state had valid grounds.

A valid endpoint cannot retroactively prove a valid path.

## Cross-domain transfer strength

When a structure appears across domains, keep at least three levels of transfer distinct:

1. **Shared problem**: only the question or framing transfers.
2. **Formal similarity**: a representation, comparison, or computational structure can transfer.
3. **Mechanism similarity**: limited prediction or intervention experience can transfer only when the relevant objects, boundary conditions, and mechanisms are sufficiently alike.

`formal similarity != mechanism evidence`

A structure that has mechanism-level support in one domain does not inherit the same status in another domain. Cross-domain reuse therefore needs its own qualification rather than being justified by vocabulary or shape alone.

## Boundary with the other dimensions

Qualification depends on [distinction](./distinction.md), but cannot be inferred from it. It governs transitions involving [value](./value.md), [capability](./capability.md), [change](./change.md), and [others](./others.md), while never replacing the content of those dimensions.
