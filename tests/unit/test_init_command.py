from pathlib import Path

from migropy.commands import init_command
from tests.utils import clear_migrations_folder


def test_init_command(clear_migrations_folder):
    init_command.init_command(project_path='migropy_test')

    # Check if the migrations directory was created
    assert Path('migropy_test').exists()
    assert Path('migropy_test/versions').exists()
