from tkinter import filedialog


def pick_image():

    file = filedialog.askopenfilename(

        title="Select Image",

        filetypes=[
            ("Images","*.png *.jpg *.jpeg *.gif")
        ]
    )

    return file