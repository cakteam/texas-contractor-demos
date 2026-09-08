#!/usr/bin/env python3
"""
gen_hospitality_demos.py — Generate high-end, responsive, mobile-hardened prototypes
for the three pilot tourist hospitality destinations:
1. Bar Harbor Lobster Bakes (Maine, US)
2. Scoff Troff Cafe (St Ives, Cornwall, UK)
3. Dip Cafe (Byron Bay, NSW, Australia)
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 1. Bar Harbor Lobster Bakes HTML
BAR_HARBOR_HTML = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Bar Harbor Lobster Bakes | Authentic Downeast Maine Seafood</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; }
    body { font-family: 'Inter', sans-serif; overflow-x: hidden; width: 100%; }
    .font-serif-heading { font-family: 'Cinzel', serif; }
    .glass-card { background: rgba(13, 33, 62, 0.85); backdrop-filter: blur(12px); border: 1px solid rgba(212, 175, 55, 0.25); }
    .glow-gold { box-shadow: 0 0 25px rgba(230, 161, 34, 0.25); }
  </style>
</head>
<body class="bg-[#071322] text-slate-100 min-h-screen flex flex-col pb-20">

  <!-- Top Announcement Bar -->
  <div class="bg-[#0b1d3a] border-b border-amber-500/20 py-2 px-4 text-xs font-medium text-amber-300 flex items-center justify-between">
    <div class="truncate flex items-center gap-1.5">
      <span class="inline-block w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
      <span class="truncate">🌲 Acadia National Park Gateway • Bar Harbor, Maine</span>
    </div>
    <a href="tel:2072884597" class="shrink-0 font-bold hover:text-white transition flex items-center gap-1">
      <span>📞 (207) 288-4597</span>
    </a>
  </div>

  <!-- Header -->
  <header class="sticky top-0 z-40 bg-[#071322]/95 backdrop-blur-md border-b border-slate-800/80 px-4 py-3">
    <div class="max-w-4xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-lg bg-gradient-to-br from-red-600 to-red-800 flex items-center justify-center text-white text-xl shadow-md font-bold">
          🦞
        </div>
        <div>
          <h1 class="font-serif-heading text-base sm:text-lg font-bold tracking-wide text-white leading-tight">BAR HARBOR</h1>
          <p class="text-[10px] tracking-widest text-amber-400 uppercase font-semibold">Lobster Bakes & Co.</p>
        </div>
      </div>
      <a href="tel:2072884597" class="bg-red-600 hover:bg-red-500 text-white text-xs sm:text-sm font-semibold px-3 sm:px-4 py-2 rounded-full shadow transition flex items-center gap-1.5">
        <span>Call Seating</span>
      </a>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="relative px-4 pt-6 pb-8 overflow-hidden">
    <div class="max-w-3xl mx-auto text-center">
      <!-- Tag -->
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-300 text-xs font-semibold mb-4">
        <span>⭐ 4.7★ Down-East Maine Tradition</span>
      </div>

      <!-- Headline -->
      <h2 class="font-serif-heading text-2xl sm:text-4xl font-extrabold text-white leading-tight mb-3">
        Steamed Over Seaweed.<br>
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-red-400 via-amber-300 to-amber-500">
          Pure Gulf of Maine Lobster.
        </span>
      </h2>

      <!-- Subtitle -->
      <p class="text-xs sm:text-sm text-slate-300 leading-relaxed max-w-xl mx-auto mb-5">
        After exploring Acadia’s granite peaks, sit down to authentic Maine hard-shell lobsters, sweet native steamer clams, sweet corn, and hot drawn butter served under coastal pines.
      </p>

      <!-- Live Service Badge -->
      <div class="glass-card rounded-xl p-3 max-w-md mx-auto mb-6 flex items-center justify-center gap-3 text-xs">
        <span class="flex h-3 w-3 relative">
          <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
          <span class="relative inline-flex rounded-full h-3 w-3 bg-emerald-500"></span>
        </span>
        <span class="font-medium text-slate-200">Tonight's Dinner Service: <strong class="text-amber-300">4:30 PM – 9:00 PM</strong></span>
      </div>

      <!-- Hero Actions -->
      <div class="flex flex-col sm:flex-row gap-3 justify-center max-w-sm mx-auto">
        <a href="tel:2072884597" class="w-full bg-gradient-to-r from-red-600 to-red-700 hover:from-red-500 hover:to-red-600 text-white font-bold py-3 px-6 rounded-xl shadow-lg transition flex items-center justify-center gap-2 text-sm">
          <span>📞 Call for Table: (207) 288-4597</span>
        </a>
        <a href="#menu" class="w-full bg-slate-800 hover:bg-slate-700 text-amber-300 border border-amber-400/30 font-semibold py-3 px-6 rounded-xl transition flex items-center justify-center gap-2 text-sm">
          <span>🦞 Explore Tonight's Bakes</span>
        </a>
      </div>
    </div>
  </section>

  <!-- Featured Dish Visual Carousel -->
  <section class="px-4 py-4 max-w-4xl mx-auto w-full">
    <div class="relative rounded-2xl overflow-hidden border border-amber-500/30 shadow-2xl">
      <img src="../assets/hospitality/barharbor_hero.jpg" alt="Bar Harbor Traditional Lobster Bake" class="w-full h-64 sm:h-80 object-cover">
      <div class="absolute inset-0 bg-gradient-to-t from-[#071322] via-transparent to-transparent"></div>
      <div class="absolute bottom-4 left-4 right-4">
        <span class="bg-red-600 text-white text-[10px] font-bold uppercase tracking-wider px-2.5 py-1 rounded">House Signature</span>
        <h3 class="font-serif-heading text-lg sm:text-xl font-bold text-white mt-1">The Traditional Acadia Lobster Bake</h3>
        <p class="text-xs text-slate-300">Live Maine Lobster, Steamer Clams, Local Sweet Corn, Baby Red Potatoes & Drawn Butter.</p>
      </div>
    </div>
  </section>

  <!-- Visual Menu Section -->
  <section id="menu" class="px-4 py-8 max-w-4xl mx-auto w-full">
    <div class="text-center mb-6">
      <span class="text-amber-400 text-xs uppercase tracking-widest font-semibold">Fresh From The Harbor</span>
      <h3 class="font-serif-heading text-xl sm:text-2xl font-bold text-white mt-1">Tonight's Culinary Highlights</h3>
      <p class="text-xs text-slate-400 mt-1">Wild-caught Maine shellfish delivered fresh daily from local boat captains.</p>
    </div>

    <!-- Dishes Grid -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
      
      <!-- Dish 1 -->
      <div class="glass-card rounded-xl p-3.5 flex gap-3.5 items-center">
        <img src="../assets/hospitality/barharbor_lobster_roll.jpg" alt="Maine Lobster Roll" class="w-20 h-20 rounded-lg object-cover shrink-0 border border-amber-500/20">
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h4 class="font-semibold text-sm text-white truncate">Overstuffed Maine Lobster Roll</h4>
            <span class="text-amber-400 font-bold text-sm shrink-0">$32</span>
          </div>
          <p class="text-xs text-slate-400 mt-1 line-clamp-2">Warm buttered brioche roll packed with sweet claw and knuckle meat, light sea salt.</p>
          <span class="inline-block mt-1 text-[10px] bg-red-950 text-red-300 border border-red-800 px-2 py-0.5 rounded font-medium">Top Seller</span>
        </div>
      </div>

      <!-- Dish 2 -->
      <div class="glass-card rounded-xl p-3.5 flex gap-3.5 items-center">
        <img src="../assets/hospitality/barharbor_chowder.jpg" alt="New England Clam Chowder" class="w-20 h-20 rounded-lg object-cover shrink-0 border border-amber-500/20">
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h4 class="font-semibold text-sm text-white truncate">Coastal Clam Chowder</h4>
            <span class="text-amber-400 font-bold text-sm shrink-0">$12</span>
          </div>
          <p class="text-xs text-slate-400 mt-1 line-clamp-2">Rich cream, sweet sea clams, tender potatoes, and Applewood bacon. Served with oyster crackers.</p>
          <span class="inline-block mt-1 text-[10px] bg-blue-950 text-blue-300 border border-blue-800 px-2 py-0.5 rounded font-medium">Gluten-Free Option</span>
        </div>
      </div>

      <!-- Dish 3 -->
      <div class="glass-card rounded-xl p-3.5 flex gap-3.5 items-center">
        <img src="../assets/hospitality/barharbor_steamers.jpg" alt="Steamed Maine Clams" class="w-20 h-20 rounded-lg object-cover shrink-0 border border-amber-500/20">
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h4 class="font-semibold text-sm text-white truncate">Native Steamer Clams Bucket</h4>
            <span class="text-amber-400 font-bold text-sm shrink-0">$22</span>
          </div>
          <p class="text-xs text-slate-400 mt-1 line-clamp-2">Full pound of sweet soft-shell clams steamed in Atlantic sea broth, served with clarified hot butter.</p>
          <span class="inline-block mt-1 text-[10px] bg-emerald-950 text-emerald-300 border border-emerald-800 px-2 py-0.5 rounded font-medium">Local Harvest</span>
        </div>
      </div>

      <!-- Dish 4 -->
      <div class="glass-card rounded-xl p-3.5 flex gap-3.5 items-center">
        <img src="../assets/hospitality/barharbor_blueberry_pie.jpg" alt="Wild Maine Blueberry Pie" class="w-20 h-20 rounded-lg object-cover shrink-0 border border-amber-500/20">
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h4 class="font-semibold text-sm text-white truncate">Wild Maine Blueberry Pie</h4>
            <span class="text-amber-400 font-bold text-sm shrink-0">$9</span>
          </div>
          <p class="text-xs text-slate-400 mt-1 line-clamp-2">Hand-picked mountain blueberries in a golden flaky butter crust, topped with vanilla bean gelato.</p>
          <span class="inline-block mt-1 text-[10px] bg-amber-950 text-amber-300 border border-amber-800 px-2 py-0.5 rounded font-medium">Homemade Daily</span>
        </div>
      </div>

    </div>
  </section>

  <!-- Interactive Lobster Bake Cost Calculator -->
  <section class="px-4 py-6 max-w-2xl mx-auto w-full">
    <div class="glass-card rounded-2xl p-5 border border-amber-500/30">
      <div class="text-center mb-4">
        <span class="text-amber-400 text-xs font-semibold uppercase tracking-wider">Party Seating Estimator</span>
        <h3 class="font-serif-heading text-lg font-bold text-white mt-1">Estimate Tonight's Lobster Bake</h3>
      </div>

      <div class="space-y-4">
        <div>
          <label class="block text-xs text-slate-300 font-medium mb-1">Number of Guests in Party</label>
          <div class="grid grid-cols-4 gap-2">
            <button onclick="setGuests(2)" class="guest-btn bg-slate-800 hover:bg-slate-700 py-2 rounded-lg text-xs font-semibold border border-slate-700 active:border-amber-400">2 People</button>
            <button onclick="setGuests(4)" class="guest-btn bg-amber-500/20 text-amber-300 py-2 rounded-lg text-xs font-semibold border border-amber-500">4 People</button>
            <button onclick="setGuests(6)" class="guest-btn bg-slate-800 hover:bg-slate-700 py-2 rounded-lg text-xs font-semibold border border-slate-700">6 People</button>
            <button onclick="setGuests(8)" class="guest-btn bg-slate-800 hover:bg-slate-700 py-2 rounded-lg text-xs font-semibold border border-slate-700">8+ Family</button>
          </div>
        </div>

        <div>
          <label class="block text-xs text-slate-300 font-medium mb-1">Preferred Lobster Bake Style</label>
          <select id="bakeType" onchange="calculateBake()" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-xs text-slate-200">
            <option value="48">Traditional 1¼ lb Acadia Lobster Bake ($48/person)</option>
            <option value="62">The Downeast Feast with Chowder & Pie ($62/person)</option>
            <option value="38">Twin Warm Buttered Lobster Rolls Combo ($38/person)</option>
          </select>
        </div>

        <div class="bg-slate-900/80 rounded-xl p-3 flex items-center justify-between border border-slate-800">
          <div>
            <p class="text-[11px] text-slate-400">Estimated Total for Party:</p>
            <p class="text-xl font-bold text-amber-400 font-serif-heading" id="totalEstimate">$248.00</p>
          </div>
          <a href="tel:2072884597" class="bg-red-600 hover:bg-red-500 text-white text-xs font-bold px-4 py-2.5 rounded-lg shadow transition">
            Call Seating
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- Directions & Hours -->
  <section class="px-4 py-6 max-w-3xl mx-auto w-full">
    <div class="bg-slate-900/60 rounded-2xl p-5 border border-slate-800 text-center">
      <h4 class="font-serif-heading text-base font-bold text-white mb-2">Visiting Bar Harbor & Acadia?</h4>
      <p class="text-xs text-slate-300 max-w-md mx-auto mb-4">
        Located right on Mount Desert Island, minutes from the Park Loop Road. Easy on-site parking for families and hiking groups.
      </p>
      <div class="flex flex-col sm:flex-row gap-3 justify-center text-xs">
        <a href="https://maps.google.com/?q=Bar+Harbor+Maine" target="_blank" class="bg-slate-800 hover:bg-slate-700 text-white py-2.5 px-5 rounded-lg border border-slate-700 flex items-center justify-center gap-1.5">
          <span>📍 Open in Google Maps</span>
        </a>
        <a href="tel:2072884597" class="bg-amber-600 hover:bg-amber-500 text-white py-2.5 px-5 rounded-lg font-semibold flex items-center justify-center gap-1.5">
          <span>📞 (207) 288-4597</span>
        </a>
      </div>
    </div>
  </section>

  <!-- Sticky Bottom Mobile Bar -->
  <div class="fixed bottom-0 left-0 right-0 z-50 bg-[#071322]/95 backdrop-blur-md border-t border-slate-800 p-2.5 px-4 flex gap-3">
    <a href="tel:2072884597" class="flex-1 bg-red-600 hover:bg-red-500 text-white font-bold py-2.5 px-3 rounded-xl text-center text-xs sm:text-sm flex items-center justify-center gap-1.5 shadow-lg">
      <span>📞 Call Seating</span>
    </a>
    <a href="https://maps.google.com/?q=Bar+Harbor+Maine" target="_blank" class="flex-1 bg-amber-600 hover:bg-amber-500 text-white font-bold py-2.5 px-3 rounded-xl text-center text-xs sm:text-sm flex items-center justify-center gap-1.5 shadow-lg">
      <span>📍 GPS Directions</span>
    </a>
  </div>

  <script>
    let currentGuests = 4;
    function setGuests(num) {
      currentGuests = num;
      document.querySelectorAll('.guest-btn').forEach(btn => {
        btn.classList.remove('bg-amber-500/20', 'text-amber-300', 'border-amber-500');
        btn.classList.add('bg-slate-800', 'text-slate-100', 'border-slate-700');
      });
      event.target.classList.remove('bg-slate-800', 'text-slate-100', 'border-slate-700');
      event.target.classList.add('bg-amber-500/20', 'text-amber-300', 'border-amber-500');
      calculateBake();
    }
    function calculateBake() {
      const perPerson = parseInt(document.getElementById('bakeType').value);
      const total = perPerson * currentGuests;
      document.getElementById('totalEstimate').innerText = '$' + total + '.00';
    }
  </script>
</body>
</html>
"""

