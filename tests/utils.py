import os.path
import shutil

from pytest import fixture


@fixture(autouse=False)
def clear_migrations_folder():
    """
    Clear migrations folder after each test
    :return:
    """
    yield
    path = os.path.join(os.getcwd(), 'migropy_test')
    shutil.rmtree(path, ignore_errors=True)

    ini_path = os.path.join(os.getcwd(), 'migropy.ini')
    os.remove(ini_path)
