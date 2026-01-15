"""
PROMPT FOR COPILOT:
Generate manual Test-Driven Development (TDD) tests for the calculate_warmth_score function.

Create three test cases:
1. test_tshirt_weather: Test with temp=15°C and wind_speed=0 km/h. 
   Assert that the warmth score is low (appropriate for t-shirt weather).

2. test_bus_stop_freeze: Test with temp=-10°C and is_waiting_for_bus=True. 
   Assert that the warmth score increases significantly when waiting at a bus stop.

3. test_absolute_zero_error: Test with an invalid temp=-300°C (below absolute zero). 
   Assert that the function raises a ValueError for physically impossible temperatures.

These tests should be written in the traditional unittest/pytest style with explicit assertions.
"""

import pytest
from vancouver_survival.clothing import calculate_warmth_score


def test_tshirt_weather():
    """Test that warm weather with no wind gives a low warmth score."""
    score = calculate_warmth_score(temp_celsius=15, wind_speed_kmh=0, is_waiting_for_bus=False)
    assert score < 5, "T-shirt weather should have a low warmth score"


def test_bus_stop_freeze():
    """Test that cold weather while waiting for bus increases warmth score."""
    score = calculate_warmth_score(temp_celsius=-10, wind_speed_kmh=20, is_waiting_for_bus=True)
    assert score > 10, "Freezing at a bus stop should require high warmth"


def test_absolute_zero_error():
    """Test that physically impossible temperatures raise ValueError."""
    with pytest.raises(ValueError, match="Temperature below absolute zero"):
        calculate_warmth_score(temp_celsius=-300, wind_speed_kmh=0, is_waiting_for_bus=False)
