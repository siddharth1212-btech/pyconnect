import os
import sqlite3

DB_FOLDER = "database"
DB_NAME = os.path.join(DB_FOLDER, "chat.db")


class Database:

    def __init__(self):

        os.makedirs(
            DB_FOLDER,
            exist_ok=True
        )

        self.create_tables()

    # ================= CONNECT =================

    def connect(self):

        conn = sqlite3.connect(DB_NAME)

        conn.execute(
            "PRAGMA foreign_keys = ON"
        )

        return conn

    # ================= CREATE TABLES =================

    def create_tables(self):

        conn = self.connect()
        cursor = conn.cursor()

        # ---------- USERS ----------

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT UNIQUE NOT NULL,

            password BLOB NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

        """)

        # ---------- MESSAGES ----------

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS messages(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            sender TEXT NOT NULL,

            message TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

        """)

        conn.commit()

        conn.close()

    # ================= SAVE MESSAGE =================

    def save_message(
        self,
        sender,
        message
    ):

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute(

            """
            INSERT INTO messages
            (sender,message)
            VALUES(?,?)
            """,

            (
                sender,
                message
            )

        )

        conn.commit()

        conn.close()

    # ================= LOAD MESSAGES =================

    def get_messages(
        self,
        limit=100
    ):

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute(

            """
            SELECT sender,message,created_at
            FROM messages
            ORDER BY id ASC
            LIMIT ?
            """,

            (
                limit,
            )

        )

        rows = cursor.fetchall()

        conn.close()

        return rows

    # ================= CLEAR CHAT =================

    def clear_messages(self):

        conn = self.connect()

        cursor = conn.cursor()

        cursor.execute(

            "DELETE FROM messages"

        )

        conn.commit()

        conn.close()