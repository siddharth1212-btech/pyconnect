import customtkinter as ctk
from datetime import datetime


class ChatBubble(ctk.CTkFrame):

    def __init__(self, parent, text, me=False):

        bg = "#2563EB" if me else "#1F2937"

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.pack(fill="x", pady=4)

        bubble = ctk.CTkFrame(
            self,
            fg_color=bg,
            corner_radius=18
        )

        if me:
            bubble.pack(anchor="e", padx=20)
        else:
            bubble.pack(anchor="w", padx=20)

        msg = ctk.CTkLabel(
            bubble,
            text=text,
            justify="left",
            wraplength=420,
            font=("Segoe UI",14)
        )

        msg.pack(
            padx=14,
            pady=(10,4)
        )

        time = ctk.CTkLabel(
            bubble,
            text=datetime.now().strftime("%I:%M %p"),
            text_color="gray80",
            font=("Segoe UI",10)
        )

        time.pack(
            anchor="e",
            padx=12,
            pady=(0,8)
        )