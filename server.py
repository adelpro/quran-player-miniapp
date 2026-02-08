#!/usr/bin/env python3
"""
Simple HTTP server for Quran Player Mini App
Run: python3 server.py
Access: http://localhost:8080
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

PORT = 8080

class MyHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = HTTPServer(('0.0.0.0', PORT), MyHandler)
    print(f"🎵 Quran Player Mini App")
    print(f"   URL: http://localhost:{PORT}")
    print(f"   Press Ctrl+C to stop")
    server.serve_forever()
