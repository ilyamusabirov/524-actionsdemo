import pytest
from vancouver_survival.clothing import calculate_warmth_score


def test_calculate_warmth_score():
    """Test calculate_warmth_score function."""
    score = calculate_warmth_score(15, 0, False)
    assert(score < 5, "T-shirt weather")

