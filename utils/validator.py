import re


class Validator:

    # ================= USERNAME =================

    @staticmethod
    def validate_username(username):

        username = username.strip()

        if len(username) < 3:
            return False, "Username must be at least 3 characters."

        if len(username) > 20:
            return False, "Username cannot exceed 20 characters."

        if not re.fullmatch(r"[A-Za-z0-9_]+", username):
            return False, "Only letters, numbers and '_' are allowed."

        return True, "Valid"

    # ================= PASSWORD =================

    @staticmethod
    def validate_password(password):

        if len(password) < 6:
            return False, "Password must be at least 6 characters."

        if len(password) > 32:
            return False, "Password cannot exceed 32 characters."

        has_letter = any(c.isalpha() for c in password)
        has_digit = any(c.isdigit() for c in password)

        if not has_letter:
            return False, "Password must contain at least one letter."

        if not has_digit:
            return False, "Password must contain at least one number."

        return True, "Valid"

    # ================= CONFIRM PASSWORD =================

    @staticmethod
    def confirm_password(password, confirm):

        if password != confirm:
            return False, "Passwords do not match."

        return True, "Matched"

    # ================= MESSAGE =================

    @staticmethod
    def validate_message(message):

        message = message.strip()

        if message == "":
            return False, "Message cannot be empty."

        if len(message) > 1000:
            return False, "Message is too long."

        return True, "Valid"

    # ================= IMAGE =================

    @staticmethod
    def validate_image(path):

        if not path:
            return False

        allowed = (
            ".png",
            ".jpg",
            ".jpeg",
            ".gif",
            ".bmp",
            ".webp"
        )

        return path.lower().endswith(allowed)