# 2. Scoff Troff Cafe HTML (St Ives, Cornwall)
SCOFF_TROFF_HTML = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Scoff Troff Cafe | Artisan Brunch & Coastal Burgers | St Ives Cornwall</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; }
    body { font-family: 'Outfit', sans-serif; overflow-x: hidden; width: 100%; }
    .font-serif-heading { font-family: 'Playfair Display', serif; }
    .glass-card { background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); }
  </style>
</head>
<body class="bg-[#0e2730] text-slate-100 min-h-screen flex flex-col pb-20">

  <!-- Top Notice Bar -->
  <div class="bg-[#091a20] border-b border-teal-500/20 py-2 px-4 text-xs font-medium text-teal-300 flex items-center justify-between">
    <div class="truncate flex items-center gap-1.5">
      <span>🐾 St Ives Harbour • Dog-Friendly Coastal Cafe</span>
    </div>
    <a href="tel:+441736797341" class="shrink-0 font-bold hover:text-white transition">
      <span>📞 01736 797341</span>
    </a>
  </div>

  <!-- Header -->
  <header class="sticky top-0 z-40 bg-[#0e2730]/95 backdrop-blur-md border-b border-teal-800/40 px-4 py-3">
    <div class="max-w-4xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-2.5">
        <div class="w-10 h-10 rounded-full bg-amber-500 flex items-center justify-center text-xl shadow">
          ☕
        </div>
        <div>
          <h1 class="font-serif-heading text-base sm:text-lg font-bold text-white leading-tight">SCOFF TROFF</h1>
          <p class="text-[10px] tracking-widest text-teal-400 uppercase font-semibold">Cafe • St Ives Cornwall</p>
        </div>
      </div>
      <a href="tel:+441736797341" class="bg-amber-500 hover:bg-amber-400 text-slate-950 text-xs sm:text-sm font-bold px-3.5 py-1.5 rounded-full shadow transition">
        Call Cafe
      </a>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="px-4 pt-6 pb-6 max-w-3xl mx-auto text-center">
    <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-teal-500/20 border border-teal-500/40 text-teal-300 text-xs font-semibold mb-3">
      <span>⭐ 4.6★ St Ives Independent Favourite</span>
    </div>

    <h2 class="font-serif-heading text-2xl sm:text-4xl font-extrabold text-white leading-tight mb-3">
      Proper Cornish Mornings.<br>
      <span class="text-transparent bg-clip-text bg-gradient-to-r from-amber-300 to-amber-500">
        Hearty Coastal Feasts.
      </span>
    </h2>

    <p class="text-xs sm:text-sm text-slate-300 leading-relaxed max-w-lg mx-auto mb-4">
      Sizzling farmhouse breakfasts, fluffy stacked buttermilk pancakes, artisan Cornish smash burgers, and traditional clotted cream teas—tucked just off St Ives harbour.
    </p>

    <!-- Key Badges -->
    <div class="flex flex-wrap items-center justify-center gap-2 mb-5 text-[11px] font-medium text-teal-200">
      <span class="bg-teal-950/80 border border-teal-700/50 px-2.5 py-1 rounded-full">🐾 100% Dog Friendly</span>
      <span class="bg-teal-950/80 border border-teal-700/50 px-2.5 py-1 rounded-full">🌿 Vegan & Veggie Options</span>
      <span class="bg-teal-950/80 border border-teal-700/50 px-2.5 py-1 rounded-full">🌾 Gluten-Free Available</span>
    </div>

    <!-- Live Status -->
    <div class="glass-card rounded-xl p-3 max-w-md mx-auto mb-5 flex items-center justify-center gap-2.5 text-xs">
      <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
      <span class="text-slate-200 font-medium">Open Today: <strong class="text-amber-300">8:30 AM – 4:00 PM</strong> (All-Day Brunch)</span>
    </div>

    <div class="flex flex-col sm:flex-row gap-3 justify-center max-w-sm mx-auto">
      <a href="tel:+441736797341" class="bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-2.5 px-5 rounded-xl shadow-lg transition text-xs sm:text-sm flex items-center justify-center gap-1.5">
        <span>📞 Call Table: 01736 797341</span>
      </a>
      <a href="#brunch-menu" class="bg-teal-900/60 hover:bg-teal-800/80 text-teal-200 border border-teal-600/40 font-semibold py-2.5 px-5 rounded-xl transition text-xs sm:text-sm flex items-center justify-center gap-1.5">
        <span>🥞 View Visual Menu</span>
      </a>
    </div>
  </section>

  <!-- Hero Photo Banner -->
  <section class="px-4 py-3 max-w-4xl mx-auto w-full">
    <div class="relative rounded-2xl overflow-hidden border border-teal-600/30 shadow-xl">
      <img src="../assets/hospitality/scofftroff_hero.jpg" alt="Scoff Troff Cafe Breakfast" class="w-full h-60 sm:h-72 object-cover">
      <div class="absolute inset-0 bg-gradient-to-t from-[#0e2730] via-transparent to-transparent"></div>
      <div class="absolute bottom-3 left-4 right-4">
        <span class="bg-amber-500 text-slate-950 text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded">All-Day Breakfast</span>
        <h3 class="font-serif-heading text-lg font-bold text-white mt-1">The Mighty Cornish Scoff</h3>
        <p class="text-xs text-slate-300">Cornish sausages, dry-cured bacon, free-range eggs, hogs pudding & toasted sourdough.</p>
      </div>
    </div>
  </section>

  <!-- Visual Menu -->
  <section id="brunch-menu" class="px-4 py-6 max-w-4xl mx-auto w-full">
    <div class="text-center mb-5">
      <span class="text-amber-400 text-xs uppercase tracking-widest font-semibold">Freshly Cooked To Order</span>
      <h3 class="font-serif-heading text-xl font-bold text-white mt-1">Favourite Morning & Lunch Plates</h3>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
      
      <!-- Item 1 -->
      <div class="glass-card rounded-xl p-3 flex gap-3 items-center">
        <img src="../assets/hospitality/scofftroff_pancakes.jpg" alt="Stacked Pancakes" class="w-20 h-20 rounded-lg object-cover shrink-0 border border-amber-500/20">
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h4 class="font-semibold text-sm text-white truncate">Berry Burst Stacked Pancakes</h4>
            <span class="text-amber-400 font-bold text-sm shrink-0">£11.50</span>
          </div>
          <p class="text-xs text-slate-300 mt-1 line-clamp-2">Three fluffy buttermilk pancakes, berry compote, mascarpone & maple syrup.</p>
          <span class="inline-block mt-1 text-[10px] bg-amber-950 text-amber-300 border border-amber-800 px-2 py-0.5 rounded">Favourite</span>
        </div>
      </div>

      <!-- Item 2 -->
      <div class="glass-card rounded-xl p-3 flex gap-3 items-center">
        <img src="../assets/hospitality/scofftroff_burger.jpg" alt="Cornish Smash Burger" class="w-20 h-20 rounded-lg object-cover shrink-0 border border-amber-500/20">
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h4 class="font-semibold text-sm text-white truncate">St Ives Harbour Beef Burger</h4>
            <span class="text-amber-400 font-bold text-sm shrink-0">£15.00</span>
          </div>
          <p class="text-xs text-slate-300 mt-1 line-clamp-2">Aged Cornish beef, Davidstow mature cheddar, bacon jam, brioche bun & rosemary chips.</p>
          <span class="inline-block mt-1 text-[10px] bg-red-950 text-red-300 border border-red-800 px-2 py-0.5 rounded">Hearty Feast</span>
        </div>
      </div>

      <!-- Item 3 -->
      <div class="glass-card rounded-xl p-3 flex gap-3 items-center">
        <img src="../assets/hospitality/scofftroff_cream_tea.jpg" alt="Cornish Cream Tea" class="w-20 h-20 rounded-lg object-cover shrink-0 border border-amber-500/20">
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h4 class="font-semibold text-sm text-white truncate">Traditional Cornish Cream Tea</h4>
            <span class="text-amber-400 font-bold text-sm shrink-0">£7.50</span>
          </div>
          <p class="text-xs text-slate-300 mt-1 line-clamp-2">Warm homemade scones, Rodda's Cornish clotted cream, Boddington's strawberry jam & tea.</p>
          <span class="inline-block mt-1 text-[10px] bg-teal-950 text-teal-300 border border-teal-800 px-2 py-0.5 rounded">Jam First!</span>
        </div>
      </div>

      <!-- Item 4 -->
      <div class="glass-card rounded-xl p-3 flex gap-3 items-center">
        <div class="w-20 h-20 rounded-lg bg-teal-900/60 flex items-center justify-center text-2xl shrink-0 border border-teal-700/50">
          ☕
        </div>
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h4 class="font-semibold text-sm text-white truncate">Cornish Roast Coffee & Teas</h4>
            <span class="text-amber-400 font-bold text-sm shrink-0">from £3.20</span>
          </div>
          <p class="text-xs text-slate-300 mt-1 line-clamp-2">Artisan flat whites, iced coffees, loose-leaf Cornish tea, and hot chocolates.</p>
          <span class="inline-block mt-1 text-[10px] bg-blue-950 text-blue-300 border border-blue-800 px-2 py-0.5 rounded">Oat & Soya Ready</span>
        </div>
      </div>

    </div>
  </section>

  <!-- Location Callout -->
  <section class="px-4 py-5 max-w-3xl mx-auto w-full text-center">
    <div class="bg-[#091a20] rounded-2xl p-4 border border-teal-800/40">
      <h4 class="font-serif-heading text-sm font-bold text-white mb-1">Find Us in St Ives</h4>
      <p class="text-xs text-slate-300 mb-3">Tucked on Fore Street, 60 seconds walk from St Ives Harbour and beach slipways.</p>
      <div class="flex gap-2 justify-center">
        <a href="https://maps.google.com/?q=Scoff+Troff+Cafe+St+Ives" target="_blank" class="bg-teal-900 hover:bg-teal-800 text-white text-xs font-semibold py-2 px-4 rounded-lg transition border border-teal-700">
          📍 Open in Google Maps
        </a>
        <a href="tel:+441736797341" class="bg-amber-500 hover:bg-amber-400 text-slate-950 text-xs font-bold py-2 px-4 rounded-lg transition">
          📞 01736 797341
        </a>
      </div>
    </div>
  </section>

  <!-- Sticky Mobile Bar -->
  <div class="fixed bottom-0 left-0 right-0 z-50 bg-[#0e2730]/95 backdrop-blur-md border-t border-teal-800/60 p-2 px-4 flex gap-2.5">
    <a href="tel:+441736797341" class="flex-1 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold py-2.5 rounded-xl text-center text-xs flex items-center justify-center gap-1">
      <span>📞 Call Cafe (01736 797341)</span>
    </a>
    <a href="https://maps.google.com/?q=Scoff+Troff+Cafe+St+Ives" target="_blank" class="flex-1 bg-teal-700 hover:bg-teal-600 text-white font-bold py-2.5 rounded-xl text-center text-xs flex items-center justify-center gap-1">
      <span>📍 Directions (Fore St)</span>
    </a>
  </div>
