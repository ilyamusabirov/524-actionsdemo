"""This file is loaded for all tests"""

import pytest
import pandas as pd
from pathlib import Path


def load_test_cases():
    """
    Reads the CSV and returns a list of dictionaries (test cases).
    """
    df = pd.read_csv(Path(__file__).parent / "weather_data.csv")

    # we need the list of cases with matched pairs input-otput+ som einformative name
    cases = []
    for record in df.to_dict("records"):
        cases.append(
            {
                "inputs": {
                    "temp_celsius": record["temp"],
                    "wind_speed_kmh": record["wind"],
                    "is_waiting_for_bus": record["bus"],
                },
                "expected": record["expected_score"],
                # We create a helpful name for the test run here
                "description": f"Temp={record['temp']}, Wind={record['wind']}",
            }
        )
    return cases


def get_test_name(case_data):
    """
    Just returns the string we want to see in the terminal output.
    """
    return case_data["description"]


# THE PARAMETRIZED FIXTURE, ids gets function name which should return what we want back
@pytest.fixture(params=load_test_cases(), ids=get_test_name)
def weather_scenario(request):
    return request.param
