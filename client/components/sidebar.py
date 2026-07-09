import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            width=270,
            fg_color="#111827",
            corner_radius=0
        )

        self.pack_propagate(False)

        title = ctk.CTkLabel(
            self,
            text="💬 PyConnect",
            font=("Segoe UI",26,"bold")
        )

        title.pack(pady=(25,15))

        self.search = ctk.CTkEntry(
            self,
            placeholder_text="Search user..."
        )

        self.search.pack(
            padx=15,
            fill="x"
        )

        ctk.CTkLabel(
            self,
            text="ONLINE",
            text_color="gray70",
            font=("Segoe UI",13,"bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(20,5)
        )

        self.user_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )

        self.user_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0,10)
        )

    def update_users(self, users):

        for widget in self.user_frame.winfo_children():
            widget.destroy()

        for user in users:

            card = ctk.CTkFrame(
                self.user_frame,
                fg_color="#1F2937",
                corner_radius=12
            )

            card.pack(
                fill="x",
                padx=5,
                pady=5
            )

            avatar = ctk.CTkLabel(
                card,
                text="👤",
                font=("Segoe UI Emoji",22)
            )

            avatar.pack(
                side="left",
                padx=12,
                pady=10
            )

            name = ctk.CTkLabel(
                card,
                text=user,
                font=("Segoe UI",14,"bold")
            )

            name.pack(
                side="left"
            )

            status = ctk.CTkLabel(
                card,
                text="🟢",
                font=("Segoe UI",15)
            )

            status.pack(
                side="right",
                padx=12
            )