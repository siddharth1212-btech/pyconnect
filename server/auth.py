import bcrypt
import sqlite3

from server.database import Database

db = Database()


class Auth:

    # ================= REGISTER =================

    @staticmethod
    def register(username, password):

        conn = db.connect()
        cursor = conn.cursor()

        username = username.strip()

        hashed_password = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        )

        try:

            cursor.execute(
                """
                INSERT INTO users
                (username,password)
                VALUES(?,?)
                """,
                (
                    username,
                    hashed_password
                )
            )

            conn.commit()

            return (
                True,
                "Registration Successful"
            )

        except sqlite3.IntegrityError:

            return (
                False,
                "Username already exists."
            )

        except Exception as e:

            return (
                False,
                str(e)
            )

        finally:

            conn.close()

    # ================= LOGIN =================

    @staticmethod
    def login(username, password):

        conn = db.connect()
        cursor = conn.cursor()

        try:

            cursor.execute(

                """
                SELECT password
                FROM users
                WHERE username=?
                """,

                (
                    username.strip(),
                )

            )

            user = cursor.fetchone()

            if not user:

                return False

            stored_password = user[0]

            if isinstance(
                stored_password,
                str
            ):

                stored_password = stored_password.encode()

            return bcrypt.checkpw(
                password.encode(),
                stored_password
            )

        except Exception:

            return False

        finally:

            conn.close()

    # ================= USER EXISTS =================

    @staticmethod
    def user_exists(username):

        conn = db.connect()
        cursor = conn.cursor()

        cursor.execute(

            """
            SELECT id
            FROM users
            WHERE username=?
            """,

            (
                username.strip(),
            )

        )

        user = cursor.fetchone()

        conn.close()

        return user is not None

    # ================= TOTAL USERS =================

    @staticmethod
    def total_users():

        conn = db.connect()
        cursor = conn.cursor()

        cursor.execute(

            """
            SELECT COUNT(*)
            FROM users
            """

        )

        total = cursor.fetchone()[0]

        conn.close()

        return total