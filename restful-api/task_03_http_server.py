#!/usr/bin/python3

"""
HTTP Server
"""

from json import dumps
import http.server


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Docstring for do_GET

        :param self: Self object
        """
        match self.path:
            case '/':
                text = "Hello, this is a simple API!"

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(text, "utf-8"))

            case '/data':
                data = {"name": "John", "age": 30, "city": "New York"}

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(bytes(dumps(data), "utf-8"))

            case '/status':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes("OK", "utf-8"))

            case '/info':
                info = {
                    "version": "1.0",
                    "description": "A simple API built with http.server"
                }

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(bytes(dumps(info), "utf-8"))

            case _:
                self.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(bytes("", "utf-8"))


httpd = http.server.HTTPServer(('127.0.0.1', 8000), Handler)
httpd.serve_forever()
