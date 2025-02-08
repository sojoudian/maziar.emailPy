import http.server

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="templates", **kwargs)

    def do_GET(self):
        if self.path == "/":
            self.path = "index.html"
        return super().do_GET()

class CustomHTTPServer(http.server.ThreadingHTTPServer):
    def __init__(self, server_address, RequestHandlerClass):
        super().__init__(server_address, RequestHandlerClass)

def run(server_class=CustomHTTPServer, handler_class=CustomHTTPRequestHandler, port=8002):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

