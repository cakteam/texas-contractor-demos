#!/usr/bin/env python3
"""
redesign_high_end_hospitality.py — Elevate the three hospitality demos to
magazine-grade, Michelin / Relais & Châteaux luxury editorial aesthetics.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================================================================
# 1. BAR HARBOR LOBSTER BAKES (Old-Money New England Coastal Luxury)
# ==============================================================================
BAR_HARBOR_LUXURY_HTML = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Bar Harbor Lobster Bakes | An Acadia Culinary Institution</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700;800&family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; }
    body { font-family: 'Plus Jakarta Sans', sans-serif; overflow-x: hidden; width: 100%; background-color: #040911; }
    .font-cinzel { font-family: 'Cinzel', serif; }
    .font-serif-luxury { font-family: 'Cormorant Garamond', Georgia, serif; }
    .gold-gradient-text {
      background: linear-gradient(135deg, #fce0ad 0%, #dfb76c 50%, #9a7432 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .gold-border { border-color: rgba(223, 183, 108, 0.3); }
    .luxury-glass {
      background: rgba(8, 18, 33, 0.78);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(223, 183, 108, 0.2);
    }
  </style>
</head>
<body class="text-stone-200 min-h-screen flex flex-col pb-24 selection:bg-amber-500 selection:text-black">

  <!-- Top Maritime Bar -->
  <div class="bg-[#03060b] border-b border-[#dfb76c]/20 py-2 px-4 text-[11px] tracking-wider uppercase text-stone-400 flex items-center justify-between gap-2">
    <div class="truncate flex items-center gap-1.5">
      <span class="w-1.5 h-1.5 rounded-full bg-[#dfb76c] animate-pulse shrink-0"></span>
      <span class="truncate">Acadia • Bar Harbor, ME</span>
    </div>
    <a href="tel:2072884597" class="shrink-0 text-amber-200 hover:text-white transition font-semibold tracking-wider flex items-center gap-1">
      <span>(207) 288-4597</span>
    </a>
  </div>

  <!-- Editorial Navigation -->
  <header class="sticky top-0 z-40 bg-[#040911]/90 backdrop-blur-xl border-b border-stone-800/60 px-4 py-4">
    <div class="max-w-5xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-full border border-[#dfb76c]/40 flex items-center justify-center text-amber-300 text-lg bg-[#0a1626]">
          ⚓
        </div>
        <div>
          <h1 class="font-cinzel text-sm sm:text-base tracking-[0.2em] text-stone-100 font-bold leading-none">BAR HARBOR</h1>
          <p class="font-serif-luxury italic text-xs text-amber-300 tracking-widest mt-0.5">Lobster Bakes • Est. Down-East</p>
        </div>
      </div>
      <a href="tel:2072884597" class="border border-[#dfb76c] hover:bg-[#dfb76c] hover:text-black text-amber-200 text-xs font-semibold tracking-wider px-4 py-2 rounded-full transition duration-300 uppercase">
        Reserve Table
      </a>
    </div>
  </header>

  <!-- Hero: Cinematic Full Bleed -->
  <section class="relative min-h-[580px] flex items-center justify-center px-4 py-16 overflow-hidden">
    <!-- Hero Background Image with Vignette -->
    <div class="absolute inset-0 z-0">
      <img src="../assets/hospitality/barharbor_hero.jpg" alt="Bar Harbor Steamed Maine Lobster" class="w-full h-full object-cover object-center scale-105 filter brightness-75">
      <div class="absolute inset-0 bg-gradient-to-t from-[#040911] via-[#040911]/60 to-[#040911]/80"></div>
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-transparent via-[#040911]/40 to-[#040911]"></div>
    </div>

    <!-- Hero Content -->
    <div class="relative z-10 max-w-2xl mx-auto text-center space-y-5">
      <!-- Crest Badge -->
      <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-stone-900/80 border border-[#dfb76c]/40 text-amber-200 text-xs tracking-widest uppercase">
        <span>★ 4.7★ An Acadia Culinary Rite of Passage ★</span>
      </div>

      <!-- Headline -->
      <h2 class="font-serif-luxury text-3xl sm:text-5xl md:text-6xl font-normal text-stone-100 leading-[1.1] tracking-tight">
        Wild Atlantic Catch.<br>
        <span class="italic gold-gradient-text font-serif-luxury">Steamed Over Fresh Seaweed.</span>
      </h2>

      <!-- Subtitle -->
      <p class="text-xs sm:text-sm text-stone-300 leading-relaxed font-light max-w-lg mx-auto tracking-wide">
        For generations, travelers returning from Acadia’s granite trails gather under coastal pines for sweet native hard-shell lobsters, local steamer clams, and hot drawn butter.
      </p>

      <!-- Live Service Pill -->
      <div class="inline-flex items-center gap-3 px-4 py-2 rounded-full luxury-glass text-xs text-stone-300 font-light">
        <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
        <span>Evening Service: <strong class="text-amber-200 font-medium">4:30 PM – 9:00 PM Tonight</strong></span>
      </div>

      <!-- CTAs -->
      <div class="pt-2 flex flex-col sm:flex-row gap-3 justify-center max-w-sm mx-auto">
        <a href="tel:2072884597" class="bg-gradient-to-r from-[#dfb76c] to-[#c2964b] hover:from-[#f0caa0] hover:to-[#dfb76c] text-stone-950 font-bold py-3.5 px-6 rounded-full shadow-xl transition tracking-wider text-xs uppercase flex items-center justify-center gap-2">
          <span>📞 Call for Seating: (207) 288-4597</span>
        </a>
        <a href="#menu" class="border border-stone-600 hover:border-amber-400/60 bg-stone-900/60 backdrop-blur-md text-stone-200 font-medium py-3.5 px-6 rounded-full transition tracking-wider text-xs uppercase flex items-center justify-center gap-2">
          <span>View Tonight's Menu</span>
        </a>
      </div>
    </div>
  </section>

  <!-- Editorial Accolade Quote -->
  <section class="border-y border-stone-800/80 bg-[#060e1a] py-8 px-4 text-center">
    <div class="max-w-xl mx-auto space-y-2">
      <p class="font-serif-luxury italic text-base sm:text-lg text-stone-300">
        “The quintessential Down-East feast. No white tablecloth pretension—just pristine Gulf of Maine lobster cracked hot by the coastal breeze.”
      </p>
      <p class="text-[11px] tracking-[0.25em] uppercase text-[#dfb76c]">Coastal New England Travel Review</p>
    </div>
  </section>

  <!-- Tasting Menu Section: Magazine Editorial Style -->
  <section id="menu" class="max-w-4xl mx-auto px-4 py-16 w-full space-y-12">
    <div class="text-center space-y-2">
      <div class="flex items-center justify-center gap-3">
        <span class="h-[1px] w-8 bg-[#dfb76c]/40"></span>
        <span class="text-[11px] tracking-[0.3em] uppercase text-amber-300 font-semibold">Le Menu Gastronomique</span>
        <span class="h-[1px] w-8 bg-[#dfb76c]/40"></span>
      </div>
      <h3 class="font-serif-luxury text-2xl sm:text-4xl text-stone-100 font-normal">Tonight's Coastal Offerings</h3>
      <p class="text-xs text-stone-400 max-w-md mx-auto font-light leading-relaxed">Sourced directly from Bar Harbor trap boats docked at dawn.</p>
    </div>

    <!-- Prix-Fixe / Featured Bakes (Editorial Split Card) -->
    <div class="luxury-glass rounded-2xl p-6 sm:p-8 space-y-6">
      <div class="flex items-center justify-between border-b border-stone-800 pb-4">
        <div>
          <span class="text-[10px] tracking-[0.2em] uppercase text-amber-400 font-bold">Signature Multi-Course</span>
          <h4 class="font-serif-luxury text-xl sm:text-2xl text-stone-100 mt-0.5">The Downeast Acadia Feast</h4>
        </div>
        <div class="text-right">
          <span class="font-serif-luxury text-2xl text-amber-300 font-bold">$62</span>
          <p class="text-[10px] text-stone-400 uppercase tracking-widest">Prix Fixe Per Guest</p>
        </div>
      </div>
      <p class="text-xs sm:text-sm text-stone-300 leading-relaxed font-light">
        A full oceanfront celebration: Choice of 1½ lb select hard-shell Maine lobster steamed in rockweed seaweed, accompanied by a steaming cup of native clam chowder, sweet corn on the cob, roasted baby reds, and finished with a warm slice of wild Maine mountain blueberry pie.
      </p>
      <div class="flex flex-wrap gap-2 text-[10px] tracking-wider uppercase text-amber-200">
        <span class="px-2.5 py-1 rounded-full bg-amber-500/10 border border-amber-500/30">Live Trap Catch</span>
        <span class="px-2.5 py-1 rounded-full bg-amber-500/10 border border-amber-500/30">Sweet Rockweed Steamed</span>
        <span class="px-2.5 py-1 rounded-full bg-amber-500/10 border border-amber-500/30">Wild Mountain Berry Pie</span>
      </div>
    </div>

    <!-- À La Carte Cards Grid -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
      
      <!-- Item 1: Lobster Roll -->
      <div class="luxury-glass rounded-2xl p-4 flex gap-4 items-center group hover:border-[#dfb76c]/50 transition duration-300">
        <img src="../assets/hospitality/barharbor_lobster_roll.jpg" alt="Maine Lobster Roll" class="w-24 h-24 rounded-xl object-cover shrink-0 border border-stone-700">
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h5 class="font-serif-luxury text-base text-stone-100 font-semibold group-hover:text-amber-200 transition">Acadian Warm Lobster Roll</h5>
            <span class="text-amber-300 font-serif-luxury text-lg font-bold shrink-0">$32</span>
          </div>
          <p class="text-xs text-stone-400 mt-1 line-clamp-2 font-light">Overflowing claw and knuckle meat poached in clarified lemon sea butter on a grilled brioche roll.</p>
          <span class="inline-block mt-2 text-[9px] tracking-widest uppercase text-amber-400 font-semibold">House Pride</span>
        </div>
      </div>

      <!-- Item 2: Clam Chowder -->
      <div class="luxury-glass rounded-2xl p-4 flex gap-4 items-center group hover:border-[#dfb76c]/50 transition duration-300">
        <img src="../assets/hospitality/barharbor_chowder.jpg" alt="Coastal Clam Chowder" class="w-24 h-24 rounded-xl object-cover shrink-0 border border-stone-700">
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h5 class="font-serif-luxury text-base text-stone-100 font-semibold group-hover:text-amber-200 transition">Native Sea Clam Chowder</h5>
            <span class="text-amber-300 font-serif-luxury text-lg font-bold shrink-0">$12</span>
          </div>
          <p class="text-xs text-stone-400 mt-1 line-clamp-2 font-light">Velvety coastal cream, sweet sea clams, hand-diced potatoes, and Applewood lardons.</p>
          <span class="inline-block mt-2 text-[9px] tracking-widest uppercase text-stone-400">Traditional Bowl</span>
        </div>
      </div>

      <!-- Item 3: Steamers Bucket -->
      <div class="luxury-glass rounded-2xl p-4 flex gap-4 items-center group hover:border-[#dfb76c]/50 transition duration-300">
        <img src="../assets/hospitality/barharbor_steamers.jpg" alt="Steamed Maine Clams" class="w-24 h-24 rounded-xl object-cover shrink-0 border border-stone-700">
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h5 class="font-serif-luxury text-base text-stone-100 font-semibold group-hover:text-amber-200 transition">Atlantic Soft-Shell Steamers</h5>
            <span class="text-amber-300 font-serif-luxury text-lg font-bold shrink-0">$22</span>
          </div>
          <p class="text-xs text-stone-400 mt-1 line-clamp-2 font-light">Freshly harvested local steamer clams served with natural sea clam liquor and melted butter.</p>
          <span class="inline-block mt-2 text-[9px] tracking-widest uppercase text-stone-400">Full Pound</span>
        </div>
      </div>

      <!-- Item 4: Wild Blueberry Pie -->
      <div class="luxury-glass rounded-2xl p-4 flex gap-4 items-center group hover:border-[#dfb76c]/50 transition duration-300">
        <img src="../assets/hospitality/barharbor_blueberry_pie.jpg" alt="Wild Maine Blueberry Pie" class="w-24 h-24 rounded-xl object-cover shrink-0 border border-stone-700">
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h5 class="font-serif-luxury text-base text-stone-100 font-semibold group-hover:text-amber-200 transition">Wild Maine Blueberry Tart</h5>
            <span class="text-amber-300 font-serif-luxury text-lg font-bold shrink-0">$9</span>
          </div>
          <p class="text-xs text-stone-400 mt-1 line-clamp-2 font-light">High-altitude hand-harvested blueberries in a flaky Normandy butter crust with vanilla cream.</p>
          <span class="inline-block mt-2 text-[9px] tracking-widest uppercase text-amber-400 font-semibold">Pastry Daily</span>
        </div>
      </div>

    </div>
  </section>

  <!-- The 3 Traditions of Down-East Steaming -->
  <section class="max-w-4xl mx-auto px-4 py-12 w-full">
    <div class="luxury-glass rounded-3xl p-6 sm:p-8 space-y-6 text-center">
      <span class="text-[11px] tracking-[0.25em] uppercase text-amber-300 font-semibold">The Heritage Method</span>
      <h3 class="font-serif-luxury text-2xl sm:text-3xl text-stone-100 font-normal">Why Rockweed Seaweed Matters</h3>
      <p class="text-xs sm:text-sm text-stone-300 max-w-xl mx-auto font-light leading-relaxed">
        We do not boil our lobsters in plain tap water. Instead, they are laid over freshly cut Gulf of Maine rockweed seaweed over wood-fired steam kettles. As the salt bubbles burst, pure mineral steam infuses the sweet meat with the essence of the ocean.
      </p>
      <div class="grid grid-cols-3 gap-3 pt-4 border-t border-stone-800">
        <div>
          <p class="font-serif-luxury text-xl sm:text-2xl text-amber-300 font-bold">100%</p>
          <p class="text-[10px] text-stone-400 uppercase tracking-wider mt-0.5">Gulf Sourced</p>
        </div>
        <div>
          <p class="font-serif-luxury text-xl sm:text-2xl text-amber-300 font-bold">Hard-Shell</p>
          <p class="text-[10px] text-stone-400 uppercase tracking-wider mt-0.5">Full Meat Ratio</p>
        </div>
        <div>
          <p class="font-serif-luxury text-xl sm:text-2xl text-amber-300 font-bold">Daily</p>
          <p class="text-[10px] text-stone-400 uppercase tracking-wider mt-0.5">Harbor Delivery</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Location Concierge -->
  <section class="max-w-3xl mx-auto px-4 py-8 text-center space-y-4">
    <h4 class="font-serif-luxury text-xl text-stone-100">Joining Us From Acadia?</h4>
    <p class="text-xs text-stone-400 max-w-md mx-auto font-light leading-relaxed">
      Situated minutes from the Park Loop Road on Mount Desert Island. Casual coastal attire welcome. Easy private parking for evening dinner guests.
    </p>
    <div class="flex justify-center gap-3 pt-2">
      <a href="https://maps.google.com/?q=Bar+Harbor+Maine" target="_blank" class="border border-stone-700 hover:border-amber-400 px-5 py-2.5 rounded-full text-xs font-semibold uppercase tracking-wider text-stone-200 transition">
        📍 Open Apple / Google Maps
      </a>
      <a href="tel:2072884597" class="bg-[#dfb76c] hover:bg-[#c2964b] text-black px-5 py-2.5 rounded-full text-xs font-bold uppercase tracking-wider transition">
        📞 (207) 288-4597
      </a>
    </div>
  </section>

  <!-- Fixed Mobile VIP Concierge Bar -->
  <div class="fixed bottom-0 left-0 right-0 z-50 bg-[#040911]/95 backdrop-blur-xl border-t border-[#dfb76c]/30 p-3 px-5 flex gap-3">
    <a href="tel:2072884597" class="flex-1 bg-gradient-to-r from-[#dfb76c] to-[#c2964b] hover:from-[#f0caa0] hover:to-[#dfb76c] text-stone-950 font-bold py-3 px-4 rounded-xl text-center text-xs tracking-wider uppercase flex items-center justify-center gap-2 shadow-2xl">
      <span>📞 Call Seating</span>
    </a>
    <a href="https://maps.google.com/?q=Bar+Harbor+Maine" target="_blank" class="flex-1 bg-stone-900 border border-[#dfb76c]/40 hover:border-amber-400 text-amber-200 font-bold py-3 px-4 rounded-xl text-center text-xs tracking-wider uppercase flex items-center justify-center gap-2 shadow-2xl">
      <span>📍 GPS Navigation</span>
    </a>
  </div>

</body>
</html>
"""

