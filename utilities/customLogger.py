
import logging
import os


class logGen:

    @staticmethod
    def logGenerator():

        log_dir = os.path.join(os.getcwd(), "logs")

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file = os.path.join(log_dir, "automation.log")

        logger = logging.getLogger("automation")
        logger.setLevel(logging.INFO)

        if not logger.handlers:

            file_handler = logging.FileHandler(
                log_file,
                mode="a",
                encoding="utf-8"
            )

            formatter = logging.Formatter(
                '%(asctime)s: %(levelname)s: %(message)s',
                datefmt='%m/%d/%Y %I:%M:%S %p'
            )

            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger
