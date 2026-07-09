from server.socket_handler import SocketServer

def main():

    server = SocketServer()

    server.start()


if __name__ == "__main__":
    main()