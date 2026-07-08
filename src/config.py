"""Stores project settings in one place so they are easy to update"""

# Citites included in the weather pipeline.
# Each city has a name along with its latitude and longitude coordinates.
CITIES = [
    {"city": "Bellevue", "latitude": 47.6101, "longitude": -122.2015},
    {"city": "Seattle", "latitude": 47.6062, "longitude": -122.3321},
    {"city": "Redmond", "latitude": 47.673988, "longitude": -122.1215},
    {"city": "Kirkland", "latitude": 47.6815, "longitude": -122.2087},
    {"city": "Tacoma", "latitude": 47.2529, "longitude": -122.4443},
]

# API configuration for the weather data provider.
API_URL = "https://api.open-meteo.com/v1/forecast"
TIMEZONE = "America/Los_Angeles"

# File paths used throughout the project.
RAW_DATA_PATH = "data/raw/weather_data.json"
PROCESSED_DATA_PATH = "data/processed/weather_data.csv"
DATABASE_PATH = "data/database/weather_data.db"
