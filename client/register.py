from tkinter import messagebox
import customtkinter as ctk

from server.auth import Auth


class RegisterScreen(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(parent, fg_color="#0D1117")

        self.pack(fill="both", expand=True)

        card = ctk.CTkFrame(
            self,
            width=450,
            height=600,
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
            text="Create Account",
            font=("Segoe UI", 28, "bold")
        ).pack(pady=(30, 10))

        ctk.CTkLabel(
            card,
            text="Join PyConnect",
            text_color="gray"
        ).pack(pady=(0, 20))

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

        self.confirm = ctk.CTkEntry(
            card,
            width=320,
            height=45,
            placeholder_text="Confirm Password",
            show="*"
        )
        self.confirm.pack(pady=10)

        ctk.CTkButton(
            card,
            text="Create Account",
            width=320,
            height=45,
            command=self.register_user
        ).pack(pady=20)

        ctk.CTkButton(
            card,
            text="Back To Login",
            width=320,
            height=45,
            fg_color="transparent",
            border_width=2,
            command=self.back_to_login
        ).pack()

    def register_user(self):

        username = self.username.get().strip()
        password = self.password.get().strip()
        confirm = self.confirm.get().strip()

        if username == "" or password == "" or confirm == "":
            messagebox.showerror(
                "Error",
                "All fields are required."
            )
            return

        if password != confirm:
            messagebox.showerror(
                "Error",
                "Passwords do not match."
            )
            return

        success, msg = Auth.register(username, password)

        if success:

            messagebox.showinfo(
                "Success",
                "Account Created Successfully"
            )

            self.destroy()

            from client.login import LoginScreen

            LoginScreen(self.master)

        else:

            messagebox.showerror(
                "Error",
                msg
            )

    def back_to_login(self):

        self.destroy()

        from client.login import LoginScreen

        LoginScreen(self.master)