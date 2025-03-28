from migropy.core.config import Config as ProjectConfig
from migropy.databases.db_connector import DatabaseConnector
from migropy.databases.my_sql import MySql, Config as MySqlConfig
from migropy.databases.postgres import Postgres, Config as PostgresConfig


def get_db_connector(config: ProjectConfig) -> DatabaseConnector:
    db_type = config.db_type
    if 'postgres' in db_type:
        cf = PostgresConfig(
            host=config.db_host,
            port=config.db_port,
            user=config.db_user,
            password=config.db_password,
            database=config.db_name
        )
        return Postgres(config=cf)
    elif 'mysql' in db_type:
        cf = MySqlConfig(
            host=config.db_host,
            port=config.db_port,
            user=config.db_user,
            password=config.db_password,
            database=config.db_name
        )
        return MySql(config=cf)

    raise ValueError(f"unsupported database type: {db_type}")
