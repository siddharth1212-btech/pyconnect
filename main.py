import customtkinter as ctk

from server.database import Database
from client.login import LoginScreen

Database()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class PyConnectApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("PyConnect")

        self.geometry("1400x850")

        self.minsize(1200,700)

        self.show_login()

    def clear(self):

        for widget in self.winfo_children():
            widget.destroy()

    def show_login(self):

        self.clear()

        LoginScreen(self)


app = PyConnectApp()

app.mainloop()