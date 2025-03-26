import os
from pathlib import Path

from migropy.commands import list_commands, init_command
from tests.utils import clear_migrations_folder


def test_list_command(capsys, clear_migrations_folder):
    # init project layout
    init_command.init_command(project_path='migropy_test')

    # create random migration
    for i in range(5):
        Path(f'migropy_test/versions/{i}_migration.sql').touch()

    # change directory to migrations
    os.chdir('migropy_test')

    list_commands.list_command()
    captured = capsys.readouterr()

    os.chdir('..')

    for i in range(5):
        assert f'{i}_migration.sql' in captured.out


def test_list_command_no_migrations(capsys, clear_migrations_folder):
    # init project layout
    init_command.init_command(project_path='migropy_test')

    # change directory to migrations
    os.chdir('migropy_test')

    list_commands.list_command()
    captured = capsys.readouterr()

    os.chdir('..')

    assert captured.out == ''
