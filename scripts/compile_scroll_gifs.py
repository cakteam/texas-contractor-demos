import os
import glob
from PIL import Image, ImageDraw, ImageFilter, ImageFont

def render_iphone_frame(screen_img):
    """Takes a PIL Image of the screen (780 x 1688) and returns phone frame image."""
    screen = screen_img.convert("RGBA")
    sw, sh = screen.size
    
    bezel_x = 36
    bezel_top = 40
    bezel_bottom = 44
    
    phone_w = sw + bezel_x * 2
    phone_h = sh + bezel_top + bezel_bottom
    
    pad_x = 40
    pad_y = 40
    canvas_w = phone_w + pad_x * 2
    canvas_h = phone_h + pad_y * 2
    
    master = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    
    # Ambient Drop Shadow
    shadow_mask = Image.new("L", (phone_w, phone_h), 0)
    shadow_draw = ImageDraw.Draw(shadow_mask)
    shadow_draw.rounded_rectangle([0, 0, phone_w - 1, phone_h - 1], radius=88, fill=160)
    
    shadow_layer = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    shadow_layer.paste(Image.new("RGBA", (phone_w, phone_h), (0, 0, 0, 140)), (pad_x, pad_y + 16), mask=shadow_mask)
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=24))
    master.paste(shadow_layer, (0, 0), mask=shadow_layer)
    
    # Phone Body
    phone_body = Image.new("RGBA", (phone_w, phone_h), (0, 0, 0, 0))
    body_draw = ImageDraw.Draw(phone_body)
    
    # Bezel
    body_draw.rounded_rectangle(
        [0, 0, phone_w - 1, phone_h - 1],
        radius=90,
        fill=(22, 27, 34, 255),
        outline=(65, 75, 90, 255),
        width=4
    )
    
    # Screen Mask
    screen_mask = Image.new("L", (sw, sh), 0)
    screen_mask_draw = ImageDraw.Draw(screen_mask)
    screen_mask_draw.rounded_rectangle([0, 0, sw - 1, sh - 1], radius=64, fill=255)
    
    screen_x = bezel_x
    screen_y = bezel_top
    phone_body.paste(screen, (screen_x, screen_y), mask=screen_mask)
    
    # Screen border
    body_draw.rounded_rectangle(
        [screen_x, screen_y, screen_x + sw - 1, screen_y + sh - 1],
        radius=64,
        outline=(20, 30, 45, 200),
        width=2
    )
    
    # Dynamic Island
    di_w = 230
    di_h = 64
    di_x = screen_x + (sw - di_w) // 2
    di_y = screen_y + 24
    body_draw.rounded_rectangle([di_x, di_y, di_x + di_w, di_y + di_h], radius=32, fill=(0, 0, 0, 255))
    
    # Time & Status Bar
    try:
        font = ImageFont.truetype("arial.ttf", 28)
    except:
        font = ImageFont.load_default()
    body_draw.text((screen_x + 64, screen_y + 36), "9:41", fill=(255, 255, 255, 220), font=font)
    
    # Battery icon
    bat_x = screen_x + sw - 100
    bat_y = screen_y + 42
    body_draw.rounded_rectangle([bat_x, bat_y, bat_x + 44, bat_y + 22], radius=6, outline=(255, 255, 255, 200), width=3)
    body_draw.rectangle([bat_x + 5, bat_y + 5, bat_x + 30, bat_y + 17], fill=(255, 255, 255, 220))
    
    # Home Bar
    bar_w = 260
    bar_h = 10
    bar_x = screen_x + (sw - bar_w) // 2
    bar_y = screen_y + sh - 28
    body_draw.rounded_rectangle([bar_x, bar_y, bar_x + bar_w, bar_y + bar_h], radius=5, fill=(255, 255, 255, 150))
    
    master.paste(phone_body, (pad_x, pad_y), mask=phone_body)
    
    # Resize to email-friendly width (480px)
    target_w = 480
    target_h = int(canvas_h * (target_w / canvas_w))
    resized = master.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    # Composite onto a soft clean background or keep transparent
    # For GIF compatibility across Outlook/Gmail, RGB on a crisp light/slate neutral background prevents haloing
    bg = Image.new("RGB", (target_w, target_h), (248, 250, 252)) # slate-50
    bg.paste(resized, (0, 0), mask=resized.split()[3])
    return bg

def create_gif(frames_dir, output_gif):
    frame_files = sorted(glob.glob(os.path.join(frames_dir, "frame_*.png")))
    if not frame_files:
        print(f"No frames found in {frames_dir}")
        return
    
    print(f"Compiling {len(frame_files)} frames from {frames_dir} -> {output_gif}...")
    rendered_frames = []
    durations = []
    
    for i, fpath in enumerate(frame_files):
        img = Image.open(fpath)
        framed = render_iphone_frame(img)
        # Convert to P mode with adaptive palette for crisp GIF rendering
        paletted = framed.convert("P", palette=Image.Palette.ADAPTIVE, colors=256)
        rendered_frames.append(paletted)
        
        # Timing:
        # First frame (Hero): 1500ms
        # Key interaction frames (middle): 1400ms
        # Normal scroll transition frames: 300ms
        if i == 0:
            durations.append(1500)
        elif i == 4 or i == 5:
            durations.append(1400)
        else:
            durations.append(350)
            
    os.makedirs(os.path.dirname(output_gif), exist_ok=True)
    rendered_frames[0].save(
        output_gif,
        save_all=True,
        append_images=rendered_frames[1:],
        duration=durations,
        loop=0,
        optimize=True
    )
    file_size_kb = os.path.getsize(output_gif) // 1024
    print(f"  -> Successfully generated {output_gif} ({file_size_kb} KB)")

if __name__ == "__main__":
    targets = [
        ("04_PREVIEWS/visual_hooks/_raw_frames/01_good_roots", "04_PREVIEWS/visual_hooks/01_good_roots_scroll.gif"),
        ("04_PREVIEWS/visual_hooks/_raw_frames/02_a_matt", "04_PREVIEWS/visual_hooks/02_a_matt_scroll.gif"),
        ("04_PREVIEWS/visual_hooks/_raw_frames/03_dapco", "04_PREVIEWS/visual_hooks/03_dapco_scroll.gif"),
    ]
    for raw_dir, gif_path in targets:
        create_gif(raw_dir, gif_path)
