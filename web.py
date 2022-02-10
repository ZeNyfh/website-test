from http.server import BaseHTTPRequestHandler, HTTPServer
import time

class web_server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.path = '//home//zhotrod//Desktop//website//main.html'
        try:
            file_to_open = open(self.path[1:]).read() # reads the file
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer(("192.168.1.157", 80), web_server)
httpd.serve_forever()