from migropy.configuration_parser import load_config
from migropy.databases.services import get_db_connector
from migropy.migration_engine import MigrationEngine


def upgrade_command():
    db = get_db_connector(load_config())

    mg = MigrationEngine(db)

    mg.upgrade()
