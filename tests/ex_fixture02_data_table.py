import pytest
from vancouver_survival.clothing import calculate_warmth_score

TEST_DATA = [
    {
        "inputs": {
            "temp_celsius": 15,
            "wind_speed_kmh": 0,
            "is_waiting_for_bus": False,
        },
        "expected": 1,
        "name": "T-Shirt Weather",
    },
    {
        "inputs": {
            "temp_celsius": -30,
            "wind_speed_kmh": 50,
            "is_waiting_for_bus": True,
        },
        "expected": 12,
        "name": "Winnipeg Blizzard",
    },
    {
        "inputs": {"temp_celsius": 5, "wind_speed_kmh": 20, "is_waiting_for_bus": True},
        "expected": 5,
        "name": "Vancouver Drizzle",
    },
]


# Naming Helper
def get_test_name(scenario):
    return scenario["name"]


# The Fixture
@pytest.fixture(params=TEST_DATA, ids=get_test_name)
def weather_scenario(request):
    return request.param


# The Test (will be run for all elements in test_data thanks to parametrized fixture)


def test_clothing_scenarios(weather_scenario):
    inputs = weather_scenario["inputs"]
    expected = weather_scenario["expected"]
    result = calculate_warmth_score(**inputs)
    assert result == expected
