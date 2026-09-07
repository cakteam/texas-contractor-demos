import httpx
import re

candidates = [
    {"name": "Chandler Roofing & Construction", "url": "https://chandlerroofing.com"},
    {"name": "A. Matt Tree Service", "url": "https://amatt-treeservice.com"},
    {"name": "Uncle Bob's Garage Door Service", "url": "https://unclebobsgaragedoorservice.com"},
    {"name": "Good Roots Roofing & Construction", "url": "https://goodrootsroofing.com"},
    {"name": "Dapco Door", "url": "https://dapcodoor.com"},
    {"name": "S&B Roofing & Exteriors", "url": "https://sbroofing.com"}
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

for c in candidates:
    print(f"\n==========================================")
    print(f"Candidate: {c['name']} ({c['url']})")
    print(f"==========================================")
    try:
        r = httpx.get(c['url'], headers=headers, timeout=12, follow_redirects=True, verify=False)
        print(f"Status: {r.status_code}, Final URL: {r.url}, Size: {len(r.text)} bytes")
        
        # Strip scripts and styles
        clean = re.sub(r'<script[\s\S]*?</script>', '', r.text, flags=re.IGNORECASE)
        clean = re.sub(r'<style[\s\S]*?</style>', '', clean, flags=re.IGNORECASE)
        
        title_m = re.search(r'<title>([\s\S]*?)</title>', r.text, re.IGNORECASE)
        print("Title:", title_m.group(1).strip() if title_m else "None")
        
        # Extract headings
        h1s = re.findall(r'<h1[^>]*>([\s\S]*?)</h1>', clean, re.IGNORECASE)
        h2s = re.findall(r'<h2[^>]*>([\s\S]*?)</h2>', clean, re.IGNORECASE)
        print("H1s:", [re.sub(r'<[^>]+>', '', h).strip() for h in h1s[:3]])
        print("H2s:", [re.sub(r'<[^>]+>', '', h).strip() for h in h2s[:5]])
        
        # Extract text preview
        plain_text = re.sub(r'<[^>]+>', ' ', clean)
        plain_text = re.sub(r'\s+', ' ', plain_text).strip()
        print("Text snippet (first 400 chars):")
        print(plain_text[:400])
    except Exception as e:
        print(f"Error fetching {c['name']}: {e}")
