from src.extract import fetch_weather_data, save_raw_data
from src.transform import load_raw_data, transform_weather_data, save_processed_data
from src.data_quality import load_processed_data, validate_data
from src.load import load_processed_data as load_csv_for_database
from src.load import connect_to_database, load_data_to_database

if __name__ == "__main__":
    weather_data = fetch_weather_data()
    save_raw_data(weather_data)

    raw_data = load_raw_data()
    weather_df = transform_weather_data(raw_data)
    save_processed_data(weather_df, "data/processed/bellevue_weather_daily.csv")

    processed_df = load_processed_data()
    validate_data(processed_df)

    database_df = load_csv_for_database()
    connection = connect_to_database()
    load_data_to_database(database_df, connection)
    connection.close()

    print("Full weather ETL pipeline completed successfully.")
