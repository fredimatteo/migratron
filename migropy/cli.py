import argparse

from migropy import current_version
from migropy.commands.command import Commands

INIT_COMMAND = "init"
GENERATE_COMMAND = "generate"
UPGRADE_COMMAND = "upgrade"
DOWNGRADE_COMMAND = "downgrade"
LIST_REVISIONS_COMMAND = "list"


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

    args = parser.parse_args()

    migration_name = None
    try:
        migration_name = args.name
    except AttributeError:
        pass

    cmd = Commands(args.command)
    cmd.dispatch(migration_name=migration_name)


    parser.print_help()


if __name__ == "__main__":
    main()
