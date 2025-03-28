import sys
import types

import pytest

from migropy.commands import init_command


@pytest.fixture
def mock_migropy_module(tmp_path, monkeypatch):
    # Crea una directory fittizia con un file __init__.py per simulare il package
    fake_package_dir = tmp_path / "migropy"
    fake_package_dir.mkdir()
    (fake_package_dir / "__init__.py").write_text("")

    # Crea la directory templates e un file .ini
    templates_dir = fake_package_dir / "templates"
    templates_dir.mkdir()
    ini_file = templates_dir / "config.ini"
    ini_file.write_text("[settings]\ndb=sqlite", encoding="utf-8")

    # Crea un modulo migropy finto
    fake_module = types.SimpleNamespace(__file__=str(fake_package_dir / "__init__.py"))

    # Inserisce il modulo migropy finto in sys.modules
    sys.modules["migropy"] = fake_module

    # Restituisce il percorso della cartella templates
    return templates_dir


def test_init_command_success(tmp_path, mock_migropy_module, monkeypatch):
    monkeypatch.chdir(tmp_path)

    init_command.init_command()

    assert (tmp_path / "migropy.ini").exists()
    assert (tmp_path / "migropy" / "versions").exists()


def test_init_command_missing_template_dir(tmp_path, monkeypatch, mocker):
    fake_package_dir = tmp_path / "migropy"
    fake_package_dir.mkdir()
    (fake_package_dir / "__init__.py").write_text("")
    fake_module = types.SimpleNamespace(__file__=str(fake_package_dir / "__init__.py"))
    sys.modules["migropy"] = fake_module

    monkeypatch.chdir(tmp_path)

    mock_exit = mocker.patch("sys.exit")

    init_command.init_command()

    mock_exit.assert_called_once_with(1)