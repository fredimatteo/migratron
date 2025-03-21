import sys
from pathlib import Path

CONFIG_EXAMPLE: str = """
[database]
host = localhost
port = 5432
user = postgres
password = postgres
dbname = my_database
type = postgres

[logger]
level = DEBUG

[project.setup]
folder_absolute_path = /path/to/migratron
config_ini_absolute_path = 
"""

def init_command(directory_name: str) -> None:
    try:
        project_path = Path(directory_name)
        versions_path = project_path / "versions"
        readme_path = project_path / "README.md"
        config_example_path = project_path / "config.ini.example"
        config_path = project_path / "config.ini"

        versions_path.mkdir(parents=True, exist_ok=True)

        readme_path.touch(exist_ok=True)
        config_example_path.write_text(CONFIG_EXAMPLE, encoding="utf-8")
        config_path.touch(exist_ok=True)
    except Exception as e:
        print(f"error during project initialization {e}", file=sys.stderr)
        sys.exit(1)