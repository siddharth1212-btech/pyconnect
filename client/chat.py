import socket
import threading
import json

import customtkinter as ctk

from client.components.sidebar import Sidebar
from client.components.header import Header
from client.components.chat_bubble import ChatBubble
from client.components.typing_indicator import TypingIndicator
from client.components.emoji_picker import EmojiPicker
from client.components.file_picker import pick_image

HOST = "127.0.0.1"
PORT = 5555


class ChatScreen(ctk.CTkFrame):

    def __init__(self, parent, username):

        super().__init__(parent)

        self.username = username

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))
        self.client.send(username.encode())

        self.configure(fg_color="#0D1117")

        self.pack(fill="both", expand=True)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.message.bind("<KeyRelease>", self.on_typing)
        self.message.bind("<FocusOut>", lambda e: self.stop_typing())
        self.message.bind("<Return>", self.send_message)

        # ================= SIDEBAR =================

        self.sidebar = Sidebar(self)

        self.sidebar.grid(
            row=0,
            column=0,
            rowspan=4,
            sticky="ns"
        )

        # ================= HEADER =================

        self.header = Header(
            self,
            username
        )

        self.header.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=10,
            pady=(10, 0)
        )

        # ================= TYPING =================

        self.typing = TypingIndicator(self)

        self.typing.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=12,
            pady=(5, 0)
        )

        # ================= CHAT =================

        self.chat_box = ctk.CTkTextbox(
            self,
            wrap="word",
            state="disabled",
            fg_color="#0B0F15",
            border_width=0,
            font=("Segoe UI", 14)
        )

        self.chat_box.grid(
            row=2,
            column=1,
            sticky="nsew",
            padx=10,
            pady=10
        )

        # ================= INPUT =================

        self.bottom = ctk.CTkFrame(
            self,
            fg_color="#161B22",
            height=70
        )

        self.bottom.grid(
            row=3,
            column=1,
            sticky="ew",
            padx=10,
            pady=(0, 10)
        )

        self.bottom.grid_columnconfigure(0, weight=1)

        self.message = ctk.CTkEntry(
            self.bottom,
            height=45,
            placeholder_text="Type your message..."
        )

        self.message.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(20, 10),
            pady=15
        )

        self.message.bind(
            "<Return>",
            self.send_message
        )

        self.emoji_btn = ctk.CTkButton(
            self.bottom,
            text="😀",
            width=45,
            command=self.open_emoji
        )

        self.emoji_btn.grid(
            row=0,
            column=1,
            padx=(0, 8),
            pady=15
        )

        self.image_btn = ctk.CTkButton(
            self.bottom,
            text="📷",
            width=45,
            command=self.send_image
        )

        self.image_btn.grid(
            row=0,
            column=2,
            padx=(0, 8),
            pady=15
        )

        self.send_btn = ctk.CTkButton(
            self.bottom,
            text="Send",
            width=120,
            command=self.send_message
        )

        self.send_btn.grid(
            row=0,
            column=3,
            padx=(0, 20),
            pady=15
        )

        threading.Thread(
            target=self.receive_messages,
            daemon=True
        ).start()
        # ================= RECEIVE =================

    def receive_messages(self):

        while True:

            try:

                data = self.client.recv(4096)

                if not data:
                    break

                packet = json.loads(
                    data.decode()
                )

                packet_type = packet.get("type")

                if packet_type == "message":

                    self.after(
                        0,
                        lambda t=packet["text"]: self.add_message(t)
                    )

                elif packet_type == "users":

                    self.after(
                        0,
                        lambda u=packet["users"]: self.update_users(u)
                    )

                elif packet_type == "typing":

                    sender = packet.get("user")

                    if sender != self.username:

                        self.after(
                            0,
                            lambda s=sender: self.typing.show(s)
                        )

                elif packet_type == "stop_typing":

                    self.after(
                        0,
                        self.typing.hide
                    )

            except Exception:

                break

    # ================= USERS =================

    def update_users(self, users):

        self.sidebar.update_users(users)

    # ================= CHAT =================

    def add_message(self, text):

        self.chat_box.configure(
            state="normal"
        )

        me = text.startswith(
            f"{self.username}:"
        )

        bubble = ChatBubble(
            self.chat_box,
            text,
            me
        )

        self.chat_box.window_create(
            "end",
            window=bubble
        )

        self.chat_box.insert(
            "end",
            "\n"
        )

        self.chat_box.configure(
            state="disabled"
        )

        self.chat_box.see("end")
        # ================= SEND =================

    def send_message(self, event=None):

        msg = self.message.get().strip()

        if not msg:
            return

        packet = {

            "type": "message",

            "text": f"{self.username}: {msg}"

        }

        try:

            self.client.send(
                json.dumps(packet).encode()
            )

        except Exception:

            self.add_message(
                "❌ Unable to send message."
            )

            return

        self.message.delete(
            0,
            "end"
        )

    # ================= EMOJI =================

    def open_emoji(self):

        EmojiPicker(
            self,
            self.insert_emoji
        )

    def insert_emoji(self, emoji):

        self.message.insert(
            "end",
            emoji
        )

    # ================= IMAGE =================

    def send_image(self):

        path = pick_image()

        if not path:
            return

        packet = {

            "type": "message",

            "text": f"{self.username}: 📷 {path}"

        }

        try:

            self.client.send(
                json.dumps(packet).encode()
            )

        except Exception:

            self.add_message(
                "❌ Failed to send image."
            )
            # ================= TYPING =================

    def send_typing(self):

        try:

            packet = {

                "type": "typing",

                "user": self.username

            }

            self.client.send(
                json.dumps(packet).encode()
            )

        except:

            pass

    def stop_typing(self):

        try:

            packet = {

                "type": "stop_typing",

                "user": self.username

            }

            self.client.send(
                json.dumps(packet).encode()
            )

        except:

            pass

    # ================= DISCONNECT =================

    def disconnect(self):

        try:

            self.stop_typing()

            self.client.close()

        except:

            pass

    # ================= CLOSE =================

    def destroy(self):

        self.disconnect()

        super().destroy()


    # ================= TYPING EVENTS =================

    def on_typing(self, event=None):

        text = self.message.get().strip()

        if text == "":

            self.stop_typing()

        else:

            self.send_typing()

    # ================= CLEAR CHAT =================

    def clear_chat(self):

        self.chat_box.configure(
            state="normal"
        )

        self.chat_box.delete(
            "1.0",
            "end"
        )

        self.chat_box.configure(
            state="disabled"
        )

    # ================= SYSTEM MESSAGE =================

    def system_message(self, text):

        self.add_message(
            f"⚙ {text}"
        )

    # ================= CONNECTION LOST =================

    def connection_lost(self):

        self.system_message(
            "Connection Lost."
        )

        try:

            self.client.close()

        except:

            pass

    # ================= RECONNECT =================

    def reconnect(self):

        try:

            self.client = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            self.client.connect(
                (HOST, PORT)
            )

            self.client.send(
                self.username.encode()
            )

            threading.Thread(
                target=self.receive_messages,
                daemon=True
            ).start()

            self.system_message(
                "Reconnected Successfully."
            )

        except:

            self.system_message(
                "Unable To Reconnect."
            )