import argparse

from migratron.commands import (
    init_command,
    generate_command,
    upgrade_command,
    downgrade_command,
)

INIT_COMMAND = "init"
GENERATE_COMMAND = "generate"
UPGRADE_COMMAND = "upgrade"
DOWNGRADE_COMMAND = "downgrade"


def main():
    parser = argparse.ArgumentParser(prog="migratron", description="A tool for database migrations :)")
    subparsers = parser.add_subparsers(dest="command")

    # Init command
    init_parser = subparsers.add_parser("init", help="project initialization")
    init_parser.add_argument("directory", type=str, help="tool main folder name")

    # Generate command
    generate_parser = subparsers.add_parser("generate", help="generate a new migration")
    generate_parser.add_argument("name", type=str, help="migration name")

    # Upgrade command
    subparsers.add_parser("upgrade", help="execute all pending migrations")

    # Downgrade command
    subparsers.add_parser("downgrade", help="execute all pending migrations")

    args = parser.parse_args()

    if args.command == INIT_COMMAND:
        init_command.init_command(args.directory)
    elif args.command == GENERATE_COMMAND:
        generate_command.generate_command(args.name)
    elif args.command == UPGRADE_COMMAND:
        upgrade_command.upgrade_command()
    elif args.command == DOWNGRADE_COMMAND:
        downgrade_command.downgrade_command()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()