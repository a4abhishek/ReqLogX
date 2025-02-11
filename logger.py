# -*- coding: utf-8 -*-

import json
import logging


class RequestLogger:
    def __init__(self, log_format="human", log_file="requests.log", log_to_file=True):
        self.log_format = log_format
        self.log_file = log_file
        self.log_to_file = log_to_file

        self.logger = logging.getLogger("RequestLogger")
        self.logger.setLevel(logging.INFO)

        # Set up stream handler with UTF-8 encoding
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(logging.Formatter("%(message)s"))
        stream_handler.stream = open(1, 'w', encoding='utf-8')  # stdout with UTF-8 encoding
        self.logger.addHandler(stream_handler)

        if log_to_file:
            # Set up file handler with UTF-8 encoding
            file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
            file_handler.setFormatter(logging.Formatter("%(message)s"))
            self.logger.addHandler(file_handler)

    def log_request(self, method, path, headers, body, client_address, protocol_version, server_address):
        if self.log_format == "human":
            log_message = self._format_human(method, path, headers, body, client_address)
        elif self.log_format == "http":
            log_message = self._format_http(method, path, headers, body, protocol_version)
        elif self.log_format == "curl":
            log_message = self._format_curl(method, path, headers, body, server_address)
        else:
            log_message = f"Unknown log format: {self.log_format}"

        self.logger.info(log_message)

    def _format_human(self, method, path, headers, body, client_address):
        return f"""
📌 Request from {client_address[0]}:{client_address[1]}
📝 Method: {method}
🔗 Path: {path}
📜 Headers:
{json.dumps(dict(headers), indent=2)}
📦 Body: {body or "None"}
{"-" * 50}
"""

    def _format_http(self, method, path, headers, body, protocol_version):
        formatted_headers = "\n".join(f"{key}: {value}" for key, value in headers.items())
        return f"""{method} {path} {protocol_version}
{formatted_headers}

{body or ""}
"""

    def _format_curl(self, method, path, headers, body, server_address):
        header_str = " ".join([f"-H '{key}: {value}'" for key, value in headers.items()])
        body_str = f"--data '{body}'" if body else ""
        return f"curl -X {method} {header_str} {body_str} 'http://{server_address}{path}'"
