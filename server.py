# -*- coding: utf-8 -*-

import argparse
import os
from configparser import ConfigParser
from http.server import BaseHTTPRequestHandler, HTTPServer

from logger import RequestLogger

# Load configuration
CONFIG_FILE = "server_config.ini"


def load_config():
    config = ConfigParser()
    if os.path.exists(CONFIG_FILE):
        config.read(CONFIG_FILE)
    else:
        config["server"] = {
            "port": "8080",
            "log_format": "human",
            "log_file": "requests.log",
            "log_to_file": "true"
        }
        with open(CONFIG_FILE, "w") as f:
            config.write(f)
    return config


config = load_config()
LOG_FORMAT = config.get("server", "log_format", fallback="human")
LOG_FILE = config.get("server", "log_file", fallback="requests.log")
LOG_TO_FILE = config.getboolean("server", "log_to_file", fallback=True)


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.handle_request()

    def do_POST(self):
        self.handle_request()

    def do_PUT(self):
        self.handle_request()

    def do_DELETE(self):
        self.handle_request()

    def do_PATCH(self):
        self.handle_request()

    def handle_request(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8') if content_length > 0 else None

        # Get protocol version and server address
        protocol_version = self.request_version
        server_address = f"{self.server.server_address[0]}:{self.server.server_address[1]}"

        # Log request
        logger.log_request(self.command, self.path, self.headers, body, self.client_address, protocol_version, server_address)

        # Respond with 200 OK
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple HTTP Request Logger Server")
    parser.add_argument("--port", type=int, help="Port to listen on. Default is 8080.",
                        default=int(config.get("server", "port", fallback=8080)))
    parser.add_argument("--log-format", type=str, help="The format to log requests in. Options are 'human', 'http', and 'curl'.",
                        default=str(config.get("server", "log_format", fallback='human')))
    args = parser.parse_args()

    # Override with CLI value
    LOG_FORMAT = args.log_format

    # Initialize logger
    logger = RequestLogger(LOG_FORMAT, LOG_FILE, LOG_TO_FILE)

    server_address = ('', args.port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Server started on port {args.port}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, shutting down the server.")
        httpd.server_close()
