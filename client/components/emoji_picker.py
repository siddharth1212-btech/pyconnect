import customtkinter as ctk

EMOJIS = [
    "😀","😁","😂","🤣","😊","😍","😘","😎",
    "😭","😡","👍","👏","🙏","🔥","❤️","💯",
    "🤔","🥳","🎉","😴","😅","😇","🤩","😜",
    "😏","🙌","👌","💪","🎮","💻","📱","🚀"
]


class EmojiPicker(ctk.CTkToplevel):

    def __init__(self, parent, callback):

        super().__init__(parent)

        self.callback = callback

        self.title("Emoji")

        self.geometry("420x260")

        self.resizable(False, False)

        self.attributes("-topmost", True)

        row = 0
        col = 0

        for emoji in EMOJIS:

            btn = ctk.CTkButton(
                self,
                text=emoji,
                width=45,
                height=45,
                command=lambda e=emoji: self.select(e)
            )

            btn.grid(
                row=row,
                column=col,
                padx=5,
                pady=5
            )

            col += 1

            if col == 8:
                col = 0
                row += 1

    def select(self, emoji):

        self.callback(emoji)

        self.destroy()