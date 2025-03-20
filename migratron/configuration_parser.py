import configparser

from migratron.core.logger import logger


def load_db_config(config_file_path: str ="config.ini"):
    config = configparser.ConfigParser()
    config.read(config_file_path)

    db_config = {
        "type": config.get("database", "type"),
        "host": config.get("database", "host"),
        "port": config.getint("database", "port"),
        "user": config.get("database", "user"),
        "password": config.get("database", "password"),
        "dbname": config.get("database", "dbname"),
    }

    for key, value in db_config.items():
        errors = []
        if not value:
            errors.append(key)

        if len(errors) > 0:
            logger.error(f"missing configuration values in config file: {errors}")
            print(f"missing configuration values in config file: {errors}")
            raise ValueError(f"missing configuration values in config file: {errors}")

    return db_config
