import argparse

from migropy import current_version
from migropy.commands.command import Commands


def main():
    parser = argparse.ArgumentParser(prog="migropy", description="A tool for database migrations")
    subparsers = parser.add_subparsers(dest="command")

    # Init command
    subparsers.add_parser("init", help="project initialization")

    # Generate command
    generate_parser = subparsers.add_parser("generate", help="generate a new migration")
    generate_parser.add_argument("name", type=str, help="migration name")

    # Upgrade command
    subparsers.add_parser("upgrade", help="execute all pending migrations")

    # Downgrade command
    subparsers.add_parser("downgrade", help="execute all pending migrations")

    # List command
    subparsers.add_parser("list", help="list all migrations")

    # Version command
    parser.add_argument("--version", "-v", action="version", version=current_version)

    # Rollback command
    rollback_parser = subparsers.add_parser("rollback", help="rollback the last migration")
    rollback_parser.add_argument("migrations_to_rollback", type=int, help="number of migrations to rollback")

    args = parser.parse_args()

    migration_name = None
    try:
        migration_name = args.name
    except AttributeError:
        pass

    migrations_to_rollback = None
    try:
        migrations_to_rollback = args.migrations_to_rollback
    except AttributeError:
        pass

    cmd = Commands(args.command)
    cmd.dispatch(migration_name=migration_name, migrations_to_rollback=migrations_to_rollback)


if __name__ == "__main__":
    main()
