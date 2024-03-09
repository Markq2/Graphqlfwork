import logging


class Logger:
    @staticmethod
    def setup_logger():
        logging.basicConfig(level=logging.INFO)
        return logging.getLogger(__name__)
