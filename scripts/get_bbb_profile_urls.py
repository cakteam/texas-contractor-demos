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

all_items = []

for cat in categories:
    url = f"https://www.bbb.org/search?find_country=USA&find_text={cat['term']}&find_loc={cat['loc'].replace(' ', '+')}"
    print(f"Fetching BBB search for {cat['term']} in {cat['loc']}...")
    try:
        r = httpx.get(url, headers=headers, timeout=20, follow_redirects=True)
        if r.status_code == 200:
            # find itemListElement
            matches = re.findall(r'\{"@type":"ListItem","position":\d+,"item":(\{.*?\})\}(?=,\{"@type":"ListItem"|\])', r.text)
            print(f"  -> Found {len(matches)} schema.org items")
            for m in matches:
                try:
                    item_data = json.loads(m)
                    all_items.append({
                        "category": cat["term"],
                        "search_loc": cat["loc"],
                        "name": re.sub(r'<[^>]+>', '', item_data.get("name", "")),
                        "phone": item_data.get("telephone", ""),
                        "bbb_profile_url": item_data.get("url", ""),
                        "address": item_data.get("address", {}).get("streetAddress", ""),
                        "city": item_data.get("address", {}).get("addressLocality", ""),
                        "state": item_data.get("address", {}).get("addressRegion", ""),
                        "zip": item_data.get("address", {}).get("postalCode", "")
                    })
                except Exception as je:
                    pass
    except Exception as e:
        print(f"Error: {e}")

print(f"Extracted {len(all_items)} total businesses with direct BBB profile URLs.")
with open("bbb_profiles_raw.json", "w", encoding="utf-8") as f:
    json.dump(all_items, f, indent=2)
