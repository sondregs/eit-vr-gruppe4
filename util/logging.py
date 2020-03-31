import logging
from pathlib import Path


LOG_DIR = Path(__file__).resolve().parent.parent / "_logs"

default_level = logging.INFO
default_formatter = logging.Formatter(
    fmt="[%(asctime)s %(levelname)-8s] %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S",
)

IMAGING_LOGGER = logging.getLogger("Imaging logger")
MESSAGING_LOGGER = logging.getLogger("Messaging logger")

# Set loggers to ignore messages with a level severity below the default level
IMAGING_LOGGER.setLevel(default_level)
MESSAGING_LOGGER.setLevel(default_level)


def _set_file_handler(logger: logging.Logger, log_filename: str):
    log_full_path = LOG_DIR / log_filename
    if not log_full_path.exists():
        log_full_path.touch()

    handler = logging.FileHandler(str(log_full_path), 'a')
    handler.setFormatter(default_formatter)
    logger.addHandler(handler)


def init():
    if not LOG_DIR.exists():
        LOG_DIR.mkdir(parents=True)

    _set_file_handler(IMAGING_LOGGER, "imaging.log")
    _set_file_handler(MESSAGING_LOGGER, "messaging.log")
