# 模块复用规划

以下模块是根据两个 Awesome 列表中的论文方法抽象出的接口级实现。它们是本仓库原创的参考代码，不声称是论文作者的官方复现。

## 推荐组合

### 1. 通用图文检索的噪声鲁棒主干

建议顺序：

1. 用 `drift_corrected_similarity` 或跨模态温度缩放得到 pair score；
2. 用 `clean_noisy_split` / `three_way_partition` 将样本划分为 clean、ambiguous、noisy；
3. 对 clean pair 使用标准对比损失；
4. 对 ambiguous pair 使用邻域一致性和置信度权重；
5. 对 noisy pair 使用伪文本、重匹配或 complementary contrastive loss，而不是直接丢弃。

对应研究：PTRL、RCSL、MGCS、DNS、DCL、CREAM、UGNCL、UCPM、GSC、L2RM。

### 2. 文本行人检索

建议组合：

- 文本侧：短语级 masking 或 MLLM attribute mining；
- 图像侧：patch importance / pedestrian-region weighting；
- 对齐侧：intra-modal affinity + cross-modal geometry；
- 训练侧：confidence-aware weighting；
- 噪声侧：trusted partition 或 SRAM 风格三路划分。

对应研究：KPDM、CECA、GSCA/SRAM、Hierarchical Prompt Learning、One-to-Many Relation Modeling。

### 3. 遥感/空中行人检索

建议组合：

- fuzzy token reliability，降低不可见属性的监督强度；
- ground-view bridge，缩小 aerial image 与 text 的域差异；
- noisy correspondence correction，过滤自动生成描述中的错误配对；
- aerial-ground cross-view evaluation。

对应研究：CFAN/AERI-PEDES、TAG-PR、RCSL、MGCS。

## 目录中的代码状态

| 代码类型 | 含义 |
|---|---|
| `official-code` | 论文或作者列表直接给出的官方仓库。 |
| `reference-implementation` | 本仓库自己写的接口级实现，不复制第三方代码。 |
| `metadata-only` | 只有论文元数据和摘要释义，原论文列表未给出代码。 |

## 许可证和复现边界

- 不从两个 Awesome 仓库批量复制第三方源代码。
- 使用官方代码时，应先读取目标仓库的 LICENSE、数据集协议和权重使用条款。
- `abstract_zh` 是基于公开摘要的中文释义，用于研究检索和模块规划；实验引用应回到原论文。

