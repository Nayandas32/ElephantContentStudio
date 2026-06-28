import sqlite3

from config.app_config import DATABASE_PATH


class DatabaseManager:

    def __init__(self):

        self.conn = sqlite3.connect(
            DATABASE_PATH
        )

        self.cursor = self.conn.cursor()

        self.create_tables()

    # ==================================================

    def create_tables(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS projects (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            description TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

        """)

        self.conn.commit()

    # ==================================================

    def create_project(

        self,

        name,

        description=""

    ):

        self.cursor.execute(

            """

            INSERT INTO projects

            (

                name,

                description

            )

            VALUES

            (

                ?,

                ?

            )

            """,

            (

                name,

                description

            )

        )

        self.conn.commit()

    # ==================================================

    def get_projects(self):

        self.cursor.execute(

            """

            SELECT

                id,

                name,

                description,

                created_at

            FROM projects

            ORDER BY id DESC

            """

        )

        return self.cursor.fetchall()

    # ==================================================

    def get_project(

        self,

        project_id

    ):

        self.cursor.execute(

            """

            SELECT *

            FROM projects

            WHERE id=?

            """,

            (

                project_id,

            )

        )

        return self.cursor.fetchone()

    # ==================================================

    def update_project(

        self,

        project_id,

        name,

        description

    ):

        self.cursor.execute(

            """

            UPDATE projects

            SET

                name=?,

                description=?

            WHERE id=?

            """,

            (

                name,

                description,

                project_id

            )

        )

        self.conn.commit()

    # ==================================================

    def delete_project(

        self,

        project_id

    ):

        self.cursor.execute(

            """

            DELETE FROM projects

            WHERE id=?

            """,

            (

                project_id,

            )

        )

        self.conn.commit()

    # ==================================================

    def get_project_count(self):

        self.cursor.execute(

            """

            SELECT COUNT(*)

            FROM projects

            """

        )

        return self.cursor.fetchone()[0]

    # ==================================================

    def close(self):

        self.conn.close()