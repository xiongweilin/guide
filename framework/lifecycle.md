# Action lifecycle: observe, compile, qualify, execute, verify

[English](lifecycle.md) | [简体中文](lifecycle.zh-CN.md)

A bounded action system need not reenact self-reference as a chronological developmental stage. A minimal useful cycle is:

1. **Acquire** a versioned, fallible world observation and an independent authority record.
2. **Compile** the next common-safe action, or a finite conditional policy with every observation branch covered.
3. **Qualify** the concrete step under present time, authority, interface scope, reachable fallback and budget.
4. **Attempt** through a mediated executor, keeping its durable effect identity and uncertainty.
5. **Observe independently** and reconcile unknown outcomes before any further conflicting action.
6. **Retain, revise or reopen** the belief, goal, constraints, policy or recovery path when new evidence changes what is qualified.

This cycle can stop, hold or terminate without a claim of success. Its planning phase may prepare future conditional branches, but does not grant permission for their later execution.

**Crucial distinctions:** plan ≠ capability; capability ≠ attempted effect; attempted effect ≠ verified real effect; verified effect ≠ completed purpose. Unknown outcomes are not a reason to blindly retry.

### Reflexive life histories

When a controller also has retained self-reference and identity continuity, the above action cycles can be analyzed as one actor's history, including its changing self-model and eventual termination. Such a structure is optional and adds no rights or governance legitimacy by itself. Termination does not erase residual effects.

See [the action-first derivation](../minimal-derivation.md) and the governed [AIOS action chain](https://github.com/xiongweilin/aios/blob/main/docs/reference/guide/action-chain.md).
