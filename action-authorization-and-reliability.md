# Action, Authorization, and Reliability

Between "knowing what is true" and "changing reality," we must distinguish at least judgment, technical capability, formal authorization, execution, real-world effect, verification, and long-term responsibility.

## 1. Knowing how to act does not mean having authority to act

Distinguish:

- epistemic sufficiency to propose a plan;
- technical capability to execute it;
- institutional authorization to execute it;
- current validity of runtime permissions.

Satisfying any one layer cannot automatically substitute for the next.

## 2. When explicit action procedures are required

An action should enter an explicit and traceable procedure when it affects:

- persistent state;
- formal records;
- shared resources;
- third parties;
- identity, rights, or reputation;
- long-lived dependencies;
- future paths that are difficult to restore.

The higher the risk, the stronger the procedure should be. Safety, privacy, rights, irreversible harm, unclear authority, missing recovery paths, power asymmetry, rapid propagation, system lock-in, critical infrastructure, and legal obligations should all trigger stricter review, approval, verification, or human involvement.

## 3. Action has at least six slices

1. **Reality and purpose**: what the current facts are and what should change;
2. **Conditions and authority**: whether preconditions, rules, authority basis, and scope hold;
3. **Plan and exposure**: how to act, how large the impact surface is, and when to stop;
4. **Execution and records**: what was actually sent and which side effects occurred;
5. **Verification and correction**: whether reality reached the intended outcome and whether reconciliation, compensation, or correction is required;
6. **Persistence, exit, and reopening**: whether the result can continue to hold and when to revalidate, reauthorize, hand off, retire, or reopen.

Qualification does not automatically carry across these slices.

## 4. Limit exposure first, then expand gradually

New plans, models, and permissions should begin with limited scope, resources, users, or time windows whenever possible.

Before expanding scope, recheck:

- whether the facts and assumptions still hold;
- whether failure modes have changed;
- whether recovery paths are actually usable;
- whether authority covers the larger scope;
- whether verification can still distinguish success from failure.

Local success does not automatically establish that larger scale, longer duration, greater authority, or higher irreversibility is also justified.

## 5. External service success does not mean real-world success

For external operations, distinguish:

`request sent → external service accepts → side effect may occur → real state becomes observable → intended outcome is verified`

Therefore:

- HTTP 2xx does not mean the goal is complete;
- a timeout does not mean the side effect did not occur;
- a command error does not prove reality remained unchanged;
- request deduplication does not mean the real-world side effect is safe to repeat.

When the outcome is ambiguous, first isolate further impact, read authoritative reality, reconcile the actual state, and only then decide whether to retry, compensate, involve a human, or close the case.

## 6. Verification must come from reality

An executor cannot prove its own success using only its return value.

High-impact actions should, where possible, independently read real state and verify:

- object identity;
- the expected outcome;
- scope;
- unexpected side effects;
- version and current validity;
- a traceable relation between the observed result and this execution.

Even a final state that matches expectations does not by itself prove that this operation caused it.

## 7. Rollback does not mean reversibility

Rolling back code or database state does not mean reality has been restored.

Recovery must account for:

- data;
- relationships;
- identity and permissions;
- rights, reputation, and opportunity;
- resources and cost;
- information that has already propagated;
- knowledge and path dependence.

Even when the final state becomes acceptable, residual responsibilities may remain, requiring compensation, notification, continued observation, or follow-up repair.

## 8. Minimum action record

For an important change, it should be possible to reconstruct at least:

- object, scope, purpose, and completion conditions;
- evidence, assumptions, and unknowns;
- roles, authority basis, and approvals;
- plan, exposure, and stop conditions;
- execution attempts, side effects, and external service references;
- observations of reality, verification, and outcomes;
- correction, rollback, compensation, handoff, and exit;
- conditions for continuation, expansion, contraction, retirement, revalidation, reauthorization, and reopening.

## 9. Long-lived qualification requires reauthorization

Long-running systems accumulate:

- exposure;
- temporary permissions that become de facto permanent;
- maintenance and audit cost;
- centralization;
- dependencies;
- recovery and exit difficulty;
- divergence between old evidence, rules, permissions, and current reality.

High-impact or long-lived permissions should not remain valid forever after one authorization. They need explicit review, revalidation, and reauthorization periods or triggers.

## 10. Reliability is a structure, not a total score

Reliability includes at least:

- whether errors can be observed;
- whether dissent can enter the process;
- whether independent verification exists;
- whether the system can stop;
- whether impact can be isolated;
- whether correction is possible;
- whether recovery is possible;
- whether history is preserved;
- whether exit or takeover is possible.

Multiple reviewers or control systems that share the same data, model, metric, funding, identity infrastructure, technical root, or authority source may fail for the same reason and should not be counted as genuinely independent redundancy.

## 11. Three dependency networks

Inspect separately:

1. normal-operation dependencies;
2. failure-propagation dependencies;
3. recovery dependencies.

Redundancy on the normal path does not imply redundancy on the recovery path.

Also compare rates: can detection, judgment, stopping, recovery, and reauthorization happen faster than harm propagation and system lock-in?

## 12. Effective reversibility and maneuverability

Reversibility includes at least:

- state reversibility: can object state be restored;
- control reversibility: can control be regained;
- epistemic reversibility: can we still determine what happened and why.

Maneuverability additionally requires the ability to generate alternatives, retain reachable paths, bear transition costs, rebuild preconditions, and regain authorization.

The most severe form of system lock-in is not merely that switching is expensive; it is that the system has lost the ability to regenerate options and recover control.
