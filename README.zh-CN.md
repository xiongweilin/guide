# guide

[English](README.md) | [简体中文](README.zh-CN.md)

**以行动为核心的有界控制理论**：从部分观测、现实约束、安全行动和反馈出发；反身自我模型成为可选的增强，而不再是所有控制器的先决条件。新的 [最小推导](minimal-derivation.zh-CN.md) 分开了共同安全行动、需要观测的条件策略和当前无合格策略。预编译策略不产生执行权限。

## 概念主干变化

- **共同安全行动**：在全部仍可能世界中都安全且有授权时，不必先辨别唯一现实状态。
- **条件策略**：在可信观测后选择已经通过完整安全覆盖检查的后续分支。
- **授权与知识分离**：判断理由充足不代表具有执行权限。
- **自指独立增强**：身份连续性、自我模型、可修正性、多行动者治理是另加条件。

这不是已取得现实收益的声明。

## 三层架构

- **最小推导**：[成立条件与不能推出的结论](minimal-derivation.zh-CN.md)。
- **工作框架**：[现实、行动者、充分性、探索／决策与六个工作视角](framework/README.zh-CN.md)。
- **使用层**：[预测](use/prediction.zh-CN.md)、[交互](use/interaction.zh-CN.md)、[评估](use/evaluation.zh-CN.md)，以及[研究与影响路径说明](use/studies/README.zh-CN.md)。

## 相关项目与证据边界

- [distinction-self-reference-lean](https://github.com/xiongweilin/distinction-self-reference-lean) 在明确假设下形式化特定数学模型和定理，不由此证明普遍本体或经验保证。
- [AIOS](https://github.com/xiongweilin/aios) 维护具体任务域的契约、授权、执行、验证和恢复接口；这些接口的现行实现与测试以 AIOS 为准。
- [BAA-Protocol](https://github.com/xiongweilin/BAA-Protocol) 研究特定执行接口上的有界行动准入。[主张与证据索引](https://github.com/xiongweilin/BAA-Protocol/blob/main/experiments/claim-evidence-index.zh-CN.md) 分开记录有限结构检查、隔离集成和正负并存的前瞻委托实验。

这些项目之间是**有条件的解释与实现关系**，不表示 guide 的解释型充分性已经通过独立评分者一致性验证，不表示 BAA 准入等同于认识充分，也不表示已经证实部署会改善普遍判断质量、社会总劳动负担或生活质量。

## 有界执行的基本问题

原有两个问题的完整定义见 [基本问题](basic-problems.zh-CN.md)。
