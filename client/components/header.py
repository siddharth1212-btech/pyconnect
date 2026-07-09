import customtkinter as ctk


class Header(ctk.CTkFrame):

    def __init__(self, parent, username):

        super().__init__(
            parent,
            height=70,
            fg_color="#161B22",
            corner_radius=15
        )

        self.grid_columnconfigure(1, weight=1)

        self.avatar = ctk.CTkLabel(
            self,
            text="👤",
            font=("Segoe UI Emoji",28)
        )

        self.avatar.grid(
            row=0,
            column=0,
            padx=20,
            pady=15
        )

        self.name = ctk.CTkLabel(
            self,
            text=username,
            font=("Segoe UI",18,"bold")
        )

        self.name.grid(
            row=0,
            column=1,
            sticky="w"
        )

        self.status = ctk.CTkLabel(
            self,
            text="🟢 Online",
            text_color="#32CD32",
            font=("Segoe UI",12)
        )

        self.status.grid(
            row=1,
            column=1,
            sticky="nw"
        )

        self.search = ctk.CTkButton(
            self,
            text="🔍",
            width=40,
            height=40
        )

        self.search.grid(
            row=0,
            column=2,
            padx=10
        )

        self.settings = ctk.CTkButton(
            self,
            text="⚙",
            width=40,
            height=40
        )

        self.settings.grid(
            row=0,
            column=3,
            padx=(0,20)
        )