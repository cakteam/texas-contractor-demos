import httpx
import json
import re

categories = [
    {"term": "roofing", "loc": "Fort Worth, TX"},
    {"term": "air-conditioning", "loc": "Plano, TX"},
    {"term": "garage-door-repair", "loc": "Arlington, TX"},
    {"term": "foundation-repair", "loc": "Dallas, TX"},
    {"term": "tree-service", "loc": "Fort Worth, TX"}
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

all_found = []

for cat in categories:
    url = f"https://www.bbb.org/search?find_country=USA&find_text={cat['term']}&find_loc={cat['loc'].replace(' ', '+')}"
    print(f"Fetching {cat['term']} in {cat['loc']}...")
    try:
        r = httpx.get(url, headers=headers, timeout=20, follow_redirects=True)
        if r.status_code == 200:
            # find results in webDigitalData
            match = re.search(r'"results":(\[.*?\])\s*,\s*"used_type_aheads"', r.text)
            if match:
                results_json = json.loads(match.group(1))
                print(f"  -> Found {len(results_json)} businesses in JSON data")
                for item in results_json:
                    all_found.append({
                        "category": cat['term'],
                        "search_loc": cat['loc'],
                        "name": item.get("business_name"),
                        "phone": item.get("business_phone"),
                        "rating": item.get("business_rating"),
                        "zip": item.get("zip_code"),
                        "bbb_id": item.get("business_id"),
                        "bbb_url": item.get("url")
                    })
            else:
                print("  -> Could not extract results JSON")
        else:
            print(f"  -> HTTP {r.status_code}")
    except Exception as e:
        print(f"  -> Error: {e}")

print(f"\nTotal businesses extracted: {len(all_found)}")
with open("bbb_candidates.json", "w", encoding="utf-8") as f:
    json.dump(all_found, f, indent=2)
