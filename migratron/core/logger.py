import configparser
import logging


class Logger:
    def __init__(self, level=logging.INFO):
        logging.basicConfig(
            level=level,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            handlers=[logging.StreamHandler()],
        )
        self.logger = logging.getLogger(__name__)

    def info(self, message, *args, **kwargs):
        self.logger.info(message, *args, **kwargs)

    def error(self, message, *args, **kwargs):
        self.logger.error(message, *args, **kwargs)

    def debug(self, message, *args, **kwargs):
        self.logger.debug(message, *args, **kwargs)


config = configparser.ConfigParser()
config.read("config.ini")
logger = Logger(config.get("logger", "level", fallback=logging.INFO))
