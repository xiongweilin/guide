# Qualification

[English](./qualification.md) | [简体中文](./qualification.zh-CN.md)

> Inspiration: the tension between rule by people and rule of law.

Qualification asks: **what conditions are sufficient for a candidate or state to enter the next state?**

It is not a universal score. It is the structure of grounds required for a state transition. Qualification is one of the six equally basic analytical dimensions in this guide; it does not rank above distinction, value, capability, change, or others, and it does not define their content.

## Minimal state structure

`unmet → accumulating → sufficient → enter`

`Unmet` is a qualification state, not an epistemic negation. It may mean a condition is known false, evidence is missing, the state is unknown, or the required basis has simply not yet been established; those reasons should remain distinguishable.

“Accumulating” need not mean a numerical increase, and “sufficient” need not mean one scalar threshold. Conditions may include:

- necessary conditions becoming satisfied;
- evidence and counterevidence being distinguished;
- dependencies becoming valid;
- authority, approval, or commitment being established;
- verification completing;
- risk, cost, and residual unknowns becoming acceptable for the current purpose.

The core question is:

> Under the current object, scope, purpose, time scale, and conditions, what makes this transition valid now?

## Two qualification regimes

Reality does not always make sufficiency available in the same way. Keep at least two regimes distinct.

### Interpretive qualification

**Interpretive qualification** is used when the conditions for sufficiency cannot be completely fixed in advance. A participant must interpret the object, context, evidence, counterevidence, purpose, competing framings, and residual unknowns, then form an accountable judgment that the current basis is sufficient or insufficient.

This is common in open-ended questions, diagnosis, strategy, design, exception handling, novel cases, and judgments whose relevant variables or weights cannot be fully enumerated beforehand.

Interpretive qualification is not arbitrary. It should preserve at least:

- the object and transition being judged;
- scope, purpose, and time scale;
- evidence and counterevidence;
- assumptions and default distinctions;
- competing interpretations or candidates that materially matter;
- residual unknowns and accepted risk;
- reasons for closure;
- who is accountable for the judgment;
- review and reopening conditions.

So:

`judgment is reasoned != criterion was fully specified in advance`

`interpretive sufficiency != universal truth`

### Specified qualification

**Specified qualification** is used when the relevant conditions have already been made explicit enough to check: a rule, predicate, threshold, state-machine guard, protocol, test, contract, approval set, or equivalent specification defines what counts as sufficient for the current transition.

Examples include an age threshold, required signatures, a schema constraint, a test suite, a policy predicate, or a versioned authorization condition.

Specified qualification should preserve at least:

- the rule or contract identity and version;
- its authority or source;
- applicability scope and effective period;
- required inputs and their versions;
- predicates, thresholds, or required conditions;
- evaluator and evaluation result;
- exceptions, override rules, and reopening conditions.

A clear rule only makes evaluation more determinate. It does not establish the rule's own applicability, authority, current validity, or value.

So:

`rule is explicit != rule is qualified for this case`

`predicate evaluates true != transition is automatically authorized`

### Tension, combination, and conversion

The two regimes solve different problems and create a persistent tension:

- specified qualification increases determinacy, repeatability, and automation, but only inside the distinctions and conditions already encoded;
- interpretive qualification can handle ambiguity, novelty, and incomplete specification, but requires accountable judgment and leaves more room for disagreement and revision.

Many real activities are **hybrid**. Hybrid is not a third primitive regime; it is an explicit composition of interpretive and specified qualification slices. A transition may require specified gates plus an interpretive closure, or an interpretive judgment may first decide whether a specified rule applies.

They can also convert over time:

`repeated interpretation → explicit rule-making → specified qualification`

`novel case / rule ambiguity / changed basis → reopening → interpretive qualification`

But conversion must be explicit. A past interpretation does not silently become a deterministic rule, and a satisfied deterministic rule does not eliminate the need to interpret whether that rule still applies.

## Qualification slice

A concrete qualification slice needs enough context to answer:

- which regime applies and what transition is being judged;
- scope, purpose, time scale, conditions, and supporting basis;
- what remains open and what is being excluded or frozen;
- who defines standards, judges, decides or authorizes, verifies, and can reopen;
- what invalidates, reviews, or revalidates the conclusion.

Different domains have different qualification conditions, so one global `qualified = true` cannot preserve all meanings. A shared result such as `sufficient` also does not erase the regime and basis that produced it.

## Qualification contraction

Qualification can matter before final entry when an intermediate narrowing itself claims that there is sufficient basis to exclude or freeze possibilities. Examples include rejecting a candidate, ending search, freezing a standard, or turning a provisional arrangement into a commitment.

Such a narrowing is a **qualification contraction** only when sufficiency is actually being asserted:

`narrowing != qualification by default`

`open space → qualified contraction → provisional closure`

A qualified contraction needs grounds proportional to what it excludes or freezes. “Not generated,” “not currently visible,” or “not found with current resources” cannot silently become “impossible.” Closure may result from repeated qualified contractions, but not every reduction of options is a qualification event.

## Definition, judgment, and decision power

Qualification sits inside a wider power structure. At least three powers should remain distinct:

