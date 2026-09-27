# Qualification

[English](./qualification.md) | [简体中文](./qualification.zh-CN.md)

Qualification asks: **what conditions are sufficient for a candidate or state to enter the next state?**

It is not a universal score. It is the structure of grounds required for a state transition.

## Minimal state structure

`unmet → accumulating → sufficient → enter`

“Accumulating” need not mean a numerical increase, and “sufficient” need not mean one scalar threshold. Conditions may include:

- necessary conditions becoming satisfied;
- evidence and counterevidence being distinguished;
- dependencies becoming valid;
- authority, approval, or commitment being established;
- verification completing;
- risk, cost, and residual unknowns becoming acceptable for the current purpose.

The core question is:

> Under the current object, scope, purpose, time scale, and conditions, what makes this transition valid now?

## Qualification slice

A concrete qualification judgment should identify at least:

- the current object or state;
- the intended next state;
- scope, purpose, and time scale;
- conditions that must be satisfied and preserved;
- degrees of freedom that remain open;
- supporting basis;
- who proposes, judges, authorizes, verifies, and reopens;
- conditions for invalidation, exit, review, and revalidation.

Different domains have different qualification conditions. One global `qualified = true` cannot preserve all of these meanings.

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

A qualification judgment is itself a claim and may need review, but the framework does not require an infinite stack of meta-qualification records before anything can proceed.

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

## Boundary with the other dimensions

Qualification depends on [distinction](./distinction.md), but cannot be inferred from it. It governs transitions involving [value](./value.md), [capability](./capability.md), [change](./change.md), and [others](./others.md), while never replacing the content of those dimensions.
