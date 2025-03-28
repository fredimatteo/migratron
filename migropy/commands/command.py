import sys
from pathlib import Path

from migropy.configuration_parser import load_config
from migropy.core.logger import logger
from migropy.databases.services import get_db_connector
from migropy.migration_engine import MigrationEngine


class Commands:
    """
    This class is used to define the commands that can be executed in the application from CLI.
    """
    def __init__(self, command: str):
        self.command = command

    def dispatch(self, **kwargs):
        """
        Dispatch the command to the appropriate method.
        """
        if not self.command:
            logger.error("No command provided.")
            sys.exit(1)

        if self.command == 'init':
            self.init()
        elif self.command == 'generate':
            self.generate(**kwargs)
        elif self.command == 'upgrade':
            self.upgrade()
        elif self.command == 'downgrade':
            self.downgrade()
        elif self.command == 'list':
            self.list()
        else:
            logger.error("Unknown command: %s", self.command)
            sys.exit(1)

    @staticmethod
    def init(project_path: str = 'migropy'):
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

    @staticmethod
    def generate(migration_name: str):
        db = get_db_connector(load_config())
        migration_engine = MigrationEngine(db)

        migration_engine.init()
        migration_engine.generate_revision(migration_name)

    @staticmethod
    def upgrade():
        db = get_db_connector(load_config())

        migration_engine = MigrationEngine(db)
        migration_engine.upgrade()

    @staticmethod
    def downgrade():
        db = get_db_connector(load_config())

        migration_engine = MigrationEngine(db)
        migration_engine.downgrade()

    @staticmethod
    def list():
        revisions = MigrationEngine().list_revisions()
        for revision in revisions:
            print('- ' + revision.name)