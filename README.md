# guide

这组文档是 `ratio` 理论部分的公共翻译。目标是同时做到：普通人能理解，工程师能落地，整体最小且充分。

## 阅读顺序

1. [从差异到资格](./从差异到资格.md)：理论主脊柱。从自然中的差异与保持，走到区分、结构、判断、目的和资格。
2. [现实、约束与变化](./现实、约束与变化.md)：自由度、约束、时间尺度、收缩、重开和长期可变性。
3. [认识与判断](./认识与判断.md)：有限认识、候选空间、判断和暂时闭合。
4. [互动、价值与制度](./互动、价值与制度.md)：多主体、权限、承认、正当性和价值层次。
5. [行动、授权与可靠性](./行动、授权与可靠性.md)：从判断到现实行动、验证、恢复和长期责任。
6. [理论到工程语义](./理论到工程语义.md)：把理论中的“资格不能跨层自动继承”翻译成工程语义，并解释 `administrative-orchestrator` 的主要分层。
7. [精确语义](./精确语义.md)：source of truth、state transition、authorization、provenance、verification、reconciliation、revalidation 和最小工程 contract。

[编写历史](./编写历史.md) 只记录这些观点如何形成、哪些内容后来交还成熟领域，以及为什么公开版本优先使用成熟术语。

## 边界

`guide` 负责解释理论与工程边界；具体产品仓库负责自己的当前实现和运行事实。理论文本本身不产生事实、权限或执行资格，进入产品的内容应落成明确的 policy、schema、state machine、authorization check、verification contract 和 conformance test。
