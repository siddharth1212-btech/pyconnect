from server.socket_handler import SocketServer


def main():

    print("=" * 55)
    print("        🚀 Welcome To PyConnect Server")
    print("=" * 55)

    server = SocketServer()

    try:

        server.start()

    except KeyboardInterrupt:

        print("\n🛑 Server Stopped Successfully.")

    except Exception as e:

        print(f"\n❌ Server Error : {e}")


if __name__ == "__main__":
    main()