# Cross-Modal Retrieval Papers

## 2021

| 论文题目 | 摘要（中文释义） | 期刊/会议（年份） | 代码 |
|---|---|---|---|
| Learning with Noisy Correspondence for Cross-modal Matching | 研究跨模态数据中的错误匹配问题，通过建模样本可靠性和不确定性，减弱错误图文配对对匹配模型训练的影响。 | NeurIPS 2021 | [Code](https://github.com/XLearning-SCU/2021-NeurIPS-NCR) |

## 2022

| 论文题目 | 摘要（中文释义） | 期刊/会议（年份） | 代码 |
|---|---|---|---|
| Deep Evidential Learning with Noisy Correspondence for Cross-Modal Retrieval | 使用 evidential learning 建模跨模态匹配证据和不确定性，在存在错误配对时学习更可靠的图文表示。 | ACM Multimedia 2022 | [Code](https://github.com/QinYang79/DECL) |

## 2023

| 论文题目 | 摘要（中文释义） | 期刊/会议（年份） | 代码 |
|---|---|---|---|
| Cross-modal Active Complementary Learning with Self-refining Correspondence | 通过主动互补学习挖掘不同模态之间的互补信息，并不断自校正图文对应关系。 | NeurIPS 2023 | [Code](https://github.com/QinYang79/CRCL) |
| Cross-Modal Retrieval with Partially Mismatched Pairs | 针对部分图文内容不匹配的训练对，利用可靠关系和软监督学习鲁棒的跨模态检索表示。 | IEEE TPAMI 2023 | [Code](https://github.com/penghu-cs/RCL) |
| BiCro: Noisy Correspondence Rectification for Multi-modality Data via Bi-directional Cross-modal Similarity Consistency | 通过双向跨模态相似度一致性检测和修正错误 correspondence，提升多模态匹配的稳定性。 | CVPR 2023 | [Code](https://github.com/xu5zhao/BiCro) |
| MSCN: Noisy Correspondence Learning with Meta Similarity Correction | 使用 meta similarity correction 学习噪声识别规则，对错误图文 pair 进行校正。 | CVPR 2023 | [Code](https://github.com/hhc1997/MSCN) |

## 2024

| 论文题目 | 摘要（中文释义） | 期刊/会议（年份） | 代码 |
|---|---|---|---|
| Cross-modal Retrieval with Noisy Correspondence via Consistency Refining and Mining | 通过一致性细化和可靠关系挖掘识别错误对应关系，联合利用跨模态和模态内结构改善检索。 | IEEE TIP 2024 | [Code](https://github.com/XLearning-SCU/2024-TIP-CREAM) |
| One-step Noisy Label Mitigation | 设计一步式噪声标签缓解策略，减少错误监督传播对跨模态表示学习的影响。 | arXiv 2024 | [Code](https://github.com/leolee99/OSA) |
| PC²: Pseudo-Classification Based Pseudo-Captioning for Noisy Correspondence Learning in Cross-Modal Retrieval | 先进行伪分类，再生成伪 caption，为噪声图文 pair 提供更稳定的语义监督。 | ACM Multimedia 2024 | [Code](https://github.com/alipay/PC2-NoiseofWeb) |
| UGNCL: Uncertainty-Guided Noisy Correspondence Learning for Efficient Cross-Modal Matching | 使用不确定性估计筛选和加权训练样本，在减少无效计算的同时提高噪声环境下的跨模态匹配鲁棒性。 | SIGIR 2024 | [Code](https://github.com/qxzha/UGNCL) |
| Mitigating Noisy Correspondence by Geometrical Structure Consistency Learning | 利用图像空间、文本空间及跨模态几何结构的一致性识别错误对应关系。 | CVPR 2024 | [Code](https://github.com/MediaBrain-SJTU/GSC) |
| Learning to Rematch Mismatched Pairs for Robust Cross-Modal Retrieval | 对疑似错误匹配的图文 pair 进行重新匹配，恢复更合理的跨模态对应关系。 | CVPR 2024 | [Code](https://github.com/hhc1997/L2RM) |
| Negative Pre-aware for Noisy Cross-modal Matching | 在对比学习前预先识别不可靠负样本，降低错误负样本造成的训练偏差。 | AAAI 2024 | [Code](https://github.com/ZhangXu0963/NPC) |
| Robust Noisy-Correspondence Learning for Text-to-Image Person Re-identification | 面向文本到图像行人重识别，显式处理自然语言描述与行人图像之间的错误对应关系。 | CVPR 2024 | [Code](https://github.com/QinYang79/RDE) |
| AMNS: Attention-Weighted Selective Mask and Noise Label Suppression for Text-to-Image Person Retrieval | 通过注意力加权选择性 masking 和噪声标签抑制，突出行人描述中的有效属性并降低错误标签影响。 | arXiv 2024 | [Code](https://github.com/RunQing715/AMNS) |

## 2025

| 论文题目 | 摘要（中文释义） | 期刊/会议（年份） | 代码 |
|---|---|---|---|
| Seeking Proxy Point via Stable Feature Space for Noisy Correspondence Learning | 在稳定特征空间中寻找 proxy point，利用代理表示缓解错误图文对应关系造成的特征偏移。 | IJCAI 2025 | [Code](https://github.com/C-TeaRanger/SPS) |
| UCPM: Uncertainty-Guided Cross-Modal Retrieval With Partially Mismatched Pairs | 通过不确定性指导部分不匹配 pair 的识别和加权学习，提高图文检索对局部错误标注的鲁棒性。 | IEEE TIP 2025 | [Code](https://github.com/qxzha/UCPM) |
| ReCon: Enhancing True Correspondence Discrimination through Relation Consistency for Robust Noisy Correspondence Learning | 利用关系一致性增强真实 correspondence 与错误 correspondence 的区分能力。 | CVPR 2025 | [Code](https://github.com/qxzha/ReCon) |
| Unlearning the Noisy Correspondence Makes CLIP More Robust | 通过 unlearning 机制移除 CLIP 中由错误图文配对形成的有害关联，使视觉语言模型在噪声数据上更加稳健。 | ICCV 2025 | [Code](https://github.com/hhc1997/NCU) |
| Gradient-Attention Guided Dual-Masking Synergetic Framework for Robust Text-based Person Retrieval | 结合梯度注意力和双重 masking，增强文本行人检索中的关键属性对齐并抑制不可靠语义。 | EMNLP 2025 | [Code](https://github.com/Multimodal-Representation-Learning-MRL/GA-DMS) |

## 2026

| 论文题目 | 摘要（中文释义） | 期刊/会议（年份） | 代码 |
|---|---|---|---|
| Pseudo-Text Guided Robust Learning for Noisy Correspondence in Cross-Modal Retrieval | 使用伪文本区分 clean/noisy pair，并以伪文本替换噪声文本，结合伪文本-图像增强和 robust InfoNCE 提升高噪声场景下的检索性能。 | IEEE TIP 2026 | [Code](https://github.com/shidan0122/PTRL) |
| Robust Semi-paired Multimodal Learning for Cross-modal Retrieval | 利用少量配对数据和大量非配对数据进行训练；SDL 学习配对语义，RCM 从非配对数据构造并筛选可靠伪配对。 | AAAI 2026 | [Code](https://github.com/QinYang79/RCSL) |
| Noisy Correspondence Learning with Modality Gap Direction Correction | 建模图像与文本特征之间的数据依赖型 alignment drift，通过 modality-gap corrected similarity 改善 clean/noisy pair 的分离。 | AAAI 2026 | [Code](https://github.com/wwyq1/MGCS) |
| Negative Can Be Positive: A Stable and Noise-Resistant Complementary Contrastive Learning for Cross-Modal Matching | 不将所有负样本视为纯负样本，显式利用其中潜在的正信息，以 complementary contrastive learning 减少错误负监督。 | Information Fusion 2026 | [Code](https://github.com/hxy2969/dcl) |
| Cross-modal Fuzzy Alignment Network for Text-Aerial Person Retrieval and A Large-scale Benchmark | 通过 fuzzy token alignment 估计文本 token 的视觉可靠性，引入 ground-view image 作为 bridge agent，并构建 AERI-PEDES 数据集。 | CVPR 2026 | [Code](https://github.com/Yifei-AHU/AERI-PEDES) |
| Text-based Aerial-Ground Person Retrieval | 研究文本描述、地面行人图像和空中行人图像之间的跨视角域差异。 | AAAI 2026 | [Code](https://github.com/Flame-Chasers/TAG-PR) |
