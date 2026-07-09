import customtkinter as ctk


class TypingIndicator(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent",
            height=28
        )

        self.pack_propagate(False)

        self.label = ctk.CTkLabel(
            self,
            text="",
            text_color="#7CFC00",
            font=("Segoe UI", 12, "italic")
        )

        self.label.pack(
            anchor="w",
            padx=18,
            pady=2
        )

        self.after_id = None

    # ================= SHOW =================

    def show(self, username):

        self.label.configure(
            text=f"✍️ {username} is typing..."
        )

        if self.after_id:
            self.after_cancel(self.after_id)

        self.after_id = self.after(
            2000,
            self.hide
        )

    # ================= HIDE =================

    def hide(self):

        self.label.configure(text="")

        self.after_id = None