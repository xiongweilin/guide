# 精确语义

> **六维定位：跨六维的工程语义。** 本篇负责防止区分、资格、价值、能力、变化和他者中的状态被压成同一个字段或被静默替代。理论定义见 [README 的六维地图](./README.zh-CN.md#人类活动的六个基础维度) 与 `theory/` 下六篇文档。

工程目标不是实现一个总控式 `qualified = true`，也不是让六维中的任何一个维度成为另外五个维度的语义 owner。目标是保存六维之间的 non-substitution，并让重要转换的依据保持显式。由于软件最容易把状态转换中的短路藏进字段和流程，本文会使用较多 qualification 机制；这种工程表达密度**不表示资格在理论上高于区分、价值、能力、变化或他者**。

六维在框架中同等基础，但不要求实现成六个独立字段、服务或层级。资格保存转换语义，区分保存表示边界，价值保存规范方向，能力保存可达性，变化保存时间与结构状态，他者保存关系和多参与者结构。工程上的要求是保存这些边界、相互作用和反馈关系，而不是强迫它们一一对应某种物理拆分，更不能把它们压成一个总状态。

核心链：

`request / trigger → problem framing / question qualification（需要解释时） → claim / fact → policy evaluation → decision → governance basis → authorization → execution → observation → verification → obligation completion → revalidation / discharge`

符合这套工程语义，不等于某个表示已经成为关于世界的真理。现实侧 observation、反例、effect 失败和条件变化都可以使当前记录、contract 或假设失效，并最终要求 guide 自身的区分和结构接受修订。

## 0. 认知边界不是一个数据库字段

工程系统必须区分认知边界与可操作语义。

- **世界（认知边界）**不是一个等待被完整序列化的对象。系统不应声称某个 schema、ontology、embedding space 或 knowledge graph 已经穷尽世界。
- 本文中的 **Reality / 现实** 指当前任务中可以由来源、observation、read-back 或 reconciliation 建立的外部状态。它属于可区分世界中的操作切片，不等于世界本身。
- **可区分范围**由当前 source、sensor、API、语言、工具、权限和能力共同限制；**已区分范围**是系统实际形成并可调用的 distinctions。两者都是带版本的操作条件，不是固定边界：新的区分、工具、接口、权限或协作方式都可能使后续可区分范围扩大或收缩。
- schema、enum、label、policy category 和 model taxonomy 都可能只是**默认区分**。存在于 schema 中不等于它具有世界本体论上的优先地位。

当系统需要解释开放式请求、自己生成问题或重构任务 framing 时，还应显式保留 problem semantics：

```text
DistinctionContext
- scope / purpose
- distinguishable_sources / interfaces
- currently_distinguished_categories
- default_distinctions / assumptions
- unknown_or_excluded_space
- version / provenance

QuestionCandidate
- text / structured_form
- objects / predicates / relations
- scope / time_scale / principals
- expected_answer_type
- source

QuestionQualification
- question_ref
- primitive_regimes: [interpretive] | [specified] | [interpretive, specified]
- presuppositions
- default_distinctions
- competing_framings
- unsupported_boundaries
- disposition: qualified | needs_refinement | reframed | rejected | unknown
- reasons
- qualified_at
```

并非每个固定 API 调用都需要单独持久化这些对象；但只要 framing 会实质改变目标、scope、authority、不可逆性或完成条件，就不能把“收到一句请求”直接压成“问题已经成立”。

### 资格机制本身也是语义

工程系统不仅要保存最终资格状态，还必须保存“这个足够是怎样成立的”。

至少区分：

- **解释型资格**：通过对语境、证据、反证、假设、竞争 framing 和剩余未知的可追责判断形成“足够”；
- **规定型资格**：按照显式且带版本的规则、predicate、threshold、guard、test、approval set 或 contract 计算“足够”；
- **混合资格**：两种原始机制的显式组合，例如先解释判断某条规则是否适用，再执行规定型 evaluation。混合资格是组合，不是第三种原始机制。

可以存在共同 envelope，但必须保留各机制自己的依据：

```text
QualificationBasis
- qualification_id
- primitive_regimes: [interpretive] | [specified] | [interpretive, specified]
- subject / target_transition
- scope / purpose / time_scale
- accountable_owner
- basis_version
- review / reopen conditions

InterpretiveQualificationAssessment
- qualification_ref
- evidence / counterevidence
- assumptions / default_distinctions
- competing_interpretations
- residual_unknowns / accepted_risk
- reasons
- accountable_judge
- disposition
- assessed_at

SpecifiedQualificationRule
- qualification_ref
- rule_id / version
- authority_source
- applicability_scope / effective_period
- required_inputs
- predicates / thresholds / required_conditions
- exceptions / override_conditions

SpecifiedQualificationEvaluation
- rule_ref
- input_versions
- result
- unmet_conditions
- evaluator
- evaluated_at
```

`解释型 assessment ≠ 规定型 rule evaluation`

`规定规则 evaluation 为真 ≠ 规则对当前对象适用 / 仍有效 / 具有 authority`

如果规则的 applicability、scope、含义或 exception handling 本身存在实质含糊，就必须先进入解释型资格；在这个问题解决之前，规定型 evaluation 不能独自承担 transition。

反复出现的解释判断可以后来被规则化，但 rule-making 必须显式产生 definition、version 和 authority。历史解释不能静默变成确定性 policy。

## 1. 先禁止语义捷径

| 已经成立的事实 | 不能自动推出 | 还需要的条件 |
| --- | --- | --- |
| 已接收到请求 / 文本 | 问题结构已经成立 | problem framing、presupposition check、question qualification |
| schema 中存在分类 | 该分类就是世界的真实边界 | source evidence、boundary validation、alternative framing |
| 已接收到数据 | 内容为真 | source、provenance、validation |
| 模型置信度高 | authoritative fact | authority、evidence |
| fact 可用 | policy 已满足 | policy version、evaluation input |
| policy 已满足 | Decision 有效 | accountable principal、scope、authority |
| Decision 有效 | approval 完成 | required roles / conditions |
| approval 完成 | runtime 可以执行 | current authorization、resource、operation |
| provider success | effect 已发生 | authoritative readback / reconciliation |
| effect 已发生 | goal 已实现 | semantic verification |
| 一个 outcome 成功 | case 已完成 | independently derived obligations |
| case 完成 | 长期责任已解除 | residual obligations、handoff、discharge |
| 历史上有效 | 现在仍有效 | freshness、revalidation、reauthorization |

如果一个字段跨越表中两个以上边界，应检查是否发生 semantic flattening。

## 2. 保持 source、claim、evidence 和 fact 区分

外部输入进入系统后，至少区分：

`raw input → representation → claim → validated / authoritative fact`

最小字段：

```text
FactClaim
- key / value
- source
- source_ref
- source_version
- observed_at
- provenance
- authority: claim | derived | authoritative
- epistemic_status: unverified | supported | contested | refuted | unknown | revalidation_required
```

AI extraction、用户输入、cache、search index 和同步 replica 默认都不是 authoritative source。

一条记录存在、很新，或模型置信度很高，都不能替代 source authority。

## 3. 保持 identity、role、delegation 和 authorization 区分

Authentication 只回答“这是谁？”

Runtime authorization 至少应绑定：

```text
Authorization
- principal
- operation
- resource / subject
- scope
- authority_source
- delegation_ref (optional)
- issued_at
- expires_at / revocation_version
```

Role、历史 assignment、组织职位或业务 Decision 都不能自动变成当前 resource permission。

Permission 不能自动跨 operation、resource、scope、context 或 time 转移。

## 4. 保持 policy definition、evaluation 和 Decision 区分

规则定义和把规则应用到当前 facts 的结果是不同对象。当规则 applicability 已经成立时，这就是规定型资格的典型工程路径；如果 applicability 本身含糊，则必须先经过解释型资格，再进入 policy evaluation。

```text
PolicyVersion
- policy_id
- version
- owner
- effective_from / until
- definition_digest

PolicyEvaluation
- policy_version
- input_fact_versions
- result
- reasons / unmet_conditions
- evaluated_at

Decision
- decision_id
- subject
- scope
- purpose
- principal
- authority_basis
- policy_version
- input_versions
- disposition
- created_at
```

Decision 必须绑定当时支持它的 inputs 和 rules。旧 ID 仍存在不表示 Decision 现在仍可使用。

## 5. 保持规则适用、激活和执行授权区分

一个 rule set 可以：

1. **适用于**当前对象；
2. **在当前范围激活**；
3. 允许某个具体 principal 对具体 resource 执行具体 operation。

三者不能合并。

Rule applicability 不会创造 resource permission；activation 也不会。

## 6. Governance basis：冻结当时为什么成立

高影响 Decision 或 grant 应保存可重建的治理依据：

```text
GovernanceBasis
- subject / case_id
- authority_epoch
- fact_dependencies + versions / digests
- policy_version + definition_digest
- scope
- required approvals / roles
- role / delegation qualification refs
- other domain qualifications
- unresolved_reviews
- expected_self_induced_changes
- created_at
```

它有两个目的：

- 重建当时为什么 Decision 或 grant 成立；
- 判断现在是否仍成立。

执行本身预期会改变的字段，不应同时被当作“变化后使 governance basis 失效”的 dependency；真正的 prerequisite dependency 变化则必须触发 revalidation。

## 7. 保持 valid state 与 valid transition 区分

显式状态机中的每个重要 transition 至少检查：

```text
current_state
+ trigger
+ expected_version
+ preconditions
+ current_authorization
+ decision / governance basis binding
+ freshness
+ allowed_side_effects
→ next_state
```

还应记录 transition provenance。

合法终点不能证明路径合法。

并发更新应使用 version column、ETag、compare-and-swap、optimistic locking 或等效机制。发生冲突时，应重新读取当前状态，而不是允许 last-writer-wins 擦掉语义冲突。

## 8. Frame condition：只改变声明范围

Operation 应声明自己拥有的 change scope，以及允许产生的 side effect。

执行后不仅验证 target field，还要验证关键的不应变化字段。

扩大范围、权限、对象集合或副作用类型，应进入新的 review / authorization 路径，而不是继承旧 Decision。

## 9. Freshness 表示依赖仍有效，不只是“时间新”

当前 qualification 可能因以下变化失效：

- authoritative source 或 source version；
- policy definition / version；
- role、delegation 或 authority；
- scope / partition / assignment；
- model / data / code / tool；
- dependency / environment / resource；
- unresolved review；
- critical assumption。

因此 freshness 应基于 dependency check，而不是只看 timestamp。

## 10. 保持 review、revalidation、reopen 和 reauthorization 区分

- **review obligation**：发生变化，需要重新检查；
- **revalidation**：判断旧 fact、Decision、basis 或 grant 是否仍适用；
- **reopen**：恢复 fact gathering、candidate generation 或 governance flow；
- **reauthorization**：重新取得执行或长期权限。

Dependency change 通常先产生 review obligation。它不应自动改写历史 Decision，也不应自动生成新 Decision。

## 11. 保持 transport idempotency 与 effect idempotence 区分

使用相同 idempotency key 可以防止一个请求被重复处理，但不能证明外部副作用可以安全重复。

Execution record 至少保存：

```text
ExecutionAttempt
- request_id
- decision_id / authorization_id
- subject / resource
- operation
- idempotency_key
- expected_postcondition
- provider_ref
- started_at / finished_at
- transport_result
```

Payment、message、account creation、grant 等操作在 timeout 后可能已经发生。含糊结果默认应进入 reconciliation；不应直接分类成 failure，也不应默认 retry。

## 12. 保持本地 transaction 与外部一致性区分

数据库 transaction 只保证本地 atomicity，无法让数据库和外部系统共同原子 commit。

根据业务语义选择 transactional outbox、inbox/deduplication、saga、compensation、durable workflow 或 reconciliation worker。

无论实现如何，系统都必须能够表示 partial success 和 unknown effect。

## 13. Observation 读取现实，不是 executor echo

```text
Observation
- authoritative_source
- subject_identity
- source_version
- observed_at
- availability
- freshness
- presence
- state
```

至少应能表示：

`present | absent | unavailable | unknown`

以及：

`fresh | stale | unknown`

Source unavailable 不代表 object absent；unverified 不代表 failed。

## 14. Verification 检查冻结的 postcondition

```text
Verification
- execution / effect ref
- expected_postcondition
- observation_ref
- disposition: verified | absent | mismatch | unavailable | stale | unknown
- differences
- verifier
- verified_at
```

Verification 应读取合适的权威现实来源，并检查 identity、target state、scope 和 unexpected side effect。

Executor 自己的 success output 不能替代对现实的独立 verification。

## 15. Effect provenance 必须连续

如果系统声称“这个 operation 产生了这个 result”，应该能够追踪：

`request → facts → evaluation → Decision → authority → execution → observation → verification → outcome`

最终状态正确，不足以证明因果链正确。人工操作、并发 operation 或重复 execution 都可能产生同一终点。

## 16. Obligation 必须独立于 planner

业务要求完成什么，不应由 execution planner 自己定义。否则一个遗漏步骤的 planner 可能制造内部一致的假成功。

```text
Obligation
- obligation_id
- subject
- required_state / operation
- authority_class
- required
- source_policy / decision

CompletionAssessment
- obligation_set_ref
- covered_effects
- verified_outcomes
- missing / mismatched obligations
- residual obligations
- satisfied
```

`verified effect ≠ case complete`

`case complete ≠ responsibility discharged`

长期责任还可能要求 handoff、successor、compensation、持续观察或明确 discharge 条件。

## 17. Record type、epistemic status 与 lifecycle 正交

不要把 record type、epistemic state 和 lifecycle 压成一个 enum。

Record 可以是 DistinctionContext、QuestionCandidate、QuestionQualification、Evidence、Observation、Assertion、Derivation、Goal、Constraint、Experiment、Decision、Action、Policy、Outcome、Revision 或 ChangeObject。

同一 record 可以同时是 unverified、supported、contested、refuted、unknown 或 revalidation_required。

历史 record 应保留；现在不可使用不意味着应从历史删除。

## 18. Audit log 不改写历史

重要链路应使用 append-only record 或等效可追踪设计。

Revoke Decision、rollback、compensate 或 reopen 应创建新记录，而不是删除旧记录。

至少应能够回答：谁在什么 input 和 rule 下做了什么；谁授权；执行了什么；现实后来变成什么；如何验证；为什么后来又变化。

## 19. Semantic entry point 是 trust boundary

来自模型、外部服务、用户或其他系统的内容，进入 semantic core 前必须按 source type 验证。

任何扩大 qualification、清除 blocker 或创建 side effect 的正向 transition，在 source、authority、freshness、scope 或 provenance 缺失时应 fail closed。

Fail closed 只意味着“系统现在不能继续”，绝不能伪造相反事实。

## 20. Responsibility role 不得互相冒充

- parser / extractor：产生 representation / claim；
- reasoner：产生 candidate 和 reason；
- policy evaluator：计算 rule result；
- decision maker：形成业务 Decision；
- authorization layer：授予当前 operation 权限；
- executor：尝试改变现实；
- observer：读取现实；
- verifier：判断 postcondition；
- reconciliation / recovery：处理 ambiguity 和 failure；
- reviewer：处理 revalidation / reopen / reauthorization。

一个进程可以实现多个 role，但 contract 和 record 必须保留这些 role 的区别。

角色分离还不等于故障独立。两个 verifier、reviewer、model 或 control path 即使语义角色不同，只要共享相同的数据、模型、指标、训练来源、identity infrastructure、authority source、技术根或利益结构，仍可能因为同一原因一起失败。

因此至少保持：

`role separation ≠ failure independence`

`multiple evaluators ≠ independent evidence`

只有当额外角色真实降低了 failure correlation，冗余才增加可靠性。高影响路径应显式记录或检查关键共同失败源，而不是只统计角色数量。

## 21. Compatibility 有多个版本轴

至少独立考虑：

- data / record schema version；
- state-machine semantics version；
- policy version；
- authorization contract version；
- runtime protocol version；
- model / evaluator version。

“旧 JSON 还能 parse”不表示 semantic compatibility。

升级时检查 field meaning、default behavior、permission、scope、historical interpretation 或 review requirement 是否被静默改变。

## 22. 最小可部署 contract

会产生现实副作用的系统，至少需要以下对象或等效语义。若系统还负责开放式问题 framing，则应在进入这些对象之前额外保留 DistinctionContext / QuestionCandidate / QuestionQualification 或等效语义：

```text
FactClaim
QualificationBasis + regime-specific assessment / evaluation
PolicyVersion / PolicyEvaluation
Decision
GovernanceBasis
Authorization
ObligationSet
ExecutionAttempt
Observation
Verification
Outcome / ReconciliationState
CompletionAssessment
ReviewObligation
AuditRecord
```

存储可以合并，语义不能合并。

## 23. 最小 invariant

1. AI output 默认不是 authoritative fact。
2. Decision 不直接创造底层 resource permission。
3. 执行前检查 current authorization 和关键 dependency version。
4. 合法终点不能证明 transition 合法。
5. 扩大 scope 需要新的 qualification。
6. Provider-unknown 结果不自动变成 failure，也不意味着可以安全 retry。
7. Verified outcome 来自现实 readback，而不是 executor self-attestation。
8. Obligation 独立于 planner。
9. Correction / rollback / compensation 不删除历史。
10. source、policy、authority、scope 或关键 dependency 变化进入 review / revalidation。
11. Revalidation 不自动续期 authority；reopening 不自动授权行动。
12. Completion 不自动等于长期 responsibility discharge。
13. 当前已区分范围不自动等于全部可区分范围；schema 中缺失的候选不能仅因此被标记为 impossible。
14. 能够解析或提出一个问题不等于问题已经获得资格；当 framing 影响后续 scope 或 authority 时，必须先 qualification。
15. 没有区分出可行路径时，能力状态应保持 `unknown`，不能直接变成 `cannot`；只有在明确有界的能力判断获得充分资格后，才能形成 `cannot`。
16. 六个分析维度不要求一一对应存储字段、服务或 runtime layer；实现可以合并存储，但不能合并语义边界。
17. 解释型资格和规定型资格不能互相冒充；qualification regime 及其 basis 必须保持可追踪。
18. 规定规则 evaluation 为真，不能自动建立该规则的 applicability、authority、freshness 或规范有效性；这些前提必须独立成立。
19. 解释型判断不能在没有显式 rule-making、versioning 和 authority 的情况下变成确定性规则。
20. 角色分离不自动产生故障独立；只有共同失败相关性实际下降时，多 reviewer / verifier / model 才能被当作可靠性增益。
21. 局部组件分别获得 qualification，不自动建立组合后的 qualification；当组合引入新的 assumption、scope、authority、dependency、feedback 或 side effect 时，必须建立组合层自己的兼容性与 qualification basis。

## 24. 最小 conformance test

至少测试：

- 默认 schema/category 不能在缺少依据时被当作世界本身的唯一边界；
- 当问题 framing 会改变 scope、authority 或完成条件时，未获得资格的问题不能直接进入 Decision / execution；
- 解释型 qualification 不能在没有显式语义桥接的情况下，被下游当成规定型 rule evaluation 使用；
- 规定规则即使 evaluation 为真，只要 stale、out-of-scope、unauthorized 或 applicability 尚未获得资格，就不能放行 transition；
- 规则 applicability 含糊时进入解释型资格，而不是默认规则已满足；
- 把反复解释规则化时必须产生新的显式 rule/version，不能改写历史 interpretive assessments；
- 尚未区分出可行路径、且候选空间尚未获得足够有界资格时，能力必须保持 `unknown`，不能直接标记为 `cannot`；
- 工具、接口、权限、能力或协作方式变化时，可以触发可区分范围的 reopening / revision，而不能只在旧范围内修改一个字段；
- 高置信度 model claim 不能直接进入 authoritative fact；
- 多个 reviewer / verifier / model 即使角色不同，只要共享关键共同失败源，就不能被测试当作独立证据或独立冗余；
- 两个或多个局部对象分别 qualified 时，若其组合产生新的 scope、assumption、authority、dependency、feedback 或 side effect，而没有组合层 basis，则不能把组合整体标记为 qualified；
- stale fact / policy / Decision / authority 被拒绝；
- operation 不能超出 authorization scope；
- 即使 endpoint 本身合法，illegal transition 也会被拒绝；
- 预期 self-induced change 不会错误使自身 governance basis 失效；
- 真正 dependency change 会触发 revalidation；
- timeout / lost acknowledgment 会进入 reconciliation，而不是直接 retry；
- provider success 但现实 mismatch 不能确认成功；
- cross-effect / cross-subject outcome 不能替代正确 verification；
- planner 漏掉 obligation 时 completion 失败；
- rollback 后原始 Decision、attempt 和 observation 仍可追踪；
- 存在 residual obligation 时，已完成 workflow 不能标记为 responsibility discharged。

这些测试比术语本身更重要：如果一个理论边界不能改变 contract、transition、failure path 或 test，就不应继续占据工程语义层。
