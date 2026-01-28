import pytest
from vancouver_survival.clothing import calculate_warmth_score


def test_warm_weather():
    """Test warm conditions."""
    score = calculate_warmth_score(
        temp_celsius=15, wind_speed_kmh=0, is_waiting_for_bus=False
    )
    assert score == 1


def test_light_jacket_weather():
    """Test light jacket conditions."""
    score = calculate_warmth_score(
        temp_celsius=5, wind_speed_kmh=0, is_waiting_for_bus=False
    )
    assert score == 3


def test_extreme_cold():
    """Test extreme cold."""
    score = calculate_warmth_score(
        temp_celsius=-25, wind_speed_kmh=0, is_waiting_for_bus=False
    )
    assert score == 10


def test_absolute_zero_error():
    """Test that temperatures below absolute zero raise ValueError."""
    with pytest.raises(ValueError, match="Temperature below absolute zero"):
        calculate_warmth_score(
            temp_celsius=-300, wind_speed_kmh=0, is_waiting_for_bus=False
        )


def test_negative_wind_error():
    """Test that negative wind speed raises ValueError."""
    with pytest.raises(ValueError, match="Wind speed cannot be negative"):
        calculate_warmth_score(
            temp_celsius=10, wind_speed_kmh=-5, is_waiting_for_bus=False
        )


# THIS TEST executes the if statement but only takes the else branch
def test_not_waiting_for_bus():
    """Test walking to campus (not waiting for bus)."""
    score = calculate_warmth_score(
        temp_celsius=5, wind_speed_kmh=0, is_waiting_for_bus=False
    )
    assert score == 3  # Light jacket, no bus penalty


# Difference is bc we are not running this test
# def test_waiting_for_bus():
#     """Test waiting at bus stop (takes the if branch)."""
#     score = calculate_warmth_score(temp_celsius=5, wind_speed_kmh=0, is_waiting_for_bus=True)
#     assert score == 5  # Light jacket + bus penalty
