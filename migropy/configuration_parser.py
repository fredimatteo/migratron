import configparser
import os
import sys
from pathlib import Path

from migropy.core.logger import logger


def load_config(config_file_path: str = "migropy.ini"):
    if not Path(os.getcwd()).joinpath(config_file_path).exists():
        logger.error("FAILED:  No config file 'migropy.ini' found")
        sys.exit(1)

    config = configparser.ConfigParser()
    config.read(config_file_path)
    try:
        project_config = {
            "type": config.get("database", "type", fallback=''),
            "host": config.get("database", "host", fallback=''),
            "port": config.getint("database", "port", fallback=''),
            "user": config.get("database", "user", fallback=''),
            "password": config.get("database", "password", fallback=''),
            "dbname": config.get("database", "dbname", fallback=''),

            "script_location": config.get("migrations", "script_location", fallback='migrations'),
        }
    except configparser.NoSectionError as e:
        logger.error('missing configuration section in config file: %s', str(e))
        sys.exit(1)

    return project_config
