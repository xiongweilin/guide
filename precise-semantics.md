# Precise Semantics

The engineering objective is not to implement a single `qualified = true`. It is to preserve the independent conditions of each qualification slice so that the system cannot automatically promote validity at one layer into validity at the next.

Core chain:

`request → claim / fact → policy evaluation → decision → governance basis → authorization → execution → observation → verification → obligation completion → revalidation / discharge`

## 1. Prohibit semantic shortcuts first

| What already holds | What it cannot automatically imply | Additional condition |
| --- | --- | --- |
| Data has been received | Content is true | source, provenance, validation |
| Model confidence is high | authoritative fact | authority, evidence |
| fact is usable | policy is satisfied | policy version, evaluation input |
| policy is satisfied | Decision is valid | accountable principal, scope, authority |
| Decision is valid | approval is complete | required roles / conditions |
| approval is complete | runtime may execute | current authorization, resource, operation |
| provider success | effect occurred | authoritative readback / reconciliation |
| effect occurred | goal achieved | semantic verification |
| one outcome succeeded | case is complete | independently derived obligations |
| case is complete | long-term responsibility discharged | residual obligations, handoff, discharge |
| historically valid | still valid now | freshness, revalidation, reauthorization |

If one field crosses more than two boundaries in this table, inspect it for semantic flattening.

## 2. Keep source, claim, evidence, and fact distinct

After external input enters the system, distinguish at least:

`raw input → representation → claim → validated / authoritative fact`

Minimum fields:

```text
FactClaim
- key / value
- source
- source_ref
- source_version
- observed_at
- provenance
- authority: claim | derived | authoritative
- epistemic_status: unverified | supported | contested | refuted | unknown | revalidation_required
```

AI extraction, user input, caches, search indexes, and synchronized replicas are not authoritative sources by default.

A record existing, being recent, or being produced with high model confidence cannot substitute for source authority.

## 3. Keep identity, role, delegation, and authorization distinct

Authentication answers only "who is this?"

Runtime authorization should bind at least:

```text
Authorization
- principal
- operation
- resource / subject
- scope
- authority_source
- delegation_ref (optional)
- issued_at
- expires_at / revocation_version
```

A role, historical assignment, organizational position, or business Decision cannot automatically become current resource permission.

Permission does not automatically transfer across operation, resource, scope, context, or time.

## 4. Keep policy definition, evaluation, and Decision distinct

A rule definition and the result of applying that rule to current facts are different objects.

```text
PolicyVersion
- policy_id
- version
- owner
- effective_from / until
- definition_digest

PolicyEvaluation
- policy_version
- input_fact_versions
- result
- reasons / unmet_conditions
- evaluated_at

Decision
- decision_id
- subject
- scope
- purpose
- principal
- authority_basis
- policy_version
- input_versions
- disposition
- created_at
```

A Decision must bind the inputs and rules that supported it at the time. The continued existence of an old ID does not mean the Decision is still usable now.

## 5. Keep rule applicability, activation, and execution authorization distinct

A rule set can:

1. be **applicable** to the current object;
2. be **active** in the current scope;
3. allow a particular principal to perform a concrete operation on a particular resource.

These three must not be collapsed.

Rule applicability does not create resource permission; activation does not create resource permission either.

## 6. Governance basis: freeze why something held at the time

A high-impact Decision or grant should preserve a reconstructable governance basis:

```text
GovernanceBasis
- subject / case_id
- authority_epoch
- fact_dependencies + versions / digests
- policy_version + definition_digest
- scope
- required approvals / roles
- role / delegation qualification refs
- other domain qualifications
- unresolved_reviews
- expected_self_induced_changes
- created_at
```

It has two purposes:

- reconstruct why the decision or grant held at the time;
- determine whether it still holds now.

Fields expected to change because of the execution itself should not simultaneously be treated as dependencies whose change invalidates the governance basis. Genuine prerequisite dependency changes, however, must trigger revalidation.

## 7. Keep valid state and valid transition distinct

Every important transition in an explicit state machine should check at least:

```text
current_state
+ trigger
+ expected_version
+ preconditions
+ current_authorization
+ decision / governance basis binding
+ freshness
+ allowed_side_effects
→ next_state
```

