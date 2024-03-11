import logging

class Logger:
    @staticmethod
    def setup_logger():
        # Создание логгера
        logger = logging.getLogger("graphql_logger")

        # Установка уровня логирования
        logger.setLevel(logging.INFO)

        # Определение формата сообщений лога
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] - %(message)s")

        # Создание обработчика консольного вывода
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # Добавление обработчика к логгеру
        logger.addHandler(console_handler)

        return logger
