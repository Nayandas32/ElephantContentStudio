import sqlite3
from pathlib import Path

from config.app_config import DATABASE_PATH
from core.logger import Logger


class DatabaseManager:

    def __init__(self):

        self.logger = Logger.get_logger()

        db_path = Path(DATABASE_PATH)

        db_path.parent.mkdir(parents=True, exist_ok=True)

        self.connection = sqlite3.connect(db_path)

        self.cursor = self.connection.cursor()

        self.logger.info("Database connected.")

        self.create_tables()

    # --------------------------------------------------

    def create_tables(self):

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS projects(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                name TEXT NOT NULL,

                created_at TEXT,

                description TEXT

            )
            """
        )

        self.connection.commit()

        self.logger.info("Database tables verified.")

    # --------------------------------------------------

    def execute(self, query, params=()):

        self.cursor.execute(query, params)

        self.connection.commit()

        return self.cursor

    # --------------------------------------------------
    # Project Manager
    # --------------------------------------------------

    def create_project(self, name, description=""):

        self.cursor.execute(
            """
            INSERT INTO projects(
                name,
                created_at,
                description
            )
            VALUES(
                ?,
                datetime('now'),
                ?
            )
            """,
            (name, description),
        )

        self.connection.commit()

        self.logger.info(f"Project created: {name}")

    # --------------------------------------------------

    def get_projects(self):

        self.cursor.execute(
            """
            SELECT
                id,
                name,
                created_at,
                description
            FROM projects
            ORDER BY id DESC
            """
        )

        return self.cursor.fetchall()

    # --------------------------------------------------

    def get_project(self, project_id):

        self.cursor.execute(
            """
            SELECT
                id,
                name,
                created_at,
                description
            FROM projects
            WHERE id = ?
            """,
            (project_id,),
        )

        return self.cursor.fetchone()

    # --------------------------------------------------

    def update_project(self, project_id, name, description=""):

        self.cursor.execute(
            """
            UPDATE projects
            SET
                name = ?,
                description = ?
            WHERE id = ?
            """,
            (name, description, project_id),
        )

        self.connection.commit()

        self.logger.info(f"Project updated: {project_id}")

    # --------------------------------------------------

    def delete_project(self, project_id):

        self.cursor.execute(
            """
            DELETE FROM projects
            WHERE id = ?
            """,
            (project_id,),
        )

        self.connection.commit()

        self.logger.info(f"Project deleted: {project_id}")

    # --------------------------------------------------

    def close(self):

        self.connection.close()

        self.logger.info("Database closed.")