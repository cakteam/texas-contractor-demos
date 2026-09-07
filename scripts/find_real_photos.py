import sys
import re
import urllib.parse
import httpx
from pathlib import Path

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def search_ddg_images(query, num=6):
    url = f"https://duckduckgo.com/?q={urllib.parse.quote(query)}&t=h_&iar=images&iax=images&ia=images"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    with httpx.Client(headers=headers, follow_redirects=True, timeout=10) as client:
        res = client.get(url)
        vqd_match = re.search(r'vqd=([0-9-_]+)', res.text)
        if not vqd_match:
            vqd_match = re.search(r'vqd=["\']([0-9-_]+)["\']', res.text)
        if not vqd_match:
            print(f"Failed to get vqd for {query}")
            return []
        vqd = vqd_match.group(1)
        params = {
            "l": "us-en",
            "o": "json",
            "q": query,
            "vqd": vqd,
            "f": ",,,",
            "p": "1"
        }
        api_url = "https://duckduckgo.com/i.js"
        api_res = client.get(api_url, params=params)
        data = api_res.json()
        results = []
        for r in data.get("results", []):
            results.append({
                "title": r.get("title", ""),
                "image": r.get("image", ""),
                "width": r.get("width", 0),
                "height": r.get("height", 0)
            })
            if len(results) >= num:
                break
        return results

queries = {
    "roof_before": "hail damage shingles roof close up",
    "roof_after": "new architectural asphalt shingle roof house",
    "garage_before": "old broken dented garage door house",
    "garage_after": "modern carriage house garage door residential",
    "tree_before": "fallen tree storm damage house roof yard",
    "tree_after": "clean pristine residential front yard trimmed trees"
}

out_dir = Path("scripts/test_img")
out_dir.mkdir(exist_ok=True)

for key, q in queries.items():
    print(f"\nSearching {key}: '{q}'...")
    items = search_ddg_images(q, 4)
    for i, it in enumerate(items):
        img_url = it["image"]
        print(f"  [{i}] {it['title'][:50]} | {it['width']}x{it['height']} | {img_url[:70]}...")
        # Try downloading candidate 0
        if i == 0:
            try:
                r = httpx.get(img_url, timeout=8, follow_redirects=True)
                if r.status_code == 200 and len(r.content) > 10000:
                    ext = ".jpg" if "png" not in img_url.lower() else ".png"
                    save_path = out_dir / f"{key}{ext}"
                    save_path.write_bytes(r.content)
                    print(f"      -> Successfully saved to {save_path} ({len(r.content)//1024} KB)")
            except Exception as e:
                print(f"      -> Download failed: {e}")
