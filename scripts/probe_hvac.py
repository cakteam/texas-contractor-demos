import urllib.request
import ssl
import re

targets = [
    ('Golden Air Conditioning', 'https://goldenmechanical.com'),
    ('AC Texas LLC', 'https://actexasllc.com'),
    ('Duck AC & Heating', 'https://duckacandheating.com'),
    ('Air Motions HVAC', 'https://airmotionshvac.com'),
    ('Prime Time Heating & Air', 'https://primetime-tx.com'),
    ('Martech HVAC', 'https://martech-hvac.com'),
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for name, url in targets:
    print(f"=== Testing: {name} ({url}) ===")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            status = resp.status
            final_url = resp.geturl()
            html = resp.read().decode('utf-8', errors='ignore')
            
            title = re.search(r'<title>(.*?)</title>', html, re.I | re.S)
            title_text = title.group(1).strip() if title else 'No title'
            
            emails = list(set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', html)))
            emails = [e for e in emails if not any(e.endswith(ext) for ext in ['png', 'jpg', 'webp', 'js', 'css', 'w3.org', 'sentry.io', 'email.com', 'domain.com'])]
            
            phones = list(set(re.findall(r'\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}', html)))[:4]
            
            cms = 'Custom/Static'
            if 'wp-content' in html: cms = 'WordPress'
            elif 'squarespace' in html: cms = 'SquareSpace'
            elif 'wix.com' in html: cms = 'Wix'
            elif 'godaddy' in html: cms = 'GoDaddy'
            elif 'weebly' in html: cms = 'Weebly'
            
            has_viewport = 'viewport' in html.lower()
            has_tel_link = 'tel:' in html.lower()
            
            print(f"Status: {status} | Final URL: {final_url}")
            print(f"Title: {title_text[:60]}")
            print(f"CMS: {cms} | Has Viewport: {has_viewport} | Has tel: {has_tel_link}")
            print(f"Emails: {emails}")
            print(f"Phones: {phones}")
    except Exception as e:
        print(f"FAILED: {e}")
    print()
