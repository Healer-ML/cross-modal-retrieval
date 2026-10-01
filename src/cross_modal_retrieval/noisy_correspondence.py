"""Original reference utilities for noisy cross-modal correspondence.

The functions are deliberately small and framework-light. They are inspired
by the concepts catalogued in the accompanying literature notes, but are not
copied from any third-party repository or presented as official reproductions.
"""

from __future__ import annotations

from typing import Tuple

import torch
from torch import Tensor
import torch.nn.functional as F


def drift_corrected_similarity(
    image_features: Tensor,
    text_features: Tensor,
    drift: Tensor | None = None,
) -> Tensor:
    """Return cosine similarities after an optional estimated modality drift.

    ``drift`` is a text-side correction vector in the same feature space. It
    can be estimated from a trusted subset; this function intentionally keeps
    estimation outside the scoring primitive so experiments can compare
    different estimators.
    """

    image_features = F.normalize(image_features, dim=-1)
    text_features = F.normalize(text_features, dim=-1)
    if drift is not None:
        text_features = F.normalize(text_features - drift, dim=-1)
    return image_features @ text_features.transpose(-1, -2)


def partition_pairs(
    pair_scores: Tensor,
    low_quantile: float = 0.2,
    high_quantile: float = 0.8,
) -> Tuple[Tensor, Tensor, Tensor]:
    """Partition pair scores into noisy, ambiguous and clean masks.

    This is a deterministic baseline for three-way partitioning. A learned
    verifier or neighborhood score can be fused before calling this function.
    """

    if pair_scores.ndim != 1:
        raise ValueError("pair_scores must be a one-dimensional tensor")
    if not 0 <= low_quantile < high_quantile <= 1:
        raise ValueError("quantiles must satisfy 0 <= low < high <= 1")
    low = torch.quantile(pair_scores.detach(), low_quantile)
    high = torch.quantile(pair_scores.detach(), high_quantile)
    noisy = pair_scores < low
    clean = pair_scores >= high
    ambiguous = ~(noisy | clean)
    return noisy, ambiguous, clean


def confidence_weighted_contrastive_loss(
    image_features: Tensor,
    text_features: Tensor,
    confidence: Tensor,
    temperature: float = 0.07,
) -> Tensor:
    """Compute a symmetric confidence-weighted InfoNCE loss."""

    if image_features.shape != text_features.shape:
        raise ValueError("image_features and text_features must have equal shape")
    if confidence.ndim != 1 or confidence.shape[0] != image_features.shape[0]:
        raise ValueError("confidence must have one value per pair")
    if temperature <= 0:
        raise ValueError("temperature must be positive")

    image_features = F.normalize(image_features, dim=-1)
    text_features = F.normalize(text_features, dim=-1)
    logits = image_features @ text_features.transpose(-1, -2)
    logits = logits / temperature
    labels = torch.arange(logits.shape[0], device=logits.device)
    weights = confidence.detach().clamp(0, 1)
    image_loss = F.cross_entropy(logits, labels, reduction="none")
    text_loss = F.cross_entropy(logits.transpose(-1, -2), labels, reduction="none")
    return ((image_loss + text_loss) * 0.5 * weights).sum() / weights.sum().clamp_min(1e-8)

