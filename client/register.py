from tkinter import messagebox
import customtkinter as ctk

from server.auth import Auth


class RegisterScreen(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent, fg_color="#0D1117")

        self.parent = parent

        self.pack(fill="both", expand=True)

        card = ctk.CTkFrame(
            self,
            width=460,
            height=610,
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
            text="Create Account",
            font=("Segoe UI", 24, "bold")
        ).pack()

        ctk.CTkLabel(
            card,
            text="Join the community",
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

        self.confirm = ctk.CTkEntry(
            card,
            width=330,
            height=45,
            placeholder_text="Confirm Password",
            show="*"
        )

        self.confirm.pack(pady=10)

        self.username.bind(
            "<Return>",
            lambda e: self.password.focus()
        )

        self.password.bind(
            "<Return>",
            lambda e: self.confirm.focus()
        )

        self.confirm.bind(
            "<Return>",
            lambda e: self.register_user()
        )

        ctk.CTkButton(
            card,
            text="Create Account",
            width=330,
            height=45,
            corner_radius=10,
            command=self.register_user
        ).pack(pady=(25, 12))

        ctk.CTkButton(
            card,
            text="Back To Login",
            width=330,
            height=45,
            fg_color="transparent",
            border_width=2,
            corner_radius=10,
            command=self.back_to_login
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

    # ================= REGISTER =================

    def register_user(self):

        username = self.username.get().strip()
        password = self.password.get().strip()
        confirm = self.confirm.get().strip()

        if not username or not password or not confirm:

            messagebox.showerror(
                "Error",
                "Please fill all fields."
            )

            return

        if len(username) < 3:

            messagebox.showerror(
                "Error",
                "Username must be at least 3 characters."
            )

            return

        if len(password) < 4:

            messagebox.showerror(
                "Error",
                "Password must be at least 4 characters."
            )

            return

        if password != confirm:

            messagebox.showerror(
                "Error",
                "Passwords do not match."
            )

            return

        success, msg = Auth.register(
            username,
            password
        )

        if success:

            self.status.configure(
                text="Account Created Successfully ✓"
            )

            self.after(
                800,
                self.back_to_login
            )

        else:

            messagebox.showerror(
                "Registration Failed",
                msg
            )

    # ================= LOGIN =================

    def back_to_login(self):

        self.parent.show_login()