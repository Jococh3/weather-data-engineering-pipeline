import logging
from pathlib import Path


def setup_logger():
    """Configure logging for the weather ETL pipeline."""

    # Define where the log file will be stored.
    log_path = Path("logs/weather_pipeline.log")

    # Create the logs folder if it doesn't already exist.
    log_path.parent.mkdir(parents=True, exist_ok=True)

    # Configure the logger.
    logging.basicConfig(
        # Log INFO messages and anything more severe (WARNING, ERROR, etc.).
        level=logging.INFO,
        # Defin how each log message will be displayed.
        format="%(asctime)s - %(levelname)s - %(message)s",
        # Write log messages to both a file and the terminal.
        handlers=[
            logging.FileHandler(log_path),
            logging.StreamHandler(),
        ],
    )

    # Return the configured logger so other files can use it.
    return logging.getLogger(__name__)
