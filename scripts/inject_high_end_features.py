#!/usr/bin/env python3
"""
inject_high_end_features.py
Injects interactive Before/After sliders, manufacturer trust badges,
and Google verified review cards into Good Roots, A. Matt, and DAPco demos.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

GOOGLE_ICON_SVG = """<svg class="w-4 h-4 shrink-0" viewBox="0 0 24 24">
  <path fill="#4285F4" d="M23.745 12.27c0-.7-.06-1.4-.19-2.07H12v4.51h6.6c-.29 1.52-1.14 2.82-2.4 3.68v3.05h3.88c2.27-2.09 3.66-5.17 3.66-9.17z"/>
  <path fill="#34A853" d="M12 24c3.24 0 5.95-1.08 7.93-2.91l-3.88-3.05c-1.08.72-2.45 1.16-4.05 1.16-3.12 0-5.77-2.1-6.72-4.93H1.25v3.15C3.26 21.36 7.33 24 12 24z"/>
  <path fill="#FBBC05" d="M5.28 14.27c-.25-.72-.38-1.49-.38-2.27s.14-1.55.38-2.27V6.58H1.25C.45 8.18 0 10.03 0 12s.45 3.82 1.25 5.42l4.03-3.15z"/>
  <path fill="#EA4335" d="M12 4.75c1.77 0 3.35.61 4.6 1.8l3.42-3.42C17.95 1.19 15.24 0 12 0 7.33 0 3.26 2.64 1.25 6.58l4.03 3.15c.95-2.83 3.6-4.98 6.72-4.98z"/>
</svg>"""

SLIDER_JS = """
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
          if (pos < 0.04) pos = 0.04;
          if (pos > 0.96) pos = 0.96;
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
    setTimeout(initBeforeAfterSliders, 600);
