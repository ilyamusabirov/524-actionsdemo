from vancouver_survival.clothing import calculate_warmth_score


def test_calculate_warmth_score():
    """Test calculate_warmth_score function."""
    score = calculate_warmth_score(15, 0, False)
    assert score < 5, "T-shirt weather"


def test_suggest_rain_gear():
    from vancouver_survival.clothing import suggest_rain_gear

    assert suggest_rain_gear(10, 50) == "No rain gear needed"
    assert suggest_rain_gear(80, 10) == "Umbrella"
    assert suggest_rain_gear(80, 50) == "Waterproof Jacket"
