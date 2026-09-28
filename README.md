# guide

![Repository: Public](https://img.shields.io/badge/repository-public-success.svg) [![Docs: EN / 中文](https://img.shields.io/badge/docs-EN%20%7C%20%E4%B8%AD%E6%96%87-blue.svg)](README.zh-CN.md)

[English](README.md) | [简体中文](README.zh-CN.md)

> Make clear what we distinguish, what is sufficient, what is worth pursuing, what can be done, how structures change, and how people affect one another.

An index of ideas and methods about the **basic structure of human activity and its engineering expression**.

Individuals, families, teams, organizations, institutions, Agents, and technical systems can all be objects of analysis. Agent is only a formal term for a participant capable of taking part in the current activity; it is not a prerequisite for the framework.

## World boundary

This repository keeps the **World** as a cognitive boundary.

Current observations, language, models, classifications, schemas, ontologies, and knowledge graphs are not entitled by default to count as the complete structure of the World simply because they are usable. The documents concern **human activity within a distinguishable world**, not a final ontology of the World itself.

Keep at least:

- **World (cognitive boundary)**: what remains beyond the current representation stays open;
- **distinguishable world / distinguishable range**: distinctions that could in principle be formed under current sensing, language, tools, interaction, capability, and interfaces;
- **distinguished range**: distinctions already acquired, formed, and currently invocable;
- **default distinctions**: classifications and boundaries silently inherited from language, culture, interfaces, institutions, historical decisions, or existing models.

Therefore:

`current representation != the World itself`

`absent from current representation != nonexistent != impossible`

## Six basic dimensions of human activity

The same activity should retain at least six analytical dimensions that cannot silently substitute for one another. They are not assumed to be independent, orthogonal, or at the same logical level:

| Dimension | Minimal structure | Core question |
| --- | --- | --- |
| [**Distinction**](./theory/distinction.md) | `World boundary → distinguishable world / range → distinguished range` | What can become distinguishable, what has been distinguished, and what remains outside the current representation? |
| [**Qualification**](./theory/qualification.md) | `interpretive / specified` + `unmet → accumulating → sufficient → enter` | What conditions are sufficient, and is sufficiency being interpreted or checked against a specified rule? |
| [**Value**](./theory/value.md) | `external norms ↔ internal norms` | What is worth pursuing, required, rejected, or refused? |
| [**Capability**](./theory/capability.md) | `unknown / cannot / capable` + `self / assisted / leverage` | Which outcomes are currently realizable, how is that known, and through what means? |
| [**Change**](./theory/change.md) | `stable / transitional / no stable structure` | Are we facing a persistent structure, a transition, or no stable structure yet? |
| [**Others**](./theory/others.md) | `relation strength × alignment / conflict` | Who affects whom, and in which dimensions are they aligned or in conflict? |

The six dimensions are not six kinds of object and not six independent axes. They are non-substitutable analytical dimensions of the same activity. They can constrain one another and form feedback loops.

The six dimensions are **equally basic within this framework**. None is the master dimension, and none is entitled to define the content of the other five. Distinction asks what can enter representation; Qualification asks what grounds are sufficient for a transition; Value asks what is worth pursuing or refusing; Capability asks what is currently realizable and by what means; Change asks what persists, transitions, or requires reopening; Others asks how multiple participants, relations, power, recognition, alignment, and conflict alter the activity. Each dimension can constrain, challenge, or reopen the others.

Qualification remains transition semantics within this set, not a higher-order owner of the framework. It has two basic regimes in tension: **interpretive qualification**, where sufficiency is established through accountable judgment over context and evidence, and **specified qualification**, where sufficiency is checked against an explicit rule, predicate, threshold, or contract. Real activities can combine both, but they cannot silently substitute for one another. Distinction and capability form one important feedback loop: current capability, tools, interfaces, and others constrain what can become distinguishable; newly formed distinctions can reveal or create new reachable paths. Other dimensions form their own feedback relations as well. The reading order is navigational, not an ontological derivation, priority order, or one-way causal stack.

For example:

`can do != worth doing`

`worth doing != qualified to act`

`stable now != valid indefinitely`

`my distinctions / values / authority != others' distinctions / values / recognition`

## Non-substitution across the six dimensions

The common rule across the repository is: **what holds at one layer does not silently establish another layer.**

Typical boundaries include:

`default distinction != structure of the World`

`question can be asked != question is qualified`

`question is qualified != answer is reliable`

`interpretive qualification != specified qualification`

`specified rule satisfied != rule is applicable / current / authoritative`

`judgment is sufficient != goal is worth committing to`

`worth doing != capable of doing`

`capable of doing != authorized to do`

`authorized != executed`

`execution success != real-world effect occurred`

`effect occurred != goal completed`

`historically valid != currently valid`

The theory explains these boundaries through the six dimensions. Precise Semantics and AIOS preserve them in engineering systems.

## Framework completeness and self-challenge

This framework does not define completeness as “all final questions already have answers.”

A more useful standard is:

`unknown is not disguised as known`

`missing responsibility is not silently substituted`

`a boundary knows how to hand off, reopen, or stop`

A framework can therefore remain incomplete in capability while still being responsible about where its current claims end.

The framework itself is not exempt from these rules. **This guide is a revisable working framework, not a source of truth about the World.** Its categories, distinctions, qualification rules, value framings, capability models, change models, and representations of others are all fallible. Reality-side observation, counterexamples, failed predictions, failed interventions, unanticipated effects, and better framings can give people sufficient reason to narrow, revise, replace, or stop using a claim or framework.

### No proof obligation for the number of dimensions

This guide does not attempt to prove why there are exactly six dimensions, and it will not create a new proof obligation if the number of dimensions changes later.

The current dimensional count is a **working closure**: it is sufficient when it helps distinguish real problems, prevents important substitutions, supports useful action and engineering, and remains responsive to reality-side failure. That is enough for current use.

So:

`current six dimensions are useful != reality has exactly six fundamental dimensions`

`dimension count changed != the old count must first be disproved`

`framework works well enough for current purposes != framework has reached a final foundation`

The framework does not recurse indefinitely into “why exactly this many dimensions?” If further questioning is not producing materially better distinctions, decisions, predictions, actions, or corrections, the count may remain provisionally closed. Reality can reopen it later.

### No formal proof obligation; evaluate by use

This guide will not attempt to establish the framework itself through formal proof. It may use precise definitions, symbolic shorthand, state machines, invariants, tests, or domain-specific formal verification when those tools improve clarity or engineering, but none of them proves that the guide is a true or final structure of the World.

The guide is evaluated primarily through six practical indicators:

| Indicator | Use question |
| --- | --- |
| **Correctness** | Do the distinctions, judgments, actions, and resulting claims remain consistent with available reality-side evidence, intended semantics, and observed outcomes? |
| **Usability** | Can people and systems understand, apply, maintain, and revise the framework without disproportionate friction? |
| **Reliability** | Under repeated use, variation, failure, and changing conditions, does the framework continue to produce dependable guidance and support correction or recovery? |
| **Performance** | Does using the framework produce decisions, coordination, or engineering results with acceptable latency, responsiveness, and throughput for the task? |
| **Capacity / scalability** | Can the framework remain usable as users, data, tasks, domains, dependencies, and interaction complexity grow, without unacceptable degradation? |
| **Efficiency** | Are useful results obtained with proportionate time, computation, money, attention, coordination, maintenance, and opportunity cost? |

These six indicators are **usage guidance**, not six new theoretical dimensions, axioms, or a proof obligation. The guide does not prove why these are exactly six either. Their relevance, measurement method, threshold, and weighting depend on the concrete use.

So:

`formal precision != formal proof of the framework`

`local formal verification != proof that the guide is true`

`good score on one indicator != overall adequacy`

`current use is good enough across relevant indicators != permanent validity`

When the relevant indicators are good enough for the current purpose, use may close provisionally without further foundational proof. When reality-side results deteriorate, the framework can be reopened by the people using it.

### Retirement is not a self-enforcing rule

A theory is not an acting subject. It cannot guarantee that people will obey its own review, replacement, or retirement guidance.

The same theory can remain useful to one person, become obsolete for another, be partially retained by a third, and be abandoned at different times. There is no requirement that retirement be synchronized across people, organizations, or contexts.

Therefore this guide does not define an impossible rule such as “the theory must retire itself when condition X is met.” It can only provide signals that may justify review, narrowing, replacement, archival, or non-use. Whether those actions happen is a matter for living participants, their contexts, their values, their capabilities, and their relations.

So:

`theory states a retirement condition != theory can enforce retirement`

`one user stops using the theory != all users should stop at the same time`

`continued use by someone != proof that the theory remains adequate everywhere`

Revision and retirement are therefore **human practices around the framework**, not autonomous behaviors of the framework itself.

A competing framing or theory does not need to translate itself into the current six-dimensional vocabulary before it can expose a blind spot or failure. Semantic mapping becomes necessary when integrating, federating, or migrating between frameworks, not as a precondition for challenge. Internal coherence is not sufficient protection against reality-side failure.

People have reason to reopen the core when repeated real problems cannot be located or handed off, when “keep open / unknown” stops producing new distinctions or useful stopping conditions, or when maintaining the framework requires growing special cases without proportional value. These are review signals, not self-executing commands issued by the framework.

A practical maintenance cycle is therefore:

`use → encounter reality / counterexamples → accumulate failures → people revise, narrow, replace, archive, or stop using when sufficiently warranted`

not continuous expansion of the core, not infinite justification of the current dimension count, and not a claim that all users will update or retire the framework together.

## Document structure

English and Simplified Chinese are two co-authoritative views of the same documents, not primary and secondary editions. Every semantic change must update both language versions together. Section structure, claim strength, examples, formulas, tables, code blocks, links, and revision boundaries should correspond; wording may differ only as required for natural translation.

The repository root keeps only three conceptual documents:

| Document | Role |
| --- | --- |
| **README** | World boundary, six-dimension map, and repository entry point |
| [**Precise Semantics**](./precise-semantics.md) | turns theoretical boundaries into implementable, verifiable engineering semantics that resist silent substitution |
| [**AIOS Architecture**](./aios-architecture.md) | shows how these boundaries are realized in a continuously operating AI runtime |

Theory lives under `theory/`:

1. [Distinction](./theory/distinction.md)
2. [Qualification](./theory/qualification.md)
3. [Value](./theory/value.md)
4. [Capability](./theory/capability.md)
5. [Change](./theory/change.md)
6. [Others](./theory/others.md)

## Suggested reading

For the framework itself, read the six files in `theory/` in whatever order best matches the problem. The listed order is navigational, not a ranking of importance.

For the engineering expression, read this page and then [Precise Semantics](./precise-semantics.md).

For one concrete implementation, continue to [AIOS Architecture](./aios-architecture.md).

The six dimensions are basic analytical dimensions of human activity. AIOS is one engineering application of them.
