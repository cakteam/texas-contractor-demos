#!/usr/bin/env python3
"""
update_hub_hospitality.py — Append the Global Tourist Hospitality Collection
to the master showcase index.html.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INDEX_PATH = BASE_DIR / "index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

HOSPITALITY_SECTION = """
    <!-- ================================================================= -->
    <!-- GLOBAL TOURIST HOSPITALITY EXPANSION (US • UK • AUSTRALIA) -->
    <!-- ================================================================= -->
    <div class="pt-8 border-t border-slate-800">
      <div class="flex items-center gap-3 mb-2">
        <span class="px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-300 text-xs font-bold uppercase tracking-wider">
          New Pipeline Experiment • Tourist Haven Hospitality
        </span>
      </div>
      <h2 class="text-3xl font-extrabold text-white">Global Tourist Haven Culinary Showcases</h2>
      <p class="text-sm text-slate-400 mt-1 max-w-3xl">
        Testing high-income, scenic travel hubs across the US, UK, and Australia. In remote destinations, tourists rely 100% on Google Maps to choose where to eat. These independent restaurateurs pour their pride into their food—converting missing Facebook links into magazine-grade mobile menus.
      </p>
    </div>

    <!-- DEMO 10: BAR HARBOR LOBSTER BAKES -->
    <article id="bar-harbor" class="glass-card rounded-3xl p-6 sm:p-8 space-y-8 border border-red-500/30">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-800 pb-6">
        <div>
          <div class="flex items-center gap-2 text-xs font-bold text-red-400 uppercase tracking-wider mb-1">
            <i data-lucide="compass" class="w-4 h-4"></i> Target #10 (US) • Acadia National Park Down-East Seafood
          </div>
          <h2 class="text-2xl font-extrabold text-white">Bar Harbor Lobster Bakes</h2>
          <p class="text-xs text-slate-400 mt-1">Bar Harbor, Mount Desert Island, ME 04609 • Phone: (207) 288-4597 • 4.7★ Down-East Tradition</p>
        </div>
        <div class="flex flex-wrap items-center gap-2 sm:gap-3">
          <a href="./barharborlobster/" target="_blank" class="px-5 py-2.5 rounded-xl bg-red-600 hover:bg-red-500 text-white font-extrabold text-xs flex items-center gap-2 shadow-lg transition-all">
            <i data-lucide="external-link" class="w-4 h-4"></i>
            <span>Open Mobile Demo</span>
          </a>
          <button onclick="copyDemoLink('barharborlobster')" class="px-3.5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700 flex items-center gap-1.5 transition-colors">
            <i data-lucide="copy" class="w-3.5 h-3.5"></i>
            <span>Copy Link</span>
          </button>
        </div>
      </div>

      <div class="grid lg:grid-cols-12 gap-8 items-start">
        <div class="lg:col-span-5 flex flex-col items-center">
          <div class="text-xs font-bold text-slate-400 mb-2 flex items-center gap-1.5">
            <i data-lucide="smartphone" class="w-4 h-4 text-red-400"></i>
            <span>Visual Hook (Authentic Maine Lobster Platter + 390px Viewport)</span>
          </div>
          <div class="max-w-[320px] w-full rounded-2xl overflow-hidden border border-slate-700 shadow-2xl bg-slate-900">
            <img src="./04_PREVIEWS/visual_hooks/10_bar_harbor_mockup.png" alt="Bar Harbor Lobster Bakes Mobile Prototype" class="w-full h-auto block">
          </div>
        </div>

        <div class="lg:col-span-7 space-y-5">
          <div class="space-y-2">
            <h3 class="text-xs font-bold uppercase tracking-wider text-red-400">The Acadia Tourist Reality & Friction</h3>
            <p class="text-sm text-slate-300 leading-relaxed">
              4 million seasonal Acadia hikers look up <em>"lobster bake near me"</em>. The business currently relies on Facebook, hitting mobile visitors with login walls and buried prices.
            </p>
          </div>
          <div class="grid sm:grid-cols-2 gap-3">
            <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
              <div class="text-xs font-bold text-slate-200 mb-1">🦞 Live Catch & Bake Tiers</div>
              <p class="text-xs text-slate-400">Instant party estimator for Traditional 1¼ lb Acadia Bakes, Downeast Feasts & Chowders.</p>
            </div>
            <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
              <div class="text-xs font-bold text-slate-200 mb-1">📍 1-Tap Park Directions</div>
              <p class="text-xs text-slate-400">Zero-friction navigation for hikers returning from Acadia's Park Loop Road.</p>
            </div>
          </div>
        </div>
      </div>
    </article>

    <!-- DEMO 11: SCOFF TROFF CAFE -->
    <article id="scoff-troff" class="glass-card rounded-3xl p-6 sm:p-8 space-y-8 border border-teal-500/30">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-800 pb-6">
        <div>
          <div class="flex items-center gap-2 text-xs font-bold text-teal-400 uppercase tracking-wider mb-1">
            <i data-lucide="compass" class="w-4 h-4"></i> Target #11 (UK) • St Ives Harbour Artisanal Brunch & Burgers
          </div>
          <h2 class="text-2xl font-extrabold text-white">Scoff Troff Cafe</h2>
          <p class="text-xs text-slate-400 mt-1">Fore Street, St Ives, Cornwall TR26 1HE, UK • Phone: +44 1736 797341 • 4.6★ Harbour Indie</p>
        </div>
        <div class="flex flex-wrap items-center gap-2 sm:gap-3">
          <a href="./scofftroff/" target="_blank" class="px-5 py-2.5 rounded-xl bg-teal-600 hover:bg-teal-500 text-white font-extrabold text-xs flex items-center gap-2 shadow-lg transition-all">
            <i data-lucide="external-link" class="w-4 h-4"></i>
            <span>Open Mobile Demo</span>
          </a>
          <button onclick="copyDemoLink('scofftroff')" class="px-3.5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700 flex items-center gap-1.5 transition-colors">
            <i data-lucide="copy" class="w-3.5 h-3.5"></i>
            <span>Copy Link</span>
          </button>
        </div>
      </div>

      <div class="grid lg:grid-cols-12 gap-8 items-start">
        <div class="lg:col-span-5 flex flex-col items-center">
          <div class="text-xs font-bold text-slate-400 mb-2 flex items-center gap-1.5">
            <i data-lucide="smartphone" class="w-4 h-4 text-teal-400"></i>
            <span>Visual Hook (Cornish Farmhouse Breakfast + 390px Viewport)</span>
          </div>
          <div class="max-w-[320px] w-full rounded-2xl overflow-hidden border border-slate-700 shadow-2xl bg-slate-900">
            <img src="./04_PREVIEWS/visual_hooks/11_scoff_troff_mockup.png" alt="Scoff Troff Cafe Mobile Prototype" class="w-full h-auto block">
          </div>
        </div>

        <div class="lg:col-span-7 space-y-5">
          <div class="space-y-2">
            <h3 class="text-xs font-bold uppercase tracking-wider text-teal-400">The Cornish Seaside Dilemma</h3>
            <p class="text-sm text-slate-300 leading-relaxed">
              Holidaymakers off Porthmeor Beach need fast answers: dog-friendly policies, vegan options, and all-day pancake availability. A clean mobile menu beats cluttered social feeds.
            </p>
          </div>
          <div class="grid sm:grid-cols-2 gap-3">
            <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
              <div class="text-xs font-bold text-slate-200 mb-1">🐾 Holidaymaker Clarity</div>
              <p class="text-xs text-slate-400">Clear 100% Dog-Friendly, Vegan, and Gluten-Free badges prevent table drop-off.</p>
            </div>
            <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
              <div class="text-xs font-bold text-slate-200 mb-1">☕ Harbour Table Call</div>
              <p class="text-xs text-slate-400">1-tap direct dialing to 01736 797341 & walking guidance from St Ives slipway.</p>
            </div>
          </div>
        </div>
      </div>
    </article>

    <!-- DEMO 12: DIP CAFE -->
    <article id="dip-cafe" class="glass-card rounded-3xl p-6 sm:p-8 space-y-8 border border-amber-500/30">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-800 pb-6">
        <div>
          <div class="flex items-center gap-2 text-xs font-bold text-amber-400 uppercase tracking-wider mb-1">
            <i data-lucide="compass" class="w-4 h-4"></i> Target #12 (AU) • Byron Bay French Artisanal Brunch & Allpress Coffee
          </div>
          <h2 class="text-2xl font-extrabold text-white">Dip Cafe Byron Bay</h2>
          <p class="text-xs text-slate-400 mt-1">21 Fletcher Street, Byron Bay, NSW 2481, Australia • Phone: (02) 6680 8864 • 4.5★ (700+ Reviews)</p>
        </div>
        <div class="flex flex-wrap items-center gap-2 sm:gap-3">
          <a href="./dipcafe/" target="_blank" class="px-5 py-2.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-extrabold text-xs flex items-center gap-2 shadow-lg transition-all">
            <i data-lucide="external-link" class="w-4 h-4"></i>
            <span>Open Mobile Demo</span>
          </a>
          <button onclick="copyDemoLink('dipcafe')" class="px-3.5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700 flex items-center gap-1.5 transition-colors">
            <i data-lucide="copy" class="w-3.5 h-3.5"></i>
            <span>Copy Link</span>
          </button>
        </div>
      </div>

      <div class="grid lg:grid-cols-12 gap-8 items-start">
        <div class="lg:col-span-5 flex flex-col items-center">
          <div class="text-xs font-bold text-slate-400 mb-2 flex items-center gap-1.5">
            <i data-lucide="smartphone" class="w-4 h-4 text-amber-400"></i>
            <span>Visual Hook (Brioche French Toast + 390px Viewport)</span>
          </div>
          <div class="max-w-[320px] w-full rounded-2xl overflow-hidden border border-slate-700 shadow-2xl bg-slate-900">
            <img src="./04_PREVIEWS/visual_hooks/12_dip_cafe_mockup.png" alt="Dip Cafe Byron Bay Mobile Prototype" class="w-full h-auto block">
          </div>
        </div>

        <div class="lg:col-span-7 space-y-5">
          <div class="space-y-2">
            <h3 class="text-xs font-bold uppercase tracking-wider text-amber-400">The Byron Bay Aesthetic Challenge</h3>
            <p class="text-sm text-slate-300 leading-relaxed">
              Design-conscious tourists choose breakfast with their eyes. Dip Cafe's house-baked brioche and shakshuka deserve an editorial look, not an unstructured social feed.
            </p>
          </div>
          <div class="grid sm:grid-cols-2 gap-3">
            <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
              <div class="text-xs font-bold text-slate-200 mb-1">🥐 Editorial Visual Menu</div>
              <p class="text-xs text-slate-400">Showcasing house brioche, Northern Rivers avocados, and Allpress coffee roast notes.</p>
            </div>
            <div class="bg-slate-900/60 p-4 rounded-xl border border-slate-800">
              <div class="text-xs font-bold text-slate-200 mb-1">☀️ Sunlit Terrace Enquiries</div>
              <p class="text-xs text-slate-400">1-tap table booking and Fletcher Street directions for holidaymakers.</p>
            </div>
          </div>
        </div>
      </div>
    </article>
"""

if "<!-- DEMO 10: BAR HARBOR" not in content:
    target_marker = "</main>"
    content = content.replace(target_marker, HOSPITALITY_SECTION + "\n  " + target_marker)
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("Master index.html successfully updated with Hospitality Collection!")
else:
    print("Hospitality collection already in index.html")
