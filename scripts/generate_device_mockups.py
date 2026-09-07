import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

def create_iphone_mockup(screenshot_path, output_path):
    # Load screenshot (780 x 1688)
    screen = Image.open(screenshot_path).convert("RGBA")
    sw, sh = screen.size
    
    # Outer bezel & dimensions
    bezel_x = 36
    bezel_top = 40
    bezel_bottom = 44
    
    phone_w = sw + bezel_x * 2
    phone_h = sh + bezel_top + bezel_bottom
    
    # Canvas with room for drop shadow
    pad_x = 60
    pad_y = 60
    canvas_w = phone_w + pad_x * 2
    canvas_h = phone_h + pad_y * 2
    
    # Create master image (RGBA transparent)
    master = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    
    # 1. Ambient Drop Shadow
    shadow_mask = Image.new("L", (phone_w, phone_h), 0)
    shadow_draw = ImageDraw.Draw(shadow_mask)
    shadow_draw.rounded_rectangle(
        [0, 0, phone_w - 1, phone_h - 1],
        radius=90,
        fill=180
    )
    
    shadow_layer = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    shadow_colored = Image.new("RGBA", (phone_w, phone_h), (0, 0, 0, 160))
    shadow_layer.paste(shadow_colored, (pad_x, pad_y + 20), mask=shadow_mask)
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=30))
    master.paste(shadow_layer, (0, 0), mask=shadow_layer)
    
    # 2. Outer Phone Body (Dark Titanium / Midnight Aluminum)
    phone_body = Image.new("RGBA", (phone_w, phone_h), (0, 0, 0, 0))
    body_draw = ImageDraw.Draw(phone_body)
    
    # Outer frame border
    body_draw.rounded_rectangle(
        [0, 0, phone_w - 1, phone_h - 1],
        radius=92,
        fill=(22, 27, 34, 255),
        outline=(65, 75, 90, 255),
        width=4
    )
    
    # Subtle inner metallic rim
    body_draw.rounded_rectangle(
        [6, 6, phone_w - 7, phone_h - 7],
        radius=86,
        outline=(30, 36, 46, 255),
        width=3
    )
    
    # Screen Mask (curved corners for the screen itself)
    screen_mask = Image.new("L", (sw, sh), 0)
    screen_mask_draw = ImageDraw.Draw(screen_mask)
    screen_mask_draw.rounded_rectangle(
        [0, 0, sw - 1, sh - 1],
        radius=68,
        fill=255
    )
    
    # Paste masked screen inside bezel
    screen_x = bezel_x
    screen_y = bezel_top
    phone_body.paste(screen, (screen_x, screen_y), mask=screen_mask)
    
    # Screen inner border outline for crisp edge
    body_draw.rounded_rectangle(
        [screen_x, screen_y, screen_x + sw - 1, screen_y + sh - 1],
        radius=68,
        outline=(15, 23, 42, 180),
        width=2
    )
    
    # 3. Dynamic Island
    di_w = 230
    di_h = 64
    di_x = screen_x + (sw - di_w) // 2
    di_y = screen_y + 24
    
    body_draw.rounded_rectangle(
        [di_x, di_y, di_x + di_w, di_y + di_h],
        radius=32,
        fill=(0, 0, 0, 255),
        outline=(25, 25, 25, 255),
        width=1
    )
    
    # Camera sensor inside dynamic island
    cam_x = di_x + di_w - 44
    cam_y = di_y + di_h // 2
    body_draw.ellipse([cam_x - 10, cam_y - 10, cam_x + 10, cam_y + 10], fill=(12, 16, 24, 255))
    body_draw.ellipse([cam_x - 5, cam_y - 5, cam_x + 5, cam_y + 5], fill=(30, 42, 60, 255))
    
    # 4. Status Bar Details
    try:
        font = ImageFont.truetype("arial.ttf", 28)
    except:
        font = ImageFont.load_default()
    
    time_x = screen_x + 64
    time_y = screen_y + 36
    body_draw.text((time_x, time_y), "9:41", fill=(255, 255, 255, 230), font=font)
    
    # Battery icon on right
    bat_x = screen_x + sw - 100
    bat_y = screen_y + 42
    body_draw.rounded_rectangle([bat_x, bat_y, bat_x + 44, bat_y + 22], radius=6, outline=(255, 255, 255, 200), width=3)
    body_draw.rectangle([bat_x + 5, bat_y + 5, bat_x + 30, bat_y + 17], fill=(255, 255, 255, 220))
    body_draw.rectangle([bat_x + 46, bat_y + 6, bat_x + 49, bat_y + 16], fill=(255, 255, 255, 180))
    
    # 5. Bottom Home Bar
    bar_w = 260
    bar_h = 10
    bar_x = screen_x + (sw - bar_w) // 2
    bar_y = screen_y + sh - 28
    body_draw.rounded_rectangle(
        [bar_x, bar_y, bar_x + bar_w, bar_y + bar_h],
        radius=5,
        fill=(255, 255, 255, 160)
    )
    
    # Paste phone body onto master canvas
    master.paste(phone_body, (pad_x, pad_y), mask=phone_body)
    
    # Resize master to standard web/email delivery size (width 600px or 640px)
    target_w = 640
    ratio = target_w / canvas_w
    target_h = int(canvas_h * ratio)
    
    final_img = master.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    final_img.save(output_path, "PNG", optimize=True)
    print(f"Generated device mockup: {output_path} ({final_img.size})")

if __name__ == "__main__":
    items = [
        ("04_PREVIEWS/01_good_roots_mobile.png", "04_PREVIEWS/visual_hooks/01_good_roots_mockup.png"),
        ("04_PREVIEWS/02_a_matt_mobile.png", "04_PREVIEWS/visual_hooks/02_a_matt_mockup.png"),
        ("04_PREVIEWS/03_dapco_mobile.png", "04_PREVIEWS/visual_hooks/03_dapco_mockup.png"),
    ]
    for src, dst in items:
        create_iphone_mockup(src, dst)
