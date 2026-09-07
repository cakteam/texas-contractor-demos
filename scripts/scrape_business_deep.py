import httpx
import re
import json

urls = {
    "goodroots": "https://goodrootsroofing.com",
    "amatt": "https://amatt-treeservice.com",
    "dapco": "https://www.dapcodoor.com"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

details = {}

for key, url in urls.items():
    print(f"Fetching {key} -> {url}...")
    try:
        r = httpx.get(url, headers=headers, follow_redirects=True, timeout=15, verify=False)
        html = r.text
        
        # Extract images
        imgs = re.findall(r'<img[^>]+src=["\'](.*?)["\']', html, re.IGNORECASE)
        # Extract links
        links = re.findall(r'<a[^>]+href=["\'](.*?)["\'][^>]*>(.*?)</a>', html, re.IGNORECASE)
        
        # Clean text
        clean = re.sub(r'<script[\s\S]*?</script>', '', html, flags=re.IGNORECASE)
        clean = re.sub(r'<style[\s\S]*?</style>', '', clean, flags=re.IGNORECASE)
        clean = re.sub(r'<[^>]+>', '\n', clean)
        lines = [l.strip() for l in clean.split('\n') if l.strip() and len(l.strip()) > 3]
        
        details[key] = {
            "url": url,
            "status": r.status_code,
            "images": imgs[:15],
            "text_lines": lines[:120]
        }
    except Exception as e:
        print(f"Error {key}: {e}")

with open("top3_scraped_details.json", "w", encoding="utf-8") as f:
    json.dump(details, f, indent=2)

print("Saved top3_scraped_details.json")
