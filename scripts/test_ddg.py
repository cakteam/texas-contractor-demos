import urllib.request
import re
import urllib.parse

req = urllib.request.Request(
    'https://html.duckduckgo.com/html/?q=roofing+contractor+Fort+Worth+TX',
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
)
with urllib.request.urlopen(req) as r:
    h = r.read().decode('utf-8', errors='ignore')

# print where result__title or result__a appears
results = re.findall(r'<a[^>]+class="result__snippet"[^>]+href="([^"]+)"[^>]*>(.*?)</a>', h)
print('snippet links:', len(results))

titles = re.findall(r'<a[^>]+class="result__a"[^>]+href="([^"]+)"[^>]*>(.*?)</a>', h)
print('title links:', len(titles))
for u, t in titles[:10]:
    # unquote uddg
    m = re.search(r'uddg=([^&]+)', u)
    actual_url = urllib.parse.unquote(m.group(1)) if m else u
    clean_t = re.sub(r'<[^>]+>', '', t)
    print(f"- {clean_t.strip()} | {actual_url}")
