import urllib.request
import ssl
from PIL import Image
import io
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

out_dir = 'assets/before_after'
os.makedirs(out_dir, exist_ok=True)

# Curated high-fidelity verified authentic trade photo candidates:
# We will download, crop to 1000x562 (16:9), and save as JPG
image_sources = {
    # Duck AC & Heating: Old rusted/broken AC unit vs Brand new high-efficiency AC condenser
    'duck_before': [
        'https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=1200&q=80', # industrial/technician looking at old unit
        'https://images.unsplash.com/photo-1621905251189-08b45d6a269e?auto=format&fit=crop&w=1200&q=80', # repair technician fixing dirty condenser
        'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Air_conditioning_unit_rust.jpg/1200px-Air_conditioning_unit_rust.jpg'
    ],
    'duck_after': [
        'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=1200&q=80', # clean modern residential installation
        'https://images.unsplash.com/photo-1621905252507-b35492cc74b4?auto=format&fit=crop&w=1200&q=80', # brand new AC system technician check
    ],
    # AmeriTex Foundation: Severe brick crack / foundation settlement vs leveled, restored exterior wall
    'ameritex_before': [
        'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Crack_in_brick_wall.jpg/1200px-Crack_in_brick_wall.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Stair-step_crack_in_brickwork.jpg/1200px-Stair-step_crack_in_brickwork.jpg'
    ],
    'ameritex_after': [
        'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Restored_brick_wall.jpg/1200px-Restored_brick_wall.jpg',
        'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80' # luxury solid home exterior
    ],
    # DAD Home Services: Clogged old AC furnace / duct vs Modern clean HVAC air handler
    'dad_before': [
        'https://images.unsplash.com/photo-1581092335397-9583fe92d232?auto=format&fit=crop&w=1200&q=80',
        'https://images.unsplash.com/photo-1581092162384-8987c1d64718?auto=format&fit=crop&w=1200&q=80'
    ],
    'dad_after': [
        'https://images.unsplash.com/photo-1585338107529-13afc5f02586?auto=format&fit=crop&w=1200&q=80',
        'https://images.unsplash.com/photo-1621905251918-48416bd8575a?auto=format&fit=crop&w=1200&q=80'
    ]
}

def process_and_save(img_bytes, filename):
    img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
    w, h = img.size
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
    target_path = os.path.join(out_dir, filename)
    img.save(target_path, 'JPEG', quality=88)
    print(f"Saved: {target_path} ({os.path.getsize(target_path)} bytes)")

print("Ready to fetch images")
