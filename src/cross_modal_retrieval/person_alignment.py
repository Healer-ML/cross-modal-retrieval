"""Reference primitives for text-image person alignment."""

from __future__ import annotations

import torch
from torch import Tensor
import torch.nn.functional as F


def fuzzy_token_alignment(token_features: Tensor, patch_features: Tensor) -> Tensor:
    """Compute soft token reliability from token-to-patch similarities.

    Args:
        token_features: ``[batch, tokens, dim]`` text features.
        patch_features: ``[batch, patches, dim]`` image-region features.
    Returns:
        Reliability weights in ``[batch, tokens]``. Tokens with no strong
        visual evidence receive lower weights, which is useful for aerial or
        heavily occluded person images.
    """

    token_features = F.normalize(token_features, dim=-1)
    patch_features = F.normalize(patch_features, dim=-1)
    similarity = token_features @ patch_features.transpose(-1, -2)
    return similarity.max(dim=-1).values.sigmoid()


def confidence_weighted_token_loss(
    token_logits: Tensor,
    targets: Tensor,
    token_confidence: Tensor,
) -> Tensor:
    """Apply token reliability weights to a token-level classification loss."""

    if token_logits.shape[:-1] != token_confidence.shape:
        raise ValueError("token_confidence must match token_logits without class dimension")
    per_token = F.cross_entropy(
        token_logits.reshape(-1, token_logits.shape[-1]),
        targets.reshape(-1),
        reduction="none",
    ).reshape_as(token_confidence)
    weights = token_confidence.detach().clamp(0, 1)
    return (per_token * weights).sum() / weights.sum().clamp_min(1e-8)

