import urllib.request
import ssl
import re

targets = [
    ('Duck AC & Heating', 'https://www.duckacandheating.com/'),
    ('Texas Air Authorities', 'https://texasairinc.com/'),
    ('Great Texas Air', 'https://greattexasair.com/'),
    ('D.A.D. Home Services', 'https://calldadac.com/'),
    ('1Tech Solutions', 'https://1techsolutions.org/')
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for name, url in targets:
    print(f"=====================================")
    print(f"=== Candidate: {name} ({url}) ===")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            status = resp.status
            final_url = resp.geturl()
            html = resp.read().decode('utf-8', errors='ignore')
            
            title = re.search(r'<title>(.*?)</title>', html, re.I | re.S)
            title_text = title.group(1).strip() if title else 'No title'
            
            cms = 'Custom/Static'
            if 'wp-content' in html: cms = 'WordPress'
            elif 'squarespace' in html: cms = 'SquareSpace'
            elif 'wix.com' in html: cms = 'Wix'
            elif 'godaddy' in html: cms = 'GoDaddy'
            elif 'weebly' in html: cms = 'Weebly'
            
            tels = re.findall(r'href=[\'"](tel:[^\'"]+)[\'"]', html, re.I)
            mailtos = re.findall(r'href=[\'"](mailto:[^\'"]+)[\'"]', html, re.I)
            
            # Check viewport
            has_viewport = 'viewport' in html.lower()
            
            # Check for reviews/rating mention
            rating_mentions = re.findall(r'(\b\d\.\d\b|\b5[-\s]star\b|\breviews?\b)', html, re.I)
            
            # Check for copyright year
            c_years = re.findall(r'©\s*(\d{4})|copyright\s*(\d{4})', html, re.I)
            
            print(f"Status: {status} | Final URL: {final_url}")
            print(f"Title: {title_text}")
            print(f"CMS: {cms} | Viewport: {has_viewport} | tel links: {len(tels)} | mailto links: {mailtos}")
            print(f"Copyright years found: {c_years}")
            print(f"Length of HTML: {len(html)} chars")
    except Exception as e:
        print(f"FAILED: {e}")
    print()
