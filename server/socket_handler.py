import socket
import threading
import json

HOST = "127.0.0.1"
PORT = 5555


class SocketServer:

    def __init__(self):

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((HOST, PORT))
        self.server.listen(100)

        self.clients = {}
        self.lock = threading.Lock()

        print("=" * 50)
        print("🚀 PyConnect Server Started")
        print(f"🌐 Listening : {HOST}:{PORT}")
        print("=" * 50)

    # ---------------- SEND ----------------

    def send_packet(self, client, packet):

        try:
            client.send(
                json.dumps(packet).encode()
            )
        except:
            pass

    # ---------------- BROADCAST ----------------

    def broadcast(self, packet, exclude=None):

        with self.lock:

            dead = []

            for client in self.clients.keys():

                if client == exclude:
                    continue

                try:
                    self.send_packet(client, packet)

                except:
                    dead.append(client)

            for client in dead:
                self.remove_client(client)

    # ---------------- ONLINE USERS ----------------
    def update_users(self):
        print("ONLINE USERS =>", list(self.clients.values()))
        packet = {
            "type": "users",
            "users": list(self.clients.values())
        }

        self.broadcast(packet)

    # ---------------- REMOVE ----------------

    def remove_client(self, client):

        with self.lock:

            if client not in self.clients:
                return

            username = self.clients[client]

            del self.clients[client]

        print(f"❌ {username} Disconnected")

        self.broadcast({

            "type": "message",

            "text": f"🔴 {username} left the chat"

        })

        self.update_users()

        try:
            client.close()
        except:
            pass

    # ---------------- HANDLE ----------------

    def handle(self, client):

        while True:

            try:

                data = client.recv(4096)

                if not data:
                    break

                packet = json.loads(data.decode())

                if packet["type"] == "message":

                    self.broadcast(packet)

                elif packet["type"] == "typing":

                    self.broadcast(
                        packet,
                        exclude=client
                    )

            except:
                break

        self.remove_client(client)

    # ---------------- START ----------------

    def start(self):

        while True:

            client, address = self.server.accept()

            username = client.recv(1024).decode().strip()

            with self.lock:
                self.clients[client] = username

            print(f"✅ {username} Connected : {address}")

            self.broadcast({

                "type": "message",

                "text": f"🟢 {username} joined the chat"

            })

            self.update_users()

            threading.Thread(

                target=self.handle,

                args=(client,),

                daemon=True

            ).start()