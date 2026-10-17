# Interaction

[English](interaction.md) | [简体中文](interaction.zh-CN.md)

## Method

1. Identify actors, affected parties, purposes, local boundaries, resources, and authority; shared reality does not imply shared representations or goals.
2. Bind messages and actions to referents, versions, scope, time, evidence, intended results, and the relevant meaning of request, report, decision, and commitment.
3. Keep definition, sufficiency judgment, decision, consent, authorization, execution, verification, and completion distinguishable when their differences matter.
4. Check [local sufficiency](../framework/sufficiency.md) for each material next transition. Where actions are coupled, also check compatibility, shared dependencies, and minimum recoverability.
5. Establish explicit handoffs, acceptance criteria, obligations, acknowledgement or refusal, expiration, escalation, and controlled correction or exit.
6. Validate independent real-world effects through [evaluation](evaluation.md); revise or reopen when meaning, authority, constraints, or outcomes diverge.

## Human–human interaction

- **Problem:** people can understand the same words while differing in facts, interpretations, incentives, values, priorities, or legitimate authority.
- **Procedure:** distinguish disputes over evidence, framing, causality, time, resources, interests, rights, and decision procedures. Identify who defines alternatives, judges sufficiency, decides, consents, or may reopen.
- **Result:** a traceable agreement or explicit disagreement identifying scope, affected parties, commitments, acceptance criteria, and rights of review or exit.
- **Example:** “release approved” may mean technical readiness, product acceptance, or legal sign-off; specify which principal approves which version under what conditions.
- **Limit:** negotiation success, voting, or strategic advantage does not by itself establish fairness, authority, or normative legitimacy.

## Human–AI interaction

- **Problem:** human instructions incompletely express intended outcomes, while an AI may interpret wording, tools, permissions, and success criteria differently.
- **Procedure:** establish objective, operating boundary, delegated authority, prohibited effects, observable postconditions, and when clarification or human approval is needed.
- **Result:** bounded delegation: permitted exploration and action, explicit unresolved unknowns, reliable verification, and handback or controlled stopping where authority or sufficient grounds are missing.
- **Example:** “ship this feature” is not by itself permission to merge any branch or deploy production; bind the request to a version, environment, required tests, approver, and read-back.
- **Limit:** a confident response, an approval click, or a successful API call is not automatically informed consent, valid authorization, real effect, or task completion.

## AI–AI interaction

- **Problem:** agents with aligned task names may still hold different local boundaries, schema versions, assumptions, capabilities, resources, and constraints.
- **Procedure:** exchange task and object identity, interface contracts, state versions, evidence, owners of shared resources, permissions, expected effects, and failure handling; coordinate concurrent writes and deadlines.
- **Result:** compatible local transitions, inspectable handoffs, and independently verified composite outcomes without requiring complete shared representations.
- **Example:** two coding agents can each pass unit tests while implementing incompatible API schemas; schema ownership, integration tests, merge guards, and recovery belong to the joint transition.
- **Limit:** local sufficiency does not imply compositional sufficiency, linear speedup, shared purpose, or global optimality.

## Shared interaction record

- **Context:** actor identity and role, affected parties, purpose, scope, time, boundary version, evidence sources, and authority.
- **Meaning:** object references, message type, relevant distinctions, interpretation, assumptions, alternatives, and unresolved mismatches.
- **Commitment:** proposal versus acceptance, decision owner, authorization, next transition and sufficiency grounds, deadline, expiry, and acceptance criteria.
- **Feedback:** execution attempt, actual effect, independent observation, verification, outstanding obligations, recovery state, and reopening conditions.

## Formal interaction mechanism cases

- **Scope:** C03, C06, C07, C08, C09, and C10 remain finite multi-actor formal mechanisms; they do not establish real-world consent, empirical predictions, or legitimate authority.


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
