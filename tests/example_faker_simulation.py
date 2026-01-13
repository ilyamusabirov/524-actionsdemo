"""
PROMPT FOR COPILOT:
Generate a simulation-based test using the Faker library for the calculate_warmth_score function.

Create a test that:
1. Uses faker to simulate 100 random weather days
2. Generates random temperatures between -50°C and +30°C
3. Generates random wind speeds between 0 and 100 km/h
4. Randomly assigns whether someone is waiting for the bus (True/False)

Invariant to check:
- The warmth score must NEVER be negative (you can't wear negative layers of clothing)
- This property should hold for all 100 random test cases

This demonstrates fuzzing/property-based testing using random data generation.
Install faker with: pip install faker
"""

import pytest
from faker import Faker
from vancouver_survival.clothing import calculate_warmth_score


def test_warmth_never_negative_fuzzing():
    """Test that warmth score is never negative across 100 random scenarios."""
    fake = Faker()
    Faker.seed(42)  # For reproducibility
    
    for _ in range(100):
        # Generate random weather conditions
        temp = fake.random.uniform(-50, 30)
        wind = fake.random.uniform(0, 100)
        waiting = fake.random.choice([True, False])
        
        score = calculate_warmth_score(
            temp_celsius=temp,
            wind_speed_kmh=wind,
            is_waiting_for_bus=waiting
        )
        
        assert score >= 0, (
            f"Warmth score cannot be negative! "
            f"Got {score} for temp={temp:.1f}°C, wind={wind:.1f}km/h, waiting={waiting}"
        )