</body>
</html>
"""

# 3. Dip Cafe HTML (Byron Bay, NSW)
DIP_CAFE_HTML = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Dip Cafe | French Artisanal Brunch & Allpress Coffee | Byron Bay NSW</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; }
    body { font-family: 'Plus Jakarta Sans', sans-serif; overflow-x: hidden; width: 100%; }
    .font-serif-heading { font-family: 'Playfair Display', serif; }
    .glass-card { background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(12px); border: 1px solid rgba(200, 90, 50, 0.15); }
  </style>
</head>
<body class="bg-[#faf6f0] text-stone-800 min-h-screen flex flex-col pb-20">

  <!-- Top Announcement Bar -->
  <div class="bg-[#2d241e] py-2 px-4 text-xs font-medium text-amber-200 flex items-center justify-between">
    <div class="truncate flex items-center gap-1.5">
      <span>☀️ Byron Bay Town Centre • Fletcher Street</span>
    </div>
    <a href="tel:+61266808864" class="shrink-0 font-bold hover:text-white transition">
      <span>📞 (02) 6680 8864</span>
    </a>
  </div>

  <!-- Header -->
  <header class="sticky top-0 z-40 bg-[#faf6f0]/95 backdrop-blur-md border-b border-stone-200 px-4 py-3">
    <div class="max-w-4xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-2.5">
        <div class="w-10 h-10 rounded-full bg-[#c85a32] flex items-center justify-center text-white text-lg font-serif-heading font-bold shadow">
          D
        </div>
        <div>
          <h1 class="font-serif-heading text-base sm:text-lg font-bold text-stone-900 leading-tight">DIP CAFE</h1>
          <p class="text-[10px] tracking-widest text-[#c85a32] uppercase font-bold">French Bistro • Byron Bay</p>
        </div>
      </div>
      <a href="tel:+61266808864" class="bg-[#c85a32] hover:bg-[#b04b25] text-white text-xs sm:text-sm font-semibold px-3.5 py-1.5 rounded-full shadow transition">
        Enquire Table
      </a>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="px-4 pt-6 pb-6 max-w-3xl mx-auto text-center">
    <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-[#c85a32]/10 border border-[#c85a32]/20 text-[#c85a32] text-xs font-semibold mb-3">
      <span>⭐ 4.5★ (700+ Byron Foodie Reviews)</span>
    </div>

    <h2 class="font-serif-heading text-2xl sm:text-4xl font-extrabold text-stone-900 leading-tight mb-3">
      Parisian Craftsmanship.<br>
      <span class="text-[#c85a32]">
        Byron Bay Sunshine.
      </span>
    </h2>

    <p class="text-xs sm:text-sm text-stone-600 leading-relaxed max-w-lg mx-auto mb-4">
      Freshly baked brioche French toast, slow-simmered Mediterranean shakshuka skillets, smashed local avocado, and velvety Allpress espresso served on sunlit Fletcher Street.
    </p>

    <!-- Key Badges -->
    <div class="flex flex-wrap items-center justify-center gap-2 mb-5 text-[11px] font-semibold text-stone-700">
      <span class="bg-white border border-stone-200 px-2.5 py-1 rounded-full shadow-sm">🥖 House-Baked Brioche</span>
      <span class="bg-white border border-stone-200 px-2.5 py-1 rounded-full shadow-sm">🥑 Northern Rivers Produce</span>
      <span class="bg-white border border-stone-200 px-2.5 py-1 rounded-full shadow-sm">☕ Allpress Specialty Coffee</span>
    </div>

    <!-- Live Status -->
    <div class="bg-white rounded-xl p-3 max-w-md mx-auto mb-5 flex items-center justify-center gap-2.5 text-xs shadow-sm border border-stone-200">
      <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
      <span class="text-stone-700 font-medium">Open Daily: <strong class="text-stone-900">7:00 AM – 2:30 PM</strong> (Walk-ins Welcome)</span>
    </div>

    <div class="flex flex-col sm:flex-row gap-3 justify-center max-w-sm mx-auto">
      <a href="tel:+61266808864" class="bg-[#c85a32] hover:bg-[#b04b25] text-white font-bold py-2.5 px-5 rounded-xl shadow-md transition text-xs sm:text-sm flex items-center justify-center gap-1.5">
        <span>📞 Call Dip: (02) 6680 8864</span>
      </a>
      <a href="#brunch-menu" class="bg-stone-100 hover:bg-stone-200 text-stone-800 border border-stone-300 font-semibold py-2.5 px-5 rounded-xl transition text-xs sm:text-sm flex items-center justify-center gap-1.5">
        <span>🥐 Visual Brunch Menu</span>
      </a>
    </div>
  </section>

  <!-- Hero Photo Banner -->
  <section class="px-4 py-3 max-w-4xl mx-auto w-full">
    <div class="relative rounded-2xl overflow-hidden border border-stone-200 shadow-xl">
      <img src="../assets/hospitality/dipcafe_hero.jpg" alt="Dip Cafe French Toast" class="w-full h-60 sm:h-72 object-cover">
      <div class="absolute inset-0 bg-gradient-to-t from-stone-900/80 via-transparent to-transparent"></div>
      <div class="absolute bottom-3 left-4 right-4">
        <span class="bg-[#c85a32] text-white text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded">Signature Brunch</span>
        <h3 class="font-serif-heading text-lg font-bold text-white mt-1">Brioche French Toast with Byron Honey</h3>
        <p class="text-xs text-stone-200">Caramelized local bananas, seasonal berry compote & organic honeycomb crumble.</p>
      </div>
    </div>
  </section>

  <!-- Visual Menu Section -->
  <section id="brunch-menu" class="px-4 py-6 max-w-4xl mx-auto w-full">
    <div class="text-center mb-5">
      <span class="text-[#c85a32] text-xs uppercase tracking-widest font-bold">Artisanal Morning Fare</span>
      <h3 class="font-serif-heading text-xl font-bold text-stone-900 mt-1">Popular Breakfast & Lunch Plates</h3>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
      
      <!-- Item 1 -->
      <div class="bg-white rounded-xl p-3.5 flex gap-3 items-center border border-stone-200 shadow-sm">
        <img src="../assets/hospitality/dipcafe_shakshuka.jpg" alt="Mediterranean Shakshuka" class="w-20 h-20 rounded-lg object-cover shrink-0 border border-stone-100">
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h4 class="font-semibold text-sm text-stone-900 truncate">Baked Eggs Shakshuka Skillet</h4>
            <span class="text-[#c85a32] font-bold text-sm shrink-0">A$23</span>
          </div>
          <p class="text-xs text-stone-500 mt-1 line-clamp-2">Spiced Mediterranean tomato sauce, poached eggs, Meredith Dairy goat feta & sourdough.</p>
          <span class="inline-block mt-1 text-[10px] bg-orange-100 text-orange-800 font-semibold px-2 py-0.5 rounded">Warm & Spiced</span>
        </div>
      </div>

      <!-- Item 2 -->
      <div class="bg-white rounded-xl p-3.5 flex gap-3 items-center border border-stone-200 shadow-sm">
        <img src="../assets/hospitality/dipcafe_avotoast.jpg" alt="Byron Smashed Avo" class="w-20 h-20 rounded-lg object-cover shrink-0 border border-stone-100">
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h4 class="font-semibold text-sm text-stone-900 truncate">Northern Rivers Smashed Avo</h4>
            <span class="text-[#c85a32] font-bold text-sm shrink-0">A$21</span>
          </div>
          <p class="text-xs text-stone-500 mt-1 line-clamp-2">Locally grown Hass avocado, marinated chevre, house toasted Egyptian dukkah & fresh lemon.</p>
          <span class="inline-block mt-1 text-[10px] bg-emerald-100 text-emerald-800 font-semibold px-2 py-0.5 rounded">Byron Classic</span>
        </div>
      </div>

      <!-- Item 3 -->
      <div class="bg-white rounded-xl p-3.5 flex gap-3 items-center border border-stone-200 shadow-sm">
        <img src="../assets/hospitality/dipcafe_flatwhite.jpg" alt="Allpress Flat White" class="w-20 h-20 rounded-lg object-cover shrink-0 border border-stone-100">
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h4 class="font-semibold text-sm text-stone-900 truncate">Allpress Espresso & Cold Brew</h4>
            <span class="text-[#c85a32] font-bold text-sm shrink-0">from A$5.00</span>
          </div>
          <p class="text-xs text-stone-500 mt-1 line-clamp-2">Velvety flat whites, single-origin cold brews, organic matcha, and Northern Rivers green juices.</p>
          <span class="inline-block mt-1 text-[10px] bg-stone-100 text-stone-800 font-semibold px-2 py-0.5 rounded">Barista Roasted</span>
        </div>
      </div>

      <!-- Item 4 -->
      <div class="bg-white rounded-xl p-3.5 flex gap-3 items-center border border-stone-200 shadow-sm">
        <div class="w-20 h-20 rounded-lg bg-[#c85a32]/10 flex items-center justify-center text-2xl shrink-0">
          🥐
        </div>
        <div class="min-w-0 flex-1">
          <div class="flex items-start justify-between gap-1">
            <h4 class="font-semibold text-sm text-stone-900 truncate">Traditional Croque Monsieur</h4>
            <span class="text-[#c85a32] font-bold text-sm shrink-0">A$22</span>
          </div>
          <p class="text-xs text-stone-500 mt-1 line-clamp-2">Smoked leg ham, aged gruyère béchamel, Dijon mustard on thick sourdough (add fried egg +A$3).</p>
          <span class="inline-block mt-1 text-[10px] bg-amber-100 text-amber-800 font-semibold px-2 py-0.5 rounded">French Bistro</span>
        </div>
      </div>

    </div>
  </section>

  <!-- Location Callout -->
  <section class="px-4 py-5 max-w-3xl mx-auto w-full text-center">
    <div class="bg-white rounded-2xl p-4 border border-stone-200 shadow-sm">
      <h4 class="font-serif-heading text-sm font-bold text-stone-900 mb-1">Stroll In on Fletcher Street</h4>
      <p class="text-xs text-stone-600 mb-3">21 Fletcher Street, Byron Bay. Outdoor sunlit terrace and covered bistro dining.</p>
      <div class="flex gap-2 justify-center">
        <a href="https://maps.google.com/?q=Dip+Cafe+Byron+Bay" target="_blank" class="bg-stone-800 hover:bg-stone-700 text-white text-xs font-semibold py-2 px-4 rounded-lg transition">
          📍 Open in Google Maps
        </a>
        <a href="tel:+61266808864" class="bg-[#c85a32] hover:bg-[#b04b25] text-white text-xs font-bold py-2 px-4 rounded-lg transition">
          📞 (02) 6680 8864
        </a>
      </div>
    </div>
  </section>

  <!-- Sticky Mobile Bar -->
  <div class="fixed bottom-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-md border-t border-stone-200 p-2.5 px-4 flex gap-2.5">
    <a href="tel:+61266808864" class="flex-1 bg-[#c85a32] hover:bg-[#b04b25] text-white font-bold py-2.5 rounded-xl text-center text-xs flex items-center justify-center gap-1 shadow">
      <span>📞 Call Table ((02) 6680 8864)</span>
    </a>
    <a href="https://maps.google.com/?q=Dip+Cafe+Byron+Bay" target="_blank" class="flex-1 bg-stone-800 hover:bg-stone-700 text-white font-bold py-2.5 rounded-xl text-center text-xs flex items-center justify-center gap-1 shadow">
      <span>📍 Directions (Fletcher St)</span>
    </a>
  </div>
</body>
</html>
"""

FILES = [
    # 1. Bar Harbor Lobster Bakes
    (BASE_DIR / "barharborlobster" / "index.html", BAR_HARBOR_HTML),
    (BASE_DIR / "03_DEMOS" / "10_bar_harbor_lobster" / "index.html", BAR_HARBOR_HTML),
    
    # 2. Scoff Troff Cafe
    (BASE_DIR / "scofftroff" / "index.html", SCOFF_TROFF_HTML),
    (BASE_DIR / "03_DEMOS" / "11_scoff_troff_cafe" / "index.html", SCOFF_TROFF_HTML),

    # 3. Dip Cafe
    (BASE_DIR / "dipcafe" / "index.html", DIP_CAFE_HTML),
    (BASE_DIR / "03_DEMOS" / "12_dip_cafe_byron" / "index.html", DIP_CAFE_HTML),
]

for file_path, content in FILES:
    file_path.parent.mkdir(parents=True, exist_ok=True)
    adjusted_content = content
    if "03_DEMOS" in str(file_path):
        adjusted_content = adjusted_content.replace("../assets/hospitality/", "../../assets/hospitality/")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(adjusted_content)
    print(f"Generated: {file_path.relative_to(BASE_DIR)}")

print("All hospitality prototypes generated successfully.")
