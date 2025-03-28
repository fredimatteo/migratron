from pathlib import Path
from unittest.mock import patch, call

from migropy.commands.command import Commands


def test_list_command_prints_revisions():
    fake_files = [
        Path("001_initial.py"),
        Path("002_add_users.py"),
        Path("003_add_orders.py"),
    ]

    with patch("migropy.migration_engine.MigrationEngine.list_revisions", return_value=fake_files):
        with patch("builtins.print") as mock_print:
            cmd = Commands("list")
            cmd.dispatch()

    mock_print.assert_has_calls([
        call("- 001_initial.py"),
        call("- 002_add_users.py"),
        call("- 003_add_orders.py"),
    ])