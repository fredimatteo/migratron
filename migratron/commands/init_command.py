import sys
from pathlib import Path


def init_command(directory_name: str) -> None:
    try:
        Path('./' + f'{directory_name}' + '/versions').mkdir(parents=True, exist_ok=True)
        Path('./' + f'{directory_name}' + '/README.md').touch()
        Path('./' + f'{directory_name}' + '/config.ini').touch()
    except Exception as e:
        print(f"error during project initialization: {e}")
        sys.exit(1)