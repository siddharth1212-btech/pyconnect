import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            width=280,
            fg_color="#111827",
            corner_radius=0
        )

        self.pack_propagate(False)

        # ================= LOGO =================

        self.logo = ctk.CTkLabel(
            self,
            text="💬 PyConnect",
            font=("Segoe UI", 28, "bold")
        )

        self.logo.pack(
            pady=(25, 5)
        )

        self.version = ctk.CTkLabel(
            self,
            text="Desktop Chat v2.0",
            text_color="gray70",
            font=("Segoe UI", 12)
        )

        self.version.pack(
            pady=(0, 20)
        )

        # ================= SEARCH =================

        self.search = ctk.CTkEntry(
            self,
            height=40,
            placeholder_text="🔍 Search User..."
        )

        self.search.pack(
            padx=15,
            fill="x"
        )

        # ================= ONLINE TITLE =================

        self.count = ctk.CTkLabel(
            self,
            text="🟢 Online Users (0)",
            font=("Segoe UI", 14, "bold"),
            text_color="#8BE28B"
        )

        self.count.pack(
            anchor="w",
            padx=15,
            pady=(20, 10)
        )

        # ================= USER LIST =================

        self.user_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )

        self.user_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 10)
        )

        # ================= FOOTER =================

        self.footer = ctk.CTkLabel(
            self,
            text="Made with ❤️ by Siddharth",
            text_color="gray60",
            font=("Segoe UI", 11)
        )

        self.footer.pack(
            pady=10
        )

    # ==================================================

    def update_users(self, users):

        self.count.configure(
            text=f"🟢 Online Users ({len(users)})"
        )

        for widget in self.user_frame.winfo_children():
            widget.destroy()

        for user in sorted(users):

            card = ctk.CTkFrame(
                self.user_frame,
                fg_color="#1F2937",
                corner_radius=15,
                height=55
            )

            card.pack(
                fill="x",
                padx=5,
                pady=5
            )

            avatar = ctk.CTkLabel(
                card,
                text="👤",
                font=("Segoe UI Emoji", 22)
            )

            avatar.pack(
                side="left",
                padx=(12, 8)
            )

            info = ctk.CTkFrame(
                card,
                fg_color="transparent"
            )

            info.pack(
                side="left",
                fill="both",
                expand=True
            )

            name = ctk.CTkLabel(
                info,
                text=user,
                anchor="w",
                font=("Segoe UI", 14, "bold")
            )

            name.pack(
                anchor="w"
            )

            subtitle = ctk.CTkLabel(
                info,
                text="Online",
                text_color="#7CFC00",
                anchor="w",
                font=("Segoe UI", 11)
            )

            subtitle.pack(
                anchor="w"
            )

            status = ctk.CTkLabel(
                card,
                text="🟢",
                font=("Segoe UI", 16)
            )

            status.pack(
                side="right",
                padx=12
            )