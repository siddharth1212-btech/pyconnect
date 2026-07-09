from tkinter import messagebox
import customtkinter as ctk

from server.auth import Auth


class LoginScreen(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent, fg_color="#0D1117")

        self.parent = parent

        self.pack(fill="both", expand=True)

        card = ctk.CTkFrame(
            self,
            width=450,
            height=520,
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
            text="💬 PyConnect",
            font=("Segoe UI", 30, "bold")
        ).pack(pady=(30, 5))

        ctk.CTkLabel(
            card,
            text="Welcome Back 👋",
            font=("Segoe UI", 24, "bold")
        ).pack()

        ctk.CTkLabel(
            card,
            text="Login to continue",
            text_color="gray70",
            font=("Segoe UI", 13)
        ).pack(pady=(5, 25))

        self.username = ctk.CTkEntry(
            card,
            width=330,
            height=45,
            placeholder_text="Username"
        )

        self.username.pack(pady=10)

        self.password = ctk.CTkEntry(
            card,
            width=330,
            height=45,
            placeholder_text="Password",
            show="*"
        )

        self.password.pack(pady=10)

        self.username.bind(
            "<Return>",
            lambda e: self.password.focus()
        )

        self.password.bind(
            "<Return>",
            lambda e: self.login_user()
        )

        ctk.CTkButton(
            card,
            text="Login",
            width=330,
            height=45,
            corner_radius=10,
            command=self.login_user
        ).pack(pady=(25, 12))

        ctk.CTkButton(
            card,
            text="Create Account",
            width=330,
            height=45,
            fg_color="transparent",
            border_width=2,
            corner_radius=10,
            command=self.open_register
        ).pack()

        self.status = ctk.CTkLabel(
            card,
            text="",
            text_color="#7CFC00",
            font=("Segoe UI", 12)
        )

        self.status.pack(pady=12)

        ctk.CTkLabel(
            card,
            text="© 2026 PyConnect | Made by Siddharth",
            text_color="gray60",
            font=("Segoe UI", 11)
        ).pack(side="bottom", pady=18)

    # ================= LOGIN =================

    def login_user(self):

        username = self.username.get().strip()
        password = self.password.get().strip()

        if not username or not password:

            messagebox.showerror(
                "Error",
                "Please enter username and password."
            )

            return

        ok = Auth.login(
            username,
            password
        )

        if not ok:

            messagebox.showerror(
                "Login Failed",
                "Invalid username or password."
            )

            return

        self.status.configure(
            text="Login Successful ✓"
        )

        self.after(
            500,
            lambda: self.parent.show_chat(username)
        )

    # ================= REGISTER =================

    def open_register(self):

        self.parent.show_register()