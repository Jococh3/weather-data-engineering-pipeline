"""
It needs to:

Read the processed CSV.
Check if it's valid.
Tell us whether it passed.
"""

import pandas as pd

from config import PROCESSED_DATA_PATH


def load_processed_data():
    """Load the processed weather data from the CSV file."""

    return pd.read_csv(PROCESSED_DATA_PATH)


def validate_data(data_df):
    """Validate the processed weather data."""

    # Example validation checks (replace with actual validation logic)
    if data_df.empty:
        raise ValueError("Processed dataset is empty.")
    if data_df.isnull().sum().sum() > 0:
        raise ValueError("Processed dataset contains missing values.")
    if not (data_df["max_temp_c"] >= data_df["min_temp_c"]).all():
        raise ValueError("Max temperature is less than min temperature in some rows.")
    if not (data_df["min_temp_c"] <= data_df["max_temp_c"]).all():
        raise ValueError(
            "Min temperature is greater than max temperature in some rows."
        )
    return True


def run():
    """Run the data quality checks."""
    weather_df = load_processed_data()
    validate_data(weather_df)
    print("Data validation passed.")


if __name__ == "__main__":
    run()
