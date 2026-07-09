import customtkinter as ctk

EMOJIS = [
    "😀","😁","😂","🤣","😊","😍","😘","😎",
    "😭","😡","🥹","😇","🤩","😜","😏","🤔",
    "👍","👎","👏","🙌","🙏","👌","💪","🤝",
    "❤️","💙","💚","💛","🖤","🤍","💜","💯",
    "🔥","✨","⭐","🌟","⚡","🎉","🥳","🎂",
    "🎮","💻","📱","📸","🎵","🚀","☕","🍕",
    "🐱","🐶","🌸","🌹","🌍","🌈","☀️","🌙",
    "😴","🤯","🤖","👀","💀","😅","😋","🤤"
]


class EmojiPicker(ctk.CTkToplevel):

    def __init__(self, parent, callback):

        super().__init__(parent)

        self.callback = callback

        self.title("😀 Emoji Picker")

        self.geometry("520x420")

        self.resizable(False, False)

        self.attributes("-topmost", True)

        self.configure(fg_color="#111827")

        self.grab_set()

        title = ctk.CTkLabel(
            self,
            text="Choose an Emoji",
            font=("Segoe UI", 20, "bold")
        )

        title.pack(
            pady=(15, 10)
        )

        self.scroll = ctk.CTkScrollableFrame(
            self,
            width=470,
            height=320,
            fg_color="#161B22"
        )

        self.scroll.pack(
            padx=15,
            pady=10,
            fill="both",
            expand=True
        )

        row = 0
        col = 0

        for emoji in EMOJIS:

            btn = ctk.CTkButton(

                self.scroll,

                text=emoji,

                width=48,

                height=48,

                corner_radius=10,

                font=("Segoe UI Emoji", 20),

                command=lambda e=emoji: self.select(e)

            )

            btn.grid(

                row=row,

                column=col,

                padx=6,

                pady=6

            )

            col += 1

            if col == 8:

                col = 0
                row += 1

    # ================= SELECT =================

    def select(self, emoji):

        self.callback(emoji)

        self.destroy()