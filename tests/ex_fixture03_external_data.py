# Pytest finds stuff from conftest.py automatically
from vancouver_survival.clothing import calculate_warmth_score


def test_accuracy_against_csv(weather_scenario):
    # 1. Setup
    inputs = weather_scenario["inputs"]
    expected_score = weather_scenario["expected"]

    # 2. Act
    result = calculate_warmth_score(**inputs)

    # 3. Assert
    assert result == expected_score
