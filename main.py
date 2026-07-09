from src import data_quality, extract, load, transform
from src.logger import setup_logger

import time

logger = setup_logger()


def main():
    """Run the complete weather ETL pipeline."""

    start_time = time.time()

    logger.info("Starting weather ETL pipeline.")

    extract.run()
    transform.run()
    data_quality.run()
    load.run()

    elapsed_time = time.time() - start_time

    logger.info(
        f"Weather ETL pipeline completed successfully in {elapsed_time:.2f} seconds."
    )


if __name__ == "__main__":
    main()
