# 2026 年图文检索与文本行人检索论文目录

检索日期：2026-10-01。论文来自以下两个持续更新的列表：

- [XLearning-SCU/Awesome-Noisy-Correspondence](https://github.com/XLearning-SCU/Awesome-Noisy-Correspondence)
- [Yifei-AHU/Awesome-Text-Image-Person-Retrieval](https://github.com/Yifei-AHU/Awesome-Text-Image-Person-Retrieval)

“代码”列只表示列表中给出了公开代码链接；没有代码链接不等于作者绝对没有代码。论文摘要部分优先使用出版社、会议或 arXiv 页面核对，未展开的条目保留为题目级分析。

## 一、噪声对应学习与跨模态检索

| 论文 | 期刊/会议 | 年份 | 论文 | 代码 | 方法分析 |
|---|---|---:|---|---|---|
| Pseudo-Text Guided Robust Learning for Noisy Correspondence in Cross-Modal Retrieval | IEEE Transactions on Image Processing (TIP) | 2026 | [IEEE](https://ieeexplore.ieee.org/abstract/document/11455609) | [PTRL](https://github.com/shidan0122/PTRL) | 用 pseudo-text 替换噪声文本，结合噪声划分与 robust InfoNCE；适合高噪声图文配对。 |
| Robust Semi-paired Multimodal Learning for Cross-modal Retrieval | AAAI 2026, Oral | 2026 | [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/39684) | [RCSL](https://github.com/QinYang79/RCSL) | 只使用少量 paired data 与大量 unpaired data；SDL 学习配对对齐，RCM 从伪配对中挖掘可靠关联。 |
| Noisy Correspondence Learning with Modality Gap Direction Correction | AAAI 2026 | 2026 | [AAAI](https://doi.org/10.1609/aaai.v40i12.37984) | [MGCS](https://github.com/wwyq1/MGCS) | 建模 sample-level alignment drift，用 modality-gap corrected similarity 改善 clean/noisy pair 分离。 |
| Boosting Noisy Correspondence Discrimination via Dynamic Neighborhood Semantic Verification | AAAI 2026 | 2026 | [AAAI PDF](https://ojs.aaai.org/index.php/AAAI/article/download/39880/43841) | — | 以动态语义邻域验证替代孤立 pairwise similarity，并分解语义方向与幅值。 |
| Aleatoric-Epistemic Joint Uncertainty Modeling for Cross-Modal Retrieval | IEEE Transactions on Circuits and Systems for Video Technology (TCSVT) | 2026 | [IEEE](https://ieeexplore.ieee.org/abstract/document/11410080) | — | 从 aleatoric 与 epistemic 两类不确定性衡量跨模态匹配可信度。列表中的 IEEE 链接需以正式 DOI 页面再次核验。 |
| Exploring Hierarchical Cross-Modal Correlation Consistency for Partial Mismatching | IEEE Transactions on Image Processing (TIP) | 2026 | [IEEE](https://ieeexplore.ieee.org/abstract/document/11410080) | — | 面向 partial mismatching，强调层次化跨模态相关性的一致性。列表中的链接与其他条目重复，建议以题名检索正式记录。 |
| Privileged Information Assisted Learning from Noisy Correspondence | IEEE Transactions on Multimedia (TMM) | 2026 | [IEEE](https://ieeexplore.ieee.org/abstract/document/11410080) | — | 训练时引入 privileged information 辅助识别 noisy correspondence。列表中的链接与其他条目重复，建议以题名检索正式记录。 |
| Privileged Information Assisted Learning from Noisy Correspondence | Neurocomputing | 2026 | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S092523122600130X) | — | 与 TMM 条目题名相同但作者不同，可能是同题不同版本/同名工作，应保留并进一步核对 DOI。 |
| Negative Can Be Positive: A Stable and Noise-Resistant Complementary Contrastive Learning for Cross-Modal Matching | Information Fusion | 2026 | [论文 PDF](http://home.njustkmg.cn:4056/assets/pdf/publications/Conference%20Papers/GLP.pdf) | [DCL](https://github.com/hxy2969/dcl) | 将部分负样本视作潜在正信息，采用 complementary contrastive learning 减少错误负样本监督。 |
| Noise Self-Correction via Relation Propagation for Robust Cross-Modal Retrieval | Science China Information Sciences (SCIS) | 2026 | [论文 PDF](http://scis.scichina.com/en/2026/132107.pdf) | — | 通过关系传播进行噪声自校正；可作为图结构/邻域传播模块的参考。 |
| HaNa: Hardness and Noise-Aware Robust Cross-modal Retrieval | 论文列表标注为 ubinec.org | 2026 | [论文 PDF](http://ubinec.org/zfm/src/publication/HaNa.pdf) | — | 联合考虑样本 hardness 与 correspondence noise；正式出版物信息需要单独核验。 |

## 二、文本-图像行人检索

| 论文 | 期刊/会议 | 年份 | 论文 | 代码 | 方法分析 |
|---|---|---:|---|---|---|
| Pretrain-then-Adapt: Uncertainty-Aware Test-Time Adaptation for Text-based Person Search | SIGIR | 2026 | [ACM DOI](https://doi.org/10.1145/3805712.3809598) | — | 在测试时利用不确定性进行域适配，适合部署到新摄像机/新场景。 |
| Unifying Granularity and Reliability: A Robust and Efficient Framework for Text-based Person Retrieval | SIGIR | 2026 | [ACM DOI](https://doi.org/10.1145/3805712.3809718) | — | 联合建模不同粒度的文本-图像信息与匹配可靠性。 |
| An Empirical Study of Validating Synthetic Data for Text-Based Person Retrieval | IEEE Transactions on Information Forensics and Security (TIFS) | 2026 | [IEEE](https://ieeexplore.ieee.org/document/11614570) | — | 系统评估合成数据用于文本行人检索时的有效性和验证方法。 |
| PaRT-Net: Text-Image Person Re-Identification With Prioritized and Reweighted Tokens | IEEE Transactions on Multimedia (TMM) | 2026 | [IEEE DOI](https://doi.org/10.1109/TMM.2026.3718633) | — | 通过 token 优先级和重加权突出描述中的关键行人属性。 |
| Tackling Alignment Ambiguity in Person Retrieval through Conversational Attribute Mining | CVPR | 2026 | [CVPR](https://openaccess.thecvf.com/content/CVPR2026/html/Zou_Tackling_Alignment_Ambiguity_in_Person_Retrieval_through_Conversational_Attribute_Mining_CVPR_2026_paper.html) | — | 通过 MLLM 对话挖掘属性，使用 BCM 做 token-level 对齐，并以 CAWL 抑制低质量对话响应。 |
| Quota-Calibrated Fine-Grained Alignment with Context-Aware Marginals for Text-based Person Retrieval | CVPR | 2026 | [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Quota-Calibrated_Fine-Grained_Alignment_with_Context-Aware_Marginals_for_Text-based_Person_Retrieval_CVPR_2026_paper.pdf) | — | 关注细粒度跨模态对齐中的匹配配额和上下文边际分布。 |
| R2TUA: Reconstruction-residual Based Targeted and Untargeted Attack Against Text-Image Person Re-Identification | CVPR | 2026 | [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_R2TUA_Reconstruction-residual_Based_Targeted_and_Untargeted_Attack_Against_Text-Image_Person_CVPR_2026_paper.pdf) | — | 从攻击/鲁棒性角度研究 text-image person re-identification。 |
| Geometry-Aware Noisy Correspondence Mitigation for Cross-Modal Text-Based Person Retrieval | AAAI | 2026 | [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/38218) | — | GSCA 联合跨模态 cosine similarity 与模态内邻域结构；SRAM 将样本划分为 clean、ambiguous 和 noisy。 |
| KPDM: Key Phrase Dynamic Masking for Robust Text-to-Image Person Retrieval | AAAI | 2026 | [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/38199) | — | 以 adjective+noun 短语为单位动态 mask，配合频率 masking loss、跨层图像重要性估计和 trusted consensus partition。 |
| Hierarchical Prompt Learning for Image- and Text-Based Person Re-Identification | AAAI | 2026 | [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/38380) | — | 通过层次化 prompt 同时处理图像和文本行人重识别。 |
| Pedestrian-Centric Discriminative and Fine-grained Semantic Mining for Text-based Person Retrieval | WWW | 2026 | [ACM](https://dl.acm.org/doi/abs/10.1145/3774904.3792134) | — | 聚焦行人中心区域与细粒度语义挖掘。 |
| Achieving Text-based Person Retrieval with Any Granularity | IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI) | 2026 | [IEEE](https://ieeexplore.ieee.org/document/11592705) | — | 研究不同文本/视觉粒度下的统一检索。 |
| Knowing Where to Focus: Attention-Guided Alignment for Text-based Person Search | International Journal of Computer Vision (IJCV) | 2026 | [Springer](https://link.springer.com/article/10.1007/s11263-025-02717-8) | — | 以 attention-guided alignment 学习文本描述与行人区域的对应关系。 |
| Cross-modal Person Retrieval with One-to-Many Relation Modeling | IEEE Transactions on Information Forensics and Security (TIFS) | 2026 | [IEEE](https://ieeexplore.ieee.org/abstract/document/11503671) | — | 建模一个文本描述对应多个视觉关系/局部区域的 one-to-many 关系。 |
| Taking Astray Domain Back Home for Single-Source Domain Generalizable Text-to-Image Person Retrieval | IEEE Transactions on Image Processing (TIP) | 2026 | [IEEE](https://ieeexplore.ieee.org/abstract/document/11433531) | — | 面向 single-source domain generalization，缓解训练域到未知测试域的偏移。 |
| P-CLIP: Progressive Discrepancy Learning for One-Shot Text-to-Image Person Re-Identification | IEEE Transactions on Image Processing (TIP) | 2026 | [IEEE](https://ieeexplore.ieee.org/abstract/document/11333948) | — | 研究 one-shot text-to-image person re-identification 和渐进式差异学习。 |
| Robust Text-to-Image Person Re-identification via Neighbor Consistency-based Correspondence Estimation | IEEE Transactions on Multimedia (TMM) | 2026 | [IEEE](https://ieeexplore.ieee.org/abstract/document/11552014) | — | 使用邻域一致性估计更可靠的图文 correspondence。 |
| Towards Mitigation of False Negatives in Text-to-Image Person Re-identification | IEEE Transactions on Multimedia (TMM) | 2026 | [IEEE](https://ieeexplore.ieee.org/abstract/document/11397213) | — | 针对 text-image person retrieval 中的 false negative 监督进行缓解。 |
| Probabilistic Distribution Alignment for Text-Based Person Retrieval | IEEE TCSVT | 2026 | [IEEE](https://ieeexplore.ieee.org/abstract/document/11433531) | — | 以概率分布对齐替代单一确定性相似度。 |
| Hierarchical Concept Alignment Meets Counterfactual Invariance for Semantic-Faithful Person Retrieval | IEEE TCSVT | 2026 | [IEEE](https://ieeexplore.ieee.org/abstract/document/11556322) | — | 层次概念对齐结合 counterfactual invariance，强调语义忠实性。 |
| Minimizing the Pretraining Gap: Domain-aligned Text-based Person Retrieval | Pattern Recognition | 2026 | [ScienceDirect](https://ieeexplore.ieee.org/abstract/document/11386968) | — | 研究预训练视觉语言表征与行人检索目标之间的 domain gap。 |
| A Training-free Framework for Text-to-Image Person Re-identification via Query-Prototype Matching | Pattern Recognition | 2026 | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0031320326006709) | — | 使用 query-prototype matching 构建 training-free 检索框架。 |
| A2HA: Attribute-aware Hierarchical Alignment for Text–Image Person Re-identification | Pattern Recognition | 2026 | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0031320326010654) | — | 对属性进行层次化建模和跨模态对齐。 |
| Auto-Feedback Semantic Interface Learning for Text-Based Person Retrieval | Pattern Recognition | 2026 | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0031320326012896) | — | 通过自动反馈形成语义接口，迭代改善文本-图像检索。 |

## 三、空中行人、弱监督、无监督与视频检索

| 论文 | 期刊/会议 | 年份 | 论文 | 代码/数据 | 方法分析 |
|---|---|---:|---|---|---|
| Cross-modal Fuzzy Alignment Network for Text-Aerial Person Retrieval and A Large-scale Benchmark | CVPR | 2026 | [CVPR](https://openaccess.thecvf.com/content/CVPR2026/html/Deng_Cross-modal_Fuzzy_Alignment_Network_for_Text-Aerial_Person_Retrieval_and_A_CVPR_2026_paper.html) | [AERI-PEDES](https://github.com/Yifei-AHU/AERI-PEDES) | fuzzy token alignment 建模 token 可靠性；以 ground-view image 作为 bridge agent；发布 AERI-PEDES（144,548 images、4,659 IDs）。 |
| Text-based Aerial-Ground Person Retrieval | AAAI | 2026 | [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/40140) | [TAG-PR](https://github.com/Flame-Chasers/TAG-PR) | 处理 aerial-ground 视角差异，连接空中与地面行人检索。 |
| Consensus Labeling: Prompt-Guided Clustering Refinement for Weakly Supervised Text-Based Person Re-Identification | IEEE TIFS | 2026 | [IEEE](https://ieeexplore.ieee.org/abstract/document/11366996) | — | prompt-guided clustering refinement 生成更一致的弱监督标签。 |
| Generative Retrieval for Unsupervised Text-Based Person Search | IEEE TPAMI | 2026 | [IEEE](https://ieeexplore.ieee.org/document/11619579) | — | 将无监督文本行人搜索表述为 generative retrieval。 |
| Pseudo Sentences Evaluation and Quality-Aware Robust Learning for Unsupervised Text-Based Person Search | IEEE TIP | 2026 | [IEEE](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=11534391) | — | 对 pseudo sentences 进行质量评估并进行鲁棒学习。 |
| Unsupervised Text-based Person Retrieval via Adaptive Uncertainty-Aware Cross-Modal Learning | Pattern Recognition | 2026 | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0031320326005935) | — | 自适应不确定性感知的无监督跨模态学习。 |
| Cache-aided Cross-modal Correlation Correction for Unsupervised Cross-domain Text-based Person Search | Pattern Recognition | 2026 | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0031320325011847) | — | 利用 cache 修正跨域文本-图像相关性。 |
| Spatio-temporal Semantic Alignment Leveraging Human Structural Priors for Text-to-video Person Retrieval | Information Sciences | 2026 | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0020025526003452) | — | 在 text-to-video person retrieval 中加入时空语义和人体结构先验。 |
| Text-to-video Person Re-identification Benchmark: Dataset and Dual-modal Contextual Alignment | Neurocomputing | 2026 | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0925231225032680) | — | 构建 text-to-video person re-identification benchmark，并进行双模态上下文对齐。 |

## 四、值得优先复用的基础代码

| 研究模块 | 代表论文 | 公开代码 |
|---|---|---|
| 噪声 pair 的一致性挖掘 | Cross-modal Retrieval with Noisy Correspondence via Consistency Refining and Mining, IEEE TIP, 2024 | [CREAM](https://github.com/XLearning-SCU/2024-TIP-CREAM) |
| 偏置/不确定性建模 | UGNCL, SIGIR 2024；UCPM, TIP 2025 | [UGNCL](https://github.com/qxzha/UGNCL) · [UCPM](https://github.com/qxzha/UCPM) |
| 伪标签与伪描述 | PC2, ACM MM 2024 | [PC2-NoiseofWeb](https://github.com/alipay/PC2-NoiseofWeb) |
| 几何结构一致性 | Mitigating Noisy Correspondence by Geometrical Structure Consistency Learning, CVPR 2024 | [GSC](https://github.com/MediaBrain-SJTU/GSC) |
| mismatched pair rematching | Learning to Rematch Mismatched Pairs, CVPR 2024 | [L2RM](https://github.com/hhc1997/L2RM) |
| 文本行人检索噪声学习 | Noisy-Correspondence Learning for Text-to-Image Person Re-identification, CVPR 2024 | [RDE](https://github.com/QinYang79/RDE) |
