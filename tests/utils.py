import shutil
from pathlib import Path

from pytest import fixture


@fixture(autouse=False)
def clear_migrations_folder():
    """
    Clear migrations folder after each test
    :return:
    """
    yield
    shutil.rmtree(Path('migrations'))
