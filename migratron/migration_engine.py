import os
import uuid
from io import StringIO
from pathlib import Path
from typing import List

from migratron.databases.db_connector import DatabaseConnector


class MigrationEngine:
    def __init__(self, db: DatabaseConnector):
        self.db: DatabaseConnector = db

    def init(self):
        self.__create_migration_table()

    def __create_migration_table(self):
        if self.db:
            self.db.execute("""
                CREATE TABLE IF NOT EXISTS migrations (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            self.db.commit()

    def _create_revision_file(self, revision_name: str) -> None:
        revision_id = self._get_last_revision_id()
        revision_id = str(int(revision_id) + 1).zfill(4)

        revision_file_name = f"{revision_id}_{revision_name}.sql"
        revision_file_path = Path(f"./versions/{revision_file_name}")

        with open(revision_file_path, "w") as revision_file:
            revision_file.writelines([
                "-- Up migration",
                "\n",
                "\n",
                "-- Down migration"
            ])

    @staticmethod
    def _get_last_revision_id() -> str:
        print(os.getcwd())
        folder = Path("./versions")
        file_names: List[str] = [obj.name for obj in folder.iterdir() if obj.is_file()]

        file_names_prefix = [file_name.split("_")[0] for file_name in file_names]
        if len(file_names_prefix) == 0:
            return '0001'

        if len(file_names_prefix) > 0:
            file_names_prefix.sort()
            return file_names_prefix[-1]

    @staticmethod
    def _get_last_revision_name() -> str:
        print(os.getcwd())
        folder = Path("./versions")
        file_names: List[str] = [obj.name for obj in folder.iterdir() if obj.is_file()]
        return file_names.sort()[-1]

    def generate_revision(self, revision_name: str = "") -> None:
        if revision_name == "":
            revision_name = str(uuid.uuid4())

        self._create_revision_file(revision_name)

    @staticmethod
    def _get_all_revisions() -> List[Path]:
        folder = Path("./versions")
        files: List[Path] = [obj for obj in folder.iterdir() if obj.is_file()]
        files_sorted: List[Path] = sorted(files, key=lambda x: x.name.split("_")[0])
        return files_sorted

    def upgrade(self):
        revisions = self._get_all_revisions()
        for revision in revisions:
            lines = revision.read_text().splitlines()
            builder = StringIO()
            for line in lines:
                if line.startswith("-- Up"):
                    pass
                if line.startswith("-- Down"):
                    break

                if not line.startswith("--"):
                    builder.write(line)
                    builder.write("\n")

            print(builder.getvalue())
            self.db.execute(builder.getvalue())
            self.db.commit()

        last_revision_name = self._get_last_revision_name()
        self.update_migration_table(last_revision_name)

    def update_migration_table(self, revision_name: str):
        self.db.execute(f"""
            INSERT INTO migrations (name) VALUES ('{revision_name}')
        """)
        self.db.commit()