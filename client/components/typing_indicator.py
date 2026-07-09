import customtkinter as ctk


class TypingIndicator(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.label = ctk.CTkLabel(
            self,
            text="",
            text_color="#7CFC00",
            font=("Segoe UI", 12, "italic")
        )

        self.label.pack(anchor="w", padx=15)

    def show(self, username):

        self.label.configure(
            text=f"{username} is typing..."
        )

    def hide(self):

        self.label.configure(text="")