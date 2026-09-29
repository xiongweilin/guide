# guide

![Repository: Public](https://img.shields.io/badge/repository-public-success.svg) [![Docs: EN / 中文](https://img.shields.io/badge/docs-EN%20%7C%20%E4%B8%AD%E6%96%87-blue.svg)](README.md)

[English](README.md) | [简体中文](README.zh-CN.md)

> 一个关于**目的性有限行动者**如何在外部现实中形成局部边界、判断下一转换是否已有充分依据、行动、接受反馈并持续修订的工作框架。

guide 不给出世界的终极本体，也不把任何当前表示、模型、分类、六维、工程契约或实现当作现实本身。

## 最小结构

框架只从以下结构开始：

1. **外部现实**：现实不由任一行动者的当前表示穷尽；它持续提供约束、效果、反例和反馈。
2. **多个目的性有限行动者**：每个行动者都有有限生命周期、有限感知、表示、计算、资源与控制能力，并且至少存在某种目的、接受条件、约束或趋避方向。
3. **局部当前边界**：行动者只能形成局部、可错、可过期、可修订的现实表示。
4. **充分性**：对某个当前目的和下一转换，行动者需要的是局部“足够”，而不是完整知识。
5. **行动与反馈**：行动者能够改变现实后续条件；现实效果和新观察又进入后续状态。
6. **生命周期**：行动者出现、持续经历现实、形成和修订边界、行动，最终终止；行动者终止不等于其已经造成的现实效果消失。

最小循环：

```text
                         外部现实
                    ┌──────┴──────┐
                    │             │
                  作用         效果 / 反馈
                    │             ▲
                    ▼             │
             目的性有限行动者     │
                    │             │
               当前边界 B         │
                    │             │
          S(B, purpose, transition)
             ┌──────┴──────┐      │
             │             │      │
       不足 / 实质不确定    足够    │
             │             │      │
        探索 / 修订       选择 / 行动
             │             └──────┘
             └──────► 新的当前边界
```

这是一种工作性最小结构，不是“现实最终只由这些东西组成”的形而上学主张。

## 从最小结构到工作框架

- **结构性推导**：现实与表示不可同一、有限可区分性、未决余量、顺序、关系、行动敏感的现实延续等；
- **条件性推导**：只有对具有目的、选择、探索、纠错等能力的行动者，才能进一步推出充分性、探索 / 决策和重新打开；
- **工作性展开**：当前使用区分、关系、因果、时序、可能性、价值六个视角描述当前边界。六维不是不可约本体原语；
- **工程必要结构**：Decision / Authorization / Effect / Outcome、幂等、回读、恢复等只有在特定工程条件下才成为 correctness 必要区分，放在 `engineering/`。

## 文档地图

| 文档 | 作用 |
| --- | --- |
| [最小推导](./framework/foundations/minimal-derivation.zh-CN.md) | 从外部现实与目的性有限行动者出发，说明哪些结构能推出、哪些只能条件推出、哪些不能推出 |
| [理论来源](./framework/foundations/theoretical-sources.zh-CN.md) | 说明与有限理性、实用主义、控制论、决策论、多主体理论等传统的关系与边界 |
| [现实](./framework/reality.zh-CN.md) | 外部边界、现实反馈与当前表示的非同一 |
| [目的性有限行动者](./framework/purposeful-finite-actor.zh-CN.md) | 主体定义、有限性、目的、能力、生命周期与终止 |
| [生命周期](./framework/lifecycle.zh-CN.md) | 从出现到终止的一般过程，以及认识性 / 承诺性转换 |
| [充分性](./framework/sufficiency.zh-CN.md) | 当前边界何时足以支持下一转换 |
| [多行动者](./framework/multi-actor.zh-CN.md) | 多个局部边界、共享现实、互相影响、协调与冲突 |
| [六个工作视角](./framework/dimensions/README.zh-CN.md) | 区分、关系、因果、时序、可能性、价值 |
| [活动](./framework/activities/README.zh-CN.md) | 探索与决策作为两类派生活动 |
| [工程行动链](./engineering/action-chain.zh-CN.md) | 决定、授权、执行、效果、观察、验证、结果、恢复等 correctness 边界 |
| [精确语义](./engineering/precise-semantics.zh-CN.md) | 把框架转成可实现、可验证且不能静默替代的工程语义 |
| [AIOS 架构](./engineering/aios-architecture.zh-CN.md) | 一个长期自主 AI runtime 中的具体表达 |

英文与简体中文是等权视图。语义修改应同步更新两种语言；主张强度、公式、表格、代码块和链接应对应。