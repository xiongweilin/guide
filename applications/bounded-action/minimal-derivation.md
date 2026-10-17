# Minimal derivation — action first, self-reference optional

[English](minimal-derivation.md) | [简体中文](minimal-derivation.zh-CN.md)

**Status:** proposed core revision, not empirical validation.

## 1. Minimal goal-directed controller

The weakest useful action model assumes: (i) external world constraints; (ii) incomplete observation with a set of compatible states; (iii) an explicitly supplied acceptability and safety relation; and (iv) available transitions including stop only when stop is actually enforceable. It does **not** require reflective self-description. Purpose does not confer authorization, legitimacy, moral status or a complete utility function.

## 2. Robust next-action sufficiency

For history H, let W(H) be a **sound overapproximation** of possible worlds, and let A(w) contain only actions that are both safe and authorized for the specific transition in world w. Define the common action set as the intersection of all A(w), for w in W(H).

When that intersection is nonempty, an action can be selected **without first identifying the actual world**, provided the abstraction correctly refines to the executable interface. This condition is sufficient, not necessary for every policy.

Three outcomes are different:
- **Robustly actionable:** a common safe and authorized action exists.
- **Needs discrimination:** no common action has been found, but a trusted observation may separate the worlds and enable a bounded conditional policy.
- **No qualified policy:** within the *enumerated model and resource horizon* there is no complete safe policy; hold, stop or escalate. This is not metaphysical impossibility.

These are algorithmic classifications, not substitutes for the prior interpretive labels insufficient/materially uncertain/sufficient.

## 3. Contingent sufficiency and value of evidence

A policy can branch on a later observation instead of requiring a new language-model proposal after the event. Every **possible** observation outcome must have a safe continuation. A missing branch remains unknown, not impossible. A new observation is instrumentally useful when it changes the available qualified continuations; reading data that cannot change a safe plan may waste scarce budget.

Prefer policies minimizing declared worst-case or expected costs **subject to** unchanged safety, authority, timing, recovery and audit requirements. A precompiled policy is never an authorization capability. Its real effect still requires live admission, binding checks, independent readback and reconciliation. Unknown effects cannot be blindly redispatched.

## 4. Optional reflexive branch

Bounded control plus feedback supports action and revision without a retained self-reference prerequisite. A separate branch adds retained reflexive distinction, identity continuity, corrigible self-models and multi-actor governance. Self-reference may enable new capacities but is **not logically necessary for all controllers**. The earlier self-reference-first ladder is retained as a specialized model, not a universal foundation.

## 5. Limits

A finite set of possible worlds, authorized steps and qualified observations never proves that the model captures all real hazards. The formal common-action result in [Lean RobustAction](https://github.com/xiongweilin/distinction-self-reference-lean/blob/main/DistinctionSelfReference/RobustAction.lean) is conditional; the [BAA policy compiler](https://github.com/xiongweilin/BAA-Protocol/blob/main/baa_protocol/contingent_policy.py) is a finite constructive implementation with independent validation, not a production guarantee.

Compare against equally equipped conditional-planning baselines and measure all C0/C1/C2 delivery, cost, unknown and unsafe outcomes; a positive result is not assumed.

Other working lenses remain at [dimensions](framework/dimensions/README.md), interpretive judgment at [sufficiency](framework/sufficiency.md), and empirical measurement at [evaluation](use/evaluation.md).
