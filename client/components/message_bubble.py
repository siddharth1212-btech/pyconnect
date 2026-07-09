import customtkinter as ctk
from datetime import datetime


class MessageBubble(ctk.CTkFrame):

    def __init__(self, parent, message, sender=False):

        bg = "#2B5278" if sender else "#1F1F1F"

        super().__init__(
            parent,
            fg_color=bg,
            corner_radius=18
        )

        self.grid_columnconfigure(0, weight=1)

        self.msg = ctk.CTkLabel(
            self,
            text=message,
            justify="left",
            wraplength=420,
            anchor="w",
            font=("Segoe UI", 14)
        )

        self.msg.grid(
            row=0,
            column=0,
            padx=14,
            pady=(10, 2),
            sticky="w"
        )

        self.time = ctk.CTkLabel(
            self,
            text=datetime.now().strftime("%I:%M %p"),
            text_color="gray80",
            font=("Segoe UI", 10)
        )

        self.time.grid(
            row=1,
            column=0,
            padx=14,
            pady=(0, 8),
            sticky="e"
        )