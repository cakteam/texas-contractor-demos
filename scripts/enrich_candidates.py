import json
import httpx
import re
import time

with open("bbb_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

print(f"Loaded {len(candidates)} candidates.")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

# Let's inspect the first 25 candidates across categories
sample = []
categories_seen = {}
for c in candidates:
    cat = c["category"]
    categories_seen[cat] = categories_seen.get(cat, 0) + 1
    if categories_seen[cat] <= 5: # take 5 from each category = 25 total
        sample.append(c)

print(f"Selected sample of {len(sample)} candidates for enrichment.")

enriched = []

for idx, c in enumerate(sample):
    name = c["name"]
    bbb_url = c.get("bbb_url")
    print(f"\n[{idx+1}/{len(sample)}] Enriching {name} ({c['category']})...")
    
    # If bbb_url is missing, construct or skip
    data = {**c}
    if bbb_url:
        try:
            r = httpx.get(bbb_url, headers=headers, timeout=15, follow_redirects=True)
            if r.status_code == 200:
                html_text = r.text
                
                # Look for website link
                # BBB usually has a link like <a class="...dtm-url..." href="https://..."> or "Find Web Address"
                web_matches = re.findall(r'href="(https?://[^"]+)"[^>]*data-typeahead="website"|class="[^"]*dtm-url[^"]*"[^>]*href="([^"]+)"', html_text)
                website = None
                for m in web_matches:
                    url = m[0] or m[1]
                    if "bbb.org" not in url and "google.com" not in url:
                        website = url
                        break
                
                # If regex didn't catch, search for standard website links
                if not website:
                    all_external = re.findall(r'<a[^>]+href="(https?://(?!www\.bbb\.org)[^"]+)"[^>]*>Visit Website</a>', html_text, re.IGNORECASE)
                    if all_external:
                        website = all_external[0]

                # Years in business
                years_match = re.search(r'Years in Business:\s*</span>\s*<span[^>]*>(\d+)', html_text)
                if not years_match:
                    years_match = re.search(r'(\d+)\s*years in business', html_text, re.IGNORECASE)
                years_in_business = years_match.group(1) if years_match else "Unknown"

                # Address
                addr_match = re.search(r'<p class="[^"]*address[^"]*">([\s\S]*?)</p>', html_text)
                address = re.sub(r'<[^>]+>', ' ', addr_match.group(1)).strip() if addr_match else ""

                data["website"] = website
                data["years_in_business"] = years_in_business
                data["address"] = address
                print(f"  Website: {website}")
                print(f"  Years: {years_in_business}")
            else:
                print(f"  BBB profile HTTP {r.status_code}")
        except Exception as e:
            print(f"  Error fetching BBB profile: {e}")

    # If website found, check website health
    web_url = data.get("website")
    data["website_status"] = "No Website"
    if web_url:
        try:
            wr = httpx.get(web_url, headers=headers, timeout=10, follow_redirects=True, verify=False)
            data["website_status_code"] = wr.status_code
            data["website_final_url"] = str(wr.url)
            
            # Check title and meta
            title_m = re.search(r'<title>([\s\S]*?)</title>', wr.text, re.IGNORECASE)
            data["website_title"] = title_m.group(1).strip() if title_m else ""
            
            # Viewport check
            has_viewport = bool(re.search(r'<meta[^>]+viewport', wr.text, re.IGNORECASE))
            data["has_viewport"] = has_viewport
            
            # Form check
            has_form = bool(re.search(r'<form', wr.text, re.IGNORECASE))
            data["has_form"] = has_form

            # Tel link check
            has_tel = bool(re.search(r'href=["\']tel:', wr.text, re.IGNORECASE))
            data["has_tel"] = has_tel

            data["page_size_bytes"] = len(wr.text)
            data["website_status"] = "Active"
            print(f"  Website check: Status {wr.status_code}, Title: '{data['website_title'][:40]}', Viewport: {has_viewport}, Tel: {has_tel}")
        except Exception as we:
            data["website_status"] = f"Failed/Broken ({str(we)[:40]})"
            print(f"  Website check failed: {we}")

    enriched.append(data)
    time.sleep(0.5)

with open("enriched_candidates.json", "w", encoding="utf-8") as f:
    json.dump(enriched, f, indent=2)

print("\nEnrichment complete! Saved to enriched_candidates.json")
