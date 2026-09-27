# AIOS 架构

> **六维定位：六维的工程应用。** 本篇不是六维框架的来源，而是展示一个持续运行技术系统怎样在工程上保存这些边界。理论定义见 [README 的六维地图](./README.zh-CN.md#人类活动的六个基础维度) 与 `theory/` 下六篇文档。

六个维度在这里仍然同等基础。资格之所以在 runtime 中频繁出现，是因为 admission 和状态转换需要显式 gate；这种实现需求不使资格成为区分、价值、能力、变化或他者的 owner，也不使它成为最高层解释。现实侧反馈可以要求这些表示中的任何一个重开，也可以要求 guide 自身重开。

## 认知边界与架构中的 Reality

AIOS 不把“世界本身”实现成一个总 ontology。

- **世界（认知边界）**：表示当前 observation、schema、模型和存储都不能被默认视为世界本身的完整结构；它不是 runtime 中的 durable object。
- **可区分世界 / 可区分范围**：由当前 source、sensor、provider、API、语言、工具、权限和 domain interface 共同决定，表示原则上能够进入系统区分与验证的现实侧面。
- **已区分范围**：AIOS 当前实际获得、形成并能够调用的 distinctions，包括已建立的 facts、categories、relationships、problem framings 和 domain states。
- 架构图中的 **Reality**：特指某个 domain 中可通过 authoritative observation、read-back 或 reconciliation 建立的现实状态，是可区分世界中的任务切片，不等于“世界本身”。
- **Personal World**：只持有一个人的 durable、qualified、可追踪的个人上下文，是已区分范围的一部分；名称不表示它拥有这个人的全部可区分世界，更不表示它是世界本体模型。

因此，AIOS 必须同时允许两种 revision：一是更新已知值，二是重新打开当前的区分、分类、问题 framing 和候选空间。后者不能被简化成“某个字段值变了”。

当一个 request、standing mandate 或 autonomous trigger 需要解释时，入口链应允许：

`trigger / request → distinction context → question / task candidate → question qualification → domain admission → judgment / decision / authorization`

固定且已 qualification 的 machine contract 可以跳过重复的问题持久化；但任何会改变 goal、scope、authority、irreversibility 或 completion semantics 的 framing 都必须先重新获得资格。

AIOS 必须保留两种资格机制，而不能把它们压成一个 `qualified` flag：

- 开放式 framing、诊断、例外处理和 applicability 含糊的情况，通常进入**解释型资格**，并保留 reasons、evidence、剩余未知和可追责的判断边界；
- 固定 contract、policy predicate、状态机 guard、verification gate 和明确 approval condition，通常进入**规定型资格**，并绑定被检查的准确 rule/version 与 input versions。

同一条 flow 可以组合两者。特别是，当 scope、含义、exception handling 或 current validity 存在实质含糊时，规定规则不能自行证明自己的 applicability，而必须先回到解释型资格。反过来，反复出现的解释结果也不能自动成为 machine contract；只有经过有 authority 的 rule-making 路径显式建立新 rule/version 后，才能进入规定型资格。

## 长期自主运行时

```text
长期、无人值守闭环：

┌────────────────────────────────────┐       有边界的 effect      ┌─────────┐
│ AIOS Runtime                       ├─────────────────────────────►│ Reality │
│ observe → distinguish / qualify    │◄─────────────────────────────┤         │
│ → frame / decide → authorize       │ 权威 read-back /            └─────────┘
│ → act → verify                     │ evidence / outcome / unknown
│ Personal World / Runtime / Domains │
│ 可替换的内部 Agent/Executor        │
└────────────────────────────────────┘
```

AIOS 是一个长期运行的 AI runtime，面向低可见度、无人值守运行。它的主闭环是：AIOS 获取现实侧 evidence，必要时检查 distinctions 与 framing 的资格，形成 Decision / Authorization，执行有边界的 action，再吸收权威 observation、read-back 和 outcome evidence。日常运行不依赖人在场。

## 临时外部介入

```text
Human
  │ 必要时 query / request / approval
  ▼
现有 Agent 产品
（短生命周期 client session）
  │ 权威检查 / 解释 / 有边界且已授权的修复 / verification
  ▼
AIOS integration boundary ─────────────► Reality（需要已授权 effect 时）
  │
  └── 向 Human 报告已验证状态，然后断开
```

用户不直接把 AIOS 当成交互式助手操作。需要 inspection、explanation 或 maintenance 时，可以使用现有 Agent 产品作为临时 intervention adapter。Agent 读取权威状态、解释当前条件，只执行有边界且已授权的变更，验证 read-back 和 recovery，报告结果，然后退出。Session 结束后 AIOS 继续运行。

这个外部 Agent 不是 AIOS runtime 的组成部分，不是 durable state 或 authority owner，也不是必须存在的 runtime dependency。API/CLI 是机器集成和维护边界，不是 AIOS 的主要人机管理界面。

```text
Human presence != system operation
Human absence != suspended agency
Intervention session != durable agency
External Agent != AIOS authority owner
Agent explanation != authoritative state
Agent repair != successful recovery
Successful recovery = authoritative state + reality read-back + required verification
```

`semantic-language` 为整个架构提供跨领域语义区分。

`guide` 持有六维框架、non-substitution、可修订边界和 architectural invariants。

Agent implementation、model provider、model-routing gateway、monitoring system 和 deployment runtime 都是可替换集成。仅仅因为某次部署使用它们，并不会使其成为 durable semantic owner。

## 架构区域

```text
┌──────────────────────────────────────────────────────────────────────┐
│ AIOS — 长期自主运行时                                                │
│                                                                      │
│ Personal World ──purpose-limited context───► internal Agent/Executor│
│       ▲                                     │                        │
│       │ provenance / revision                │ analysis / candidate  │
│       │                                     ▼                        │
│       └──────────────────────────► domain admission                  │
│                         │                                            │
│ semantic-language / World Runtime / Domain Controllers              │
│ responsibility / authority / work / effects / recovery / read-back   │
└─────────────────────────┬────────────────────────────────────────────┘
                          │ governed effect / evidence return
                          ▼
┌──────────────────────────────────────────────────────────────────────┐
│ REALITY                                                              │
│ external systems / source repositories / builds / deployments /      │
│ traffic / infrastructure / organizational systems                    │
└──────────────────────────────────────────────────────────────────────┘

带外，仅在需要时：
Human ⇄ existing short-lived Agent product ⇄ AIOS machine boundary
```

AIOS runtime 是 headless 且仅容器运行。容器只是部署边界，不是 durable semantic owner。内部 Agent/executor implementation、model provider、monitoring system 和外部 Agent client 都保持可替换；AIOS 自主连续性不依赖其中任何一个具体实现。

## 仓库拓扑

| 仓库 / 组件 | 所有权 |
| --- | --- |
| [guide](https://github.com/xiongweilin/guide) | 六维框架、non-substitution、可修订边界、architectural invariant |
| [aios](https://github.com/xiongweilin/aios) | AIOS 源码组件的 monorepo 和 Git owner |
| [semantic-language](https://github.com/xiongweilin/aios/tree/main/src/semantic/semantic_language) | 跨领域含义和 non-substitution rule |
| [personal-world](https://github.com/xiongweilin/aios/tree/main/src/kernel/personal_world) | durable personal facts、preference、relationship、resource link、provenance、revision、freshness、privacy boundary、purpose-limited context |
| [world-runtime](https://github.com/xiongweilin/aios/tree/main/src/kernel/world_runtime) | durable agency state、responsibility、authority、decision、qualification、execution identity、recovery、reconciliation、history |
| [control-plane](https://github.com/xiongweilin/aios/tree/main/src/domains/control_plane) | operational incident、有边界 repair、monitoring、operational provider、operational outcome evidence |
| [administrative-orchestrator](https://github.com/xiongweilin/aios/tree/main/src/domains/administrative_orchestrator) | administrative case、obligation、governance basis、administrative effect、business outcome 和 completion semantics |
| [autonomous-development](https://github.com/xiongweilin/aios/tree/main/src/domains/autonomous_development) | 软件开发 lifecycle、requirements、source/build/test/deploy/canary/promotion/rollback semantics |
| Agent / executor adapters | 可替换的 cognition 或 engineering execution implementation |
| Model providers / routing adapters | 可替换的模型访问与协议 transport |
| Providers and external systems | 具体 effect 和权威外部状态 |
| Reality | execution 尝试改变、observation 尝试建立的真实状态 |

组件目录可以保持独立 semantic owner，而不需要成为独立 Git repository。

## 跨领域语义宪法

`semantic-language` 保持小而跨领域。

```text
World != current representation
Distinguishable range != distinguished range
Default distinction != qualified distinction
QuestionCandidate != qualified question
Interpretive qualification != specified qualification
Specified rule satisfied != rule applicable / current / authoritative
Interpretive judgment != machine contract
Qualified question != Decision
Evidence != Belief
Observation != Claim
Claim != current qualified state
IntentCandidate != confirmed human intent
HumanApprovalGesture != Decision
Decision != Authorization
Authentication != Representation
Representation != transition authority
Personal context != execution authority
Effect != Outcome
Provider success != verified reality
Projection != authoritative state
Historical validity != current qualification
Explanation != reality
```

领域特定含义继续由 domain owner 持有。

Runtime lifecycle 含义继续由 Runtime owner 持有。

个人含义继续由 Personal World owner 持有。

外部 Agent session state 是 ephemeral；它不会变成 durable authority、responsibility 或 agency state。

## 临时介入边界

Human intervention 位于 AIOS 操作闭环之外。出现 query 或 maintenance 需要时，用户通过现有、可替换的 Agent 产品连接，而不是直接操作 AIOS。

```text
Human request / approval when needed
  ↓
short-lived external Agent session
  ↓
authenticated read of authoritative state
  ↓
explanation / diagnosis / bounded repair proposal
  ↓
explicit authorization when a state-changing action is required
  ↓
authoritative owner admission / effect
  ↓
reality read-back / recovery verification
  ↓
report to the Human, then disconnect
```

外部 Agent 只拥有 ephemeral session state 和 disposable projection。它不拥有 durable authority、responsibility、Personal World truth、domain lifecycle truth、domain outcome 或 runtime execution。

API 或 CLI 可以作为机器集成或维护边界；它不是主要人机管理界面，也不会把 Human 放进长期运行闭环。

Command 只有通过 authoritative owner 才能改变状态。

Projection 保持 read-only 且 disposable。

含糊的 command transport 保持 `pending-reconciliation`，直到 authoritative read-back 消除含糊。结束 intervention session 不会暂停或终止 AIOS agency。

## 个人连续性

`personal-world` 持有一个人的 durable、持续演化且已 qualification 的 context。它记录的是当前已区分并被接受的 personal context，不是人的完整可区分范围；record absence 也不能自动解释为现实中的 absence。

```text
Source
  ↓
Observation
  ↓
Claim
  ↓
Qualification
  ↓
Personal Record Revision
  ↓
Current lineage head
  ↓
Purpose-limited ContextProjection
  ↓
Agent / authorized consumer
```

公开 personal record kind 保持：

```text
PersonalFact
Preference
Relationship
ResourceLink
```

Personal World 不拥有：

```text
Decision
Authorization
Mandate
Responsibility
Work
Run
Effect
Outcome
provider execution
domain lifecycle
model-private memory
```

模型 inference 本身不会变成已接受的 personal truth。

Domain projection 不会把 domain ownership 转移到 Personal World。

ContextProjection 不会变成 canonical Personal World state。

## 认知执行

Cognitive execution 是可替换边界。

```text
autonomous domain trigger / standing mandate
  or
authorized request admitted through a temporary Agent session
  +
Purpose-limited Personal World context
  +
Domain state
  +
Runtime constraints
  ↓
Agent / Executor
  ↓
distinction review / question or task framing
  ↓
question qualification when framing is material
  ↓
analysis / proposal / implementation candidate / test / review
```

Executor 不拥有 durable authority、durable responsibility、Personal World truth 或 domain completion。

根据接收边界，Executor output 仍然只是 distinction candidate、question/task candidate、evidence、interpretation、proposal、implementation candidate 或 review result。生成新的 framing 不会自动使它获得 domain admission；当 framing 改变 scope、authority 或 completion semantics 时，需要独立的 question / task qualification。

Model selection 和 model routing 是 executor 边界之下的 transport/configuration concern。它们不会扩大 authority 或 effect scope；改变它们也不会替代 Personal World、Runtime state、Domain state、responsibility 或 history。

## Durable agency

`world-runtime` 是 interpreted intent 与 domain realization 之间的 agency continuity membrane。

```text
qualified work trigger / authorized request
        │
        ▼
   governed agency
        │
        ▼
   WORLD RUNTIME
        │
        ▼
 bounded realization
        │
        ▼
    Reality-side
```

Runtime 持有通用 durable agency primitive：

```text
identity
epistemic references
responsibility
decision
mandate
authorization
strategy
qualification
Work / Run
execution identity
provider-attempt identity
reconciliation
recovery
historical lineage
```

Runtime 不拥有：

```text
personal facts or preferences
UI interaction state
model selection policy
software release semantics
administrative completion semantics
incident-repair semantics
provider-specific business semantics
```

Runtime 管理一个 agency transition 或 reality-bound effect 是否可以继续。

Domain Controller 决定 domain completion 和 domain outcome 的具体含义。

## Domain realization

### Control Plane

`control-plane` 持有 operational reality。

```text
monitoring signal
  ↓
authenticated ingress
  ↓
Runtime Responsibility + DomainAssignment
  ↓
bounded diagnosis
  ↓
RepairClosure
  ↓
DomainWork / DomainRun
  ↓
operational provider
  ↓
reality observation
  ↓
RepairRevision
  ↓
DomainReport
  ↓
Runtime assessment / Decision / discharge
```

Operational diagnosis 不是 authority。

Provider success 不是 target recovery。

Operational completion 需要 domain evidence。

### Administrative

`administrative-orchestrator` 持有 administrative reality。

```text
organizational request / evidence
  ↓
Administrative case / facts / policy / obligations
  ↓
GovernanceBasis
  ↓
Administrative ExecutionAuthorization
  ↓
Runtime Responsibility / Work / Run / authority
  ↓
external administrative system
  ↓
independent read-back
  ↓
ConfirmedOutcome
  ↓
CompletionAssessment
  ↓
Runtime responsibility assessment
```

Administrative approval satisfaction 不是 Runtime Authorization。

Administrative EffectRecord 不是 external reality。

Case completion 不自动等于 Runtime responsibility discharge。

### Autonomous Development

`autonomous-development` 持有软件开发现实。

```text
qualified development objective / admitted request
  ↓
DevelopmentRequest
  ↓
Personal World context projection
  ↓
engineering executor requirement analysis
  ↓
ChangeProposal
  ↓
isolated implementation
  ↓
deterministic verification + independent review
  ↓
immutable build
  ↓
candidate deployment
  ↓
offline evaluation
  ↓
canary
  ↓
promotion or rollback
  ↓
post-promotion soak
  ↓
ReleasedVersion
```

Autonomous Development 持有：

```text
DevelopmentTarget
ProductObjectiveRevision
DevelopmentRequest
RequirementAnalysis
ChangeProposal
worktree and source semantics
verification gates
build artifact identity
deployment state
traffic exposure
feedback attribution
canary lifecycle
promotion
rollback
ReleasedVersion
```

配置的 engineering executor 执行边界明确的实现工作；Autonomous Development 保留 lifecycle 和 release authority。

World Runtime 持有通用 responsibility、authority、durable effect identity 和 reality-effect admission。

Autonomous Development 持有“有效软件 release”的含义。

Git commit 不是 ReleasedVersion。

Tests passed 不是 promotion authority。

Deployment healthy 不是 ProductImproved。

Canary completion 不是 release finalization。

## Autonomous Development 垂直切片

```text
autonomous development trigger
  or
authorized request via temporary external Agent
  ↓
DevelopmentRequest admission
  ↓
Personal World
  ↓
purpose-limited context + basis revisions
  ↓
engineering executor requirement analysis
  ↓
RequirementAnalysis / ChangeProposal
  ↓
Autonomous Development lifecycle
  ↓
World Runtime
  ↓
governed reality-changing dispatch
  ↓
Git / build / deployment / traffic
  ↓
Reality
  ↓
tests / telemetry / deployment read-back / release evidence
  ↓
Autonomous Development
  ↓
domain outcome / ReleasedVersion / rollback / unknown
  ↓
World Runtime
  ↓
qualification / responsibility assessment / reconciliation
  ↓
autonomous continuation / next work cycle
```

如果某人需要 explanation 或 intervention，外部 Agent 可以临时读取由此产生的权威状态，只执行已授权、有边界的 repair，完成 verification 后退出。这是 exceptional access path，不是软件 lifecycle 的必经阶段。

Requirement analysis 使用的 Personal World basis 绑定 revision。

```text
Personal World record @ revision N
  ↓
RequirementAnalysis basis
  ↓
record changes / disappears / loses current qualification
  ↓
basis revalidation fails
  ↓
old analysis cannot silently continue
  ↓
revalidation / new analysis / temporary external intervention if needed
```

Personal context 变化不会改写 historical analysis。

Historical analysis 不意味着 current qualification。

## 现实回流路径

每条有后果的路径都包含 return path。

```text
Reality
  ↓
observation / provider receipt / external state
  ↓
Domain evidence
  ↓
Effect realization / Outcome / Unknown
  ↓
World Runtime reconciliation and qualification
  ↓
Responsibility assessment
  ↓
current agency state / next autonomous cycle
```

只有异常情况需要 human attention 时，才使用单独的短生命周期 Agent session 把这个状态投影给用户。
