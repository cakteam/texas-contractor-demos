import httpx
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'}
url = 'https://www.bbb.org/us/tx/fort-worth/profile/roofing-consultants/chandler-roofing-construction-0825-1000221772'
r = httpx.get(url, headers=headers, follow_redirects=True, timeout=15)
print('Status:', r.status_code)

# find lines mentioning website or href
for line in r.text.split('\n'):
    if 'website' in line.lower() or 'href' in line.lower() and 'http' in line:
        if any(w in line.lower() for w in ['visit', 'primary', 'website', 'chandler']):
            print('Line:', line[:150])
            break

# search for domain patterns
all_urls = re.findall(r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', r.text)
filtered = set(u for u in all_urls if not any(x in u for x in ['bbb.org', 'google', 'adobe', 'schema.org', 'w3.org', 'facebook', 'twitter', 'instagram', 'linkedin', 'youtube', 'gtag', 'cloudfront']))
print('Potential business domains:', list(filtered)[:10])
