import httpx
import re

sites = [
    {"name": "Hargrave Foundation Repair", "url": "https://hargraveinc.com"},
    {"name": "Texas Air Doctors", "url": "https://texasairdoctors.com"},
    {"name": "Good Roots Roofing & Construction", "url": "https://goodrootsroofing.com"},
    {"name": "A. Matt Tree Service", "url": "https://amatt-treeservice.com"},
    {"name": "Dapco Door", "url": "https://www.dapcodoor.com"},
    {"name": "Veteran Brothers Roofing", "url": "https://veteranbros.com"}
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

for s in sites:
    print(f"\n======================================")
    print(f"Site: {s['name']} -> {s['url']}")
    print(f"======================================")
    try:
        r = httpx.get(s['url'], headers=headers, follow_redirects=True, timeout=12, verify=False)
        print(f"Status: {r.status_code}, Final URL: {r.url}, Size: {len(r.text)} bytes")
        
        # Meta description
        desc_m = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']', r.text, re.IGNORECASE)
        print("Meta Description:", desc_m.group(1).strip() if desc_m else "None")
        
        # Phone
        phones = re.findall(r'(\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})', r.text)
        print("Phones found:", list(set(phones))[:4])
        
        # Clean text
        clean = re.sub(r'<script[\s\S]*?</script>', '', r.text, flags=re.IGNORECASE)
        clean = re.sub(r'<style[\s\S]*?</style>', '', clean, flags=re.IGNORECASE)
        clean = re.sub(r'<[^>]+>', ' ', clean)
        clean = re.sub(r'\s+', ' ', clean).strip()
        print("Text snippet (300 chars):", clean[:300])
    except Exception as e:
        print(f"Error: {e}")
