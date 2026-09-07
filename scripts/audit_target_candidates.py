import httpx
import re
import json
import ssl

targets = [
    {"name": "Veritas Roofing", "niche": "Roofing & Storm Restoration", "city": "Fort Worth, TX", "url": "https://veritasroofingtx.com"},
    {"name": "Lon Smith Roofing & Construction", "niche": "Roofing & Storm Restoration", "city": "Fort Worth, TX", "url": "https://www.lonsmith.com"},
    {"name": "Tarrant Roofing", "niche": "Roofing & Storm Restoration", "city": "Fort Worth, TX", "url": "https://tarrantroofing.com"},
    {"name": "Veteran Brothers Roofing & Restoration", "niche": "Roofing & Storm Restoration", "city": "Fort Worth, TX", "url": "https://veteranbros.com"},
    {"name": "3:16 Roofing and Construction", "niche": "Roofing & Storm Restoration", "city": "Keller / Fort Worth, TX", "url": "https://316roofing.com"},
    {"name": "Old Pro Roofing", "niche": "Roofing & Storm Restoration", "city": "Fort Worth, TX", "url": "https://oldproroofing.com"},
    {"name": "High Pointe Roofing and Construction", "niche": "Roofing & Storm Restoration", "city": "Fort Worth, TX", "url": "https://highpointeroofing.com"},
    {"name": "S&B Roofing & Exteriors", "niche": "Roofing & Storm Restoration", "city": "Fort Worth, TX", "url": "https://sbroofing.com"},
    {"name": "A. Matt Tree Service", "niche": "Tree Removal & Arborist", "city": "Fort Worth, TX", "url": "https://amatt-treeservice.com"},
    {"name": "Integrity Tree Care", "niche": "Tree Removal & Arborist", "city": "Fort Worth, TX", "url": "https://integritytreecare.org"},
    {"name": "Texas Tree Surgeons", "niche": "Tree Removal & Arborist", "city": "Dallas / Fort Worth, TX", "url": "https://texastreesurgeons.com"},
    {"name": "Uncle Bob's Garage Door Service", "niche": "Garage Door Repair & Install", "city": "Fort Worth / Arlington, TX", "url": "https://unclebobsgaragedoorservice.com"},
    {"name": "Dapco Door", "niche": "Garage Door Repair & Install", "city": "Grand Prairie / Arlington, TX", "url": "https://dapcodoor.com"},
    {"name": "Family Christian Doors", "niche": "Garage Door Repair & Install", "city": "Arlington, TX", "url": "https://familychristiandoors.com"},
    {"name": "Garage & Gate Service Pros", "niche": "Garage Door Repair & Install", "city": "Grand Prairie, TX", "url": "https://garageservicepros.com"},
    {"name": "Garage Door Medics", "niche": "Garage Door Repair & Install", "city": "Fort Worth / Dallas, TX", "url": "https://gdmedics.com"},
    {"name": "Precision Garage Door Fort Worth", "niche": "Garage Door Repair & Install", "city": "Fort Worth, TX", "url": "https://precisiondoorfortworth.com"},
    {"name": "Structured Foundation Repairs", "niche": "Foundation Repair & Drainage", "city": "Dallas / Fort Worth, TX", "url": "https://structuredfoundation.com"},
    {"name": "Advanced Foundation Repair", "niche": "Foundation Repair & Drainage", "city": "Dallas / Fort Worth, TX", "url": "https://foundationrepairs.com"},
    {"name": "Hargrave Foundation Repair", "niche": "Foundation Repair & Drainage", "city": "Dallas / Fort Worth, TX", "url": "https://hargraveinc.com"},
    {"name": "Coolinary Arts Heating & Cooling", "niche": "HVAC & AC Repair", "city": "Dallas, TX", "url": "https://coolinaryarts.com"},
    {"name": "Total Air & Heat Co.", "niche": "HVAC & AC Repair", "city": "Plano / Dallas, TX", "url": "https://totalair.com"},
    {"name": "Texas Air Doctors", "niche": "HVAC & AC Repair", "city": "Fort Worth / Arlington, TX", "url": "https://texasairdoctors.com"},
    {"name": "Chandler Roofing & Construction", "niche": "Roofing & Storm Restoration", "city": "Fort Worth, TX", "url": "https://chandlerroofing.com"},
    {"name": "Good Roots Roofing & Construction", "niche": "Roofing & Storm Restoration", "city": "Fort Worth, TX", "url": "https://goodrootsroofing.com"},
    {"name": "Tarrant County Roofing", "niche": "Roofing & Storm Restoration", "city": "Fort Worth, TX", "url": "https://tarrantcountyroofing.com"}
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

results = []

print(f"Auditing {len(targets)} candidates...")

for t in targets:
    name = t["name"]
    url = t["url"]
    print(f"Auditing {name} ({url})...")
    audit = {
        **t,
        "reachable": False,
        "status_code": None,
        "final_url": None,
        "title": "",
        "has_viewport": False,
        "has_tel_link": False,
        "has_form": False,
        "cms_detected": "Custom/Static",
        "has_reviews_badge": False,
        "has_emergency_mention": False,
        "page_size_kb": 0,
        "issues": []
    }
    try:
        r = httpx.get(url, headers=headers, timeout=12, follow_redirects=True, verify=False)
        audit["reachable"] = True
        audit["status_code"] = r.status_code
        audit["final_url"] = str(r.url)
        audit["page_size_kb"] = round(len(r.text) / 1024, 1)
        
        html = r.text.lower()
        
        # Title
        title_m = re.search(r'<title>([\s\S]*?)</title>', r.text, re.IGNORECASE)
        audit["title"] = title_m.group(1).strip() if title_m else ""
        
        # Meta viewport
        audit["has_viewport"] = "name=\"viewport\"" in html or "name='viewport'" in html
        if not audit["has_viewport"]:
            audit["issues"].append("Missing mobile viewport tag (terrible mobile UX)")

        # Tel link
        audit["has_tel_link"] = 'href="tel:' in html or "href='tel:" in html
        if not audit["has_tel_link"]:
            audit["issues"].append("No click-to-call tel: links (friction for mobile users)")

        # Form
        audit["has_form"] = "<form" in html
        if not audit["has_form"]:
            audit["issues"].append("No lead capture / quote form on homepage")

        # CMS
        if "wp-content" in html or "wp-includes" in html:
            audit["cms_detected"] = "WordPress"
        elif "wix.com" in html or "wixsite" in html:
            audit["cms_detected"] = "Wix"
        elif "squarespace" in html:
            audit["cms_detected"] = "Squarespace"
        elif "godaddy" in html:
            audit["cms_detected"] = "GoDaddy Builder"
        elif "weebly" in html:
            audit["cms_detected"] = "Weebly"

        # Trust / Review signals
        audit["has_reviews_badge"] = any(k in html for k in ["google review", "5.0 star", "5 star", "customer reviews", "testimonials", "bbb accredited"])
        audit["has_emergency_mention"] = any(k in html for k in ["24/7", "emergency", "same day", "urgent"])

        # Check for slow/bloated or outdated tags
        if "<table" in html and "width=" in html:
            audit["issues"].append("Uses legacy HTML tables for layout")
        if "http://" in str(r.url):
            audit["issues"].append("Not enforcing HTTPS")

        print(f"  -> Reached ({r.status_code}), CMS: {audit['cms_detected']}, Viewport: {audit['has_viewport']}, Tel: {audit['has_tel_link']}, Form: {audit['has_form']}")

    except Exception as e:
        audit["reachable"] = False
        audit["issues"].append(f"Connection failed / domain issue: {str(e)[:60]}")
        print(f"  -> Failed: {e}")

    results.append(audit)

with open("audit_results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("\nAudit completed. Saved to audit_results.json")
