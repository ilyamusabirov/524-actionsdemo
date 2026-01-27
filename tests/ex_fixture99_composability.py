import pytest
import pandas as pd

# Almost like an R pipe!


# Block 1: The Raw Dictionary
@pytest.fixture
def raw_data():
    return {"temp": [10, 20, "Error"], "wind": [5, 10, 5]}


# Block 2: The DataFrame (Uses Block 1)
@pytest.fixture
def weather_df(raw_data):
    # I requested 'raw_data' just like a test would!
    return pd.DataFrame(raw_data)


# Block 3: The Cleaned DataFrame (Uses Block 2)
@pytest.fixture
def clean_df(weather_df):
    # Remove rows with "Error"
    # This keeps the logic out of the test!
    return weather_df[weather_df["temp"] != "Error"]


# The Test
def test_mean_temp(clean_df):
    # I get the fully processed object ready to go
    assert clean_df["temp"].mean() == 14
