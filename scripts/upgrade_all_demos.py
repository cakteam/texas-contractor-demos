#!/usr/bin/env python3
"""
upgrade_all_demos.py — High-End Transformation Upgrade for Top 3 Demos
- Injects Interactive Before/After Split Slider
- Injects Official Brand & Manufacturer Badges (GAF, Owens Corning, LiftMaster, BBB A+)
- Upgrades Google Reviews into authentic Google multi-color branded cards
- Synchronizes updated demos to both 03_DEMOS and root route folders (goodroots, amatttree, dapcodoor)
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Shared Slider CSS & JS
SLIDER_SCRIPT = """
    // --- Interactive Before / After Split Slider ---
    function initBeforeAfterSliders() {
      document.querySelectorAll('.ba-slider-container').forEach(container => {
        const beforeWrap = container.querySelector('.ba-before-wrap');
        const beforeImg = container.querySelector('.ba-before-img');
        const handle = container.querySelector('.ba-handle');
        let isDragging = false;

        function updateWidth() {
          if (beforeImg) beforeImg.style.width = container.offsetWidth + 'px';
        }
        window.addEventListener('resize', updateWidth);
        updateWidth();

        function setPosition(x) {
          const rect = container.getBoundingClientRect();
          let pos = (x - rect.left) / rect.width;
          if (pos < 0.05) pos = 0.05;
          if (pos > 0.95) pos = 0.95;
          const pct = (pos * 100).toFixed(1) + '%';
          beforeWrap.style.width = pct;
          handle.style.left = pct;
        }

        container.addEventListener('mousedown', e => { isDragging = true; setPosition(e.clientX); });
        window.addEventListener('mouseup', () => { isDragging = false; });
        window.addEventListener('mousemove', e => { if (isDragging) setPosition(e.clientX); });

        container.addEventListener('touchstart', e => { isDragging = true; setPosition(e.touches[0].clientX); }, { passive: true });
        window.addEventListener('touchend', () => { isDragging = false; });
        window.addEventListener('touchmove', e => { if (isDragging) setPosition(e.touches[0].clientX); }, { passive: true });
      });
    }
    window.addEventListener('DOMContentLoaded', initBeforeAfterSliders);
    setTimeout(initBeforeAfterSliders, 500);
"""

GOOGLE_ICON = """<svg class="w-4 h-4 shrink-0" viewBox="0 0 24 24">
  <path fill="#4285F4" d="M23.745 12.27c0-.7-.06-1.4-.19-2.07H12v4.51h6.6c-.29 1.52-1.14 2.82-2.4 3.68v3.05h3.88c2.27-2.09 3.66-5.17 3.66-9.17z"/>
  <path fill="#34A853" d="M12 24c3.24 0 5.95-1.08 7.93-2.91l-3.88-3.05c-1.08.72-2.45 1.16-4.05 1.16-3.12 0-5.77-2.1-6.72-4.93H1.25v3.15C3.26 21.36 7.33 24 12 24z"/>
  <path fill="#FBBC05" d="M5.28 14.27c-.25-.72-.38-1.49-.38-2.27s.14-1.55.38-2.27V6.58H1.25C.45 8.18 0 10.03 0 12s.45 3.82 1.25 5.42l4.03-3.15z"/>
  <path fill="#EA4335" d="M12 4.75c1.77 0 3.35.61 4.6 1.8l3.42-3.42C17.95 1.19 15.24 0 12 0 7.33 0 3.26 2.64 1.25 6.58l4.03 3.15c.95-2.83 3.6-4.98 6.72-4.98z"/>
</svg>"""

print("Helper definitions ready.")