# ==============================================================================
# 2. SCOFF TROFF CAFE (British Heritage Coastal Gastro-Bistro, Cornwall)
# ==============================================================================
SCOFF_TROFF_LUXURY_HTML = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Scoff Troff Cafe | Artisanal Coastal Bistro & Cornish Brunch | St Ives</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; }
    body { font-family: 'Plus Jakarta Sans', sans-serif; overflow-x: hidden; width: 100%; background-color: #071513; }
    .font-playfair { font-family: 'Playfair Display', Georgia, serif; }
    .brass-gradient {
      background: linear-gradient(135deg, #f7e0b5 0%, #d8a858 50%, #9e7530 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .luxury-sage-glass {
      background: rgba(12, 33, 29, 0.82);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(216, 168, 88, 0.22);
    }
  </style>
</head>
<body class="text-stone-200 min-h-screen flex flex-col pb-24 selection:bg-amber-400 selection:text-black">

  <!-- Top Coastal Notice -->
  <div class="bg-[#040c0b] border-b border-[#d8a858]/20 py-2 px-4 text-[11px] tracking-wider uppercase text-stone-400 flex items-center justify-between gap-2">
    <div class="truncate flex items-center gap-1.5">
      <span class="w-1.5 h-1.5 rounded-full bg-[#d8a858] animate-pulse shrink-0"></span>
      <span class="truncate">St Ives Harbour • Cornwall</span>
    </div>
    <a href="tel:+441736797341" class="shrink-0 text-amber-200 hover:text-white transition font-semibold tracking-wider flex items-center gap-1">
      <span>01736 797341</span>
    </a>
  </div>

  <!-- Header -->
  <header class="sticky top-0 z-40 bg-[#071513]/90 backdrop-blur-xl border-b border-stone-800/60 px-4 py-4">
    <div class="max-w-5xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-full border border-[#d8a858]/40 flex items-center justify-center text-amber-300 text-base bg-[#0e2722]">
          ☕
        </div>
        <div>
          <h1 class="font-playfair text-base sm:text-lg tracking-wider text-stone-100 font-bold leading-none">SCOFF TROFF</h1>
          <p class="font-playfair italic text-xs text-amber-300 tracking-widest mt-0.5">Artisan Cafe • St Ives Cornwall</p>
        </div>
      </div>
      <a href="tel:+441736797341" class="border border-[#d8a858] hover:bg-[#d8a858] hover:text-black text-amber-200 text-xs font-semibold tracking-wider px-4 py-2 rounded-full transition duration-300 uppercase">
        Table Inquiry
      </a>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="relative min-h-[560px] flex items-center justify-center px-4 py-16 overflow-hidden">
    <!-- Hero Image -->
    <div class="absolute inset-0 z-0">
      <img src="../assets/hospitality/scofftroff_hero.jpg" alt="Scoff Troff Cafe Breakfast" class="w-full h-full object-cover object-center filter brightness-75 scale-105">
      <div class="absolute inset-0 bg-gradient-to-t from-[#071513] via-[#071513]/60 to-[#071513]/80"></div>
    </div>

    <div class="relative z-10 max-w-2xl mx-auto text-center space-y-5">
      <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-stone-900/80 border border-[#d8a858]/40 text-amber-200 text-xs tracking-widest uppercase">
        <span>★ 4.6★ St Ives' Premier Independent Brunch ★</span>
      </div>

      <h2 class="font-playfair text-3xl sm:text-5xl md:text-6xl font-normal text-stone-100 leading-[1.12]">
        Proper Cornish Mornings.<br>
        <span class="italic brass-gradient">Honest Coastal Craft.</span>
      </h2>

      <p class="text-xs sm:text-sm text-stone-300 leading-relaxed font-light max-w-lg mx-auto tracking-wide">
        Tucked just off the cobblestones of St Ives harbour, where golden farmhouse breakfasts, stacked buttermilk pancakes, and Rodda’s clotted cream teas meet the morning sea salt air.
      </p>

      <!-- Badges -->
      <div class="flex flex-wrap items-center justify-center gap-2 text-[11px] uppercase tracking-wider text-amber-200">
        <span class="px-3 py-1 rounded-full luxury-sage-glass">🐾 100% Dog Friendly</span>
        <span class="px-3 py-1 rounded-full luxury-sage-glass">🌿 Cornish Farm Sourced</span>
        <span class="px-3 py-1 rounded-full luxury-sage-glass">🌾 Gluten-Free Options</span>
      </div>

      <!-- Live Service -->
      <div class="inline-flex items-center gap-3 px-4 py-2 rounded-full luxury-sage-glass text-xs text-stone-300 font-light">
        <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
        <span>Open Today: <strong class="text-amber-200 font-medium">8:30 AM – 4:00 PM (All-Day Brunch)</strong></span>
      </div>

      <!-- CTAs -->
      <div class="pt-2 flex flex-col sm:flex-row gap-3 justify-center max-w-sm mx-auto">
        <a href="tel:+441736797341" class="bg-gradient-to-r from-[#d8a858] to-[#b5873a] hover:from-[#fae0b0] hover:to-[#d8a858] text-stone-950 font-bold py-3.5 px-6 rounded-full shadow-xl transition tracking-wider text-xs uppercase flex items-center justify-center gap-2">
          <span>📞 Call Cafe: 01736 797341</span>
        </a>
        <a href="#menu" class="border border-stone-600 hover:border-amber-400/60 bg-stone-900/60 backdrop-blur-md text-stone-200 font-medium py-3.5 px-6 rounded-full transition tracking-wider text-xs uppercase flex items-center justify-center gap-2">
          <span>Explore The Menu</span>
        </a>
      </div>
    </div>
  </section>

  <!-- Editorial Accolade -->
  <section class="border-y border-stone-800/80 bg-[#091e1a] py-8 px-4 text-center">
    <div class="max-w-xl mx-auto space-y-2">
      <p class="font-playfair italic text-base sm:text-lg text-stone-300">
        “The kind of seaside haven you wish every British beach town had—unhurried, dog-welcoming, and serving breakfast plates that set you up for a day on the coastal path.”
      </p>
      <p class="text-[11px] tracking-[0.25em] uppercase text-[#d8a858]">Cornish Good Food Guide</p>
    </div>
  </section>

  <!-- Visual Menu -->
  <section id="menu" class="max-w-4xl mx-auto px-4 py-16 w-full space-y-12">
    <div class="text-center space-y-2">
      <div class="flex items-center justify-center gap-3">
        <span class="h-[1px] w-8 bg-[#d8a858]/40"></span>
        <span class="text-[11px] tracking-[0.3em] uppercase text-amber-300 font-semibold">Morning & Midday Fare</span>
        <span class="h-[1px] w-8 bg-[#d8a858]/40"></span>
      </div>
      <h3 class="font-playfair text-2xl sm:text-4xl text-stone-100 font-normal">Signature Kitchen Plates</h3>
      <p class="text-xs text-stone-400 max-w-md mx-auto font-light leading-relaxed">Cooked fresh to order using eggs from free-range Cornish hens and bakery sourdough.</p>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
      
      <!-- Dish 1 -->
      <div class="luxury-sage-glass rounded-2xl p-4 flex gap-4 items-center group hover:border-[#d8a858]/50 transition duration-300">
        <img src="../assets/hospitality/scofftroff_hero.jpg" alt="The Mighty Cornish Scoff" class="w-24 h-24 rounded-xl object-cover shrink-0 border border-stone-700">
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h5 class="font-playfair text-base text-stone-100 font-semibold group-hover:text-amber-200 transition">The Mighty Cornish Scoff</h5>
            <span class="text-amber-300 font-playfair text-lg font-bold shrink-0">£14.50</span>
          </div>
          <p class="text-xs text-stone-400 mt-1 line-clamp-2 font-light">Cornish butcher sausages, dry-cured back bacon, farm eggs, hogs pudding, beans & toast.</p>
          <span class="inline-block mt-2 text-[9px] tracking-widest uppercase text-amber-400 font-semibold">House Pride</span>
        </div>
      </div>

      <!-- Dish 2 -->
      <div class="luxury-sage-glass rounded-2xl p-4 flex gap-4 items-center group hover:border-[#d8a858]/50 transition duration-300">
        <img src="../assets/hospitality/scofftroff_pancakes.jpg" alt="Stacked Buttermilk Pancakes" class="w-24 h-24 rounded-xl object-cover shrink-0 border border-stone-700">
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h5 class="font-playfair text-base text-stone-100 font-semibold group-hover:text-amber-200 transition">Berry Burst Stacked Pancakes</h5>
            <span class="text-amber-300 font-playfair text-lg font-bold shrink-0">£11.50</span>
          </div>
          <p class="text-xs text-stone-400 mt-1 line-clamp-2 font-light">Fluffy triple buttermilk pancakes, warm wild berry compote, mascarpone & pure maple.</p>
          <span class="inline-block mt-2 text-[9px] tracking-widest uppercase text-stone-400">All-Day Sweet</span>
        </div>
      </div>

      <!-- Dish 3 -->
      <div class="luxury-sage-glass rounded-2xl p-4 flex gap-4 items-center group hover:border-[#d8a858]/50 transition duration-300">
        <img src="../assets/hospitality/scofftroff_burger.jpg" alt="St Ives Harbour Smash Burger" class="w-24 h-24 rounded-xl object-cover shrink-0 border border-stone-700">
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h5 class="font-playfair text-base text-stone-100 font-semibold group-hover:text-amber-200 transition">St Ives Harbour Beef Burger</h5>
            <span class="text-amber-300 font-playfair text-lg font-bold shrink-0">£15.00</span>
          </div>
          <p class="text-xs text-stone-400 mt-1 line-clamp-2 font-light">Dry-aged Cornish beef patties, mature Davidstow cheddar, house bacon jam & rosemary chips.</p>
          <span class="inline-block mt-2 text-[9px] tracking-widest uppercase text-amber-400 font-semibold">Lunch Favourite</span>
        </div>
      </div>

      <!-- Dish 4 -->
      <div class="luxury-sage-glass rounded-2xl p-4 flex gap-4 items-center group hover:border-[#d8a858]/50 transition duration-300">
        <img src="../assets/hospitality/scofftroff_cream_tea.jpg" alt="Traditional Cornish Cream Tea" class="w-24 h-24 rounded-xl object-cover shrink-0 border border-stone-700">
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h5 class="font-playfair text-base text-stone-100 font-semibold group-hover:text-amber-200 transition">Traditional Cornish Cream Tea</h5>
            <span class="text-amber-300 font-playfair text-lg font-bold shrink-0">£7.50</span>
          </div>
          <p class="text-xs text-stone-400 mt-1 line-clamp-2 font-light">Two warm buttermilk scones, thick Rodda's Cornish clotted cream & Boddington’s jam (Jam first!).</p>
          <span class="inline-block mt-2 text-[9px] tracking-widest uppercase text-stone-400">Cornish Classic</span>
        </div>
      </div>

    </div>
  </section>

  <!-- Location Concierge -->
  <section class="max-w-3xl mx-auto px-4 py-8 text-center space-y-4">
    <h4 class="font-playfair text-xl text-stone-100">Finding Us on Fore Street</h4>
    <p class="text-xs text-stone-400 max-w-md mx-auto font-light leading-relaxed">
      A 60-second stroll from St Ives Harbour Beach. Dogs of all sizes always welcome with fresh water bowls provided.
    </p>
    <div class="flex justify-center gap-3 pt-2">
      <a href="https://maps.google.com/?q=Scoff+Troff+Cafe+St+Ives" target="_blank" class="border border-stone-700 hover:border-amber-400 px-5 py-2.5 rounded-full text-xs font-semibold uppercase tracking-wider text-stone-200 transition">
        📍 Google Maps Navigation
      </a>
      <a href="tel:+441736797341" class="bg-[#d8a858] hover:bg-[#b5873a] text-black px-5 py-2.5 rounded-full text-xs font-bold uppercase tracking-wider transition">
        📞 01736 797341
      </a>
    </div>
  </section>

  <!-- Fixed Mobile Bar -->
  <div class="fixed bottom-0 left-0 right-0 z-50 bg-[#071513]/95 backdrop-blur-xl border-t border-[#d8a858]/30 p-3 px-5 flex gap-3">
    <a href="tel:+441736797341" class="flex-1 bg-gradient-to-r from-[#d8a858] to-[#b5873a] hover:from-[#fae0b0] hover:to-[#d8a858] text-stone-950 font-bold py-3 px-4 rounded-xl text-center text-xs tracking-wider uppercase flex items-center justify-center gap-2 shadow-2xl">
      <span>📞 Call Cafe</span>
    </a>
    <a href="https://maps.google.com/?q=Scoff+Troff+Cafe+St+Ives" target="_blank" class="flex-1 bg-stone-900 border border-[#d8a858]/40 hover:border-amber-400 text-amber-200 font-bold py-3 px-4 rounded-xl text-center text-xs tracking-wider uppercase flex items-center justify-center gap-2 shadow-2xl">
      <span>📍 St Ives Directions</span>
    </a>
  </div>

</body>
</html>
"""

# ==============================================================================
# 3. DIP CAFE (Sun-Drenched French Riviera Meets Byron Bay Coastal Luxury)
# ==============================================================================
DIP_CAFE_LUXURY_HTML = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Dip Cafe | Parisian Artisanal Bistro & Byron Bay Sunshine</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Italiana&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; }
    body { font-family: 'Plus Jakarta Sans', sans-serif; overflow-x: hidden; width: 100%; background-color: #0e0a08; }
    .font-italiana { font-family: 'Italiana', serif; }
    .font-serif-luxury { font-family: 'Playfair Display', Georgia, serif; }
    .luxury-terracotta-glass {
      background: rgba(24, 18, 14, 0.84);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(200, 90, 50, 0.28);
    }
  </style>
</head>
<body class="text-stone-200 min-h-screen flex flex-col pb-24 selection:bg-[#c85a32] selection:text-white">

  <!-- Top Announcement -->
  <div class="bg-[#080504] border-b border-[#c85a32]/20 py-2 px-4 text-[11px] tracking-wider uppercase text-stone-400 flex items-center justify-between gap-2">
    <div class="truncate flex items-center gap-1.5">
      <span class="w-1.5 h-1.5 rounded-full bg-[#c85a32] animate-pulse shrink-0"></span>
      <span class="truncate">Byron Bay • Fletcher St</span>
    </div>
    <a href="tel:+61266808864" class="shrink-0 text-amber-200 hover:text-white transition font-semibold tracking-wider flex items-center gap-1">
      <span>(02) 6680 8864</span>
    </a>
  </div>

  <!-- Header -->
  <header class="sticky top-0 z-40 bg-[#0e0a08]/90 backdrop-blur-xl border-b border-stone-800/80 px-4 py-4">
    <div class="max-w-5xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-full bg-[#c85a32] flex items-center justify-center text-white font-italiana text-xl font-bold shadow-md">
          D
        </div>
        <div>
          <h1 class="font-italiana text-lg tracking-[0.2em] text-stone-100 font-bold leading-none">DIP CAFE</h1>
          <p class="font-serif-luxury italic text-xs text-[#e08358] tracking-widest mt-0.5">Bistrot Français • Byron Bay</p>
        </div>
      </div>
      <a href="tel:+61266808864" class="border border-[#c85a32] hover:bg-[#c85a32] hover:text-white text-amber-200 text-xs font-semibold tracking-wider px-4 py-2 rounded-full transition duration-300 uppercase">
        Table Enquiry
      </a>
    </div>
  </header>

  <!-- Hero: Sunlit Riviera Elegance with Dark Luxury Glass Card -->
  <section class="relative min-h-[580px] flex items-center justify-center px-4 py-16 overflow-hidden">
    <!-- Hero Image Background -->
    <div class="absolute inset-0 z-0">
      <img src="../assets/hospitality/dipcafe_hero.jpg" alt="Dip Cafe French Toast" class="w-full h-full object-cover object-center filter brightness-75 scale-105">
      <div class="absolute inset-0 bg-gradient-to-t from-[#0e0a08] via-[#0e0a08]/60 to-[#0e0a08]/80"></div>
    </div>

    <div class="relative z-10 max-w-xl mx-auto text-center space-y-4 luxury-terracotta-glass p-6 sm:p-8 rounded-3xl shadow-2xl">
      <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-stone-900/90 border border-[#c85a32]/40 text-amber-200 text-[11px] tracking-widest uppercase shadow-sm">
        <span>★ 4.5★ Byron Bay's Beloved French Kitchen ★</span>
      </div>

      <h2 class="font-italiana text-3xl sm:text-5xl text-stone-100 font-normal leading-[1.12] tracking-wide">
        Parisian Craftsmanship.<br>
        <span class="font-serif-luxury italic text-[#e08358]">Byron Bay Sunshine.</span>
      </h2>

      <p class="text-xs sm:text-sm text-stone-300 leading-relaxed font-light max-w-md mx-auto tracking-wide">
        Golden house-baked brioche French toast, slow-simmered Mediterranean shakshuka skillets, and silky Allpress espresso on sun-drenched Fletcher Street.
      </p>

      <!-- Provenance Badges -->
      <div class="flex flex-wrap items-center justify-center gap-1.5 text-[10px] uppercase tracking-wider text-stone-200 font-medium">
        <span class="px-2.5 py-1 rounded-full bg-stone-900/80 border border-stone-700 shadow-sm">🥖 House Brioche</span>
        <span class="px-2.5 py-1 rounded-full bg-stone-900/80 border border-stone-700 shadow-sm">🥑 Local Organic</span>
        <span class="px-2.5 py-1 rounded-full bg-stone-900/80 border border-stone-700 shadow-sm">☕ Allpress Roast</span>
      </div>

      <!-- Live Service -->
      <div class="inline-flex items-center gap-2.5 px-3.5 py-1.5 rounded-full bg-stone-900/80 border border-stone-700 text-xs text-stone-300 font-light shadow-sm">
        <span class="w-2 h-2 rounded-full bg-emerald-400 shrink-0"></span>
        <span>Open Daily: <strong class="text-amber-200 font-medium">7:00 AM – 2:30 PM</strong></span>
      </div>

      <!-- CTAs -->
      <div class="pt-2 flex flex-col sm:flex-row gap-2.5 justify-center max-w-sm mx-auto">
        <a href="tel:+61266808864" class="bg-gradient-to-r from-[#c85a32] to-[#a23f1b] hover:from-[#e0754e] hover:to-[#c85a32] text-white font-bold py-3 px-5 rounded-full shadow-lg transition tracking-wider text-xs uppercase flex items-center justify-center gap-2">
          <span>📞 Call Dip: (02) 6680 8864</span>
        </a>
        <a href="#menu" class="bg-stone-900/80 hover:bg-stone-800 border border-stone-700 text-stone-200 font-semibold py-3 px-5 rounded-full transition tracking-wider text-xs uppercase flex items-center justify-center gap-2 shadow-sm">
          <span>Visual Brunch Menu</span>
        </a>
      </div>
    </div>
  </section>

  <!-- Editorial Accolade -->
  <section class="border-y border-stone-800/80 bg-[#140f0c] py-8 px-4 text-center">
    <div class="max-w-xl mx-auto space-y-2">
      <p class="font-serif-luxury italic text-base sm:text-lg text-stone-300">
        “A chic French seaside bistro bathed in sub-tropical Byron light. The brioche is transcendent and the vibe is effortlessly stylish.”
      </p>
      <p class="text-[11px] tracking-[0.25em] uppercase text-[#e08358] font-bold">Broadsheet Australia</p>
    </div>
  </section>

  <!-- Visual Menu -->
  <section id="menu" class="max-w-4xl mx-auto px-4 py-16 w-full space-y-12">
    <div class="text-center space-y-2">
      <div class="flex items-center justify-center gap-3">
        <span class="h-[1px] w-8 bg-[#c85a32]/40"></span>
        <span class="text-[11px] tracking-[0.3em] uppercase text-amber-300 font-bold">Petit Déjeuner & Déjeuner</span>
        <span class="h-[1px] w-8 bg-[#c85a32]/40"></span>
      </div>
      <h3 class="font-italiana text-3xl sm:text-4xl text-stone-100 font-normal">Morning Culinary Highlights</h3>
      <p class="text-xs text-stone-400 max-w-md mx-auto font-light leading-relaxed">Honouring traditional French recipes infused with pristine Byron Hinterland harvest.</p>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
      
      <!-- Dish 1 -->
      <div class="luxury-terracotta-glass rounded-2xl p-4 flex gap-4 items-center group hover:border-[#c85a32]/60 transition duration-300">
        <img src="../assets/hospitality/dipcafe_hero.jpg" alt="Brioche French Toast" class="w-24 h-24 rounded-xl object-cover shrink-0 border border-stone-700">
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h5 class="font-serif-luxury text-base text-stone-100 font-semibold group-hover:text-amber-200 transition">Brioche French Toast with Byron Honey</h5>
            <span class="text-amber-300 font-serif-luxury text-lg font-bold shrink-0">A$24</span>
          </div>
          <p class="text-xs text-stone-400 mt-1 line-clamp-2 font-light">House-baked golden brioche, caramelized bananas, mixed forest berries & honeycomb crumble.</p>
          <span class="inline-block mt-2 text-[9px] tracking-widest uppercase text-amber-400 font-bold">Signature</span>
        </div>
      </div>

      <!-- Dish 2 -->
      <div class="luxury-terracotta-glass rounded-2xl p-4 flex gap-4 items-center group hover:border-[#c85a32]/60 transition duration-300">
        <img src="../assets/hospitality/dipcafe_shakshuka.jpg" alt="Baked Eggs Shakshuka" class="w-24 h-24 rounded-xl object-cover shrink-0 border border-stone-700">
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h5 class="font-serif-luxury text-base text-stone-100 font-semibold group-hover:text-amber-200 transition">Baked Eggs Shakshuka Skillet</h5>
            <span class="text-amber-300 font-serif-luxury text-lg font-bold shrink-0">A$23</span>
          </div>
          <p class="text-xs text-stone-400 mt-1 line-clamp-2 font-light">Spiced Mediterranean sugo, free-range poached eggs, Meredith Dairy goat feta & sourdough.</p>
          <span class="inline-block mt-2 text-[9px] tracking-widest uppercase text-stone-400">Warm & Spiced</span>
        </div>
      </div>

      <!-- Dish 3 -->
      <div class="luxury-terracotta-glass rounded-2xl p-4 flex gap-4 items-center group hover:border-[#c85a32]/60 transition duration-300">
        <img src="../assets/hospitality/dipcafe_avotoast.jpg" alt="Northern Rivers Smashed Avo" class="w-24 h-24 rounded-xl object-cover shrink-0 border border-stone-700">
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h5 class="font-serif-luxury text-base text-stone-100 font-semibold group-hover:text-amber-200 transition">Northern Rivers Smashed Avo</h5>
            <span class="text-amber-300 font-serif-luxury text-lg font-bold shrink-0">A$21</span>
          </div>
          <p class="text-xs text-stone-400 mt-1 line-clamp-2 font-light">Local Hass avocado, marinated chevre, house toasted Egyptian dukkah & fresh lemon.</p>
          <span class="inline-block mt-2 text-[9px] tracking-widest uppercase text-stone-400">Byron Staple</span>
        </div>
      </div>

      <!-- Dish 4 -->
      <div class="luxury-terracotta-glass rounded-2xl p-4 flex gap-4 items-center group hover:border-[#c85a32]/60 transition duration-300">
        <img src="../assets/hospitality/dipcafe_flatwhite.jpg" alt="Allpress Flat White" class="w-24 h-24 rounded-xl object-cover shrink-0 border border-stone-700">
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h5 class="font-serif-luxury text-base text-stone-100 font-semibold group-hover:text-amber-200 transition">Allpress Specialty Roast</h5>
            <span class="text-amber-300 font-serif-luxury text-lg font-bold shrink-0">from A$5</span>
          </div>
          <p class="text-xs text-stone-400 mt-1 line-clamp-2 font-light">Double-shot espresso, silky organic milk, single-origin cold brews, and ceremonial matcha.</p>
          <span class="inline-block mt-2 text-[9px] tracking-widest uppercase text-amber-400 font-bold">Barista Pull</span>
        </div>
      </div>

    </div>
  </section>

  <!-- Location Concierge -->
  <section class="max-w-3xl mx-auto px-4 py-8 text-center space-y-4">
    <h4 class="font-italiana text-2xl text-stone-100">21 Fletcher Street, Byron Bay</h4>
    <p class="text-xs text-stone-400 max-w-md mx-auto font-light leading-relaxed">
      Steps from Main Beach. Sunlit outdoor Parisian terrace and shaded indoor bistro seating.
    </p>
    <div class="flex justify-center gap-3 pt-2">
      <a href="https://maps.google.com/?q=Dip+Cafe+Byron+Bay" target="_blank" class="border border-stone-700 hover:border-amber-400 px-5 py-2.5 rounded-full text-xs font-semibold uppercase tracking-wider text-stone-200 transition">
        📍 Google Maps Navigation
      </a>
      <a href="tel:+61266808864" class="bg-[#c85a32] hover:bg-[#a23f1b] text-white px-5 py-2.5 rounded-full text-xs font-bold uppercase tracking-wider transition">
        📞 (02) 6680 8864
      </a>
    </div>
  </section>

  <!-- Fixed Mobile Bar -->
  <div class="fixed bottom-0 left-0 right-0 z-50 bg-[#0e0a08]/95 backdrop-blur-xl border-t border-[#c85a32]/30 p-3 px-5 flex gap-3">
    <a href="tel:+61266808864" class="flex-1 bg-gradient-to-r from-[#c85a32] to-[#a23f1b] hover:from-[#e0754e] hover:to-[#c85a32] text-white font-bold py-3 px-4 rounded-xl text-center text-xs tracking-wider uppercase flex items-center justify-center gap-2 shadow-xl">
      <span>📞 Call Table</span>
    </a>
    <a href="https://maps.google.com/?q=Dip+Cafe+Byron+Bay" target="_blank" class="flex-1 bg-stone-900 border border-[#c85a32]/40 hover:border-amber-400 text-amber-200 font-bold py-3 px-4 rounded-xl text-center text-xs tracking-wider uppercase flex items-center justify-center gap-2 shadow-xl">
      <span>📍 Fletcher St Directions</span>
    </a>
  </div>

</body>
</html>
"""

FILES = [
    # 1. Bar Harbor Lobster Bakes
    (BASE_DIR / "barharborlobster" / "index.html", BAR_HARBOR_LUXURY_HTML),
    (BASE_DIR / "03_DEMOS" / "10_bar_harbor_lobster" / "index.html", BAR_HARBOR_LUXURY_HTML),
    
    # 2. Scoff Troff Cafe
    (BASE_DIR / "scofftroff" / "index.html", SCOFF_TROFF_LUXURY_HTML),
    (BASE_DIR / "03_DEMOS" / "11_scoff_troff_cafe" / "index.html", SCOFF_TROFF_LUXURY_HTML),

    # 3. Dip Cafe
    (BASE_DIR / "dipcafe" / "index.html", DIP_CAFE_LUXURY_HTML),
    (BASE_DIR / "03_DEMOS" / "12_dip_cafe_byron" / "index.html", DIP_CAFE_LUXURY_HTML),
]

for file_path, content in FILES:
    file_path.parent.mkdir(parents=True, exist_ok=True)
    adjusted_content = content
    if "03_DEMOS" in str(file_path):
        adjusted_content = adjusted_content.replace("../assets/hospitality/", "../../assets/hospitality/")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(adjusted_content)
    print(f"Generated High-End Luxury Demo: {file_path.relative_to(BASE_DIR)}")

print("All 3 hospitality demos elevated to ultra-luxury editorial standard!")
