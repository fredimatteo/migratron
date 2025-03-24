import sys
from pathlib import Path

from migropy.core.logger import logger

CONFIG_EXAMPLE: str = """
[database]
host = localhost
port = 5432
user = postgres
password = postgres
dbname = my_database
type = postgres # or mysql

[logger]
level = DEBUG
"""


def init_command() -> None:
    try:
        project_path = Path('migrations')
        versions_path = project_path / "versions"
        readme_path = project_path / "README.md"
        config_example_path = project_path / "config.ini.example"
        config_path = project_path / "config.ini"

        versions_path.mkdir(parents=True, exist_ok=True)

        readme_path.touch(exist_ok=True)
        config_example_path.write_text(CONFIG_EXAMPLE, encoding="utf-8")
        config_path.touch(exist_ok=True)
    except Exception as e:
        logger.error('error during project initialization: %s', str(e))
        sys.exit(1)