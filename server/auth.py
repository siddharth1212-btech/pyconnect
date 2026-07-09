import bcrypt
from server.database import Database

db = Database()


class Auth:

    @staticmethod
    def register(username, password):

        conn = db.connect()
        cursor = conn.cursor()

        hashed = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        )

        try:

            cursor.execute(
                "INSERT INTO users(username,password) VALUES(?,?)",
                (username, hashed)
            )

            conn.commit()
            conn.close()

            return True, "Registration Successful"

        except Exception:

            conn.close()

            return False, "Username already exists"

    @staticmethod
    def login(username, password):

        conn = db.connect()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT password FROM users WHERE username=?",
            (username,)
        )

        user = cursor.fetchone()

        conn.close()

        if user:

            if bcrypt.checkpw(
                password.encode(),
                user[0]
            ):
                return True

        return False