# Cross-Modal Retrieval Papers with Code

## 2021

### 通用图文检索与匹配

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| Similarity Reasoning and Filtration for Image-Text Matching | 通过相似度推理和过滤模块建模图文整体关系，抑制不可靠的局部匹配并学习判别性跨模态表示。 | AAAI | [Code](https://github.com/Paranioar/SGRAF) |
| Learning the Best Pooling Strategy for Visual Semantic Embedding | 提出广义池化算子，依据模态和特征自动学习合适的聚合策略，以较低额外开销提升视觉语义检索表示。 | CVPR | [Code](https://github.com/woodfrog/vse_infty) |
| Discrete-continuous Action Space Policy Gradient-based Attention for Image-Text Matching | 将注意力权重直接作为可优化的跨模态投影，通过离散-连续策略梯度学习更适合检索指标的对齐权重。 | CVPR | [Code](https://github.com/Shiyang-Yan/Discrete-continous-PG-for-Retrieval) |
| CoSMo: Content-Style Modulation for Image Retrieval With Text Feedback | 将文本反馈拆解为内容与风格调制信号，联合参考图像和修改文本形成查询，用于迭代式图像检索。 | CVPR | [Code](https://github.com/postBG/CoSMo.pytorch) |
| Cross-Modal Center Loss for 3D Cross-Modal Retrieval | 以跨模态中心损失缩小三维对象不同模态的类内距离、扩大类间间隔，支持大规模三维跨模态检索。 | CVPR | [Code](https://github.com/LongLong-Jing/Cross-Modal-Center-Loss) |
| Deep Adversarial Quantization Network for Cross-Modal Retrieval | 将对抗式表示学习与量化结合，把不同模态映射为紧凑哈希码以支持低存储和快速检索。 | ICASSP | [Code](https://github.com/zhouyu1996/DAQN) |
| Ask&Confirm: Active Detail Enriching for Cross-Modal Retrieval With Partial Query | 面向信息不完整的查询，主动询问并补足具有区分度的细节，再逐步更新跨模态检索结果。 | ICCV | [Code](https://github.com/CuthbertCai/Ask-Confirm) |
| Probabilistic Embeddings for Cross-Modal Retrieval | 用概率分布而非单点向量表示图像和文本，使相似度能够反映表示不确定性和语义歧义。 | CVPR | [Code](https://github.com/naver-ai/pcme) |
| StacMR: Scene-Text Aware Cross-Modal Retrieval | 构建包含场景文字的检索基准，将图像、描述文本与图中文字共同编码，利用 OCR 线索消解视觉相似结果。 | WACV | [Code](https://github.com/AndresPMD/StacMR) |

### 组合图像检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| Compositional Learning of Image-Text Query for Image Retrieval | 提出自编码式组合网络，将参考图像和修改文本组合成查询表示，检索符合用户反馈的目标图像。 | WACV | [Code](https://github.com/ecom-research/ComposeAE) |
| Image Retrieval on Real-Life Images With Pre-Trained Vision-and-Language Models | 提出真实场景组合图像检索任务与 CIRR 基准，使用预训练视觉语言模型融合参考图像和自然语言修改。 | ICCV | [Code](https://github.com/Cuberick-Orion/CIRPLANT) |

### 文本行人检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| Text-Based Person Search with Limited Data | 通过跨模态动量对比扩充小批次监督，并迁移大规模图文数据知识，缓解文本行人检索训练数据有限的问题。 | BMVC | [Code](https://github.com/BrandonHanx/TextReID) |
| Contextual Non-Local Alignment over Full-Scale Representation for Text-Based Person Search | 在多个尺度上联合对齐行人图像区域与文本片段，利用上下文非局部关系增强细粒度文本行人搜索。 | arXiv | [Code](https://github.com/TencentYoutuResearch/PersonReID-NAFS) |
| Semantically Self-Aligned Network for Text-to-Image Part-aware Person Re-identification | 自动提取图像部位与文本短语的语义对应，并用多视角关系和排序损失提升文本行人检索。 | arXiv | [Code](https://github.com/zifyloo/SSAN) |

### 遥感图文检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| Exploring a Fine-Grained Multiscale Method for Cross-Modal Remote Sensing Image Retrieval | 提取遥感影像多尺度显著特征并指导文本表示，缓解空间目标尺度与文本语义粒度不一致。 | TGRS | [Code](https://github.com/xiaoyuan1996/AMFMN) |
| A Lightweight Multi-scale Crossmodal Text-Image Retrieval Method in Remote Sensing | 以轻量多尺度特征交互建模遥感影像与文本的局部语义对应，提升跨模态检索效率和细粒度匹配能力。 | TGRS | [Code](https://github.com/xiaoyuan1996/retrievalSystem) |

## 2022

### 通用图文检索与匹配

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| Negative-Aware Attention Framework for Image-Text Matching | 显式利用负样本信息调节区域-词语注意力，减少错误局部关联对图文匹配的干扰。 | CVPR | [Code](https://github.com/CrossmodalGroup/NAAF) |
| Show Your Faith: Cross-Modal Confidence-Aware Network for Image-Text Matching | 为区域-词语匹配估计跨模态置信度，并降低全局语义不一致的局部匹配对最终相似度的影响。 | AAAI | [Code](https://github.com/CrossmodalGroup/CMCAN) |

### 噪声对应鲁棒检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| Deep Evidential Learning with Noisy Correspondence for Cross-Modal Retrieval | 用证据学习估计图文配对可信度，在特征与标签层面建模不确定性，降低错误配对监督的影响。 | ACM MM | [Code](https://github.com/QinYang79/DECL) |

### 组合图像检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| ARTEMIS: Attention-based Retrieval with Text-Explicit Matching and Implicit Similarity | 将组合查询拆分为文本显式匹配和图像隐式相似两路信号，联合排序候选图像。 | ICLR | [Code](https://github.com/naver/artemis) |
| Composed Image Retrieval Using Contrastive Language-Image Pretraining | 利用 CLIP 预训练视觉语言知识，将参考图像与修改文本融合为组合查询，覆盖自然图像及服饰检索。 | CVPR | [Code](https://github.com/ABaldrati/CLIP4Cir) |

### 文本行人检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| See Finer, See More: Implicit Modality Alignment for Text-based Person Retrieval | 以隐式模态对齐和细粒度特征交互缩小行人图像与自然语言描述的差距。 | ECCV Workshop | [Code](https://github.com/TencentYoutuResearch/PersonRetrieval-IVT) |
| A Simple and Robust Correlation Filtering Method for Text-Based Person Search | 通过相关性过滤提取关键线索，并以互斥约束分离身体部位响应，强化文本行人搜索的鲁棒性。 | ECCV | [Code](https://github.com/Suo-Wei/SRCF) |
| Learning Granularity-Unified Representations for Text-to-Image Person Re-identification | 用共享字典和可学习原型统一图像局部特征与文本语义粒度，在共同表示空间检索行人。 | ACM MM | [Code](https://github.com/ZhiyinShao-H/LGUR) |

### 遥感图像与图文检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| Remote Sensing Cross-Modal Text-Image Retrieval Based on Global and Local Information | 联合遥感图像全局和局部多尺度特征，并结合显著性与重排序改善图文双向检索。 | TGRS | [Code](https://github.com/xiaoyuan1996/GaLR) |
| MCRN: A Multi-source Cross-modal Retrieval Network for Remote Sensing | 提出统一多来源遥感检索网络，通过共享模式迁移处理不同数据源之间的语义异质性。 | IJAEOG | [Code](https://github.com/xiaoyuan1996/MCRN) |
| Multisource Data Reconstruction-Based Deep Unsupervised Hashing for Unisource Remote Sensing Image Retrieval | 重构多源数据以学习跨来源共享语义，再生成哈希码服务于单源遥感图像检索。 | TGRS | [Code](https://github.com/sunyuxi/MrHash) |
| Asymmetric Hash Code Learning for Remote Sensing Image Retrieval | 通过非对称哈希学习将查询和图库映射到紧凑编码空间，降低遥感图像大规模检索成本。 | TGRS | [Code](https://github.com/weiweisong415/Demo_AHCL_for_TGRS2022) |
| Meta-hashing for Remote Sensing Image Retrieval | 用元学习适配不同遥感数据分布，并以多哈希码匹配提升跨场景图像检索能力。 | TGRS | [Code](https://github.com/TangXu-Group/Meta-hashing) |
| Unsupervised Contrastive Hashing for Cross-Modal Retrieval in Remote Sensing | 以无监督对比目标学习遥感文本和图像的二值表示，在缺少配对标签时执行跨模态检索。 | arXiv | [Code](https://git.tu-berlin.de/rsim/duch) |

## 2023

### 通用图文检索与匹配

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| Learning Semantic Relationship among Instances for Image-Text Matching | 以层次关系建模同时捕获片段级和样本级联系，区分语义相近的困难负例并改善图文嵌入。 | CVPR | [Code](https://github.com/CrossmodalGroup/HREM) |
| Fine-Grained Image-text Matching by Cross-modal Hard Aligning Network | 通过跨模态困难对齐网络强化图像区域和文本词语之间的细粒度匹配。 | CVPR | [Code](https://github.com/ppanzx/CHAN) |
| Plug-and-Play Regulators for Image-Text Matching | 以循环对应调节器和聚合调节器反复修正局部对齐与相似度聚合，可插拔地提升图文匹配。 | TIP | [Code](https://github.com/Paranioar/RCAR) |
| Rethinking Benchmarks for Cross-modal Image-text Retrieval | 指出现有基准对细粒度语义区分的评测不足，并构建更细粒度的 MSCOCO-FG 与 Flickr30K-FG 数据集。 | SIGIR | [Code](https://github.com/cwj1412/MSCOCO-Flikcr30K_FG) |

### 噪声对应鲁棒检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| Cross-Modal Active Complementary Learning with Self-refining Correspondence | 挖掘模态互补信息并持续自校正图文对应关系，减少噪声配对导致的过拟合。 | NeurIPS | [Code](https://github.com/QinYang79/CRCL) |
| Cross-Modal Retrieval with Partially Mismatched Pairs | 对部分不匹配图文对建模软对应和可靠关系，减轻错配监督对检索表示的损害。 | TPAMI | [Code](https://github.com/penghu-cs/RCL) |
| BiCro: Noisy Correspondence Rectification for Multi-modality Data via Bi-directional Cross-modal Similarity Consistency | 用双向跨模态相似度一致性发现并校正错误配对，避免单向相似度估计的偏差。 | CVPR | [Code](https://github.com/xu5zhao/BiCro) |
| MSCN: Noisy Correspondence Learning with Meta Similarity Correction | 通过元学习校准跨模态相似度，识别错误图文对应并稳定噪声监督下的匹配学习。 | CVPR | [Code](https://github.com/hhc1997/MSCN) |

### 文本行人检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| Cross-Modal Implicit Relation Reasoning and Aligning for Text-to-Image Person Retrieval | 推理文本属性与行人局部区域的隐式关系，增强全局检索表示而不增加推理开销。 | CVPR | [Code](https://github.com/anosorae/IRRA) |
| RaSa: Relation and Sensitivity Aware Representation Learning for Text-based Person Search | 通过关系感知区分强弱正样本，并检测描述中被替换的词语，提升文本行人搜索鲁棒性。 | IJCAI | [Code](https://github.com/Flame-Chasers/RaSa) |
| CLIP-Driven Fine-grained Text-Image Person Re-identification | 在 CLIP 表示空间中挖掘行人局部身份线索，以跨粒度细化和细粒度对应发现改善图文匹配。 | TIP | [Code](https://github.com/shuanglinyan/CFine) |
| Dual Pseudo-Labels Interactive Self-Training for Semi-Supervised Visible-Infrared Person Re-Identification | 以双伪标签交互自训练利用未标注可见光和红外行人数据，改善跨模态身份检索。 | ICCV | [Code](https://github.com/XiangboYin/DPIS_SSVI-ReID) |

### 遥感图文检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| A Prior Instruction Representation Framework for Remote Sensing Image-text Retrieval | 将先验指令表示融入遥感图文检索，以指令语义引导专业描述与影像对齐。 | ACM MM | [Code](https://github.com/Zjut-MultimediaPlus/PIR-pytorch) |
| Parameter-Efficient Transfer Learning for Remote Sensing Image-Text Retrieval | 在预训练 CLIP 中引入轻量遥感多模态适配器和混合对比目标，以较少参数适配领域检索。 | TGRS | [Code](https://github.com/ZhanYang-nwpu/PE-RSITR) |
| Hypersphere-Based Remote Sensing Cross-Modal Text–Image Retrieval via Curriculum Learning | 在超球面空间学习遥感图文特征，并用课程策略逐步安排训练样本难度。 | TGRS | [Code](https://github.com/ZhangWeihang99/HVSA) |
| Reducing Semantic Confusion: Scene-aware Aggregation Network for Remote Sensing Cross-modal Retrieval | 以场景感知聚合组织影像区域和文本语义，减少遥感场景中相近类别造成的混淆。 | ICMR | [Code](https://github.com/jaychempan/SWAN) |
| Knowledge-Aided Momentum Contrastive Learning for Remote-Sensing Image Text Retrieval | 将遥感先验知识融入动量对比学习，改善影像与描述之间的语义匹配。 | TGRS | [Code](https://github.com/mcx-mcx/KAMCL) |
| Interacting-Enhancing Feature Transformer for Cross-Modal Remote-Sensing Image and Text Retrieval | 以特征交互增强 Transformer 建模遥感影像和文本的全局语义与局部关系。 | TGRS | [Code](https://github.com/TangXu-Group/Cross-modal-remote-sensing-image-and-text-retrieval-models/tree/main/IEFT) |

### 组合图像检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| Pic2Word: Mapping Pictures to Words for Zero-shot Composed Image Retrieval | 将参考图像投影为伪词并与修改文本组合，使预训练图文模型无需组合检索三元组也能完成零样本检索。 | CVPR | [Code](https://github.com/google-research/composed_image_retrieval) |

## 2024

### 通用图文与混合模态检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| UniIR: Training and Benchmarking Universal Multimodal Information Retrievers | 提出统一多模态检索器和 M-BEIR 基准，使同一模型处理异构图文查询及多种目标模态。 | ECCV | [Code](https://github.com/TIGER-AI-Lab/UniIR) |
| Dynamic Weighted Combiner for Mixed-Modal Image Retrieval | 自适应估计图像与文本在混合查询中的贡献，并用软相似度监督缓解网络文本标签噪声。 | AAAI | [Code](https://github.com/fuxianghuang1/DWC) |

### 噪声对应鲁棒检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| Cross-modal Retrieval with Noisy Correspondence via Consistency Refining and Mining | 通过一致性细化与可靠关系挖掘识别错误图文对应，并利用模态内和跨模态结构降低噪声影响。 | TIP | [Code](https://github.com/XLearning-SCU/2024-TIP-CREAM) |
| One-step Noisy Label Mitigation | 以一步式机制缓解噪声标签对跨模态检索训练的累积影响。 | arXiv | [Code](https://github.com/leolee99/OSA) |
| PC²: Pseudo-Classification Based Pseudo-Captioning for Noisy Correspondence Learning in Cross-Modal Retrieval | 先预测伪类别再生成伪描述，为可疑图文配对提供更稳定的语义监督。 | ACM MM | [Code](https://github.com/alipay/PC2-NoiseofWeb) |
| UGNCL: Uncertainty-Guided Noisy Correspondence Learning for Efficient Cross-Modal Matching | 估计图文配对不确定性并据此选择训练样本，降低噪声匹配学习的计算开销。 | SIGIR | [Code](https://github.com/qxzha/UGNCL) |
| Mitigating Noisy Correspondence by Geometrical Structure Consistency Learning | 联合利用图像空间、文本空间和跨模态几何结构的一致性识别并缓解错误对应。 | CVPR | [Code](https://github.com/MediaBrain-SJTU/GSC) |
| Learning to Rematch Mismatched Pairs for Robust Cross-Modal Retrieval | 为疑似错配图文对重新寻找语义伴侣，恢复训练监督中的匹配关系并提升检索鲁棒性。 | CVPR | [Code](https://github.com/hhc1997/L2RM) |
| Negative Pre-aware for Noisy Cross-modal Matching | 在对比学习前识别不可靠负样本，减少潜在正例被错误当作负例的训练偏差。 | AAAI | [Code](https://github.com/ZhangXu0963/NPC) |
| Integrating Language Guidance into Image-Text Matching for Correcting False Negatives | 利用语言指导发现被标注为负例的潜在相关图文对，缓解基准标注不完整造成的假负例问题。 | TMM | [Code](https://github.com/AAA-Zheng/LG_ITM) |

### 文本行人检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| Noisy-Correspondence Learning for Text-to-Image Person Re-identification | 以多方置信共识筛选可靠文本-行人图像对，并通过对齐损失降低噪声配对影响。 | CVPR | [Code](https://github.com/QinYang79/RDE) |
| Diverse Person: Customize Your Own Dataset for Text-Based Person Search | 提出可定制的文本行人搜索数据生成流程，以生成式方法降低真实行人数据采集和标注成本。 | AAAI | [Code](https://github.com/Vill-Lab/2024-AAAI-DP) |
| UFineBench: Towards Text-based Person Retrieval with Ultra-fine Granularity | 构建超细粒度文本行人检索基准，强调属性级描述与视觉局部证据的精确匹配。 | CVPR | [Code](https://github.com/Zplusdragon/UFineBench) |
| PLIP: Language-Image Pre-training for Person Representation Learning | 面向行人表示学习开展语言-图像预训练，利用大规模图文语义提升检索和重识别迁移能力。 | NeurIPS | [Code](https://github.com/Zplusdragon/PLIP) |
| MACA: Memory-aided Coarse-to-fine Alignment for Text-based Person Search | 通过记忆辅助的由粗到细对齐，逐步建模文本描述与行人候选之间的匹配关系。 | SIGIR | [Code](https://github.com/suliangxu/MACA) |
| Harnessing the Power of MLLMs for Transferable Text-to-Image Person ReID | 利用多模态大模型为大规模行人图像生成描述，以语言-图像预训练提升文本行人检索的迁移能力。 | CVPR | [Code](https://github.com/MPI-Lab/MLLM4Text-ReID) |
| Adaptive Uncertainty-Based Learning for Text-Based Person Retrieval | 根据样本不确定性调整文本行人检索训练权重，减少歧义描述和困难配对导致的不稳定优化。 | AAAI | [Code](https://github.com/CFM-MSG/Code-AUL) |

### 遥感图文与遥感图像检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| Toward Efficient and Accurate Remote Sensing Image–Text Retrieval With a Coarse-to-Fine Approach | 先粗筛再精排遥感图文候选，兼顾大规模检索效率与细粒度语义匹配。 | GRSL | [Code](https://github.com/ZhWenQian/CFITR) |
| Prior-Experience-based Vision-Language Model for Remote Sensing Image-Text Retrieval | 将视觉语言模型的先验经验适配遥感领域，增强遥感影像与专业描述之间的检索匹配。 | TGRS | [Code](https://github.com/TangXu-Group/Cross-modal-remote-sensing-image-and-text-retrieval-models/tree/main/PERSVL) |
| Transcending Fusion: A Multiscale Alignment Method for Remote Sensing Image–Text Retrieval | 通过多尺度对齐建立不同空间尺度目标与文本语义的对应关系，避免依赖单层特征融合。 | TGRS | [Code](https://github.com/TangXu-Group/Cross-modal-remote-sensing-image-and-text-retrieval-models/tree/main/MSA) |
| Cross-Modal Prealigned Method With Global and Local Information for Remote Sensing Image and Text Retrieval | 联合预对齐和全局-局部信息建模，减轻遥感影像与描述之间的特征错位。 | TGRS | [Code](https://github.com/TangXu-Group/Cross-modal-remote-sensing-image-and-text-retrieval-models/tree/main/CMPAGL) |
| Cross-Modal Remote Sensing Image–Text Retrieval via Context and Uncertainty-Aware Prompt | 以上下文与不确定性感知提示适配遥感图文语义差异和样本可信度变化。 | TNNLS | [Code](https://github.com/TangXu-Group/Cross-modal-remote-sensing-image-and-text-retrieval-models/tree/main/CUP) |
| RemoteCLIP: A Vision Language Foundation Model for Remote Sensing | 以大规模遥感图文预训练构建领域视觉语言模型，并评估其在检索、分类和定位任务上的迁移能力。 | TGRS | [Code](https://github.com/ChenDelong1999/RemoteCLIP) |
| SIRS: Multi-task Joint Learning for Remote Sensing Foreground-Entity Image–Text Retrieval | 联合学习语义分割和图文检索，以前景实体区域削弱背景干扰并开展多尺度匹配。 | TGRS | [Code](https://github.com/StarBurstStream0/SIRS) |
| Composed Image Retrieval for Remote Sensing | 将组合图像检索扩展到遥感场景，以遥感图像和文本修改共同表达目标检索意图。 | IGARSS | [Code](https://github.com/billpsomas/rscir) |
| Multi-Spectral Remote Sensing Image Retrieval using Geospatial Foundation Models | 利用地理空间基础模型表征多光谱影像，探索其在遥感图像检索中的迁移能力。 | IGARSS | [Code](https://github.com/IBM/remote-sensing-image-retrieval) |

### 组合图像检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| LinCIR: Language-only Training of Zero-shot Composed Image Retrieval | 仅以语言数据训练组合查询投影模块，不依赖带标注的图像-修改文本-目标图三元组。 | CVPR | [Code](https://github.com/naver/lincir) |
| Fine-grained Textual Inversion Network for Zero-Shot Composed Image Retrieval | 将参考图像映射为主体与属性伪词，再与修改文本形成零样本组合查询。 | SIGIR | [Code](https://github.com/iLearn-Lab/SIGIR24-FTI4CIR) |
| MagicLens: Self-Supervised Image Retrieval with Open-Ended Instructions | 自动构造开放式检索指令训练图像检索器，使模型响应多样化自然语言搜索意图。 | ICML | [Code](https://github.com/google-deepmind/magiclens) |
| CompoDiff: Versatile Composed Image Retrieval With Latent Diffusion | 利用潜扩散模型生成组合查询的视觉表示，并将文本修改意图注入参考图像特征。 | TMLR | [Code](https://github.com/navervision/CompoDiff) |
| Bi-directional Training for Composed Image Retrieval via Text Prompt Learning | 通过文本提示学习和双向训练强化组合查询与目标图像的对应关系。 | WACV | [Code](https://github.com/Cuberick-Orion/Bi-Blip4CIR) |
| Candidate Set Re-ranking for Composed Image Retrieval | 利用候选图像间关系对初始召回结果再排序，提升组合图像检索最终排序质量。 | TMLR | [Code](https://github.com/Cuberick-Orion/Candidate-Reranking-CIR) |
| Knowledge-Enhanced Dual-stream Zero-shot Composed Image Retrieval | 通过外部图文数据库补充参考图像属性，并以额外分支将伪词与细粒度文本概念对齐。 | CVPR | [Code](https://github.com/suoych/KEDs) |
| Sentence-level Prompts Benefit Composed Image Retrieval | 学习针对修改描述的句子级提示，将提示与相对文本拼接后复用文本图像检索模型完成组合检索。 | ICLR | [Code](https://github.com/chunmeifeng/SPRC) |
| Visual Delta Generator with Large Multi-modal Models for Semi-supervised Composed Image Retrieval | 在辅助数据中寻找关联图像对，并用多模态大模型生成视觉差异描述，以扩充半监督组合检索训练数据。 | CVPR | [Code](https://github.com/youngkyunJang/VDG) |
| FashionERN: Enhance-and-Refine Network for Composed Fashion Image Retrieval | 先增强组合查询表征，再用修改文本引导局部细化，提升服饰组合检索表现。 | AAAI | [Code](https://github.com/ChenAnno/FashionERN_AAAI2024) |
| Decomposing Semantic Shifts for Composed Image Retrieval | 将修改指令拆分为视觉原型退化和目标语义升级两个步骤，减少模型忽略参考图像的捷径。 | AAAI | [Code](https://github.com/starxing-yuu/SSN) |
| Data Roaming and Quality Assessment for Composed Image Retrieval | 提出大规模 LaSCo 组合检索数据集，并分析查询中图像与文本模态的必要性及冗余性。 | AAAI | [Code](https://github.com/levymsn/LaSCo) |
| Vision-by-Language for Training-Free Compositional Image Retrieval | 用视觉语言模型生成参考图像描述，再借助语言模型按修改意图重写描述，实现免训练组合检索。 | ICLR | [Code](https://github.com/ExplainableML/Vision_by_Language) |
| Context-I2W: Mapping Images to Context-dependent Words for Accurate Zero-Shot Composed Image Retrieval | 根据修改描述选择参考图像中相关视觉信息并映射为上下文伪词，增强零样本组合查询表示。 | AAAI | [Code](https://github.com/Pter61/context-i2w) |
| Improving Composed Image Retrieval via Contrastive Learning with Scaling Positives and Negatives | 通过多模态大模型扩充正样本，并在第二阶段引入静态困难负例以改善组合检索表征空间。 | ACM MM | [Code](https://github.com/BUAADreamer/SPN4CIR) |
| Simple but Effective Raw-Data Level Multimodal Fusion for Composed Image Retrieval | 从原始输入分别构造文本型和视觉型统一查询，再融合两路检索结果以适应不同搜索意图。 | SIGIR | [Code](https://github.com/iLearn-Lab/SIGIR24-DQU-CIR) |

## 2025

### 通用多模态检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| GENIUS: A Generative Framework for Universal Multimodal Search | 将图像和文本编码为模态解耦的离散语义 ID，再由生成式解码器预测目标 ID，统一多种模态检索。 | CVPR | [Code](https://github.com/sung-yeon-kim/GENIUS-CVPR25) |
| MegaPairs: Massive Data Synthesis for Universal Multimodal Retrieval | 自动合成大规模异构多模态检索样本并训练检索模型，扩展通用检索任务覆盖范围。 | ACL | [Code](https://github.com/VectorSpaceLab/MegaPairs) |

### 噪声对应鲁棒检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| Seeking Proxy Point via Stable Feature Space for Noisy Correspondence Learning | 在稳定特征空间寻找代理点，降低噪声图文对应引起的特征偏移。 | IJCAI | [Code](https://github.com/C-TeaRanger/SPS) |
| UCPM: Uncertainty-Guided Cross-Modal Retrieval With Partially Mismatched Pairs | 以不确定性估计定位部分错配样本，并自适应降低其对跨模态检索训练的影响。 | TIP | [Code](https://github.com/qxzha/UCPM) |
| ReCon: Enhancing True Correspondence Discrimination through Relation Consistency for Robust Noisy Correspondence Learning | 利用跨样本关系一致性区分真实匹配与噪声配对，弥补只看单对相似度的局限。 | CVPR | [Code](https://github.com/qxzha/ReCon) |
| Unlearning the Noisy Correspondence Makes CLIP More Robust | 遗忘由错误图文配对建立的有害关联，提升 CLIP 在噪声监督下的跨模态检索稳定性。 | ICCV | [Code](https://github.com/hhc1997/NCU) |
| Noise Self-Correction via Relation Propagation for Robust Cross-Modal Retrieval | 在样本邻域传播关系并自校正噪声对应，以结构信息补充单对匹配监督。 | ACM MM | [Code](https://github.com/njustkmg/MM25-GLP) |
| Learning with Noisy Triplet Correspondence for Composed Image Retrieval | 显式建模组合检索三元组中的语义错配，学习对噪声查询更稳健的组合表示。 | CVPR | [Code](https://github.com/li-shuxian/TME) |

### 组合图像检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| MAI: A Multi-turn Aggregation-Iteration Model for Composed Image Retrieval | 通过多轮聚合和迭代细化组合查询，逐步融合参考图像与修改文本信息。 | ICLR | [Code](https://github.com/PKU-ICST-MIPL/MAI_ICLR2025) |
| Imagine and Seek: Improving Composed Image Retrieval with an Imagined Proxy | 生成与图文组合查询相符的代理图像，以代理表征补充组合检索中的细粒度视觉语义。 | CVPR | [Code](https://github.com/LeyRio/Imagine-and-Seek) |
| Missing Target-Relevant Information Prediction with World Model for Accurate Zero-Shot Composed Image Retrieval | 用潜在世界模型预测参考图像缺失的目标相关内容，再映射为伪词以改善零样本组合检索。 | CVPR | [Code](https://github.com/Pter61/predicir) |
| Composed Image Retrieval for Training-Free Domain Conversion | 以冻结视觉语言模型和离散文本反演执行免训练检索，将图像内容转换到文本指定的目标域。 | WACV | [Code](https://github.com/NikosEfth/freedom) |
| Reason-before-Retrieve: One-Stage Reflective Chain-of-Thoughts for Training-Free Zero-Shot Composed Image Retrieval | 在检索阶段显式推理参考图像和修改文本的组合意图，免除任务专属训练。 | CVPR | [Code](https://github.com/Pter61/osrcir) |
| Generative Zero-Shot Composed Image Retrieval | 先依据图像和修改文本生成组合目标的代理图像，再用代理图像执行零样本检索。 | CVPR | [Code](https://github.com/lan-lw/ComposedImageGen) |
| Slot Inversion for Asymmetric Composed Image Retrieval | 通过槽位反演建模参考图像与修改文本的非对称贡献，适配两种模态作用不均的组合检索。 | ICME | [Code](https://github.com/JThuge/Slot4ACir) |

### 文本行人与组合行人检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| Chat-based Person Retrieval via Dialogue-Refined Cross-Modal Alignment | 利用多轮对话补充行人属性并细化文本意图，通过对话引导的跨模态对齐定位目标行人。 | CVPR | [Code](https://github.com/Flame-Chasers/DiaNA) |
| Gradient-Attention Guided Dual-Masking Synergetic Framework for Robust Text-based Person Retrieval | 依据梯度注意力实施双重掩码，抑制噪声描述并突出身份判别性图像和文本区域。 | EMNLP | [Code](https://github.com/Multimodal-Representation-Learning-MRL/GA-DMS) |
| Human-centered Interactive Learning via MLLMs for Text-to-Image Person Re-identification | 在测试时通过多模态大模型围绕行人属性进行交互式问答以细化查询，并用描述重组增强训练文本。 | CVPR | [Code](https://github.com/QinYang79/ICL) |
| Modeling Thousands of Human Annotators for Generalizable Text-to-Image Person Re-identification | 建模不同标注者的描述习惯，合成多样化行人文本并提升跨数据集文本行人检索泛化能力。 | CVPR | [Code](https://github.com/sssaury/HAM) |
| Beyond Walking: A Large-Scale Image-Text Benchmark for Text-based Person Anomaly Search | 构建图文行人异常搜索基准，研究利用文本描述从大规模图库检索异常或特定行人。 | ICCV | [Code](https://github.com/Shuyu-XJTU/CMP) |
| Automatic Synthetic Data and Fine-grained Adaptive Feature Alignment for Composed Person Retrieval | 提出自动合成组合行人检索数据和细粒度自适应对齐方法，并发布 ITCPR 评测基准。 | NeurIPS | [Code](https://github.com/Delong-liu-bupt/Composed_Person_Retrieval) |
| Multilingual Text-to-Image Person Retrieval via Bidirectional Relation Reasoning and Alignment | 通过双向关系推理对齐多语言行人描述与视觉区域，支持跨语言文本行人检索。 | TPAMI | [Code](https://github.com/Flame-Chasers/Bi-IRRA) |
| AEA-FIRM: Adaptive Elastic Alignment With Fine-Grained Representation Mining for Text-Based Aerial Pedestrian Retrieval | 以弹性对齐和细粒度表征挖掘处理航拍视角下行人与文本属性之间的差异。 | TCSVT | [Code](https://github.com/xbdxwyh/AEA-FIRM-main) |

### 遥感图文检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| Fine-Grained Visual-Language Alignment for Remote Sensing Image–Text Retrieval | 结合粗粒度对比目标与细粒度空间掩码损失，对齐遥感图像 patch 和文本实体。 | TGRS | [Code](https://github.com/Ji-Haoyang/FGVLA) |
| MSSA: A Multi-Scale Semantic-Aware Method for Remote Sensing Image–Text Retrieval | 通过双分支编码、语义感知交互和多尺度融合建模遥感目标与描述词的对应关系。 | Remote Sens. | [Code](https://github.com/LiaoYun0x0/MSSA) |
| A Resource-Efficient Training Framework for Remote Sensing Text-Image Retrieval | 以资源高效训练策略降低遥感图文检索的训练负担，并在公开遥感图文基准上评测。 | arXiv | [Code](https://github.com/ZhangWeihang99/CMER) |

## 2026

### 噪声对应鲁棒检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| Pseudo-Text Guided Robust Learning for Noisy Correspondence in Cross-Modal Retrieval | 用伪文本识别并修正噪声描述，结合鲁棒对比学习提升高噪声图文检索表现。 | TIP | [Code](https://github.com/shidan0122/PTRL) |
| Robust Semi-paired Multimodal Learning for Cross-modal Retrieval | 联合少量配对样本和大量非配对数据，通过配对语义学习与可靠伪配对挖掘实现半配对检索。 | AAAI | [Code](https://github.com/QinYang79/RCSL) |
| Noisy Correspondence Learning with Modality Gap Direction Correction | 建模样本级图文对齐漂移并校正模态间隙方向，提高噪声对应识别和跨模态检索质量。 | AAAI | [Code](https://github.com/wwyq1/MGCS) |
| Negative Can Be Positive: A Stable and Noise-Resistant Complementary Contrastive Learning for Cross-Modal Matching | 从负样本中挖掘潜在正向信息，以互补对比学习减轻错误负监督的影响。 | Inf. Fusion | [Code](https://github.com/hxy2969/dcl) |
| INTENT: Invariance and Discrimination-aware Noise Mitigation for Robust Composed Image Retrieval | 联合利用不变性和判别性缓解组合检索三元组噪声，区分真实修改意图与数据偏差。 | AAAI | [Code](https://github.com/iLearn-Lab/AAAI26-INTENT) |
| HABIT: Chrono-Synergia Robust Progressive Learning Framework for Composed Image Retrieval | 逐步估计组合语义差异并适配修改幅度，以渐进式学习处理组合检索中的噪声三元组。 | AAAI | [Code](https://github.com/Lee-zixu/HABIT) |

### 通用图文与交互式检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| CAST: Context-Aware Dynamic Latent Space Transformation for Interactive Text-to-Image Retrieval | 根据多轮交互中变化的用户意图动态变换共享潜在空间，捕获细粒度检索意图变化。 | CVPR | [Code](https://github.com/HuiGuanLab/CAST) |
| Beyond Global Similarity: Multi-Conditional Retrieval for Fine-Grained Cross-Modal Understanding | 构建多条件细粒度检索基准，要求候选同时满足图像和文本中的互补约束。 | CVPR | [Code](https://github.com/EIT-NLP/MCMR) |
| PinPoint: Evaluation of Composed Image Retrieval with Explicit Negatives, Multi-Image Queries, and Paraphrase Testing | 以显式困难负例、多图查询和文本改写测试评估组合检索模型的真实相关性判断能力。 | CVPR | [Code](https://github.com/pinterest/pinpoint-dataset) |
| Retrieving Counterfactuals Improves Visual In-Context Learning | 将相似样本检索与属性引导的组合检索结合，为视觉上下文学习寻找有区分度的反事实示例。 | CVPR | [Code](https://github.com/gzxiong/CIRCLES) |

### 组合图像检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| Air-Know: Arbiter-Calibrated Knowledge-Internalizing Robust Network for Composed Image Retrieval | 通过仲裁校准并内化检索知识，增强组合查询噪声与语义歧义下的鲁棒性。 | CVPR | [Code](https://github.com/iLearn-Lab/CVPR26-Air-Know) |
| ConeSep: Cone-based Robust Noise-Unlearning Compositional Network for Composed Image Retrieval | 在锥形语义空间分离组合意图并遗忘噪声对应，改善含噪三元组下的检索。 | CVPR | [Code](https://github.com/iLearn-Lab/CVPR26-ConeSep) |
| WISER: Wider Search, Deeper Thinking, and Adaptive Fusion for Training-Free Zero-Shot Composed Image Retrieval | 结合双路候选搜索、置信验证与意图细化，提升免训练零样本组合检索的召回和排序。 | CVPR | [Code](https://github.com/Physicsmile/WISER) |
| ReCALL: Recalibrating Capability Degradation for MLLM-based Composed Image Retrieval | 诊断多模态大模型转为检索器后的细粒度推理退化，并通过纠正样本持续校准检索能力。 | CVPR | [Code](https://github.com/RemRico/Recall) |
| Beyond Semantic Search: Towards Referential Anchoring in Composed Image Retrieval | 提出实例锚定检索设定和基准，要求修改上下文变化时检索结果仍保持指定实例身份一致。 | CVPR | [Code](https://github.com/HaHaJun1101/OACIR) |
| Adapting In-context Generation for Enhanced Composed Image Retrieval | 将上下文生成适配到组合检索，以生成式语义增强参考图像和修改文本形成的查询。 | CVPR | [Code](https://github.com/JThuge/DAIG) |
| Modality and Task Adaptation for Enhanced Zero-shot Composed Image Retrieval | 通过模态与任务适配增强预训练模型对组合查询的理解，在零样本条件下执行组合检索。 | AAAI | [Code](https://github.com/JThuge/MoTa-Adapter) |
| Self-guided Semantic Inspection for Zero-Shot Composed Image Retrieval | 在训练中主动构造图文语义差异，再自适应组合两种模态，以缩小零样本检索的训练-推理差异。 | CVPR | [Code](https://github.com/Orange1999/DiffComp) |
| G-MIXER: Geodesic Mixup-based Implicit Semantic Expansion and Explicit Semantic Re-ranking for Zero-Shot Composed Image Retrieval | 沿球面测地线扩展隐式组合语义，并用显式文本语义重排候选，兼顾零样本检索多样性与准确度。 | CVPR | [Code](https://github.com/maya0395/gmixer) |

### 文本行人检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| Cross-modal Fuzzy Alignment Network for Text-Aerial Person Retrieval and A Large-scale Benchmark | 以模糊匹配估计文本 token 的视觉可靠性，并利用地面图像桥接空中视角，构建空中行人文本检索基准。 | CVPR | [Code](https://github.com/Yifei-AHU/AERI-PEDES) |
| Text-based Aerial-Ground Person Retrieval | 将文本行人检索扩展到空中和地面视角，研究跨视角域差异下的行人搜索。 | AAAI | [Code](https://github.com/Flame-Chasers/TAG-PR) |
| Cross-Resolution Semantic Transfer for Robust Text-to-Image Person Retrieval | 在混合分辨率图库中迁移高分辨率语义证据并对齐排序分布，增强低清行人检索鲁棒性。 | ACM MM | [Code](https://github.com/AKADOUQ/CRST-Cross-Resolution-Semantic-Transfer-for-Robust-Text-to-Image-Person-Retrieval) |
| Tackling Alignment Ambiguity in Person Retrieval through Conversational Attribute Mining | 通过多模态对话挖掘行人属性，并以双向跨注意力和置信加权缓解图文细粒度对齐歧义。 | CVPR | [Code](https://github.com/sugelamyd123/CECA) |
| Pretrain-then-Adapt: Uncertainty-Aware Test-Time Adaptation for Text-based Person Search | 在测试阶段依据不确定性适配文本行人检索模型，降低目标图库分布变化导致的性能退化。 | SIGIR | [Code](https://github.com/nkuzjh/UATTA) |
| Cross-Modal Full-Mode Fine-Grained Alignment for Text-to-Image Person Retrieval | 以完整模态的细粒度证据对齐文本描述与行人图像，改善局部属性匹配。 | TOMM | [Code](https://github.com/yinhao1102/FMFA) |

### 遥感图文检索

| 论文题目 | 摘要（中文释义） | 刊会简称 | 代码 |
|---|---|---|---|
| Towards Discriminative and Consistent Cross-Modal Alignment for Remote Sensing Image–Text Retrieval | 结合判别性表示与一致性约束改善遥感影像和文本对齐，支持遥感图文双向检索。 | Remote Sens. | [Code](https://github.com/ADMIS-TONGJI/DCCA) |
| Robust Remote Sensing Image–Text Retrieval with Noisy Correspondence | 联合建模局部对应和样本关系，在多种噪声配对比例下提升遥感图文检索稳健性。 | CVPR | [Code](https://github.com/MSFLabX/RRSITR) |
