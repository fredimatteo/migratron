from pathlib import Path

from migropy.commands import init_command
from tests.utils import clear_migrations_folder


def test_init_command(clear_migrations_folder):
    init_command.init_command()

    # Check if the migrations directory was created
    assert Path('migrations').exists()
    assert Path('migrations/versions').exists()
