from tkinter import filedialog
import os


IMAGE_TYPES = [
    ("All Supported Images", "*.png *.jpg *.jpeg *.gif *.webp *.bmp"),
    ("PNG Image", "*.png"),
    ("JPEG Image", "*.jpg *.jpeg"),
    ("GIF Image", "*.gif"),
    ("WEBP Image", "*.webp"),
    ("Bitmap Image", "*.bmp"),
]


def pick_image():

    path = filedialog.askopenfilename(

        title="Select Image",

        filetypes=IMAGE_TYPES

    )

    if not path:
        return None

    if not os.path.exists(path):
        return None

    return path


def pick_file():

    path = filedialog.askopenfilename(

        title="Select File"

    )

    if not path:
        return None

    if not os.path.exists(path):
        return None

    return path


def get_filename(path):

    if not path:
        return ""

    return os.path.basename(path)