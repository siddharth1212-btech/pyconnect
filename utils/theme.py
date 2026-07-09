import customtkinter as ctk

# ================= COLORS =================

BACKGROUND = "#0D1117"
CARD = "#161B22"
SIDEBAR = "#111827"

PRIMARY = "#2563EB"
SECONDARY = "#1F2937"

SUCCESS = "#22C55E"
ERROR = "#EF4444"
WARNING = "#F59E0B"

TEXT = "#FFFFFF"
SUBTEXT = "#9CA3AF"

# ================= FONTS =================

TITLE_FONT = ("Segoe UI", 28, "bold")
HEADER_FONT = ("Segoe UI", 22, "bold")
SUBTITLE_FONT = ("Segoe UI", 16)
BODY_FONT = ("Segoe UI", 14)
SMALL_FONT = ("Segoe UI", 11)

# ================= BUTTON =================

BUTTON_HEIGHT = 45
BUTTON_RADIUS = 10

# ================= ENTRY =================

ENTRY_HEIGHT = 45

# ================= WINDOW =================

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 850


# ================= APPLY THEME =================

def apply_theme():

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")