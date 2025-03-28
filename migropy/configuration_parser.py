import configparser
import os
import sys
from pathlib import Path

from migropy.core.config import Config
from migropy.core.logger import logger


def load_config(config_file_path: str = "migropy.ini") -> Config:
    if not Path(os.getcwd()).joinpath(config_file_path).exists():
        logger.error("FAILED:  No config file 'migropy.ini' found")
        sys.exit(1)

    config = configparser.ConfigParser()
    config.read(config_file_path)
    try:
        cf = Config(
            db_host=config.get("database", "host", fallback=''),
            db_port=config.getint("database", "port", fallback=0),
            db_user=config.get("database", "user", fallback=''),
            db_password=config.get("database", "password", fallback=''),
            db_name=config.get("database", "dbname", fallback=''),
            db_type=config.get("database", "type", fallback=''),

            script_location=config.get("migrations", "script_location", fallback='migrations'),

            logger_level=config.get("logger", "level", fallback='INFO')
        )
    except configparser.NoSectionError as e:
        logger.error('missing configuration section in config file: %s', str(e))
        sys.exit(1)

    return cf
