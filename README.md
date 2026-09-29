# guide

![Repository: Public](https://img.shields.io/badge/repository-public-success.svg) [![Docs: EN / 中文](https://img.shields.io/badge/docs-EN%20%7C%20%E4%B8%AD%E6%96%87-blue.svg)](README.zh-CN.md)

[English](README.md) | [简体中文](README.zh-CN.md)

> A working framework for how **purposeful finite actors** form local boundaries in external reality, judge whether the next transition has sufficient grounds, act, receive feedback, and keep revising.

guide does not provide an ultimate ontology of the world. It does not identify reality with any current representation, model, classification, six-lens decomposition, engineering contract, or implementation.

## Minimal structure

The framework starts only from the following structure:

1. **External reality**: reality is not exhausted by any actor's current representation and continues to provide constraints, effects, counterexamples, and feedback.
2. **Multiple purposeful finite actors**: each actor has a finite lifetime and bounded sensing, representation, computation, resources, and control, and has at least some purpose, acceptability condition, constraint, or approach/avoid direction.
3. **Local current boundary**: an actor can form only a local, fallible, expirable, revisable representation of reality.
4. **Sufficiency**: for a current purpose and next transition, the actor needs local adequacy rather than complete knowledge.
5. **Action and feedback**: an actor can change conditions of future reality; effects and new observations enter later actor states.
6. **Lifecycle**: an actor emerges, undergoes reality, forms and revises boundaries, acts, and eventually terminates; actor termination does not erase effects already left in reality.

Minimal loop:

```text
                         external reality
                    ┌────────┴────────┐
                    │                 │
                 influence       effect / feedback
                    │                 ▲
                    ▼                 │
              purposeful finite actor│
                    │                 │
              current boundary B     │
                    │                 │
          S(B, purpose, transition)  │
             ┌──────┴──────┐         │
             │             │         │
   insufficient / uncertain sufficient
             │             │         │
      explore / revise   choose / act
             │             └─────────┘
             └──────► new current boundary
```

This is a working minimal structure, not a metaphysical claim that reality is ultimately composed only of these items.

## From the minimum to the working framework

- **Structural derivations**: representation is not reality, finite distinguishability, unresolved remainder, order, relation, and action-sensitive continuations;
- **Conditional derivations**: sufficiency, exploration / decision, and reopening require further conditions such as purpose, selectable action, exploration, or corrigibility;
- **Working decomposition**: the current framework uses distinction, relation, causality, temporality, possibility, and value as six lenses on the current boundary. They are not irreducible ontological primitives;
- **Engineering necessities**: Decision / Authorization / Effect / Outcome, idempotency, read-back, and recovery become correctness-critical only under additional engineering conditions and belong in `engineering/`.

## Documentation map

| Document | Role |
| --- | --- |
| [Minimal derivation](./framework/foundations/minimal-derivation.md) | What follows, follows conditionally, or does not follow from external reality and purposeful finite actors |
| [Theoretical sources](./framework/foundations/theoretical-sources.md) | Relations to bounded rationality, pragmatism, cybernetics, decision theory, multi-agent theory, and neighboring traditions |
| [Reality](./framework/reality.md) | External boundary, reality feedback, and non-identity with current representation |
| [Purposeful finite actor](./framework/purposeful-finite-actor.md) | Actor definition, finitude, purpose, capability, lifecycle, and termination |
| [Lifecycle](./framework/lifecycle.md) | General process from emergence to termination and epistemic / commitment transitions |
| [Sufficiency](./framework/sufficiency.md) | When a current boundary is adequate for a next transition |
| [Multi-actor](./framework/multi-actor.md) | Multiple local boundaries, shared reality, interaction, coordination, and conflict |
| [Six working lenses](./framework/dimensions/README.md) | Distinction, relation, causality, temporality, possibility, and value |
| [Activities](./framework/activities/README.md) | Exploration and decision as derived activity types |
| [Engineering action chain](./engineering/action-chain.md) | Correctness boundaries among decision, authorization, execution, effect, observation, verification, outcome, and recovery |
| [Precise semantics](./engineering/precise-semantics.md) | Implementable, verifiable engineering semantics that forbid silent substitution |
| [AIOS architecture](./engineering/aios-architecture.md) | A concrete expression in a long-running autonomous AI runtime |

English and Simplified Chinese are equal views. Semantic changes should update both languages with corresponding claim strength, formulas, tables, code blocks, and links.