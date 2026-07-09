import customtkinter as ctk


class InputBar(ctk.CTkFrame):

    def __init__(self, parent, send_callback, emoji_callback, image_callback):

        super().__init__(
            parent,
            fg_color="#161B22",
            height=70
        )

        self.grid_columnconfigure(0, weight=1)

        self.entry = ctk.CTkEntry(
            self,
            placeholder_text="Type a message...",
            height=45
        )

        self.entry.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(20,10),
            pady=12
        )

        self.entry.bind("<Return>", lambda e: send_callback())

        self.emoji = ctk.CTkButton(
            self,
            text="😀",
            width=45,
            command=emoji_callback
        )

        self.emoji.grid(
            row=0,
            column=1,
            padx=(0,8)
        )

        self.image = ctk.CTkButton(
            self,
            text="📷",
            width=45,
            command=image_callback
        )

        self.image.grid(
            row=0,
            column=2,
            padx=(0,8)
        )

        self.send = ctk.CTkButton(
            self,
            text="Send",
            width=110,
            command=send_callback
        )

        self.send.grid(
            row=0,
            column=3,
            padx=(0,20)
        )