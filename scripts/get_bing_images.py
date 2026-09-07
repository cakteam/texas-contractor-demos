import subprocess
import re
import json
import urllib.parse
import httpx
from pathlib import Path

def get_bing_images(query, count=5):
    encoded = urllib.parse.quote(query)
    url = f"https://www.bing.com/images/search?q={encoded}&first=1"
    chrome_cmd = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "--headless=new",
        "--disable-gpu",
        "--dump-dom",
        url
    ]
    try:
        proc = subprocess.run(chrome_cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore", timeout=20)
        # Bing images encode direct image URL in 'murl&quot;:&quot;(http[^&]+)&quot;'
        murls = re.findall(r'murl&quot;:&quot;(https?://[^&]+)&quot;', proc.stdout)
        clean_urls = []
        for u in murls:
            u_clean = urllib.parse.unquote(u)
            if u_clean.startswith("http") and not u_clean.endswith(".svg"):
                clean_urls.append(u_clean)
            if len(clean_urls) >= count:
                break
        return clean_urls
    except Exception as e:
        print(f"Error for {query}: {e}")
        return []

queries = {
    "goodroots_before": "hail damaged roof shingles close up",
    "goodroots_after": "new architectural shingle roof house front",
    "dapco_before": "damaged dented garage door residential",
    "dapco_after": "modern residential carriage garage door exterior",
    "amatt_tree_hazard": "storm damaged fallen tree house yard"
}

out_dir = Path("e:/GoogleAntigravity/Gmap-store/assets/images")
out_dir.mkdir(parents=True, exist_ok=True)

with httpx.Client(headers={"User-Agent": "Mozilla/5.0"}, timeout=12, follow_redirects=True) as client:
    for key, q in queries.items():
        print(f"\nSearching '{q}'...")
        urls = get_bing_images(q, count=4)
        print(f"Found {len(urls)} image URLs.")
        saved = False
        for idx, u in enumerate(urls):
            try:
                print(f"  Trying [{idx}]: {u[:80]}...")
                r = client.get(u)
                if r.status_code == 200 and len(r.content) > 20000:
                    ext = ".jpg" if "png" not in u.lower() else ".png"
                    target = out_dir / f"{key}{ext}"
                    target.write_bytes(r.content)
                    print(f"    -> SAVED {target.name} ({len(r.content)//1024} KB)")
                    saved = True
                    break
            except Exception as err:
                print(f"    Failed: {err}")
        if not saved:
            print(f"    WARNING: No image saved for {key}")
