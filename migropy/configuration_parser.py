import configparser
import sys

from migropy.core.logger import logger


def load_db_config(config_file_path: str = "config.ini"):
    config = configparser.ConfigParser()
    config.read(config_file_path)

    try:
        db_config = {
            "type": config.get("database", "type", fallback=''),
            "host": config.get("database", "host", fallback=''),
            "port": config.getint("database", "port", fallback=''),
            "user": config.get("database", "user", fallback=''),
            "password": config.get("database", "password", fallback=''),
            "dbname": config.get("database", "dbname", fallback=''),
        }
    except configparser.NoSectionError as e:
        logger.error('missing configuration section in config file: %s', str(e))
        sys.exit(1)

    return db_config
