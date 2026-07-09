from datetime import datetime
import os
import random


# ================= TIME =================

def current_time():

    return datetime.now().strftime("%I:%M %p")


def current_date():

    return datetime.now().strftime("%d-%m-%Y")


def current_datetime():

    return datetime.now().strftime("%d-%m-%Y %I:%M %p")


# ================= FILE =================

def get_filename(path):

    if not path:
        return ""

    return os.path.basename(path)


def get_extension(path):

    if not path:
        return ""

    return os.path.splitext(path)[1].lower()


def format_size(size):

    if size < 1024:
        return f"{size} B"

    elif size < 1024 * 1024:
        return f"{size / 1024:.2f} KB"

    elif size < 1024 * 1024 * 1024:
        return f"{size / (1024 * 1024):.2f} MB"

    return f"{size / (1024 * 1024 * 1024):.2f} GB"


# ================= TEXT =================

def capitalize(text):

    return text.strip().title()


def shorten(text, limit=40):

    if len(text) <= limit:
        return text

    return text[:limit] + "..."


# ================= RANDOM =================

def random_avatar():

    avatars = [
        "😀", "😎", "🤖", "👨", "👩",
        "🦁", "🐼", "🐱", "🐸", "🐧",
        "🐯", "🐵", "🦊", "🐻", "🐨"
    ]

    return random.choice(avatars)


# ================= COLORS =================

def random_color():

    colors = [
        "#2563EB",
        "#22C55E",
        "#F59E0B",
        "#EF4444",
        "#A855F7",
        "#06B6D4",
        "#EC4899"
    ]

    return random.choice(colors)


# ================= CONNECTION =================

def is_localhost(host):

    return host in (
        "127.0.0.1",
        "localhost"
    )