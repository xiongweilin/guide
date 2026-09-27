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

The same activity should retain at least six coordinates that cannot silently substitute for one another:

| Dimension | Minimal structure | Core question |
| --- | --- | --- |
| [**Distinction**](./theory/distinction.md) | `World boundary → distinguishable world / range → distinguished range` | What has entered the current world, and what has not? |
| [**Qualification**](./theory/qualification.md) | `unmet → accumulating → sufficient → enter` | What conditions are sufficient for a candidate or state to advance? |
| [**Value**](./theory/value.md) | `external norms ↔ internal norms` | What is worth pursuing, required, rejected, or refused? |
| [**Capability**](./theory/capability.md) | `cannot → self-capable → assisted-capable → leverage-capable` | Which outcomes are currently realizable, and through what means? |
| [**Change**](./theory/change.md) | `stable / transitional / no stable structure` | Are we facing a persistent structure, a transition, or no stable structure yet? |
| [**Others**](./theory/others.md) | `relation strength × alignment / conflict` | Who affects whom, and in which dimensions are they aligned or in conflict? |

The six dimensions are not six kinds of object. They are six coordinates of the same activity.

For example:

`can do != worth doing`

`worth doing != qualified to act`

`stable now != valid indefinitely`

`my distinctions / values / authority != others' distinctions / values / recognition`

## Qualification and non-substitution

The common rule across the repository is: **what holds at one layer does not silently establish another layer.**

Typical boundaries include:

`default distinction != structure of the World`

`question can be asked != question is qualified`

`question is qualified != answer is reliable`

`judgment is sufficient != goal is worth committing to`

`worth doing != capable of doing`

`capable of doing != authorized to do`

`authorized != executed`

`execution success != real-world effect occurred`

`effect occurred != goal completed`

`historically valid != currently valid`

The theory explains these boundaries through the six dimensions. Precise Semantics and AIOS preserve them in engineering systems.

## Document structure

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

For the framework itself, read the six files in `theory/` in order.

For the engineering expression, read this page and then [Precise Semantics](./precise-semantics.md).

For one concrete implementation, continue to [AIOS Architecture](./aios-architecture.md).

The six dimensions are basic coordinates of human activity. AIOS is one engineering application of them.
