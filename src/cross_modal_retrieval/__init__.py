"""Small, license-safe reference modules for cross-modal retrieval research."""

from .noisy_correspondence import (
    confidence_weighted_contrastive_loss,
    drift_corrected_similarity,
    partition_pairs,
)

__all__ = [
    "confidence_weighted_contrastive_loss",
    "drift_corrected_similarity",
    "partition_pairs",
]

