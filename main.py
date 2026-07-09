import customtkinter as ctk

from server.database import Database
from client.login import LoginScreen


# ================= DATABASE =================

Database()

# ================= THEME =================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# ================= APP =================

class PyConnectApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("💬 PyConnect")

        self.geometry("1400x850")

        self.minsize(1200, 700)

        self.protocol(
            "WM_DELETE_WINDOW",
            self.on_close
        )

        self.current_screen = None

        self.show_login()

    # ================= CLEAR =================

    def clear(self):

        if self.current_screen:

            try:
                self.current_screen.destroy()
            except:
                pass

        self.current_screen = None

    # ================= LOGIN =================

    def show_login(self):

        self.clear()

        self.current_screen = LoginScreen(self)

    # ================= REGISTER =================

    def show_register(self):

        from client.register import RegisterScreen

        self.clear()

        self.current_screen = RegisterScreen(self)

    # ================= CHAT =================

    def show_chat(self, username):

        print("Opening Chat")

        self.clear()
        
        from client.chat import ChatScreen

        self.current_screen = ChatScreen(
           self,
           username
        )

        print("Chat Loaded")

    # ================= CLOSE =================

    def on_close(self):

        try:

            if (
                self.current_screen
                and hasattr(self.current_screen, "disconnect")
            ):

                self.current_screen.disconnect()

        except:
            pass

        self.destroy()


# ================= START =================

if __name__ == "__main__":

    app = PyConnectApp()

    app.mainloop()