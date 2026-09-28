# Exploration

[English](./exploration.md) | [简体中文](./exploration.zh-CN.md)

Exploration is the activity used when the current boundary is **insufficient or materially uncertain**. It is not a dimension.

Exploration asks:

> When is the current boundary insufficient for the current purpose, what kinds of candidates may be missing beyond it, is further exploration worth its cost now, and how should the boundary be reopened without disguising unknowns as knowns?

## 1. What exploration handles

At minimum distinguish:

1. unknown values inside known structure;
2. incomplete candidate space;
3. currently inaccessible but potentially important content.

`unknown value != missing candidate != currently inaccessible`

`boundary has a gap != missing structure is already known`

Exploration mainly handles the latter two, but it can also acquire a missing value when that value could materially change the decision.

## 2. Signals for reopening

Typical signals include:

- persistent counterexamples or unclassifiable residuals;
- repeated failure of prediction, explanation, coordination, or intervention;
- growing special cases;
- important outcome change without corresponding structure in the model;
- persistent disagreement not reducible to known factual or value differences;
- assumed transfer failing in a new context;
- new participants, tools, sensors, interfaces, permissions, or data sources;
- material changes in relations, environment, dependencies, time scale, authority, value, or risk;
- a high-impact decision highly sensitive to an unresolved assumption;
- the system losing the ability to recover, exit, or generate alternatives.

These are reopening signals, not proof that a particular alternative is correct.

## 3. Whether to explore now

Unknowns do not create an unlimited duty to explore. Consider at least:

- **decision sensitivity**: could the missing content change choice or commitment?
- **discriminative value**: is there an observation or probe that can distinguish important candidates?
- **cost**: time, attention, computation, money, coordination, opportunity cost;
- **risk / irreversibility**: could exploration itself cause harm, lock-in, privacy, or rights impacts?
- **urgency**: what is lost by delay?
- **reversibility of acting now**: can the system safely try a recoverable path first?
- **future option value**: can exploration preserve or create important options?
- **current sufficiency**: even if incomplete in principle, is the current boundary already enough for the next step?

These considerations need not collapse into one numerical objective.

Possible dispositions include retaining the boundary, local probing, reopening a particular assumption or dimension, expanding candidate space, reframing the problem, deferring exploration while retaining unknowns and triggers, or stopping because current exploration lacks grounds, authority, or safety.

## 4. Candidate generation without circular admission

Exploration can generate:

- different object boundaries;
- different relation structures;
- different causal mechanisms;
- different time scales;
- missing participants;
- different possible paths;
- different evidence sources or interfaces;
- different value framings and constraints;
- different institutional or execution arrangements;
- competing problem framings.

A competing framing need not first translate into the current framework before it can challenge it.

`challenge admission != semantic migration`

## 5. Increase discrimination, not only data volume

A useful exploration question is:

> Which observation, comparison, experiment, interaction, or bounded intervention would best distinguish the competing candidates that still matter?

Actions can include independent sources, changed measurement interfaces, participants with different local boundaries, counterexamples, boundary cases, recoverable experiments, changing one relevant condition, comparing competing predictions, new tools, or bounded alternative paths.

`more observations != more discriminating evidence`

`higher model confidence != boundary sufficient`

`can run experiment != authorized to run experiment`

## 6. Depth of reopening

Exploration can occur at different depths:

1. acquire a value;
2. revise a local distinction or relation;
3. revise causal or temporal structure;
4. expand candidate space;
5. reframe the problem;
6. challenge the framework.

Prefer the shallowest reopening that materially resolves the issue, but do not stay shallow merely to protect the old structure.

## 7. Stopping exploration

Provisional closure can be justified when:

- remaining candidates are unlikely to change the decision;
- important competing candidates are sufficiently distinguished within current capability;
- further information has little practical value relative to cost;
- delay risk exceeds residual-unknown risk;
- the next probe is unsafe, unauthorized, or irreversible;
- a recoverable path is available and preserves correction capability;
- unresolved parts can be carried explicitly as unknown.

At closure preserve what was explored, what was excluded and why, what remains unknown, which boundary is provisionally accepted, what triggers review, and what new tool, permission, evidence, or event would make exploration worthwhile again.

`stop exploring != no unknowns`

`provisional closure != permanent completeness`

## 8. Common failures

- premature closure;
- infinite exploration;
- admitting only challenges expressible in current vocabulary;
- assuming novelty is superiority;
- accumulating data without increasing discrimination;
- using information value to override authority, safety, or rights;
- reporting impossibility because no path was found;
- globally discarding useful structure after a local failure.

The goal is not maximum openness but **proportionate reopenability**.

## 9. Relation to dimensions and sufficiency

Exploration uses all six dimensions:

- distinction: what boundary should reopen?
- relation: which participants, dependencies, powers, or structures were omitted?
- causality: which competing mechanisms need discrimination?
- temporality: did failure come from transition, delay, or stale grounds?
- possibility: is candidate space incomplete?
- value: which unknowns justify cost or risk?

[Sufficiency](../sufficiency.md) controls when exploration starts, continues, and stops.

When exploration produces a new provisional boundary, activity can move to [Decision](./decision.md); reality-side feedback after action may start exploration again.
