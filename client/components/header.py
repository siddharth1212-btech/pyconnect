import customtkinter as ctk


class Header(ctk.CTkFrame):

    def __init__(self, parent, username):

        super().__init__(
            parent,
            height=75,
            fg_color="#161B22",
            corner_radius=15
        )

        self.grid_columnconfigure(1, weight=1)

        # ================= PROFILE =================

        self.avatar = ctk.CTkLabel(
            self,
            text="👤",
            font=("Segoe UI Emoji", 30)
        )

        self.avatar.grid(
            row=0,
            column=0,
            rowspan=2,
            padx=(20, 12),
            pady=12
        )

        self.username = ctk.CTkLabel(
            self,
            text=username,
            font=("Segoe UI", 18, "bold")
        )

        self.username.grid(
            row=0,
            column=1,
            sticky="w",
            pady=(12, 0)
        )

        self.status = ctk.CTkLabel(
            self,
            text="🟢 Connected",
            text_color="#7CFC00",
            font=("Segoe UI", 12)
        )

        self.status.grid(
            row=1,
            column=1,
            sticky="nw"
        )

        # ================= RIGHT BUTTONS =================

        self.search = ctk.CTkButton(
            self,
            text="🔍",
            width=42,
            height=42,
            corner_radius=10
        )

        self.search.grid(
            row=0,
            column=2,
            rowspan=2,
            padx=(0, 8)
        )

        self.theme = ctk.CTkButton(
            self,
            text="🌙",
            width=42,
            height=42,
            corner_radius=10
        )

        self.theme.grid(
            row=0,
            column=3,
            rowspan=2,
            padx=(0, 8)
        )

        self.notify = ctk.CTkButton(
            self,
            text="🔔",
            width=42,
            height=42,
            corner_radius=10
        )

        self.notify.grid(
            row=0,
            column=4,
            rowspan=2,
            padx=(0, 8)
        )

        self.settings = ctk.CTkButton(
            self,
            text="⚙",
            width=42,
            height=42,
            corner_radius=10
        )

        self.settings.grid(
            row=0,
            column=5,
            rowspan=2,
            padx=(0, 20)
        )