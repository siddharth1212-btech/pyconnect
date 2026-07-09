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
        self.server.listen()

        self.clients = []
        self.usernames = []

        print(f"Server Running : {HOST}:{PORT}")

    def send_packet(self, client, packet):

        try:
            client.send(json.dumps(packet).encode())
        except:
            pass

    def broadcast(self, packet):

        for client in self.clients:
            self.send_packet(client, packet)

    def update_users(self):

        packet = {
            "type": "users",
            "users": self.usernames
        }

        self.broadcast(packet)

    def remove_client(self, client):

        if client in self.clients:

            index = self.clients.index(client)

            username = self.usernames[index]

            self.clients.pop(index)
            self.usernames.pop(index)

            self.broadcast({
                "type": "message",
                "text": f"🔴 {username} left the chat"
            })

            self.update_users()

            client.close()

    def handle(self, client):

        while True:

            try:

                data = client.recv(4096)

                if not data:
                    break

                packet = json.loads(data.decode())

                self.broadcast(packet)

            except:
                break

        self.remove_client(client)

    def start(self):

        while True:

            client, address = self.server.accept()

            username = client.recv(1024).decode()

            self.clients.append(client)
            self.usernames.append(username)

            print(f"{username} Connected : {address}")

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