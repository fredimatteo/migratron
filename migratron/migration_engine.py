import sys
import uuid
from io import StringIO
from pathlib import Path
from typing import List

from migratron.core.logger import logger
from migratron.databases.db_connector import DatabaseConnector

FIRST_REVISION_ID = '0000'
UP_PREFIX = "-- Up"
COMMENT_PREFIX = "--"
DOWN_PREFIX = "-- Down"
REVISION_TEMPLATE = [
    "-- Up migration",
    "\n",
    "\n",
    "-- Down migration"
]


class MigrationEngine:
    """
    Migration engine class

    This class is responsible for managing the migrations of the database.
    """

    def __init__(self, db: DatabaseConnector):
        self.db: DatabaseConnector = db

    def init(self):
        self.__create_migration_table()

    def __create_migration_table(self) -> None:
        """
        Create the migration table if it does not exist
        :return: None
        """
        if self.db:
            logger.debug('creating migrations table')
            self.db.execute("""
                CREATE TABLE IF NOT EXISTS migrations (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            self.db.commit()

    def __create_revision_file(self, revision_name: str) -> None:
        """
        Create a new revision file
        :param revision_name: str
        :return: None
        """
        revision_id = self.__get_last_revision_id()
        revision_id = str(int(revision_id) + 1).zfill(4)

        revision_file_name = f"{revision_id}_{revision_name}.sql"
        revision_file_path = Path(f"./versions/{revision_file_name}")

        with open(revision_file_path, "w") as revision_file:
            revision_file.writelines(REVISION_TEMPLATE)

    @staticmethod
    def __get_last_revision_id() -> str:
        """
        Get the last revision id
        :return: str
        """
        folder = Path("./versions")
        file_names: List[str] = [obj.name for obj in folder.iterdir() if obj.is_file()]

        file_names_prefix = [file_name.split("_")[0] for file_name in file_names]
        if len(file_names_prefix) == 0:
            return FIRST_REVISION_ID


        file_names_prefix.sort()
        return file_names_prefix[-1]

    @staticmethod
    def __get_last_revision_name(is_downgrade: bool = False) -> str:
        """
        Get the last revision name
        :param is_downgrade: bool
        :return: str
        """
        folder = Path("./versions")
        file_names: List[str] = [obj.name for obj in folder.iterdir() if obj.is_file()]
        file_names.sort()
        return file_names[-1] if not is_downgrade else file_names[0]

    def generate_revision(self, revision_name: str = "") -> None:
        """
        Generate a new revision
        :param revision_name: str
        :return: None
        """
        for char in revision_name:
            if not char.isalnum() and char != " " and char != "_":
                logger.error('invalid revision name. Only alphanumeric characters, spaces and underscores are allowed')
                sys.exit(1)

        revision_name = revision_name.replace(" ", "_")
        if revision_name == "":
            revision_name = str(uuid.uuid4())

        self.__create_revision_file(revision_name)

    @staticmethod
    def __get_all_revisions() -> List[Path]:
        folder = Path("./versions")
        files: List[Path] = [obj for obj in folder.iterdir() if obj.is_file()]
        files_sorted: List[Path] = sorted(files, key=lambda x: x.name.split("_")[0])
        return files_sorted

    def list_revisions(self) -> List[Path]:
        return self.__get_all_revisions()

    def upgrade(self) -> None:
        revisions = self.__get_all_revisions()
        for revision in revisions:
            lines = revision.read_text().splitlines()
            builder = StringIO()
            for line in lines:
                if line.startswith(UP_PREFIX):
                    pass
                if line.startswith(DOWN_PREFIX):
                    break

                if not line.startswith(COMMENT_PREFIX):
                    builder.write(line)
                    builder.write("\n")

            self.db.execute(builder.getvalue())
            self.db.commit()

        last_revision_name = self.__get_last_revision_name()
        self.upsert_migration_table(last_revision_name)

    def downgrade(self) -> None:
        revisions = self.__get_all_revisions()
        revisions.reverse()
        for revision in revisions:
            lines = revision.read_text().splitlines()
            builder = StringIO()
            is_down = False
            for line in lines:
                if line.startswith(DOWN_PREFIX) or line.startswith(UP_PREFIX):
                    is_down = True
                    continue

                if not line.startswith(COMMENT_PREFIX) and is_down:
                    builder.write(line)
                    builder.write("\n")

            is_down = False
            self.db.execute(builder.getvalue())
            self.db.commit()

        last_revision_name = self.__get_last_revision_name(is_downgrade=True)
        self.upsert_migration_table(last_revision_name)

    def upsert_migration_table(self, revision_name: str) -> None:
        if not self.at_least_one_revision_executed():
            self.db.execute(f"""
                INSERT INTO migrations (name) VALUES ('{revision_name}')
            """)
        else:
            self.db.execute(f"""
                UPDATE migrations SET name = '{revision_name}'
            """)

        self.db.commit()

    def at_least_one_revision_executed(self) -> bool:
        logger.debug('checking if at least one revision has been executed')
        result = self.db.execute("SELECT COUNT(*) FROM migrations")
        return result.fetchone()[0] > 0