import http.server
import socketserver

# Set the directory you want to serve files from
directory = '.'  # This represents the current directory

# Set the port you want the server to run on
port = 8080

# Create a handler to serve files
handler = http.server.SimpleHTTPRequestHandler

# Create the server
httpd = socketserver.TCPServer(("", port), handler)

print(f"Serving on port {port} from directory {directory}")

# Start the server
httpd.serve_forever()
