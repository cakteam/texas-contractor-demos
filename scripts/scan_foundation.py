import urllib.request
import ssl
import re

targets = [
    ('Friar Foundation Repair', 'https://friarfoundationrepair.com/'),
    ('Lifetime Foundation Repair', 'https://lifetimefoundationrepairs.com/'),
    ('Straight Line Foundation', 'https://straightlinefoundationrepair.com/'),
    ('AmeriTex Foundation Repair', 'https://ameritexfoundationrepair.com/')
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
            
            tels = re.findall(r'href=[\'"](tel:[^\'"]+)[\'"]', html, re.I)
            mailtos = re.findall(r'href=[\'"](mailto:[^\'"]+)[\'"]', html, re.I)
            raw_emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', html)
            real_emails = [e for e in set(raw_emails) if not any(x in e.lower() for x in ['sentry', 'wixpress', 'png', 'jpg', 'webpack'])]
            
            print(f"Status: {status} | Title: {title_text[:60]}")
            print(f"CMS: {cms} | tel links: {len(tels)} | mailto: {mailtos}")
            print(f"Emails found: {real_emails}")
    except Exception as e:
        print(f"FAILED: {e}")
    print()
