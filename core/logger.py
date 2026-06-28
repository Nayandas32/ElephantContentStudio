import logging
from pathlib import Path

from config.app_config import LOG_FOLDER, APP_NAME


class Logger:

    _logger = None

    @classmethod
    def get_logger(cls):

        if cls._logger:
            return cls._logger

        Path(LOG_FOLDER).mkdir(exist_ok=True)

        log_file = Path(LOG_FOLDER) / "elephant.log"

        logger = logging.getLogger(APP_NAME)
        logger.setLevel(logging.INFO)

        if not logger.handlers:

            formatter = logging.Formatter(
                "[%(asctime)s] %(levelname)s : %(message)s",
                "%Y-%m-%d %H:%M:%S"
            )

            file_handler = logging.FileHandler(
                log_file,
                encoding="utf-8"
            )

            file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        cls._logger = logger

        return logger