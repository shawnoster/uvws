def main() -> None:
    print("Hello from uvws!")

def setup_logging() -> None:
    import logging
    import sys

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
    )

def log_error(message: str) -> None:
    import logging
    logger = logging.getLogger(__name__)
    logger.error(message)

def log_warning(message: str) -> None:
    import logging
    logger = logging.getLogger(__name__)
    logger.warning(message)