Transition provenance should also be recorded.

A legitimate endpoint does not prove a legitimate path.

Concurrent updates should use a version column, ETag, compare-and-swap, optimistic locking, or an equivalent mechanism. On conflict, reread the current state rather than allowing last-writer-wins behavior to erase a semantic conflict.

## 8. Frame conditions: change only the declared scope

An operation should declare the scope of change it owns and the side effects it is allowed to produce.

After execution, verify not only target fields but also critical fields that should not have changed.

Expanding scope, permissions, object sets, or side-effect types should enter a new review / authorization path rather than inheriting an old Decision.

## 9. Freshness means dependencies are still valid, not merely recent

Current qualification can become invalid because of changes to:

- authoritative source or source version;
- policy definition / version;
- role, delegation, or authority;
- scope / partition / assignment;
- model / data / code / tool;
- dependency / environment / resource;
- unresolved review;
- critical assumption.

Freshness should therefore be based on dependency checks, not merely timestamps.

## 10. Keep review, revalidation, reopen, and reauthorization distinct

- **review obligation**: a change occurred that requires renewed examination;
- **revalidation**: determine whether an old fact, Decision, basis, or grant still applies;
- **reopen**: restore fact gathering, candidate generation, or governance flow;
- **reauthorization**: obtain execution or long-lived permission again.

A dependency change normally creates a review obligation first. It should not automatically rewrite a historical Decision, nor should it automatically generate a new Decision.

## 11. Keep transport idempotency and effect idempotence distinct

Using the same idempotency key can prevent duplicate processing of one request, but it does not prove that the external side effect is safe to repeat.

Execution records should preserve at least:

```text
ExecutionAttempt
- request_id
- decision_id / authorization_id
- subject / resource
- operation
- idempotency_key
- expected_postcondition
- provider_ref
- started_at / finished_at
- transport_result
```

Payments, messages, account creation, grants, and similar operations may already have occurred after a timeout. An ambiguous result should enter reconciliation by default; it should not be classified as failure directly and should not be retried by default.

## 12. Keep local transactions and external consistency distinct

A database transaction guarantees only local atomicity. It cannot make the database and an external system commit atomically together.

Choose transactional outbox, inbox / deduplication, saga, compensation, durable workflow, or reconciliation workers according to business semantics.

Regardless of implementation, the system must be able to represent partial success and unknown effect.

## 13. Observation reads reality; it is not an executor echo

```text
Observation
- authoritative_source
- subject_identity
- source_version
- observed_at
- availability
- freshness
- presence
- state
```

At minimum it should represent:

`present | absent | unavailable | unknown`

and:

`fresh | stale | unknown`

An unavailable source does not mean the object is absent; unverified does not mean failed.

## 14. Verification checks the frozen postcondition

```text
Verification
- execution / effect ref
- expected_postcondition
- observation_ref
- disposition: verified | absent | mismatch | unavailable | stale | unknown
- differences
- verifier
- verified_at
```

Verification should read the appropriate authoritative reality source and check identity, target state, scope, and unexpected side effects.

An executor's own success output cannot substitute for independent verification of reality.

## 15. Effect provenance must remain continuous

If the system claims that "this operation produced this result," it should be able to trace:

`request → facts → evaluation → Decision → authority → execution → observation → verification → outcome`

A correct final state is insufficient to prove that the causal chain was correct. Manual action, concurrent operations, or duplicate execution can produce the same endpoint.

## 16. Obligations must be independent of the planner

What the business requires to be completed should not be defined by the execution planner itself. Otherwise a planner that omits a step can produce a self-consistent false success.

```text
Obligation
- obligation_id
- subject
- required_state / operation
- authority_class
- required
- source_policy / decision

CompletionAssessment
- obligation_set_ref
- covered_effects
- verified_outcomes
- missing / mismatched obligations
- residual obligations
- satisfied
```

`verified effect ≠ case complete`

`case complete ≠ responsibility discharged`

Long-term responsibility may also require handoff, a successor, compensation, continued observation, or explicit discharge conditions.

## 17. Record type, epistemic status, and lifecycle are orthogonal

