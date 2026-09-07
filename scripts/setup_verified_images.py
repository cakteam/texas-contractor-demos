import shutil
from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent.parent
IMG_DIR = BASE_DIR / "assets" / "before_after"
IMG_DIR.mkdir(parents=True, exist_ok=True)

# Standardize dimensions to crisp 16:9 (1000 x 562) for perfect slider alignment
def fit_image(src_path, dst_path, target_size=(1000, 562)):
    im = Image.open(src_path).convert("RGB")
    # Resize with thumbnail / crop
    w, h = im.size
    tw, th = target_size
    ratio = max(tw / w, th / h)
    new_w = int(w * ratio)
    new_h = int(h * ratio)
    resized = im.resize((new_w, new_h), Image.Resampling.LANCZOS)
    left = (new_w - tw) // 2
    top = (new_h - th) // 2
    cropped = resized.crop((left, top, left + tw, top + th))
    cropped.save(dst_path, "JPEG", quality=90, optimize=True)
    print(f"Processed {dst_path.name}: {cropped.size} ({dst_path.stat().st_size // 1024} KB)")

src_base = BASE_DIR / "assets" / "images"

# 1. Good Roots: Hail Damage vs New Shingles
fit_image(src_base / "goodroots_roof_before.jpg", IMG_DIR / "goodroots_before.jpg")
fit_image(src_base / "goodroots_roof_after.jpg", IMG_DIR / "goodroots_after.jpg")

test_base = BASE_DIR / "scripts" / "test_img"

# 2. A. Matt: Chipper & Branches vs Clean Trimming
fit_image(test_base / "amatt_before.jpg", IMG_DIR / "amatt_before.jpg")
fit_image(test_base / "amatt_after.jpg", IMG_DIR / "amatt_after.jpg")

# 3. DAPco: Old Weathered Door vs Modern Carriage Door
fit_image(src_base / "dapco_garage_before.jpg", IMG_DIR / "dapco_before.jpg")
fit_image(src_base / "dapco_garage_after.jpg", IMG_DIR / "dapco_after.jpg")

print("All verified before/after images standardized in assets/before_after/!")
