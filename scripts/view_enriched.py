import json

with open("enriched_candidates.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total enriched: {len(data)}")
for i, d in enumerate(data):
    print(f"{i+1}. {d.get('name')} | Cat: {d.get('category')} | Web: {d.get('website')} | Rating: {d.get('rating')} | Phone: {d.get('phone')} | Years: {d.get('years_in_business')} | Status: {d.get('website_status')}")
