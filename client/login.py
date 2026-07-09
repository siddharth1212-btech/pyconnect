from tkinter import messagebox
import customtkinter as ctk

from server.auth import Auth


class LoginScreen(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent, fg_color="#0D1117")

        self.pack(fill="both", expand=True)

        card = ctk.CTkFrame(
            self,
            width=450,
            height=500,
            corner_radius=20,
            fg_color="#161B22"
        )

        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        ctk.CTkLabel(
            card,
            text="Welcome Back 👋",
            font=("Segoe UI", 28, "bold")
        ).pack(pady=(40, 10))

        ctk.CTkLabel(
            card,
            text="Login to continue using PyConnect",
            text_color="gray"
        ).pack(pady=(0, 25))

        self.username = ctk.CTkEntry(
            card,
            width=320,
            height=45,
            placeholder_text="Username"
        )

        self.username.pack(pady=10)

        self.password = ctk.CTkEntry(
            card,
            width=320,
            height=45,
            placeholder_text="Password",
            show="*"
        )

        self.password.pack(pady=10)

        ctk.CTkButton(
            card,
            text="Login",
            width=320,
            height=45,
            command=self.login_user
        ).pack(pady=20)

        ctk.CTkButton(
            card,
            text="Create Account",
            width=320,
            height=45,
            fg_color="transparent",
            border_width=2,
            command=self.open_register
        ).pack()

        ctk.CTkLabel(
            card,
            text="© 2026 PyConnect | Made by Siddharth",
            text_color="gray",
            font=("Segoe UI", 12)
        ).pack(side="bottom", pady=20)

    def login_user(self):

        username = self.username.get().strip()
        password = self.password.get().strip()

        if username == "" or password == "":
            messagebox.showerror(
                "Error",
                "Enter Username & Password"
            )
            return

        if Auth.login(username, password):

            from client.chat import ChatScreen

            self.destroy()

            ChatScreen(
                self.master,
                username
            )

        else:

            messagebox.showerror(
                "Error",
                "Invalid Username or Password"
            )

    def open_register(self):

        from client.register import RegisterScreen

        self.destroy()

        RegisterScreen(self.master)