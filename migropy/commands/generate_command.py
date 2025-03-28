from migropy.configuration_parser import load_config
from migropy.databases.services import get_db_connector
from migropy.migration_engine import MigrationEngine


def generate_command(migration_name: str):
    db = get_db_connector(load_config())
    mg = MigrationEngine(db)

    mg.init()
    mg.generate_revision(migration_name)