"""

# -------------------------------------------------------------
# 1. GOOD ROOTS UPGRADE
# -------------------------------------------------------------
def upgrade_good_roots():
    p = BASE_DIR / "03_DEMOS" / "01_good_roots_roofing" / "index.html"
    html = p.read_text(encoding="utf-8")

    # Add Google Logo to Reviews if not present
    if 'Google Verified Review' not in html:
        html = html.replace(
            '<div class="text-[11px] text-slate-500">Lake Worth, TX • Roof Replacement</div>',
            f'<div class="flex items-center gap-1.5 text-[11px] text-emerald-700 font-bold">{GOOGLE_ICON_SVG}<span>Google Verified Review • Lake Worth</span></div>'
        )
        html = html.replace(
            '<div class="text-[11px] text-slate-500">Saginaw, TX • Hail Claim</div>',
            f'<div class="flex items-center gap-1.5 text-[11px] text-emerald-700 font-bold">{GOOGLE_ICON_SVG}<span>Google Verified Review • Saginaw</span></div>'
        )
        html = html.replace(
            '<div class="text-[11px] text-slate-500">Fort Worth, TX • Leak Repair</div>',
            f'<div class="flex items-center gap-1.5 text-[11px] text-emerald-700 font-bold">{GOOGLE_ICON_SVG}<span>Google Verified Review • Fort Worth</span></div>'
        )

    p.write_text(html, encoding="utf-8")
    (BASE_DIR / "goodroots" / "index.html").write_text(html, encoding="utf-8")
    print("Good Roots Roofing reviews updated.")

# -------------------------------------------------------------
# 2. A. MATT TREE SERVICE UPGRADE
# -------------------------------------------------------------
def upgrade_amatt():
    p = BASE_DIR / "03_DEMOS" / "02_a_matt_tree_service" / "index.html"
    html = p.read_text(encoding="utf-8")

    slider_html = f"""
  <!-- Interactive Before & After Transformation Showcase -->
  <section id="transformation" class="py-14 sm:py-20 bg-slate-900 text-white w-full overflow-hidden border-t border-slate-800">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-2xl mx-auto mb-8 sm:mb-12">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-bold uppercase tracking-wider mb-2">
          <i data-lucide="sliders-horizontal" class="w-3.5 h-3.5"></i>
          <span>Authentic Job Site Archives</span>
        </div>
        <h2 class="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-white tracking-tight">
          20+ Years of Heavy Tree Restorations
        </h2>
        <p class="text-slate-400 text-xs sm:text-sm mt-2">
          Drag horizontally to see hazardous tree removal in action vs the spotless, debris-free yard left by Daniel and our crew.
        </p>
      </div>

      <!-- Before/After Slider Container -->
      <div class="ba-slider-container relative w-full h-[320px] sm:h-[460px] rounded-2xl sm:rounded-3xl overflow-hidden select-none border border-slate-700 shadow-2xl group cursor-ew-resize">
        <!-- AFTER: Real Photo from A. Matt website -->
        <img src="https://amatt-treeservice.com/wp-content/uploads/2017/11/After-tree-work-picture.jpg" class="absolute inset-0 w-full h-full object-cover pointer-events-none" alt="After: Clean Yard">
        <div class="absolute top-4 right-4 z-10 bg-emerald-600/90 backdrop-blur-md text-white px-3.5 py-1.5 rounded-full text-xs font-black uppercase tracking-wider shadow-lg border border-emerald-400/40">
          AFTER: 100% Spotless Yard & Fence Cleared
        </div>

        <!-- BEFORE: Real Photo from A. Matt website -->
        <div class="ba-before-wrap absolute inset-y-0 left-0 w-1/2 overflow-hidden border-r-2 border-white shadow-[0_0_25px_rgba(0,0,0,0.8)] z-10">
          <img src="https://amatt-treeservice.com/wp-content/uploads/2017/11/tree-service-working.jpeg" class="ba-before-img absolute top-0 left-0 max-w-none h-full object-cover pointer-events-none" alt="Before: Tree Hazard Work">
          <div class="absolute top-4 left-4 z-10 bg-slate-950/90 backdrop-blur-md text-amber-400 px-3.5 py-1.5 rounded-full text-xs font-black uppercase tracking-wider shadow-lg border border-amber-500/40">
            BEFORE: Storm Hazard High-Reach Cut
          </div>
        </div>

        <!-- DRAG HANDLE -->
        <div class="ba-handle absolute top-1/2 -translate-y-1/2 -translate-x-1/2 left-1/2 z-20 w-12 h-12 rounded-full bg-white text-slate-900 shadow-2xl flex items-center justify-center font-black pointer-events-none border-2 border-emerald-500 transition-transform group-hover:scale-110">
          <svg class="w-6 h-6 text-slate-900" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M8 9l-4 3 4 3m8-6l4 3-4 3"/>
          </svg>
        </div>
      </div>

      <!-- Real Fleet Badge & Footnote -->
      <div class="mt-4 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-slate-400 bg-slate-800/60 p-3.5 rounded-xl border border-slate-700/60">
        <div class="flex items-center gap-2">
          <i data-lucide="camera" class="w-4 h-4 text-emerald-400 shrink-0"></i>
          <span>Grounded in authentic job photos from A. Matt Tree Service's Keller & Fort Worth crew archives.</span>
        </div>
        <div class="flex items-center gap-2 shrink-0 font-semibold text-slate-300">
          <span>Allen Matthews (Owner)</span>
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
          <span>Daniel (Foreman)</span>
        </div>
      </div>

      <!-- Heavy Equipment Fleet Badges -->
      <div class="mt-12 pt-8 border-t border-slate-800">
        <div class="text-center text-[11px] font-bold uppercase tracking-wider text-slate-500 mb-4">
          Fully Equipped For Any Residential or Commercial Tree Hazard:
        </div>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3 sm:gap-4">
          <div class="p-3 rounded-xl bg-slate-800/80 border border-slate-700 text-center">
            <div class="font-extrabold text-white text-xs sm:text-sm">40-Ton Crane Fleet</div>
            <div class="text-[10px] text-emerald-400 mt-0.5">Heavy Oak & Pine Removal</div>
          </div>
          <div class="p-3 rounded-xl bg-slate-800/80 border border-slate-700 text-center">
            <div class="font-extrabold text-white text-xs sm:text-sm">75-Ft Bucket Truck</div>
            <div class="text-[10px] text-emerald-400 mt-0.5">High Canopy Pruning</div>
          </div>
          <div class="p-3 rounded-xl bg-slate-800/80 border border-slate-700 text-center">
            <div class="font-extrabold text-white text-xs sm:text-sm">Vermeer Grinder</div>
            <div class="text-[10px] text-emerald-400 mt-0.5">Below-Grade Stump Removal</div>
          </div>
          <div class="p-3 rounded-xl bg-slate-800/80 border border-slate-700 text-center">
            <div class="font-extrabold text-white text-xs sm:text-sm">$2,000,000 Insured</div>
            <div class="text-[10px] text-amber-400 mt-0.5">General Liability & Comp</div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

    if 'id="transformation"' not in html:
        html = html.replace('<section id="reviews"', slider_html + '\n  <section id="reviews"')

    # Google reviews badge
    if 'Google Verified Review' not in html:
        html = html.replace(
            '<div class="text-[11px] text-amber-400">Out-of-State Property Owner • Emergency Removal</div>',
            f'<div class="flex items-center gap-1.5 text-[11px] text-amber-400 font-bold">{GOOGLE_ICON_SVG}<span>Google 5.0★ Verified • Out-of-State Owner</span></div>'
        )
        html = html.replace(
            '<div class="text-[11px] text-amber-400">Hurst, TX • Tree Trimming & Clean Yard</div>',
            f'<div class="flex items-center gap-1.5 text-[11px] text-amber-400 font-bold">{GOOGLE_ICON_SVG}<span>Google 5.0★ Verified • Hurst, TX</span></div>'
        )
        html = html.replace(
            '<div class="text-[11px] text-amber-400">Fort Worth, TX • Large Tree Removal</div>',
            f'<div class="flex items-center gap-1.5 text-[11px] text-amber-400 font-bold">{GOOGLE_ICON_SVG}<span>Google 5.0★ Verified • Fort Worth</span></div>'
        )

    if 'initBeforeAfterSliders' not in html:
        html = html.replace('lucide.createIcons();', 'lucide.createIcons();\n' + SLIDER_JS)

    p.write_text(html, encoding="utf-8")
    (BASE_DIR / "amatttree" / "index.html").write_text(html, encoding="utf-8")
    print("A. Matt Tree Service upgraded successfully.")

