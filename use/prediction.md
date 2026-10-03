# Prediction

[English](prediction.md) | [简体中文](prediction.zh-CN.md)

Prediction asks: **What may follow under explicitly stated models, evidence, scope, and conditions?** It is conditional inference, not guaranteed outcomes or an automatic choice of action. A formal game equilibrium is not an empirical forecast of human behavior.

## Method

1. Specify the target, outcome, time horizon, and applicability conditions; distinguish formal inference, empirical forecasts, and intervention/causal forecasts.
2. State the model, payoffs, preferences, move order, information, sources, ungenerated alternatives, and residual unknowns.
3. Derive conditional results. Report multiple equilibria, proven nonexistence, or identification limits without presenting one answer as uniquely determined.
4. Change material assumptions to test counterfactuals and sensitivity; actors may adapt to rules, published predictions, or others' actions.
5. Freeze empirical forecasts, baselines and metrics ex ante; verify independent outcomes using [evaluation](evaluation.md).

Foundations: [sufficiency](../framework/sufficiency.md), [causality](../framework/dimensions/causality.md), [possibility](../framework/dimensions/possibility.md), and [multi-actor systems](../framework/multi-actor.md).

## Formal-model cases

These are finite mathematical fixtures, **not observational evidence about human behavior**. Each preserves assumptions, reproducible expectations, changes of conditions, and prohibited extrapolations.

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

## Validation boundary

Run `python -m unittest discover -s tests -p "test_judgment_cases.py" -v` from the repository root. These tests check finite instances, not general theorems or empirical predictive accuracy. For mechanism cases see [leverage](leverage.md); for validation methods see [evaluation](evaluation.md).
