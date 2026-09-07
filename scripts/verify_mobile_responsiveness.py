import subprocess
import os
import time
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8771

def start_server():
    server = HTTPServer(("127.0.0.1", PORT), SimpleHTTPRequestHandler)
    server.serve_forever()

server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()
time.sleep(1)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def test_viewport(url, width=390, height=844):
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--window-size={width},{height}",
        "--dump-dom",
        url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    return res.stdout

print("Mobile test runner ready on port", PORT)
