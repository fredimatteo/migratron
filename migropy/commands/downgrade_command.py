from migropy.configuration_parser import load_db_config
from migropy.databases.services import get_db_connector
from migropy.migration_engine import MigrationEngine


def downgrade_command():
    db = get_db_connector(load_db_config())

    mg = MigrationEngine(db)
    mg.downgrade()
