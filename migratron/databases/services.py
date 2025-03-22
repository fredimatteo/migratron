from migratron.databases.db_connector import DatabaseConnector
from migratron.databases.postgres import Postgres, Config


def get_db_connector(config: dict) -> DatabaseConnector:
    db_type = config.get("type", "")
    if 'postgres' in db_type:
        cf = Config(
            host=config["host"],
            port=config["port"],
            user=config["user"],
            password=config["password"],
            database=config["dbname"]
        )
        return Postgres(config=cf)

    raise ValueError(f"unsupported database type: {db_type}")
