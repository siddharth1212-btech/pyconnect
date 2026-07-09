import socket
import threading
import json

import customtkinter as ctk
from client.components.message_bubble import MessageBubble
from client.components.header import Header
from client.components.sidebar import Sidebar
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

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # ================= SIDEBAR =================

        self.sidebar = Sidebar(self)

        self.sidebar.grid(
            row=0,
            column=0,
            rowspan=3,
            sticky="ns"
        )

        ctk.CTkLabel(
            self.sidebar,
            text="💬 PyConnect",
            font=("Segoe UI",24,"bold")
        ).pack(pady=(25,15))

        ctk.CTkLabel(
            self.sidebar,
            text="ONLINE USERS",
            font=("Segoe UI",14,"bold"),
            text_color="gray80"
        ).pack()

        self.users = ctk.CTkScrollableFrame(
            self.sidebar,
            width=220,
            height=600
        )

        self.users.pack(
            padx=15,
            pady=15,
            fill="both",
            expand=True
        )

        # ================= HEADER =================

        self.header = Header(
            self,
            self.username
        )

        self.header.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=10,
            pady=(10,0)
        )

        ctk.CTkLabel(
            self.header,
            text=f"General Chat  |  {username}",
            font=("Segoe UI",20,"bold")
        ).pack(
            side="left",
            padx=20,
            pady=18
        )
        self.typing = TypingIndicator(self)

        self.typing.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=15,
            pady=(0, 5)
)

        # ================= CHAT =================

        self.chat_box = ctk.CTkTextbox(
            self,
            state="disabled",
            wrap="word",
            font=("Consolas",14)
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
            height=70,
            fg_color="#161B22"
        )

        self.bottom.grid(
            row=3,
            column=1,
            sticky="ew",
            padx=10,
            pady=(0,10)
        )

        self.bottom.grid_columnconfigure(0, weight=1)

        self.message = ctk.CTkEntry(
            self.bottom,
            placeholder_text="Type a message...",
            height=45
        )

        self.message.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(20,10),
            pady=15
        )


        self.message.bind("<Return>", self.send_message)

        self.emoji_btn = ctk.CTkButton(
        self.bottom,
            text="😀",
            width=45,
            command=self.open_emoji
        )

        self.emoji_btn.grid(
            row=0,
            column=1,
            padx=(0,8),
            pady=15
        )
        self.image_btn = ctk.CTkButton(self.bottom,text="📷",width=45,command=self.send_image)

        self.image_btn.grid(row=0,column=2,padx=(0,8),pady=15)

        self.send_btn = ctk.CTkButton(self.bottom, text="Send", width=120, command=self.send_message)

        self.send_btn.grid(row=0,column=3,padx=(0,20),pady=15)

        threading.Thread(target=self.receive_messages,daemon=True).start()
            # ================= RECEIVE =================

    def receive_messages(self):

        while True:

            try:

                data = self.client.recv(4096)

                if not data:
                    break

                packet = json.loads(data.decode())

                if packet["type"] == "message":

                    self.after(
                        0,
                        lambda t=packet["text"]: self.add_message(t)
                    )

                elif packet["type"] == "users":

                    self.after(
                        0,
                        lambda u=packet["users"]: self.update_users(u)
                    )

            except Exception:

                break

    # ================= USERS =================

    def update_users(self, users):

        self.sidebar.update_users(users)

        for widget in self.users.winfo_children():
            widget.destroy()

        for user in users:

            if user == self.username:
                text = f"🟢 {user} (You)"
            else:
                text = f"🟢 {user}"

            lbl = ctk.CTkLabel(
                self.users,
                text=text,
                anchor="w",
                font=("Segoe UI",14)
            )

            lbl.pack(
                fill="x",
                padx=8,
                pady=5
            )

    # ================= CHAT =================

    def add_message(self, text):

        self.chat_box.configure(state="normal")

        me = text.startswith(f"{self.username}:")

        bubble = ChatBubble(
            self.chat_box,
            text,
            me
        )

        self.chat_box.window_create(
            "end",
            window=bubble
        ) 

        self.chat_box.insert("end", "\n")

        self.chat_box.configure(state="disabled")

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
            self.add_message("❌ Unable to send message.")
            return

        self.message.delete(0, "end")

    # ================= DISCONNECT =================

        # ================= DISCONNECT =================

    def disconnect(self):

        try:
            self.client.close()
        except:
            pass

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

        self.client.send(
            json.dumps(packet).encode()
        )