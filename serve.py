#!/usr/bin/env python3
import argparse
import json
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class HomepageHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        super().end_headers()

    def do_GET(self):
        if self.path == "/health":
            body = json.dumps(
                {"ok": True, "service": "xiaowu-homepage"},
                ensure_ascii=False,
            ).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()


def main():
    parser = argparse.ArgumentParser(description="小伍个人主页静态服务")
    parser.add_argument("--port", type=int, default=4006)
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), HomepageHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
