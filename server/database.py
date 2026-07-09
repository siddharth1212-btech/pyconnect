import sqlite3

DB_NAME = "database/chat.db"


class Database:

    def __init__(self):
        self.create_tables()

    def connect(self):
        return sqlite3.connect(DB_NAME)

    def create_tables(self):

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """)

        conn.commit()
        conn.close()