# guide

![Repository: Public](https://img.shields.io/badge/repository-public-success.svg) [![Docs: EN / 中文](https://img.shields.io/badge/docs-EN%20%7C%20%E4%B8%AD%E6%96%87-blue.svg)](README.zh-CN.md)

[English](README.md) | [简体中文](README.zh-CN.md)

> A working framework for how a finite system forms a current boundary under reality, judges whether it is sufficient, explores when it is not, decides when it is, and receives reality-side feedback through an action chain.

This repository does not attempt to provide a final ontology of reality, nor does it treat any cognitive model, optimization method, or engineering implementation as reality itself. It requires only that a finite system make the boundary of its current activity sufficiently explicit, prevent important semantics from being silently substituted, avoid disguising unknowns as knowns, and remain revisable through reality-side feedback after action.

## Overall structure

```text
Reality (external boundary)
    │
    ▼
Finite system
    │
    ▼
Current activity / current purpose
    │
    ▼
Construct current boundary B
    │
    ├─ Distinction
    ├─ Relation
    ├─ Causality
    ├─ Temporality
    ├─ Possibility
    └─ Value
    │
    ▼
Sufficiency S(B, purpose, next transition)
    ├─ insufficient / materially uncertain → explore → revise B
    └─ sufficient                         → decide
                                               │
                                               ▼
                                          action chain
                                               │
                                               ▼
                                            reality
                                               │
                                      reality-side feedback
                                               │
                                    retain / revise / reopen
```

Each position has a different responsibility:

- **Reality** is the external boundary. A representation, model, schema, ontology, classification, or knowledge graph is not reality itself.
- **Finite system** is the user of the framework. A person, team, organization, institution, Agent, or technical system may be analyzed as a finite system; all are limited by sensing, language, time, computation, resources, authority, and control.
- **Six dimensions** describe the current activity boundary: distinction, relation, causality, temporality, possibility, and value.
- **Sufficiency** is an operator, not a seventh dimension. It asks whether the current boundary is enough for the next transition under the current purpose.
- **Exploration and decision** are activities, not dimensions. Explore when the boundary is insufficient; decide when it is provisionally sufficient.
- **The action chain** connects decision to reality while preserving the differences among decision, authorization, execution, real-world effect, observation, verification, outcome, and reopening.

## Six dimensions

The six dimensions are not six kinds of object and are not assumed to be independent, orthogonal, or at the same logical level. They are six descriptive dimensions that the current framework does not allow to silently substitute for one another.

| Dimension | Core question |
| --- | --- |
| [**Distinction**](./framework/dimensions/distinction.md) | What can be distinguished, what has been distinguished, and what remains outside the current representation? |
| [**Relation**](./framework/dimensions/relation.md) | How are distinguished contents connected, composed, dependent, constrained, and mutually affected? |
| [**Causality**](./framework/dimensions/causality.md) | What changes cause what other changes, and what interventions can change which outcomes? |
| [**Temporality**](./framework/dimensions/temporality.md) | What happens before or after what, for how long and at what rate, and when does a structure remain valid or fail? |
| [**Possibility**](./framework/dimensions/possibility.md) | What else may occur, and which paths are reachable, callable, unknown, or excluded? |
| [**Value**](./framework/dimensions/value.md) | What is worth pursuing, avoiding, maintaining, committing to, or refusing? |

Typical non-substitutions:

Throughout this repository, `A != B` is shorthand for a non-substitution rule: establishing A does not by itself establish B, and A must not silently substitute for B. It does not mean that a valid transition, mapping, or qualified realization from A to B is impossible.

`a classification exists in the current representation != reality has only that classification`

`relation exists != causal effect exists`

`temporal order observed != causality established`

`possible != currently controllable by this system`

`can do != authorized to do != worth doing`

`stable now != permanently valid`

`individual preference != collective value != legitimate collective decision`

## Sufficiency operator

[Sufficiency](./framework/sufficiency.md) does not ask whether the current model is complete. It asks:

> Is the current boundary sufficient for the current purpose and next transition?

Sufficiency is therefore local, purpose-relative, time-relative, and reopenable. It can be established through two basic mechanisms:

- **Interpretive sufficiency**: an accountable judgment over context, evidence, counterevidence, competing explanations, residual unknowns, and risk.
- **Specified sufficiency**: checking an explicit and versioned rule, predicate, threshold, guard, test, or contract.

They can be combined but cannot silently substitute for each other.

`sufficient for the next step != complete boundary`

`specified rule satisfied != rule currently applicable / valid / authoritative`

`interpretive judgment is reasoned != a deterministic rule already exists`

## Exploration and decision

[Exploration](./framework/activities/exploration.md) reopens the current boundary when it is insufficient or materially uncertain. Its purpose is not endless information accumulation, but greater discriminative power among important competing candidates, with a stopping condition when further exploration is no longer worth its cost.

[Decision](./framework/activities/decision.md) forms a choice after the current boundary is provisionally sufficient. It permits multiple admissible options, partial orderings, incommensurable reasons, and explicit choice procedures without disguising the resulting choice as logically forced.

`unknown exists != exploration must continue indefinitely`

`multiple admissible options != choice needs no reason`

`no unique optimum != no accountable decision is possible`

## Action chain

The [action chain](./framework/action-chain.md) closes the framework back onto reality:

```text
decision
→ commitment / governance basis
→ authorization
→ execution
→ real-world effect
→ observation
→ verification
→ outcome / completion judgment
→ retain, revise, recover, or reopen
```

These positions cannot be collapsed into one notion of “success”:

`decision != authorization`

`authorization != execution`

`execution succeeded != real-world effect occurred`

`effect occurred != goal completed`

`goal completed != long-term responsibility discharged`

Reality-side feedback may require only a value update, or it may reopen relations, causal assumptions, time structure, possibility, value, the problem framing, or even the current six-dimensional closure itself.

## Working closure, not final completeness

The current six dimensions are a **working closure**, not a proof that reality has exactly six fundamental dimensions.

The framework may close provisionally when it is sufficient for the current use. Counterexamples, prediction failures, intervention failures, structural tension, unexpected consequences, accumulating special cases, loss of recoverability, or a better competing framing can all justify reopening.

Therefore:

`current six dimensions are useful != reality has exactly six ultimate dimensions`

`internal coherence != consistency with reality`

`local formal verification passed != guide has been proven true`

A competing theory need not first translate itself into guide vocabulary before it can challenge guide through consequences, counterexamples, predictions, or practice. Semantic mapping becomes necessary for integration, migration, or federation.

guide does not require a theory to retire itself. A theory is not an acting subject; revision, narrowing, replacement, archival, and non-use are practices of the finite systems using it.

## Evaluation in use

The framework does not establish its ultimate validity through formal proof. Concrete use can be evaluated through task-relevant indicators including:

- correctness;
- usability;
- reliability;
- performance;
- capacity / scalability;
- efficiency.

These are usage indicators, not new theoretical dimensions. Good performance on one indicator does not establish overall sufficiency; deteriorating reality-side results can reopen the framework.

## Document map

| Document | Role |
| --- | --- |
| [Reality](./framework/reality.md) | external boundary, distinguishable range, current representation, and reality-side correction |
| [Finite system](./framework/finite-system.md) | user, epistemic status, capability, and control boundary |
| `framework/dimensions/` | six descriptive dimensions |
| [Sufficiency](./framework/sufficiency.md) | operator controlling exploration / decision transitions |
| [Exploration](./framework/activities/exploration.md) | reopening activity when the boundary is insufficient |
| [Decision](./framework/activities/decision.md) | choice activity when the boundary is sufficient |
| [Action chain](./framework/action-chain.md) | closed loop from decision to reality-side feedback |
| [Precise Semantics](./engineering/precise-semantics.md) | engineering semantics that preserve the structure without silent substitution |
| [AIOS Architecture](./engineering/aios-architecture.md) | one concrete expression in a continuously operating AI system |

English and Simplified Chinese are co-authoritative views. Semantic changes should update both; section structure, claim strength, formulas, tables, code blocks, and links should correspond.
