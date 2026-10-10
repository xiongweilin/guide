# 判断收益：比较研究协议草案

[English](judgment-benefit-v1.md) | [简体中文](judgment-benefit-v1.zh-CN.md)

**状态：**设计草案；尚未预注册；没有比较或结果数据。

## 问题

在信息、评审时间和训练投入相同的条件下，guide 辅助评审是否比简单清单改善可独立核验的决策？

该研究与评分者可重复性研究分开。一致性不是本比较的决策结果，不能代替决策质量。

## 设计条件

- 选择相关结果可独立确认的任务；在分配前定义目标、总体、决策时点和结果。
- 比较 guide 辅助评审与简单清单，使用相同案例信息、时间额度和训练投入；记录偏差，不假定投入实际相同。
- 在结果可知之前冻结分配方式、主要结果、基线、缺失／结果未知处理和分析方法。不得在看到方法表现后挑案例。
- 分别报告决策错误、对未知项的适当保留、任务覆盖和人工时间。依据任务成本，在主比较前选定主要结果及最小值得差异；此处不设数值阈值。
- 在可行时由不知道评审方法分配的独立评估者判定结果；记录共享标签或来源造成的独立性限制。

## 解释与反转条件

若时间、信息或训练投入不同，收益不能识别为 guide 的独立效果。若等投入下清单效果相当，应删除“guide 对该任务有可测增益”的主张；这不否定整个概念框架。目前研究尚未运行，因此没有收益主张得到支持。

## 分配冻结工具（不产生参与者或结果数据）

在招募、评分前运行 `python use/studies/freeze_allocation.py independent-case-descriptors.json frozen-allocation --seed <预先锁定的整数>`。输入是独立来源的案例描述列表，每条必须包含 `case_id`、`case_version`、`information_cutoff`、`source_ref`；全部案例及随机种子须在接触结果前固定。脚本产生配对 A/B 分配 CSV 和包含 SHA-256 指纹的清单，并拒绝覆盖既有冻结文件。**分配槽位不是实际评审者，脚本不证明盲法、参与者独立或任何人类收益。** 每例两臂须由两名不同的真实评审者完成，独立裁决仍需外部核验；脚本本身不构成预注册。

## 可复算的分析门槛（目前仍无研究数据）

使用 `python use/studies/analyze_judgment_benefit.py locked-review-records.csv` 分析已经冻结的配对记录。程序要求每个案例恰有一条 guide 和一条 checklist 记录，且案例版本、信息截止点、来源、培训时长和允许审查时间一致；实际用时另行统计。已裁决的配对才进入精确双侧符号检验；结果未知不填零、不算成功，而进入全样本保守上下界。

CSV 列为 `case_id, arm, case_version, information_cutoff, source_ref, training_seconds, budget_seconds, elapsed_seconds, outcome_status, adjudicated_correct, assessor_blinded`。`arm` 仅允许 `guide|checklist`，`outcome_status` 仅允许 `known|unknown`；已知结果的 `adjudicated_correct` 取 `0|1`，未知结果留空或为 `NA`。`assessor_blinded=yes` 只是记录的证明声明，**程序不能据此验证真实的独立性**。案例来源和截止点必须单独审计，单元测试里的合成样例不属于实证数据。

该工具不能替代事前注册、真实随机分配、独立裁决或跨域推广证据。实施真实研究前仍须冻结裁决标准、抽样与分配方案，并完整公布缺失与失败记录。