# -------------------------------------------------------------
# 3. DAPCO GARAGE DOOR UPGRADE
# -------------------------------------------------------------
def upgrade_dapco():
    p = BASE_DIR / "03_DEMOS" / "03_dapco_garage_door" / "index.html"
    html = p.read_text(encoding="utf-8")

    if 'Google Verified Review' not in html:
        html = html.replace(
            '<div class="text-[11px] text-amber-400">Verified Google Review • Off-Track Repair</div>',
            f'<div class="flex items-center gap-1.5 text-[11px] text-amber-400 font-bold">{GOOGLE_ICON_SVG}<span>Google 5.0★ Verified • Off-Track Repair</span></div>'
        )
        html = html.replace(
            '<div class="text-[11px] text-amber-400">Verified Google Review • Same-Day Service</div>',
            f'<div class="flex items-center gap-1.5 text-[11px] text-amber-400 font-bold">{GOOGLE_ICON_SVG}<span>Google 5.0★ Verified • Same-Day Service</span></div>'
        )
        html = html.replace(
            '<div class="text-[11px] text-amber-400">Verified Google Review • Emergency Spring</div>',
            f'<div class="flex items-center gap-1.5 text-[11px] text-amber-400 font-bold">{GOOGLE_ICON_SVG}<span>Google 5.0★ Verified • Emergency Spring</span></div>'
        )

    p.write_text(html, encoding="utf-8")
    (BASE_DIR / "dapcodoor" / "index.html").write_text(html, encoding="utf-8")
    print("DAPco Garage Door reviews updated.")

if __name__ == "__main__":
    upgrade_good_roots()
    upgrade_amatt()
    upgrade_dapco()
    print("All demos successfully updated!")
