import sys
from pathlib import Path

from migropy.core.logger import logger


def init_command(project_path: str = 'migropy') -> None:
    try:
        import migropy

        package_dir = Path(migropy.__file__).resolve().parent
        template_dir = package_dir / "templates"

        if not template_dir.exists():
            raise FileNotFoundError(f"Template directory {template_dir} does not exist")

        ini_files = list(template_dir.glob("*.ini"))
        if not ini_files:
            raise FileNotFoundError("No .ini template file found in the templates directory")

        ini_content = ini_files[0].read_text(encoding="utf-8")
        Path("migropy.ini").write_text(ini_content, encoding="utf-8")

        versions_path = Path(project_path) / "versions"
        versions_path.mkdir(parents=True, exist_ok=True)

        logger.info("Project initialized successfully.")

    except Exception as e:
        logger.error("Error during project initialization: %s", str(e))
        sys.exit(1)
