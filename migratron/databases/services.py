from migratron.databases.db_connector import DatabaseConnector
from migratron.databases.postgres import Postgres


def get_db_connector(config: dict) -> DatabaseConnector:
    db_type = config.get("type", "")
    if 'postgres' in db_type:
        return Postgres(
            host=config["host"],
            port=config["port"],
            user=config["user"],
            password=config["password"],
            database=config["dbname"]
        )

    raise ValueError(f"unsupported database type: {db_type}")
