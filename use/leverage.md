# Leverage

[English](leverage.md) | [简体中文](leverage.zh-CN.md)

## Method

1. Specify the purpose, acceptable outcomes, hard constraints, and affected actors; do not equate individual gains with collective welfare.
2. Identify available structures: independent action and aligned interests of others, matching and bargaining rules, incentives, networks, resources, interfaces, institutions, and time windows.
3. Distinguish **possible, reachable, controllable, callable**; check resources, dependencies, permission, consent, and exit options.
4. Analyze strategic responses, rivalry, coordination, move order, information asymmetry, externalities, and reflexive feedback.
5. Compare feasible paths for cost, fragility, lock-in, recoverability, and future options; form commitments only with proportionate grounds and authority.
6. Verify real effects through [evaluation](evaluation.md) and revise on mismatch; do not confuse formal equilibrium with observed outcomes.

## Interaction method: from structural analysis to coordinated action

- **Boundary:** Leverage is not manipulation or the treatment of other people as callable tools. Formal games establish conditional mechanism results; real interaction also requires eliciting others' positions, consent, capability evidence, explicit commitments, and feedback.
- **Participants:** Human-to-human, human-to-organization, and human-to-AI interactions can be analyzed, but shared goals, representations, and authority cannot be presumed. AI used for suggestions need not qualify as an actor under guide; only a particular system with the required persistent state, action capacity, and other conditions can be analyzed as a purposeful finite actor.
- **Purpose:** Use information exchange, complementary resources, coordination, or delegation to increase callable paths without overriding third-party rights, authorization, or hard constraints; do not confuse this with maximizing control over others.

| Material gap | Suitable interaction move | Ground for proceeding |
| --- | --- | --- |
| The other's goals or limits are unknown | Open questions, restatement, permission to decline | Their express account; unstated points remain hypotheses |
| Factual or causal models differ | Exchange sources, clarify terms, seek discriminating observations | Differences narrow, or coordination can retain them explicitly |
| Goals differ but capabilities complement each other | Offer alternatives, negotiate contributions and returns | Each side understands burdens and voluntarily accepts terms |
| Division of labor or delegation is required | Specify task, decision rights, execution rights, and acceptance owner | Consent and authorization are verifiable; otherwise do not act |
| Stakes are high or lock-in is plausible | Bounded pilot, staged commitment, exit and compensation paths | Dependencies, risks, stopping and recovery are sufficiently clear |
| Observed effects differ from expectations | Independent read-back, mismatch analysis, renegotiation or exploration | The executor's own account is not substituted for real effects |

## Human-to-human interaction

1. **Ask rather than assume:** State one's own objectives, then ask about the other's purposes, unacceptable costs, resources, deadlines, and decision rights. Separate their statements and independently verifiable facts from one's interpretations; silence is not consent.
2. **Define a minimal joint problem:** Confirm the object, vocabulary, time scale, and affected people. Divergent values or worldviews need not prevent limited agreement on interfaces, roles, timing, and verification.
3. **Propose complementary arrangements:** Offer comparable alternatives with each party's contributions, gains, risks, outside options, and genuine exit. Include third-party burdens; bilateral gains do not automatically establish public legitimacy.
4. **Make commitments explicit:** Independently confirm who decides, executes, supplies resources, delivers when, verifies, and can change terms. Politeness, guesses about agreement, or expertise do not authorize someone to bind others.
5. **Review and renegotiate:** Examine deliverables and real outcomes. After refusal, conflict, or changed conditions, narrow the scope, amend terms, use applicable procedures, or stop; agreement is not mandatory.

### P1 Cross-team API migration

- **Situation:** Team A wants to retire an API still used by team B; A cannot unilaterally commit B to a migration deadline.
- **Interaction:** A asks about B's dependencies, migration cost, and time window, then proposes a compatibility window, phased migration, or delay and compares the costs with B.
- **Commitment:** Each team confirms responsible owners, integration deadlines, joint acceptance checks, and rollback arrangements; formal approval remains with authorized roles.
- **Acceptance:** Jointly agreed compatibility tests and actual calls are checked; A releasing successfully does not prove B's workflows are working.
- **Failure path:** If B declines, misses the deadline, or integration fails, retain compatibility, renegotiate, or stop; silence is not acceptance.
- **Boundary:** This illustrates conditional coordination, not a guarantee that discussion resolves resource conflicts or institutional limits.

## Human-to-AI interaction

1. **Identify the mode:** Treat answers, retrieval, and drafting as tool outputs. Where a particular AI agent has persistent state and real callable actions, separately assess its task direction, scope, permissions, and stop controls. Linguistic performance does not establish consciousness, reliability, or legitimate authority.
2. **Specify a task contract:** Supply the goal, inputs and authoritative sources, allowed data and tools, prohibited acts, output format, time bounds, how uncertainty should be reported, and when approval is required.
3. **Stage action authority:** First ask AI to clarify, analyze, and present alternatives with evidence. File edits, outbound messages, external API calls, payments, and production deployment need separate scope and authorization checks; tool availability is not permission.
4. **Separate claims from effects:** Distinguish AI statements, tool results, execution, authoritative read-back, and independent acceptance. Fluency, passing tests, or a successful executor receipt does not by itself establish the intended real-world outcome.
5. **Correct against feedback:** Give specific counterexamples and observed results. Reframe tasks when assumptions, authority, or conditions change rather than retrying blindly. Reconcile unknown external effects before replaying potentially irreversible operations.
6. **Preserve affected parties' rights:** Shared data, privacy, third-party interests, and irreversible changes may require separate human or institutional decisions; an AI recommendation is not others' consent.

