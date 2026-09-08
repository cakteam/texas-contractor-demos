#!/usr/bin/env python3
"""
setup_hospitality_assets.py — Download high-resolution culinary assets
for the three pilot hospitality demos:
1. Bar Harbor Lobster Bakes (Bar Harbor, ME)
2. Scoff Troff Cafe (St Ives, Cornwall, UK)
3. Dip Cafe (Byron Bay, NSW, Australia)
"""

import os
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
HOSP_DIR = BASE_DIR / "assets" / "hospitality"
HOSP_DIR.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

IMAGES = {
    # 1. Bar Harbor Lobster Bakes
    "barharbor_hero.jpg": "https://images.unsplash.com/photo-1599488615731-7e5c2823ff28?auto=format&fit=crop&w=1200&q=85",
    "barharbor_lobster_roll.jpg": "https://images.unsplash.com/photo-1625944525533-473f1a3d54e7?auto=format&fit=crop&w=1000&q=85",
    "barharbor_chowder.jpg": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=1000&q=85",
    "barharbor_blueberry_pie.jpg": "https://images.unsplash.com/photo-1519869325930-281384150729?auto=format&fit=crop&w=1000&q=85",
    "barharbor_steamers.jpg": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=1000&q=85",

    # 2. Scoff Troff Cafe (St Ives, Cornwall)
    "scofftroff_hero.jpg": "https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?auto=format&fit=crop&w=1200&q=85",
    "scofftroff_pancakes.jpg": "https://images.unsplash.com/photo-1528207776546-365bb710ee93?auto=format&fit=crop&w=1000&q=85",
    "scofftroff_burger.jpg": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=1000&q=85",
    "scofftroff_cream_tea.jpg": "https://images.unsplash.com/photo-1587314168485-3236d6710814?auto=format&fit=crop&w=1000&q=85",

    # 3. Dip Cafe (Byron Bay, NSW)
    "dipcafe_hero.jpg": "https://images.unsplash.com/photo-1484723091739-30a097e8f929?auto=format&fit=crop&w=1200&q=85",
    "dipcafe_avotoast.jpg": "https://images.unsplash.com/photo-1525351484163-7529414344d8?auto=format&fit=crop&w=1000&q=85",
    "dipcafe_shakshuka.jpg": "https://images.unsplash.com/photo-1590301157890-4810ed352733?auto=format&fit=crop&w=1000&q=85",
    "dipcafe_flatwhite.jpg": "https://images.unsplash.com/photo-1517701604599-bb29b565090c?auto=format&fit=crop&w=1000&q=85",
}

for filename, url in IMAGES.items():
    dest = HOSP_DIR / filename
    if dest.exists() and dest.stat().st_size > 10000:
        print(f"Already exists: {filename}")
        continue
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp, open(dest, "wb") as f:
            f.write(resp.read())
        print(f"Downloaded: {filename} ({dest.stat().st_size // 1024} KB)")
    except Exception as e:
        print(f"Failed {filename}: {e}")

print("Hospitality asset setup complete.")
