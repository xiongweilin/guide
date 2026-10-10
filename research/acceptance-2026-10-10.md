# Action-first concept reconstruction — merge acceptance record

Date: 2026-10-10. Scope: **research-code merge**, not empirical validation or a frozen ontology release.

## Immutable candidate and reproducibility

- Repository: `xiongweilin/guide`, PR [#31](https://github.com/xiongweilin/guide/pull/31).
- Examined source HEAD: `d543958242e3b5f362ea8a79f52d9dad6fe6b86d`.
- Base on inspection: `d20aa4896a9f4aca88c3ca54a206a83ffc302282`; no merge-base drift.
- [GitHub Actions 38052360804](https://github.com/xiongweilin/guide/actions/runs/38052360804): **29 tests passed** on the examined logic. Earlier run [38052357160](https://github.com/xiongweilin/guide/actions/runs/38052357160) was also green.
- New regression: `tests/test_action_first_semantics.py` enumerates **512** possible binary safe/authorized truth relations across three worlds × three actions, and all **7** nonempty belief sets per relation. It checks action validity, refinement monotonicity, observation separating action requirements, lack of gain for uninformative observation, and omitted-real-world counterexample.

## Claim acceptance matrix

| Claim | Evidence | Decision |
| --- | --- | --- |
| Basic action does not require a retained self-model as a stipulated premise | New bilingual derivation, bounded-actor and lifecycle, plus Lean model-relative counterexample | **Qualified conceptual revision** |
| A common authorized safe action remains safe under genuine belief refinement | Exhaustive finite regression and conditional Lean `RobustAction.survives_information_refinement` | **Accepted in finite/model-relative scope** |
| Observation may unlock branch-dependent safe actions | Disjoint-action countermodel and BAA conditional policy integration | **Accepted in enumerated model** |
| The framework improves real human judgment | No new paired human trials | **NOT ACCEPTED** |
| The proposed dependencies constitute a universal ontology | No such proof | **NOT ACCEPTED** |

## Explicit limitation and merge gate

A nonempty common action intersection is a sufficient decision criterion *only when* the compatible-world set conservatively covers reality, actions accurately refine to their execution surfaces and authorization comes externally. No actual-world sufficiency follows when hazards are missing.

Merge the **research framework** only when PR tests remain green on the final tree and PR HEAD is unchanged at merge. Do not use this acceptance record to claim real-world judgment gain; that requires independent adjudicated empirical studies. The existing historical studies remain unmodified.

The Git commit containing this note may differ from the **examined source HEAD**; a documentation-only acceptance commit must be checked again in CI.
