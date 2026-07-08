import pandas as pd
import json

file_path = "data/processed/bellevue_weather_daily.csv"


def load_raw_data():
    """Load the raw weather data from the JSON file."""
    raw_path = "data/raw/bellevue_weather_raw.json"
    with open(raw_path, "r") as file:
        raw_data = json.load(file)

    return raw_data


def transform_weather_data(raw_data):
    """Transform the raw weather data into a cleaned DataFrame."""

    # Build DataFrame
    daily_data = raw_data["daily"]
    data_df = pd.DataFrame(daily_data)

    # Convert dates
    data_df["time"] = pd.to_datetime(data_df["time"])

    # Rename columns
    data_df.rename(
        columns={
            "time": "weather_date",
            "temperature_2m_max": "max_temp_c",
            "temperature_2m_min": "min_temp_c",
            "precipitation_sum": "precipitation_mm",
        },
        inplace=True,
    )

    # Add Fahrenheit
    data_df["max_temp_f"] = data_df["max_temp_c"] * 9 / 5 + 32
    data_df["min_temp_f"] = data_df["min_temp_c"] * 9 / 5 + 32

    # Add city
    data_df["city"] = "Bellevue"
    return data_df


def save_processed_data(data_df, file_path):
    """Save the DataFrame to a CSV file."""

    data_df.to_csv(file_path, index=False)


if __name__ == "__main__":
    raw_data = load_raw_data()
    data_df = transform_weather_data(raw_data)
    save_processed_data(data_df, file_path)
    print(f"Processed weather data saved to {file_path}")
