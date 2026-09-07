import json

with open("audit_results.json", "r", encoding="utf-8") as f:
    audits = json.load(f)

# Enhance audit results with commercial evaluation
pipeline = []
for a in audits:
    name = a["name"]
    category = a["niche"]
    url = a["url"]
    status_code = a.get("status_code")
    cms = a.get("cms_detected", "Unknown")
    issues = a.get("issues", [])
    
    # Commercial scoring & qualification
    status = "Eliminated"
    reason = ""
    
    if name == "Good Roots Roofing & Construction":
        status = "Selected - Top 3 Finalist"
        reason = "BBB Accredited (A rating), high-ticket roofing ($8k-$20k), active business in Fort Worth. Website is a catastrophic GoDaddy builder error repeating brand name 9x and slogan 8x, zero quote capture, missing images. Huge ROI upside."
    elif name == "A. Matt Tree Service":
        status = "Selected - Top 3 Finalist"
        reason = "20+ years family owned, 4.9 stars (99+ reviews), heavy equipment owner-operator. Website is stuck in 2013 on WordPress 'Tempera' with 'Comments are closed' and snow-plowing banners. High-ticket storm removal jobs ($1.5k-$6k)."
    elif name == "Dapco Door":
        status = "Selected - Top 3 Finalist"
        reason = "15+ years in business, 5.0 star Google rating, 24/7 emergency repair. Website has embarrassing public conversion leaks: main 'Reviews' nav link leads to 404 error, Facebook widget displays broken OAuth error code, H1 is raw phone number."
    elif name in ["Lon Smith Roofing & Construction", "Tarrant Roofing", "Veteran Brothers Roofing & Restoration", "Texas Tree Surgeons", "Structured Foundation Repairs"]:
        status = "Eliminated - Already Modern / Large Enterprise"
        reason = f"Company already has a mature, heavily optimized multi-page WordPress website with modern lead capture and dedicated marketing team. Hard to sell web redesign."
    elif not a.get("reachable"):
        status = "Eliminated - Inaccessible / Technical Deadlock"
        reason = f"Domain unreachable or SSL protocol violation: {issues[0] if issues else 'Connection failed'}. High risk of dormant or disconnected business."
    elif status_code == 403:
        status = "Eliminated - Cloudflare / Bot Wall"
        reason = "Site protected by heavy enterprise CDN/WAF. Not a simple local owner-operator website update."
    elif name in ["Total Air & Heat Co.", "Texas Air Doctors", "Garage Door Medics", "Precision Garage Door Fort Worth", "Advanced Foundation Repair"]:
        status = "Eliminated - Mature Regional Player"
        reason = "Established multi-location brand with full corporate marketing stack. Low owner-direct outbound conversion."
    elif name in ["3:16 Roofing and Construction", "Old Pro Roofing", "S&B Roofing & Exteriors", "Uncle Bob's Garage Door Service", "Hargrave Foundation Repair"]:
        status = "Qualified Contender - Tier 2"
        reason = "Good viable candidate with outdated layout, but Top 3 selections exhibit significantly more dramatic conversion leaks and clearer sales angles."
    else:
        status = "Eliminated - Secondary Candidate"
        reason = "Lacks urgent commercial trigger or has lower ticket size."

    pipeline.append({
        "name": name,
        "niche": category,
        "city": a["city"],
        "url": url,
        "status": status,
        "status_code": status_code,
        "cms": cms,
        "has_viewport": a.get("has_viewport"),
        "has_tel": a.get("has_tel_link"),
        "has_form": a.get("has_form"),
        "issues": issues,
        "selection_rationale": reason
    })

with open("01_CANDIDATE_RESEARCH/candidate_pipeline.json", "w", encoding="utf-8") as f:
    json.dump(pipeline, f, indent=2)

# Generate Markdown report
md_lines = [
    "# Candidate Pipeline & Screening Matrix (26 DFW Local Businesses)",
    "",
    "| Business Name | Niche & City | Website | CMS / Tech | Mobile Viewport | Click-to-Call | Status | Rationale |",
    "| :--- | :--- | :--- | :--- | :---: | :---: | :--- | :--- |"
]

for p in pipeline:
    vp = "✅" if p["has_viewport"] else "❌"
    tel = "✅" if p["has_tel"] else "❌"
    status_badge = f"**{p['status']}**" if "Selected" in p['status'] else p['status']
    md_lines.append(f"| **{p['name']}** | {p['niche']}<br>*{p['city']}* | [{p['url'].replace('https://', '')}]({p['url']}) | {p['cms']} | {vp} | {tel} | {status_badge} | {p['selection_rationale']} |")

with open("01_CANDIDATE_RESEARCH/candidate_pipeline.md", "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print("Saved candidate_pipeline.json and candidate_pipeline.md")
