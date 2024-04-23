from http.server import SimpleHTTPRequestHandler
import socketserver

PORT: int = 9000
Handler = SimpleHTTPRequestHandler

server = socketserver.TCPServer(("", PORT), Handler)


def Listen() -> str:
    print("Starting Server...")
    print(f"Listening on the port: {PORT}\n")
    return server.handle_request()


def StopListen() -> str:
    print("Closing Listener...")
    return server.shutdown()
