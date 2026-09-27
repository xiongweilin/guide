# 精确语义

> **六维定位：跨六维的语义边界。** 本篇负责防止区分、资格、价值、能力、变化和他者中的状态被压成同一个字段或被静默替代。总纲见[《人类活动的六个基础维度》](./six-dimensions-of-human-activity.zh-CN.md)。

工程目标不是实现一个 `qualified = true`，而是保存每个 qualification slice 的独立条件，使系统不能把某一层的有效性自动提升为下一层的有效性。

核心链：

`request / trigger → problem framing / question qualification（需要解释时） → claim / fact → policy evaluation → decision → governance basis → authorization → execution → observation → verification → obligation completion → revalidation / discharge`

## 0. 认知边界不是一个数据库字段

工程系统必须区分认知边界与可操作语义。

- **世界（认知边界）**不是一个等待被完整序列化的对象。系统不应声称某个 schema、ontology、embedding space 或 knowledge graph 已经穷尽世界。
- 本文中的 **Reality / 现实** 指当前任务中可以由来源、observation、read-back 或 reconciliation 建立的外部状态。它属于可区分世界中的操作切片，不等于世界本身。
- **可区分范围**由当前 source、sensor、API、语言、工具和权限共同限制；**已区分范围**是系统实际形成并可调用的 distinctions。
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
- presuppositions
- default_distinctions
- competing_framings
- unsupported_boundaries
- disposition: qualified | needs_refinement | reframed | rejected | unknown
- reasons
- qualified_at
```

并非每个固定 API 调用都需要单独持久化这些对象；但只要 framing 会实质改变目标、scope、authority、不可逆性或完成条件，就不能把“收到一句请求”直接压成“问题已经成立”。

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

规则定义和把规则应用到当前 facts 的结果是不同对象。

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

## 24. 最小 conformance test

至少测试：

- 默认 schema/category 不能在缺少依据时被当作世界本身的唯一边界；
- 当问题 framing 会改变 scope、authority 或完成条件时，未获得资格的问题不能直接进入 Decision / execution；
- 高置信度 model claim 不能直接进入 authoritative fact；
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