### A1 Delegating a code change to AI

- **Situation:** A maintainer needs to fix an API defect, but the root cause is uncertain and the AI has no production deployment authority.
- **Interaction:** Ask the AI to inspect relevant code, contracts, and tests, separating facts from hypotheses and proposing a minimal patch; only edit scoped files after maintainer approval.
- **Commitment:** The AI can deliver a patch, explanation, and test results; commits, merges, and deployments follow actual repository permissions and approval rules.
- **Acceptance:** Inspect the diff, relevant tests, and regressions. Production behavior, when relevant, also requires proportionate reality-side verification.
- **Failure path:** Revise hypotheses on test failures; read back unknown external effects before retrying; stop and ask for permission before out-of-scope actions.
- **Boundary:** A produced patch does not establish correctness, deployment authorization, or completed business outcomes.

## Interaction record and reopening

- **Minimal record:** Purpose and next transition, participants and affected parties, confirmed observations versus conjectures, available mechanisms or capabilities, chosen interaction, explicit commitments, authority limits, unresolved issues, acceptance evidence, and reopening triggers.
- **Proportionate process:** Low-risk reversible communication needs no heavy workflow. Cross-actor, persistent delegation, or high-impact actions justify stronger evidence, independent checks, and recovery provisions.
- **Reopen when:** Consent is withdrawn, abilities or permissions change, key predictions fail, third-party effects emerge, correction is too slow, or results diverge. Reassess [sufficiency](../framework/sufficiency.md) and return to [exploration](../framework/activities/exploration.md) if needed.
- **Non-substitution:** Communication is not commitment; commitment is not authorization; execution is not external effect; effect is not completed outcome; bilateral benefits are not global optimality or normative legitimacy.

## Formal mechanism cases

## C03 Gale–Shapley: proposing side changes the stable allocation

- Assumptions: Men A: X>Y and B: Y>X; women X: B>A and Y: A>B. Strict complete rankings, one-to-one deferred acceptance.
- Expectation: Men propose → A-X, B-Y. Women propose → B-X, A-Y. Neither matching contains a blocking pair.
- Change: Switching the proposing side changes this fixture's outcome. Reordering proposals within the same side does not change the standard algorithm's result for fixed strict preferences.
- Do not infer: Stable formal matching establishes enduring real-world consent or relationship quality.

## C06 Public goods: free-riding incentives

- Assumptions: Four actors each start with 1 unit, contribute either 0 or 1, and receive an equal quarter of twice total contributions plus unspent endowment.
- Expectation: Contributing 1 adds only 0.5 to personal common-pool receipts, so not contributing strictly dominates for every profile of others. All contribute → 2 each, sum 8; none → 1 each, sum 4.
- Change: A different return multiplier or incentive arrangement needs a new calculation.
- Do not infer: Privately dominant choices maximize collective output.

## C07 Single-item VCG auction: qualified truth-telling incentives

- Assumptions: Private values, quasi-linear utility, standard second-price auction; values and truthful bids A=10, B=8, C=5.
- Expectation: A wins, pays 8, utility 2. Truthful bidding is weakly dominant under the standard mechanism, not strictly better than every deviation.
- Change: Collusion, externalities, or violated mechanism assumptions require requalification.
- Do not infer: A submitted bid verifies an actor's private valuation.

## C08 Congestion game: equilibrium versus minimum total delay

- Assumptions: Two travelers use route A or B; latency of A equals its number of travelers, latency of B is fixed at 2.5.
- Expectation: (A,A) is a strict Nash equilibrium, latency 2 per traveler and total 4; a split assignment costs 1+2.5=3.5 and minimizes total cost among four action profiles.
- Change: Altering the number of travelers or latency functions changes the game.
- Do not infer: Local optimality establishes compositional sufficiency or global optimization.

## C09 Nash bargaining: dependence on disagreement point

- Assumptions: Transferable total 10, disagreement point (1,3), linear utilities, continuous feasible allocations and individual rationality.
- Expectation: Maximize (x-1)(y-3) under x+y=10; unique Nash bargaining solution (4,6).
- Change: New disagreement points, utility mappings or feasibility constraints need a new solution.
- Do not infer: The mathematical solution establishes legal or ethical entitlement.

## C10 Cooperative core: existence of a stable grand-coalition allocation

- Assumptions: Actors A/B/C each yield 0 alone; any pair yields 100; grand coalition yields 120. Transferable utilities, full allocation of coalition value.
- Expectation A: Core empty; pair constraints summed require 2×120≥300, which is false.
- Change: Raising grand-coalition value from 120 to 150 gives a nonempty core with unique allocation (50,50,50).
- Do not infer: Feasible pairwise cooperation guarantees a stable grand coalition.
