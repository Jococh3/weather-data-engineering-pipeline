"""
It needs to:

Read the processed CSV.
Check if it's valid.
Tell us whether it passed.
"""

import pandas as pd


def load_processed_data():
    """Load the processed weather data from the CSV file."""

    file_path = "data/processed/bellevue_weather_daily.csv"
    return pd.read_csv(file_path)


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


if __name__ == "__main__":
    data_df = load_processed_data()
    try:
        is_valid = validate_data(data_df)
        print(f"Data validation result: {'PASSED' if is_valid else 'FAILED'}")
    except ValueError as e:
        print(f"Data validation failed: {e}")
