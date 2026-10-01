# guide

![Repository: Public](https://img.shields.io/badge/repository-public-success.svg) [![Docs: EN / 中文](https://img.shields.io/badge/docs-EN%20%7C%20%E4%B8%AD%E6%96%87-blue.svg)](README.zh-CN.md)

[English](README.md) | [简体中文](README.zh-CN.md)

> A working framework that starts from **minimal self-reference under external reality**, then adds only the conditions needed for finite agency, purpose, local sufficiency, action, feedback, and revision.

guide does not provide an ultimate ontology of the world. It does not identify reality with any current representation, model, classification, six-lens decomposition, engineering contract, or implementation.

## Minimal structure

The foundation starts only from three conditions:

1. **External constraint**: reality is not exhausted by the current representation and continues to constrain it.
2. **Reflexive distinction**: the process making distinctions distinguishes itself from non-self reality.
3. **Retained re-entry**: that self / non-self difference enters and remains in the current representation and can again become an object of the distinction process that produced it.

Together these conditions are sufficient only for the weakest **minimal self-reference** used by guide. They do not by themselves establish a continuing self, a self-model, agency, purpose, consciousness, or normativity.

Minimal self-reference:

```text
external reality
      │
      │ constraint
      ▼
distinction process
      │
      ├──► self / non-self difference
      │              │
      │              ▼
      │       current representation
      │              │
      └──────────────┘
             re-entry
```

The working subject is obtained along the main dependency spine by adding further conditions:

- **identity continuity** → the self-side can be retained as the same continuing process across later distinctions;
- **agency** → some executable transitions change conditions of future reality;
- **finitude** → lifetime, sensing, representation, computation, resources, and control are bounded;
- **purposefulness** → some continuations, paths, constraints, or outcomes matter differently for action.

Only at that point does guide use the working subject **purposeful finite actor**.

A corrigible self-model is a separate strengthening: reality-side mismatch must be able to revise retained self-related content. It is not required merely for actor status.

For actors that can continue acquiring distinctions or enter commitment-bearing action, a local sufficiency problem appears:

```text
Reality ↔ purposeful finite actor
                 │
          current boundary B
                 │
        S(B, purpose, transition)
           ┌─────┴─────┐
           │           │
       insufficient   sufficient
       / uncertain       │
           │             │
     explore / revise  choose / act
           │             │
           └──────► reality
                       │
                  effect / feedback
                       │
                 retain / revise /
                     reopen
```

The order above is a dependency order for the framework, not a claim that every real system develops through these stages chronologically.

## From the minimum to the working framework

- **Foundation**: minimal self-reference, continuity, agency, finitude, and purpose form the main dependency spine; corrigible self-modeling remains an additional branch rather than a hidden actor requirement;
- **Conditional derivations**: sufficiency, exploration / decision, and reopening require additional capabilities such as an explore / commit alternative or corrigibility;
- **Working decomposition**: distinction, relation, causality, temporality, possibility, and value are six lenses on a current boundary, not irreducible ontological primitives;
- **Engineering necessities**: Decision / Authorization / Effect / Outcome, idempotency, read-back, and recovery become correctness-critical only under additional engineering conditions and remain in `engineering/`.

## Three-layer documentation architecture

guide is organized into three layers that answer different questions and should
not substitute for one another:

1. **Foundation layer** (`framework/foundations/`): states the minimal starting
   conditions, the working dependency spine adopted here, and the theoretical
   sources and scope limits behind those claims.
2. **Framework layer** (`framework/`): describes reality, purposeful finite
   actors, lifecycle, sufficiency, multi-actor interaction, the six working
   lenses, and exploration / decision as analysis concepts. It does not directly
   prescribe databases, services, or state machines.
3. **Engineering and application layer** (`engineering/`): promotes only those
   distinctions whose collapse creates concrete correctness failures into
   implementable semantics, action-chain boundaries, and the AIOS application.

The foundation explains why particular premises and dependencies are adopted;
the framework explains how finite action is analyzed; engineering explains
which distinctions an implementation must preserve. Higher layers may depend on
lower ones, but implementation structure is not evidence for foundational
ontology.

## Formalization status

A mathematically explicit subset of guide is formalized in
[distinction-self-reference-lean](https://github.com/xiongweilin/distinction-self-reference-lean).
The formal layer includes the separation of effective finitude from finite state
spaces, an exact no-ambiguity criterion for local sufficiency, constructive
conditions for conditional composition, dependency-aware evidence validity and
version migration, evaluator grounding, and structure-preserving framework
translations.

Those Lean results prove claims inside explicit models. They do **not** turn the
whole philosophical framework into a theorem, and they do not prove that guide
is the unique or absolutely minimal theory of actors. The formal dependency
spine corresponding to guide is isolated in `GuideCore.lean`.

## Documentation map

| Document | Role |
| --- | --- |
| [Minimal derivation](./framework/foundations/minimal-derivation.md) | Layered conditions from minimal self-reference to purposeful finite actors, sufficiency, feedback, and multi-actor structure |
| [Theoretical sources](./framework/foundations/theoretical-sources.md) | Relations to bounded rationality, pragmatism, cybernetics, decision theory, multi-agent theory, and neighboring traditions |
| [Reality](./framework/reality.md) | External boundary, reality feedback, and non-identity with current representation |
| [Purposeful finite actor](./framework/purposeful-finite-actor.md) | Derived working subject: self-reference, continuity, finitude, purpose, capability, lifecycle, and termination |
| [Lifecycle](./framework/lifecycle.md) | General process from emergence to termination and epistemic / commitment transitions |
| [Sufficiency](./framework/sufficiency.md) | When a current boundary is adequate for a next transition |
| [Multi-actor](./framework/multi-actor.md) | Multiple local boundaries, shared reality, interaction, coordination, and conflict |
| [Six working lenses](./framework/dimensions/README.md) | Distinction, relation, causality, temporality, possibility, and value |
| [Activities](./framework/activities/README.md) | Exploration and decision as derived activity types |
| [Engineering action chain](./engineering/action-chain.md) | Correctness boundaries among decision, authorization, execution, effect, observation, verification, outcome, and recovery |
| [Precise semantics](./engineering/precise-semantics.md) | Implementable, verifiable engineering semantics that forbid silent substitution |
| [AIOS architecture](./engineering/aios-architecture.md) | A concrete expression in a long-running autonomous AI runtime |

English and Simplified Chinese are equal views. Semantic changes should update both languages with corresponding claim strength, formulas, tables, code blocks, and links.
