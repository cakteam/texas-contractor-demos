import httpx
import re

url = "https://chandlerroofing.com"
r = httpx.get(url, follow_redirects=False, timeout=10)
print("Status:", r.status_code)
print("Headers:", r.headers)
print("Body:", r.text[:500])
