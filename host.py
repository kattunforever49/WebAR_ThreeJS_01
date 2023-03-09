import http.server
import socketserver
import sys

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    # Define custom MIME types for JavaScript module scripts
    MIME_TYPES = {
        '.js': 'application/javascript',
        '.mjs': 'application/javascript'
    }

    def guess_type(self, path):
        # Override the default MIME type guessing method to include our custom types
        base, ext = http.server.os.path.splitext(path)
        if ext in self.MIME_TYPES:
            return self.MIME_TYPES[ext]
        else:
            return super().guess_type(path)

if __name__ == "__main__":
    # Set the default port number to 8000
    PORT = 8000

    # Check if a port number was provided as a command-line argument
    if len(sys.argv) > 1:
        try:
            PORT = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using default port 8000.")

    # Start the server with our custom handler
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()
