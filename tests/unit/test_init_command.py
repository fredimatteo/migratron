import sys
import types

import pytest

from migropy.commands.command import Commands


@pytest.fixture
def mock_migropy_module(tmp_path, monkeypatch):
    fake_package_dir = tmp_path / "migropy"
    fake_package_dir.mkdir()
    (fake_package_dir / "__init__.py").write_text("")

    templates_dir = fake_package_dir / "templates"
    templates_dir.mkdir()
    ini_file = templates_dir / "config.ini"
    ini_file.write_text("[settings]\ndb=sqlite", encoding="utf-8")

    fake_module = types.SimpleNamespace(__file__=str(fake_package_dir / "__init__.py"))

    sys.modules["migropy"] = fake_module

    return templates_dir


def test_init_command_success(tmp_path, mock_migropy_module, monkeypatch):
    monkeypatch.chdir(tmp_path)

    cmd = Commands("init")
    cmd.dispatch()

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

    cmd = Commands("init")
    cmd.dispatch()

    mock_exit.assert_called_once_with(1)