import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0'}

targets = [
    ('Duck AC', 'https://www.duckacandheating.com/'),
    ('AmeriTex', 'https://ameritexfoundationrepair.com/'),
    ('DAD AC', 'https://calldadac.com/')
]

for name, u in targets:
    print(f"=== IMAGES FOR {name} ===")
    req = urllib.request.Request(u, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Extract URLs
            raw_urls = re.findall(r'https?://[^\s"\'<>]+\.(?:jpg|jpeg|png|webp)', html, re.I)
            # Wix media hashes
            wix_hashes = re.findall(r'https://static\.wixstatic\.com/media/[a-zA-Z0-9_~]+(?:\.jpg|\.png|\.webp)?', html)
            all_imgs = set(raw_urls + wix_hashes)
            filtered = [x for x in all_imgs if not any(k in x.lower() for k in ['logo', 'icon', 'svg', 'pixel', 'sentry', 'avatar', 'gravatar'])]
            print(f"Found {len(filtered)} photos:")
            for img in filtered[:8]:
                print(" ", img)
    except Exception as e:
        print("Error:", e)
    print()
