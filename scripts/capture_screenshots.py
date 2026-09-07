import subprocess
import os
import time
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8765

def start_server():
    server = HTTPServer(("127.0.0.1", PORT), SimpleHTTPRequestHandler)
    server.serve_forever()

# Start background local web server
server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()
print(f"Local server started on http://127.0.0.1:{PORT}")
time.sleep(1)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

demos = [
    {
        "id": "01_good_roots",
        "url": f"http://127.0.0.1:{PORT}/03_DEMOS/01_good_roots_roofing/index.html"
    },
    {
        "id": "02_a_matt",
        "url": f"http://127.0.0.1:{PORT}/03_DEMOS/02_a_matt_tree_service/index.html"
    },
    {
        "id": "03_dapco",
        "url": f"http://127.0.0.1:{PORT}/03_DEMOS/03_dapco_garage_door/index.html"
    }
]

os.makedirs("04_PREVIEWS", exist_ok=True)

for d in demos:
    d_id = d["id"]
    url = d["url"]
    
    # Desktop screenshot (1440x900)
    desktop_out = os.path.abspath(f"04_PREVIEWS/{d_id}_desktop.png")
    print(f"Capturing desktop screenshot for {d_id}...")
    cmd_desktop = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1440,960",
        f"--screenshot={desktop_out}",
        url
    ]
    subprocess.run(cmd_desktop, check=True)
    print(f"  -> Saved {desktop_out} ({os.path.getsize(desktop_out)} bytes)")

    # Mobile screenshot (390x844 - iPhone 14 / modern smartphone)
    mobile_out = os.path.abspath(f"04_PREVIEWS/{d_id}_mobile.png")
    print(f"Capturing mobile screenshot for {d_id}...")
    cmd_mobile = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=390,844",
        f"--screenshot={mobile_out}",
        url
    ]
    subprocess.run(cmd_mobile, check=True)
    print(f"  -> Saved {mobile_out} ({os.path.getsize(mobile_out)} bytes)")

print("\nAll screenshots successfully captured in 04_PREVIEWS!")
