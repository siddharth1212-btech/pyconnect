import customtkinter as ctk
from datetime import datetime


class ChatBubble(ctk.CTkFrame):

    def __init__(self, parent, text, me=False):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.pack(
            fill="x",
            pady=6,
            padx=5
        )

        bubble_color = "#2563EB" if me else "#1F2937"

        bubble = ctk.CTkFrame(
            self,
            fg_color=bubble_color,
            corner_radius=18
        )

        if me:

            bubble.pack(
                anchor="e",
                padx=15
            )

        else:

            bubble.pack(
                anchor="w",
                padx=15
            )

        # ================= MESSAGE =================

        self.message = ctk.CTkLabel(
            bubble,
            text=text,
            wraplength=500,
            justify="left",
            anchor="w",
            font=("Segoe UI", 14)
        )

        self.message.pack(
            padx=14,
            pady=(10, 4),
            anchor="w"
        )

        # ================= FOOTER =================

        footer = ctk.CTkFrame(
            bubble,
            fg_color="transparent"
        )

        footer.pack(
            fill="x",
            padx=10,
            pady=(0, 8)
        )

        self.time = ctk.CTkLabel(
            footer,
            text=datetime.now().strftime("%I:%M %p"),
            text_color="gray80",
            font=("Segoe UI", 10)
        )

        self.time.pack(
            side="right"
        )

        if me:

            self.status = ctk.CTkLabel(
                footer,
                text="✓✓",
                text_color="#A5F3FC",
                font=("Segoe UI", 10, "bold")
            )

            self.status.pack(
                side="right",
                padx=(0, 6)
            )