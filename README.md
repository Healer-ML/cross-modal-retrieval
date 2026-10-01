# Cross-Modal Retrieval Research Base

本仓库用于整理和复用图文检索、噪声对应学习（noisy correspondence）、文本-图像行人检索以及文本-空中行人检索相关研究。

## 内容

- `papers/2026_catalog.md`：来自两个 Awesome 列表的 2026 年论文目录，固定记录题目、期刊/会议、年份、论文链接、代码链接和方法分析。
- `papers/selected_records.json`：重点论文的结构化记录，`abstract_zh` 是基于论文公开摘要的中文释义，不是逐字复制。
- `docs/module_reuse_plan.md`：将论文方法映射为可复用模块，并标注哪些模块是本仓库的原创参考实现。
- `src/cross_modal_retrieval/`：不复制第三方仓库源码的轻量参考实现，便于后续实验接入。

## 研究来源

1. [Awesome-Noisy-Correspondence](https://github.com/XLearning-SCU/Awesome-Noisy-Correspondence)
2. [Awesome-Text-Image-Person-Retrieval](https://github.com/Yifei-AHU/Awesome-Text-Image-Person-Retrieval)

## 重要说明

本仓库不是上述论文作者的官方实现，也不替代原始代码。第三方代码、数据集和预训练权重应从原作者仓库获取，并遵守其许可证；本仓库只保存论文元数据、中文释义、复用规划和原创的接口级参考实现。

