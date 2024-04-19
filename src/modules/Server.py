from http.server import SimpleHTTPRequestHandler
import socketserver

PORT: int = 9000
Handler = SimpleHTTPRequestHandler

server = socketserver.TCPServer(("", PORT), Handler)


def Listen() -> str:
    print("Starting Server...")
    print(f"Listening on the port: {PORT}\n")
    return server.handle_request()


def ServerClose() -> None:
    try:
        server.shutdown_request()
        return f"Port {PORT} Listener closed succesfully..."
    except:
        return f"Could not close the Port {PORT} Listener..."

