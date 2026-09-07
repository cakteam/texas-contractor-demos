import urllib.request
import urllib.parse
import re
import json
import ssl
import os
from PIL import Image
import io

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def search_ddg_images(query):
    try:
        url = f"https://duckduckgo.com/?q={urllib.parse.quote(query)}"
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=8) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            m = re.search(r'vqd=([0-9-]+)', html)
            if not m:
                m = re.search(r'vqd="([^"]+)"', html)
            if not m:
                return []
            vqd = m.group(1)
            
        iurl = f"https://duckduckgo.com/i.js?l=us-en&o=json&q={urllib.parse.quote(query)}&vqd={vqd}&f=,,,&p=1"
        req2 = urllib.request.Request(iurl, headers=headers)
        with urllib.request.urlopen(req2, context=ctx, timeout=8) as resp2:
            data = json.loads(resp2.read().decode('utf-8'))
            return [x['image'] for x in data.get('results', [])[:10]]
    except Exception as e:
        print(f"Error searching '{query}': {e}")
        return []

def download_and_crop(url, out_path):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            content = resp.read()
            img = Image.open(io.BytesIO(content)).convert('RGB')
            w, h = img.size
            if w < 300 or h < 200:
                print(f"Image too small ({w}x{h}): {url}")
                return False
                
            target_ratio = 16.0 / 9.0
            current_ratio = w / float(h)
            
            if current_ratio > target_ratio:
                new_w = int(h * target_ratio)
                left = (w - new_w) // 2
                img = img.crop((left, 0, left + new_w, h))
            else:
                new_h = int(w / target_ratio)
                top = (h - new_h) // 2
                img = img.crop((0, top, w, top + new_h))
                
            img = img.resize((1000, 562), Image.Resampling.LANCZOS)
            img.save(out_path, 'JPEG', quality=88)
            print(f"SUCCESS: Saved {out_path} ({os.path.getsize(out_path)} bytes) from {url[:70]}")
            return True
    except Exception as e:
        print(f"Failed to download {url[:60]}: {e}")
        return False

# Search and download test candidates for:
# 1. Duck AC Before (broken dirty outdoor AC condenser)
# 2. Duck AC After (modern new outdoor AC condenser unit)
# 3. AmeriTex Before (foundation stair step brick crack)
# 4. AmeriTex After (repaired foundation exterior brick wall)
# 5. DAD AC Before (dirty dusty indoor AC unit / evaporator coil)
# 6. DAD AC After (clean modern indoor HVAC unit / air handler)

queries = {
    'duck_before': 'rusted dirty outdoor air conditioner condenser unit broken',
    'duck_after': 'modern residential air conditioner condenser outdoor unit brand new',
    'ameritex_before': 'exterior brick wall stair step crack foundation settlement',
    'ameritex_after': 'solid brick home foundation repaired level exterior',
    'dad_before': 'dirty dusty hvac evaporator coil clogged attic unit',
    'dad_after': 'clean new hvac air handler installation attic residential'
}

os.makedirs('assets/before_after_candidates', exist_ok=True)

for key, q in queries.items():
    print(f"\n--- Searching for {key}: '{q}' ---")
    urls = search_ddg_images(q)
    print(f"Found {len(urls)} image URLs")
    for idx, u in enumerate(urls[:5]):
        out_file = f"assets/before_after_candidates/{key}_{idx+1}.jpg"
        if download_and_crop(u, out_file):
            print(f"  Got candidate {idx+1} for {key}")
            break
