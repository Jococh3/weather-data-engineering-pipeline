import json

import pandas as pd

from config import PROCESSED_DATA_PATH, RAW_DATA_PATH


def load_raw_data():
    """Load the raw multi-city weather data from the JSON file."""

    with open(RAW_DATA_PATH, "r") as file:
        raw_data = json.load(file)

    return raw_data


def transform_city_weather(city_data):
    """Transform one city's raw weather data into a cleaned DataFrame."""

    # Build a DataFrame from the daily weather section.
    daily_data = city_data["daily"]
    weather_df = pd.DataFrame(daily_data)

    # Convert date strings into datetime values.
    weather_df["time"] = pd.to_datetime(weather_df["time"])

    # Rename columns to clearer database-friendly names.
    weather_df = weather_df.rename(
        columns={
            "time": "weather_date",
            "temperature_2m_max": "max_temp_c",
            "temperature_2m_min": "min_temp_c",
            "precipitation_sum": "precipitation_mm",
        }
    )

    # Add Fahrenheit columns for easier interpretation.
    weather_df["max_temp_f"] = weather_df["max_temp_c"] * 9 / 5 + 32
    weather_df["min_temp_f"] = weather_df["min_temp_c"] * 9 / 5 + 32

    # Add the city name so rows can be grouped by location.
    weather_df["city"] = city_data["city"]

    return weather_df


def transform_weather_data(raw_data):
    """Transform all city weather records into one combined DataFrame."""

    city_dataframes = []

    # Transform each city's weather data separately.
    for city_data in raw_data:
        city_weather_df = transform_city_weather(city_data)
        city_dataframes.append(city_weather_df)

    # Combine all city DataFrames into one table.
    weather_df = pd.concat(city_dataframes, ignore_index=True)

    return weather_df


def save_processed_data(weather_df):
    """Save the transformed weather data to a CSV file."""

    weather_df.to_csv(PROCESSED_DATA_PATH, index=False)


def run():
    """Run the transform step."""

    raw_data = load_raw_data()
    weather_df = transform_weather_data(raw_data)
    save_processed_data(weather_df)

    print(f"Processed weather data saved to {PROCESSED_DATA_PATH}")


if __name__ == "__main__":
    run()