1. **Definition power**: the power to set or revise the problem boundary, candidate space, categories, admissible evidence, criteria, thresholds, verification standards, and completion conditions.
2. **Judgment power**: the power to interpret the current basis and judge whether the defined conditions are met or sufficient. This is where qualification is most directly exercised.
3. **Decision power**: the power to decide whether a judgment becomes commitment, authorization, resource allocation, rule adoption, action, continuation, suspension, or termination.

Keep separate:

`power to define != power to judge != power to decide`

`standard-setting authority != evaluator authority != action / commitment authority`

Holding one of these powers does not automatically grant the other two. A participant who can define a standard cannot therefore declare that the standard has been met; a participant who judges that a basis is sufficient does not therefore gain authority to commit resources or change reality; a decision-maker does not therefore gain authority to redefine evidence or lower the standard after seeing the result.

This separation need not always mean three different people or institutions. In low-impact, easily reversible activity, one participant may legitimately hold several roles. But as impact, irreversibility, dependency, or power asymmetry grows, the framework should make the separation more real through independent evidence, independent evaluation, bounded rule-change authority, external veto or stop paths, review, appeal, or other checks appropriate to the domain.

The main failure to prevent is a self-validating loop:

`define the rule → judge against the rule → decide the consequence → redefine the rule when inconvenient`

A process can be procedurally tidy at every local step and still be captured if the same position controls what counts as a candidate, what counts as sufficient, and whether the resulting judgment becomes binding.

Qualification therefore does not generate definition power or decision power. It asks whether the current basis is sufficient within a defined transition. The legitimacy, allocation, and limits of the surrounding powers remain separate questions that may require value, others, domain governance, law, institutional procedure, or other external structures.

## Responsibility and qualification are orthogonal

Responsibility asks **who** is accountable for defining, proposing, judging, authorizing, executing, verifying, stopping, repairing, recording, or reopening.

Qualification asks whether the **current basis is sufficient** for the transition under consideration.

Keep separate:

`responsible role exists != qualification conditions are satisfied`

`qualification conditions are satisfied != authority is automatically granted`

A role can own a judgment without being entitled to fabricate its evidence or prerequisites. Conversely, a basis can be sufficient while the relevant authority still belongs to someone else.

## No-shortcut rule

When moving from `X` to `Y` materially depends on an intermediate responsibility, basis, or qualification `R`, it cannot be silently omitted:

`X → R → Y`, not `X → Y`.

If `R` is missing, add the missing position when it is genuinely necessary, hand it off to the domain or procedure that owns it, keep the question open while basis is obtained, or stop making the stronger claim. This prevents semantic substitution; it does not guarantee that the eventual conclusion is correct.

## Composition qualification

Qualification is not automatically compositional:

`qualified(C1) + qualified(C2) + ... != qualified(C1 ∘ C2 ∘ ...)`

Local qualification does not establish joint compatibility or qualification of the composition. A separate composition basis is needed only when interaction introduces material new assumptions, scope, timing, permissions, dependencies, side effects, feedback, or failure propagation.

## Handoff completeness

A material handoff should preserve enough context to prevent downstream overclaim:

- the current conclusion or state, with scope, purpose, and time scale;
- supporting basis, key assumptions, residual unknowns, and material alternatives;
- invalidation, review, revalidation, or reopening conditions;
- the limits of current closure and authority.

`handoff != downstream requalification`

Transfer does not silently create broader scope, stronger evidence, new authority, or permanent validity.

## Qualification does not silently inherit

The repository-wide non-substitution rule applies directly to qualification:

`valid at one slice != automatically valid at the next`

In particular:

`evidence exists != judgment is sufficient`

`judgment is sufficient != goal is worth committing to`

`goal is worth committing to != authority to decide`

`effect occurred != goal is complete`

A qualification only carries the scope and basis actually established for that slice.

## Finite closure and reopening

Finite activity needs provisional closure:

`open → converge → provisional closure → continue → conditions change → review / reopen`

Closure is local to the current object, scope, purpose, time scale, and basis; it is not permanent truth or an absolute foundation. The framework does not require an infinite stack of prior meta-qualifications before action.

Material changes in facts, scope, dependencies, authority, value, cost, risk, or environment can trigger review, revalidation, or reopening. Reopening restores candidate and choice space; it does not automatically create a new answer, decision, or authority.

`provisional local closure != absolute foundation`

`qualification may be reviewed != every qualification requires endless prior qualification`

## State and transition

A resulting state may be acceptable while the path used to reach it was invalid.

Qualification therefore checks both:

- whether the current state is acceptable;
- whether the transition from the previous state had valid grounds.

A valid endpoint cannot retroactively prove a valid path.

## Cross-domain transfer strength

When a structure appears across domains, keep at least three levels of transfer distinct:

1. **Shared problem**: only the question or framing transfers.
2. **Formal similarity**: a representation, comparison, or computational structure can transfer.
3. **Mechanism similarity**: limited prediction or intervention experience can transfer only when the relevant objects, boundary conditions, and mechanisms are sufficiently alike.

`formal similarity != mechanism evidence`

A structure that has mechanism-level support in one domain does not inherit the same status in another domain. Cross-domain reuse therefore needs its own qualification rather than being justified by vocabulary or shape alone.

## Boundary with the other dimensions

Qualification uses [distinction](./distinction.md) to identify what is being judged, but cannot be inferred from it. It can constrain transitions involving [value](./value.md), [capability](./capability.md), [change](./change.md), and [others](./others.md) without defining their content.
