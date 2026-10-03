# Multi-actor judgment and prediction: ten reproducible cases

[English](./judgment-prediction-cases.md) | [简体中文](./judgment-prediction-cases.zh-CN.md)

> These are **formal-model fixtures** for the [judgment and prediction validation protocol](../judgment-validation.md). They check within-model derivations and changes of assumptions, not empirical human behavior or the framework's overall truth. Payoffs are local to the stated fixtures.

## Use and acceptance

Each case specifies **assumptions → testable claim → independently reproducible expectation → changed-condition expectation → prohibited inference**.

From the repository root, run the Python standard-library tests:

```bash
python -m unittest discover -s tests -p "test_judgment_cases.py" -v
```

Automated tests check only these **finite numerical examples**, plus Markdown fence balance and local links for this case collection and the validation protocol. They neither prove general theorems nor measure empirical forecast quality.

## C01 One-shot prisoner's dilemma: individual versus collective optimum

- Assumptions: Simultaneous cooperate C or defect D; (C,C)=(3,3), (C,D)=(-1,5), (D,C)=(5,-1), (D,D)=(1,1).
- Expectation: D strictly dominates C for both; unique pure Nash equilibrium (D,D), total 2. (C,C) totals 6 and Pareto-dominates (D,D).
- Change: Repeated observable interaction cannot inherit the full-game result merely from one-shot dominance.
- Do not infer: Nash equilibrium means maximum social welfare or normative rightness.

## C02 Repeated prisoner's dilemma: fixed end versus uncertain continuation

- Assumptions: C01 stage payoffs, perfect information about past actions, fully rational players, no extra reputational utility.
- Expectation A: With a commonly known horizon of exactly 200 rounds, backward induction yields the all-defect path as the unique subgame-perfect equilibrium path.
- Expectation B: With independent continuation probability δ and grim-trigger punishment, cooperation deters one-shot defection when 3/(1-δ) ≥ 5+δ/(1-δ), i.e. δ ≥ 1/2 (indifference at equality).
- Change: δ=0.4 violates this condition; δ=0.6 satisfies it.
- Do not infer: Grim trigger is universally optimal against all opponents or under observation noise.

## C03 Gale–Shapley: proposing side changes the stable allocation

- Assumptions: Men A: X>Y and B: Y>X; women X: B>A and Y: A>B. Strict complete rankings, one-to-one deferred acceptance.
- Expectation: Men propose → A-X, B-Y. Women propose → B-X, A-Y. Neither matching contains a blocking pair.
- Change: Switching the proposing side changes this fixture's outcome. Reordering proposals within the same side does not change the standard algorithm's result for fixed strict preferences.
- Do not infer: Stable formal matching establishes enduring real-world consent or relationship quality.

## C04 Stable roommates: prove nonexistence

- Assumptions: Strict rankings A: B>C>D; B: C>A>D; C: A>B>D; D: A>B>C; everyone must have exactly one roommate.
- Expectation: Of three perfect matchings, AB/CD is blocked by BC; AC/BD by AB; AD/BC by AC. No stable perfect matching exists.
- Change: Changed preferences or admissibility constraints define a new problem to solve.
- Do not infer: A failed search, without proof, establishes impossibility.

## C05 Stag hunt: beliefs determine a best response

- Assumptions: Each chooses stag S or hare H; (S,S)=(4,4), (S,H)=(0,3), (H,S)=(3,0), (H,H)=(3,3).
- Expectation: Pure Nash equilibria are (S,S) and (H,H). With belief p that the other hunts stag, utility of S is 4p and utility of H is 3, equal at p=0.75.
- Change: p=0.5 favors H; p=0.8 favors S.
- Do not infer: Calculating a best response accurately estimates an actual opponent's probability.

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
- Expectation B: Grand-coalition value 150 instead yields a nonempty core with unique allocation (50,50,50).
- Do not infer: Feasible pairwise cooperation guarantees a stable grand coalition.

## Suggested validation record

- Capture each fixture's model version, inputs, independent calculation, and expected conclusion.
- After meaningful condition changes, withdraw applicability to the new setting before recomputing; retain history.
- Repair proven formal inconsistencies. Use separate ex ante forecasts and real-world outcome records for empirical accuracy; never manufacture such measurements from static examples.
