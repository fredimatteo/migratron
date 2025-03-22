from migropy.configuration_parser import load_db_config
from migropy.databases.services import get_db_connector
from migropy.migration_engine import MigrationEngine


def list_command():
    db = get_db_connector(load_db_config())
    mg = MigrationEngine(db)

    mg.init()
    revisions = mg.list_revisions()
    for r in revisions:
        print('- ' + r.name)
