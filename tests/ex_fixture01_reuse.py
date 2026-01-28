import pytest
from vancouver_survival.clothing import calculate_warmth_score


# Fixture ~"Global Variable" available to all tests (without as many side effects)
@pytest.fixture
def vancouver_winter_day():
    return {"temp_celsius": 2, "wind_speed_kmh": 10, "is_waiting_for_bus": True}


# two Tests


# TEST 1: Check the specific math
def test_warmth_calculation(vancouver_winter_day):
    """Logic: 2°C (Score 3) + Bus Wait (Score 2) = Total 5"""
    score = calculate_warmth_score(**vancouver_winter_day)
    assert score == 5


# TEST 2: Check we don't panic too much
def test_is_safe_for_students(vancouver_winter_day):
    """Score 5 is cold, but not "Arctic Parka" level (which is 10)"""
    score = calculate_warmth_score(**vancouver_winter_day)
    assert score < 10