Do not flatten record type, epistemic state, and lifecycle into one enumeration.

A record can be Evidence, Observation, Assertion, Derivation, Goal, Constraint, Experiment, Decision, Action, Policy, Outcome, Revision, or ChangeObject.

The same record can simultaneously be unverified, supported, contested, refuted, unknown, or revalidation_required.

Historical records should be retained; being unusable now does not mean being deleted from history.

## 18. Audit logs do not rewrite history

Important chains should use append-only records or an equivalent traceable design.

Revoking a Decision, rolling back, compensating, or reopening should create new records rather than delete old ones.

At minimum, the record should answer: who did what under which inputs and rules; who authorized it; what was executed; what reality later became; how it was verified; and why it was later changed.

## 19. Semantic entry points are trust boundaries

Content from models, external services, users, or other systems must be validated according to source type before entering the semantic core.

A positive transition that expands qualification, clears a blocker, or creates a side effect should fail closed when source, authority, freshness, scope, or provenance is missing.

Fail closed means only "the system cannot continue now." It must not fabricate the opposite fact.

## 20. Responsibility roles must not impersonate one another

- parser / extractor: produces representation / claim;
- reasoner: produces candidates and reasons;
- policy evaluator: computes rule results;
- decision maker: makes a business Decision;
- authorization layer: grants permission for the current operation;
- executor: attempts to change reality;
- observer: reads reality;
- verifier: judges the postcondition;
- reconciliation / recovery: handles ambiguity and failure;
- reviewer: handles revalidation / reopen / reauthorization.

One process may implement multiple roles, but contracts and records must preserve the distinctions among those roles.

## 21. Compatibility has multiple version axes

Consider at least these axes independently:

- data / record schema version;
- state-machine semantics version;
- policy version;
- authorization contract version;
- runtime protocol version;
- model / evaluator version.

"Old JSON still parses" does not imply semantic compatibility.

During upgrades, check whether field meaning, default behavior, permission, scope, historical interpretation, or review requirements have changed silently.

## 22. Minimum deployable contract

A system that produces real side effects needs at least these objects or equivalent semantics:

```text
FactClaim
PolicyVersion / PolicyEvaluation
Decision
GovernanceBasis
Authorization
ObligationSet
ExecutionAttempt
Observation
Verification
Outcome / ReconciliationState
CompletionAssessment
ReviewObligation
AuditRecord
```

Storage may be consolidated; semantics must not be.

## 23. Minimum invariants

1. AI output is not an authoritative fact by default.
2. A Decision does not directly create low-level resource permission.
3. Current authorization and critical dependency versions are checked before execution.
4. A legitimate endpoint does not prove that the transition was legitimate.
5. Expanding scope requires new qualification.
6. A provider-unknown result does not automatically become failure and does not imply safe retry.
7. A verified outcome comes from real-world readback, not executor self-attestation.
8. Obligations are independent of the planner.
9. Correction / rollback / compensation does not erase history.
10. Changes to source, policy, authority, scope, or critical dependencies enter review / revalidation.
11. Revalidation does not automatically renew authority; reopening does not automatically authorize action.
12. Completion does not automatically equal long-term responsibility discharge.

## 24. Minimum conformance tests

At minimum, test that:

- a high-confidence model claim cannot enter authoritative facts directly;
- stale facts / policies / Decisions / authority are rejected;
- an operation cannot exceed authorization scope;
- an illegal transition is rejected even when its endpoint is otherwise legitimate;
- expected self-induced change does not incorrectly invalidate its own governance basis;
- a genuine dependency change triggers revalidation;
- timeout / lost acknowledgment enters reconciliation rather than direct retry;
- provider success with a real-world mismatch cannot be confirmed as success;
- a cross-effect / cross-subject outcome cannot substitute for the correct verification;
- completion fails when the planner omits an obligation;
- after rollback, the original Decision, attempt, and observation remain traceable;
- a completed workflow cannot be marked responsibility discharged while residual obligations remain.

These tests matter more than the terminology itself: if a theoretical boundary cannot change a contract, transition, failure path, or test, it should not continue to occupy the engineering semantic layer.
