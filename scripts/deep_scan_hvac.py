import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = [
    ('Duck AC & Heating', 'https://www.duckacandheating.com/'),
    ('Prime Time Heating & Air', 'https://www.primetime-tx.com/'),
    ('Martech HVAC', 'https://martech-hvac.com')
]

for name, u in urls:
    print(f"=== ANALYZING: {name} ===")
    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            
            # Find dummy text
            dummies = re.findall(r'(\bexample\b|\blorem\b|\b000-000|\b000\.000|\bmysite\b|\bplaceholder\b)', html, re.I)
            print("Dummy patterns found:", set(dummies))
            
            # Find about highlights
            about_matches = re.findall(r'([^.\n]*?(?:family|owner|years in business|licensed|TACLA)[^.\n]*?\.)', html, re.I)
            print("About highlights:")
            for a in about_matches[:4]:
                print("  -", a.strip()[:120])
                
            # Find all tel links
            tels = re.findall(r'href=[\'"](tel:[^\'"]+)[\'"]', html, re.I)
            print("tel: links found:", tels)
            
            # Find email links
            mailtos = re.findall(r'href=[\'"](mailto:[^\'"]+)[\'"]', html, re.I)
            print("mailto: links found:", mailtos)
            
            # Look for contact form action or email
            raw_emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', html)
            real_emails = [e for e in set(raw_emails) if not any(x in e.lower() for x in ['sentry', 'wixpress', 'png', 'jpg', 'webpack'])]
            print("Real emails found in source:", real_emails)
    except Exception as e:
        print("Error:", e)
    print()
