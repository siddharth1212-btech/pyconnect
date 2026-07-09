import customtkinter as ctk


class SplashScreen(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent, fg_color="#0D1117")

        self.pack(fill="both", expand=True)

        # Logo
        logo = ctk.CTkLabel(
            self,
            text="💬",
            font=("Segoe UI Emoji", 80)
        )

        logo.pack(pady=(90, 15))

        # Title
        title = ctk.CTkLabel(
            self,
            text="PyConnect",
            font=("Segoe UI", 40, "bold"),
            text_color="#4F8CFF"
        )

        title.pack()

        # Subtitle
        subtitle = ctk.CTkLabel(
            self,
            text="Modern Real-Time Chat Application",
            font=("Segoe UI", 18),
            text_color="#C9D1D9"
        )

        subtitle.pack(pady=(10, 40))

        # Progress Bar
        self.progress = ctk.CTkProgressBar(
            self,
            width=420,
            height=10,
            progress_color="#4F8CFF"
        )

        self.progress.pack()

        self.progress.set(0)

        # Loading Text
        self.loading = ctk.CTkLabel(
            self,
            text="Loading...",
            font=("Segoe UI", 14),
            text_color="gray"
        )

        self.loading.pack(pady=20)

        self.value = 0

        self.animate()

    def animate(self):

        self.value += 0.01

        self.progress.set(self.value)

        if self.value < 1:
            self.after(20, self.animate)
        else:
            self.loading.configure(text="Ready ✔")