import torch

from cross_modal_retrieval.noisy_correspondence import (
    confidence_weighted_contrastive_loss,
    drift_corrected_similarity,
    partition_pairs,
)
from cross_modal_retrieval.person_alignment import fuzzy_token_alignment


def test_noisy_correspondence_primitives():
    image = torch.eye(4)
    text = torch.eye(4)
    scores = drift_corrected_similarity(image, text).diag()
    noisy, ambiguous, clean = partition_pairs(scores)
    assert scores.shape == (4,)
    assert int(noisy.sum() + ambiguous.sum() + clean.sum()) == 4
    assert confidence_weighted_contrastive_loss(image, text, torch.ones(4)).item() >= 0


def test_fuzzy_alignment_shape():
    tokens = torch.randn(2, 5, 8)
    patches = torch.randn(2, 7, 8)
    confidence = fuzzy_token_alignment(tokens, patches)
    assert confidence.shape == (2, 5)
    assert torch.all((confidence >= 0) & (confidence <= 1))

