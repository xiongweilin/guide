# Basic problems for bounded AI autonomy

[English](basic-problems.md) | [简体中文](basic-problems.zh-CN.md)

## Scope

These are two working problems for a sufficiently capable AI acting within a **bounded system**: specified purpose, operating scope, accessible interfaces, relevant constraints, and feedback channels. A bounded system still has incomplete observations, changing reality, and unknown future conditions.

The two problems are candidate foundations for reliable autonomous execution, not a proof of universal necessity or sufficiency. Addressing them alone does not establish correct values, authority, global optimality, compositional safety, or guaranteed termination.

## 1. Local sufficiency for the next transition

For the current purpose and a **specific next transition**, does the actor have proportionate grounds to proceed?

`S(B, P, T) → {insufficient grounds, material uncertainty, sufficient}`

- **B — current boundary:** available distinctions, observations, assumptions, evidence, retained state, and unresolved unknowns.
- **P — purpose:** objectives, constraints, acceptable outcomes, and consequences that matter.
- **T — next transition:** inquiry, provisional judgment, decision, commitment, execution, verification, or controlled stopping.
- **Local, not complete:** sufficiency for forming a hypothesis is not sufficiency for irreversible action, or for declaring the task complete.
- **Explore or commit:** seek discriminating evidence if unresolved distinctions could materially change T; otherwise proceed with explicit remaining unknowns, proportionate risk, and invalidation conditions.
- **Revise or reopen:** changing reality, dependencies, evidence, or purposes can invalidate an earlier sufficiency boundary. An action being triggered does not show that it was warranted.

A particular rule-derived case admits a precise observational criterion: if states indistinguishable under the current observation require different commitments, that observation is insufficient for this commitment. This is **not** a theorem for every context-dependent judgment.

See [sufficiency](framework/sufficiency.md) and [exploration/decision](framework/activities/README.md).

## 2. The interaction–meaning gap

Successful transmission, shared wording, a valid tool call, or a successful status code does **not** prove that interacting actors attach the same meaning to it or that the intended real-world outcome occurred.

- **Representation:** reality, what can be distinguished, what has been distinguished, and the actor's current representation are different boundaries. Missing candidates are not automatically impossible candidates.
- **Other actors:** in human–human, human–AI, and AI–AI interaction, actors may have different histories, roles, purposes, classifications, temporal scopes, and authority, even when messages use identical symbols.
- **Action semantics:** a proposal is not a decision; a decision is not authorization; attempted execution is not effect; effect is not verified outcome; outcome is not necessarily completion.
- **Working bridge:** identify referents, scope, versions, sources, expected commitment and effect, responsible actor, authorization, postconditions, independent read-back, divergence handling, and conditions for revision.
- **Residual mismatch:** only alignment relevant to the next joint transition is required. A complete shared worldview or exhaustive representation of reality cannot be presumed.

See [reality](framework/reality.md), [multiple actors](framework/multi-actor.md), and [interaction](use/interaction.md).

## 3. The joint execution loop

- Interpret interactions as revisable claims about goals, state, capability, authority, and effects; do not silently promote a signal into a verified fact.
- Use local sufficiency to choose inquiry, commitment, authorized action, verification, revision, or a controlled stop.
- Compare independently observed real effects with declared postconditions using [evaluation](use/evaluation.md). Mismatches can reopen both the meaning mapping and the sufficiency judgment.
- Coupled actions also require coverage of the joint purpose, compatibility of shared states and constraints, and minimum recoverability. **Locally sufficient transitions are not automatically sufficient in combination.**

## 4. Acceptance questions for a bounded system

- Can each material transition identify its purpose, current boundary, evidence, unresolved unknowns, sufficiency judgment, and invalidation conditions?
- Can parties distinguish requests, commitments, permissions, attempts, effects, verification, outcomes, and completion?
- Can a mismatch be independently detected and handled through clarification, reconciliation, recovery, reauthorization, revision, or stopping?
- For multiple actors, are coupled resources and state changes compatible, with a controlled response to material failure?

Passing these checks supports a bounded, revisable autonomous loop; it does not imply universal unattended automation.
