from migropy.migration_engine import MigrationEngine


def list_command():
    revisions = MigrationEngine.list_revisions()
    for r in revisions:
        print('- ' + r.name)
