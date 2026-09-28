# Action chain: from current boundary to reality-side feedback

[English](./action-chain.md) | [简体中文](./action-chain.zh-CN.md)

The action chain is the **loop structure** of the framework. The six dimensions describe the current boundary; sufficiency controls exploration or decision; the action chain connects decisions to reality and returns reality-side feedback into the next cycle.

## 1. Minimal loop

```text
current activity / current purpose
    ↓
six-dimensional current boundary
    ↓
sufficiency judgment
    ├─ insufficient → explore → revise boundary ─┐
    └─ sufficient   → decide                    │
                        ↓                       │
                    action chain                │
                        ↓                       │
                      reality                   │
                        ↓                       │
                reality-side feedback           │
                        ↓                       │
              retain / revise / reopen ─────────┘
```

This is not a strict one-way pipeline. A decision may expose a missing distinction and return to exploration; execution may reveal expired authority; observation may falsify a causal assumption; changes in value or relations may invalidate the prior decision.

## 2. Inside the action chain

For consequential activity, preserve at least:

```text
decision
→ commitment / governance basis
→ authorization
→ execution attempt
→ real-world effect
→ observation
→ verification
→ outcome
→ completion / residual obligations
→ retain, recover, revise, or reopen
```

These positions need not each be separate database objects, but their semantics must not disappear.

At minimum:

`candidate != decision`

`decision != authorization`

`authorization != execution`

`executor reported success != real-world effect occurred`

`real-world effect occurred != expected postconditions verified`

`postconditions verified != all goals / obligations completed`

`case completed != long-term responsibility discharged`

## 3. Decision and commitment

A decision selects from the current admissible space. It may close alternatives, allocate resources, create expectations for others, trigger authority requests, or form path dependence.

A consequential decision should preferably bind:

- current boundary / version;
- candidates and important exclusions;
- important reasons and conflicts;
- accepted unknowns;
- decision-maker and authority source;
- time scale;
- commitments created;
- expected effects;
- review, reversal, and reopening conditions.

A good outcome cannot prove that the earlier decision process was sound; a bad outcome cannot by itself prove that the earlier decision was unreasonable.

## 4. Authorization and execution

Technical capability does not create authority, and a decision does not automatically create underlying resource permission.

Authorization should bind at least:

- who;
- which object or resource;
- which operation;
- what scope;
- authority source;
- issue time, expiry, or revocation.

Execution should recheck current state, version, preconditions, authorization, critical dependencies, and allowed side effects.

A legitimate final state cannot prove that the transition path was legitimate.

## 5. External effects and partial success

A database transaction can guarantee only a local boundary. It cannot make the local database and external reality commit atomically.

The action chain must therefore represent:

- execution completed but effect unknown;
- external effect occurred but local confirmation missing;
- partial success;
- repeated request where the external effect cannot safely repeat;
- compensation required;
- reconciliation required;
- recovery required;
- reauthorization required.

`transport idempotency != effect idempotence`

Timeout or lost acknowledgment must not automatically become "failed and safe to retry." Ambiguous external effects should enter reconciliation.

## 6. Observation and verification

Observation reads state from the reality side; it does not echo the executor's own output.

Observation should preserve source, subject identity, source version, observation time, availability, and freshness.

Verification checks frozen postconditions, for example:

- the correct object changed;
- the target state occurred;
- the scope is correct;
- important non-target state remained unchanged;
- important side effects did not occur.

An executor's own success response cannot replace independent reality-side readback.

## 7. Effect provenance

If a system claims "this action produced this result," it should be able to trace:

```text
current boundary
→ sufficiency basis
→ decision
→ authorization
→ execution
→ real-world effect
→ observation
→ verification
→ outcome
```

A correct final state does not prove the causal chain: concurrent operations, manual actions, repeated execution, or other actors may have produced the same endpoint.

## 8. Obligations and completion

The executor or planner should not define what the business requires for completion. Otherwise an omitted step can produce internally consistent false success.

Therefore **obligations** and **plans** remain separate.

`plan finished != all obligations satisfied`

Completion should check required states, required operations, authority conditions, verification results, and residual obligations. Long-running responsibility may additionally require handoff, successor assignment, compensation, continued observation, or explicit release.

## 9. Feedback and reopening

Reality-side feedback may trigger different response depths:

1. update a value in the current representation;
2. revalidate old facts, rules, authority, or dependencies;
3. revise one six-dimensional structure;
4. reopen the candidate space or problem framing;
5. return to exploration;
6. form a new decision;
7. stop, compensate, or recover;
8. narrow, replace, or abandon the framework.

History should not be deleted because a decision is reopened. Reversal, compensation, rollback, and new decisions should create new traceable records.

`reopen != automatic reversal`

`historical decision invalid now != historical decision never existed`

## 10. Rate, reversibility, and lock-in

Correction speed must be commensurate with reality-side change and damage speed.

Compare:

`detect + judge + stop + recover + reauthorize`

with:

`error propagation + damage accumulation + lock-in`

A correction mechanism existing on paper does not mean it is fast enough.

Effective reversibility also distinguishes:

- **state reversibility**: can the reality-side state return to acceptable conditions?
- **control reversibility**: can the finite system regain the ability to stop, modify, take over, migrate, or exit?
- **epistemic reversibility**: do the evidence, knowledge, records, dissent channels, and verification capability needed for revision still exist?

The action chain does not require everything to be reversible. It requires irreversible commitment to keep its reasons, authority, risk, and recovery boundary explicit.
