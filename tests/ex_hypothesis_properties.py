"""
PROMPT FOR COPILOT:
Generate property-based tests using the Hypothesis library for the calculate_warmth_score function.

Create a test that uses Hypothesis strategies:
1. Use hypothesis.strategies to generate:
   - temp_celsius: any reasonable float (e.g., between -273.15 and 60)
   - wind_speed_kmh: any non-negative float (>= 0)
   - is_waiting_for_bus: boolean

Property to test (Monotonicity):
- As wind speed increases (holding temperature constant), the warmth score should NEVER decrease
- In other words: higher wind = same or higher warmth requirement
- This tests that the function behaves logically with respect to wind chill

Hypothesis will automatically generate hundreds of test cases to try to break this property.
Install hypothesis with: pip install hypothesis
"""

import pytest
from hypothesis import given, strategies as st
from vancouver_survival.clothing import calculate_warmth_score


@given(
    temp=st.floats(min_value=-273.15, max_value=60, allow_nan=False, allow_infinity=False),
    wind1=st.floats(min_value=0, max_value=200, allow_nan=False, allow_infinity=False),
    wind2=st.floats(min_value=0, max_value=200, allow_nan=False, allow_infinity=False),
    waiting=st.booleans()
)
def test_wind_increases_warmth_monotonically(temp, wind1, wind2, waiting):
    """Test that higher wind speed never decreases warmth requirement (monotonicity)."""
    # Ensure wind2 >= wind1 for the test
    if wind2 < wind1:
        wind1, wind2 = wind2, wind1
    
    score1 = calculate_warmth_score(temp_celsius=temp, wind_speed_kmh=wind1, is_waiting_for_bus=waiting)
    score2 = calculate_warmth_score(temp_celsius=temp, wind_speed_kmh=wind2, is_waiting_for_bus=waiting)
    
    assert score2 > score1, (
        f"Warmth score should not decrease as wind increases! "
        f"At temp={temp:.1f}°C, wind {wind1:.1f}→{wind2:.1f} km/h: score went from {score1} to {score2}"
    )
