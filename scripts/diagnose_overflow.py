import subprocess
import os
import json
import time
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8770
server = HTTPServer(('127.0.0.1', PORT), SimpleHTTPRequestHandler)
t = threading.Thread(target=server.serve_forever, daemon=True)
t.start()
time.sleep(1)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# We can run headless chrome with remote debugging or a small script
# Let's inspect the files directly and test fixes
demos = [
    "03_DEMOS/01_good_roots_roofing/index.html",
    "03_DEMOS/02_a_matt_tree_service/index.html",
    "03_DEMOS/03_dapco_garage_door/index.html"
]

print("Ready to diagnose.")
