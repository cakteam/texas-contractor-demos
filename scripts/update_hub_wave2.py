with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

wave2_html = '''
    <!-- ==================== WAVE 2 EXPANSION ==================== -->
    <div class="pt-8 border-t border-slate-800">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-400 text-xs font-bold uppercase tracking-wider mb-2">
        <span class="w-2 h-2 rounded-full bg-cyan-400 animate-pulse"></span>
        Wave 2 High-Ticket Pipeline (HVAC & Foundation Repair)
      </div>
      <h2 class="text-2xl font-black text-white">Expanded North Texas Contractor Demos</h2>
    </div>

    <!-- DEMO 4: DUCK AC & HEATING -->
    <article id="duck-ac" class="glass-card rounded-3xl p-6 sm:p-8 space-y-8">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-800 pb-6">
        <div>
          <div class="flex items-center gap-2 text-xs font-bold text-cyan-400 uppercase tracking-wider mb-1">
            <i data-lucide="snowflake" class="w-4 h-4"></i> Target Candidate #4 • Emergency HVAC & Cooling
          </div>
          <h2 class="text-2xl font-extrabold text-white">Duck AC & Heating</h2>
          <p class="text-xs text-slate-400 mt-1">Arlington & DFW, TX • info@duckacandheating.com • (817) 631-8281 • 5.0★ Google Verified</p>
        </div>
        <div class="flex flex-wrap items-center gap-2 sm:gap-3">
          <a href="./duckac/" target="_blank" class="px-5 py-2.5 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-extrabold text-xs flex items-center gap-2 shadow-lg shadow-cyan-500/20 transition-all">
            <i data-lucide="external-link" class="w-4 h-4"></i>
            <span>Open Mobile Demo</span>
          </a>
          <button onclick="copyDemoLink('duckac')" class="px-3.5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700 flex items-center gap-1.5 transition-colors">
            <i data-lucide="copy" class="w-3.5 h-3.5"></i>
            <span>Copy Link</span>
          </button>
        </div>
      </div>

      <div class="grid lg:grid-cols-12 gap-8 items-start">
        <div class="lg:col-span-5 flex flex-col items-center">
          <div class="max-w-[320px] w-full rounded-2xl overflow-hidden border border-slate-700/60 shadow-2xl bg-slate-900">
            <img src="./assets/before_after/duck_after.jpg" alt="Duck AC Preview" class="w-full h-auto block">
          </div>
        </div>

        <div class="lg:col-span-7 space-y-5">
          <div>
            <span class="text-xs font-bold uppercase tracking-wider text-rose-400">The Severe Mobile Leak:</span>
            <h3 class="text-lg font-bold text-white mt-1">Phone number has NO clickable 'tel:' link on mobile & Wix dummy text</h3>
            <p class="text-xs text-slate-400 mt-2 leading-relaxed">
              In 100°F+ Texas summer weather, desperate homeowners tap the phone number on their phones and nothing happens. Also contains Wix boilerplate 'example@mysite.com' in live code.
            </p>
          </div>

          <div class="grid grid-cols-2 gap-3 text-xs">
            <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800">
              <div class="text-slate-400 text-[11px]">Avg Ticket Size</div>
              <div class="text-base font-extrabold text-white mt-0.5">$6,500 - $16,000</div>
              <div class="text-[10px] text-cyan-400 mt-1">AC Replacement / Heat Pump</div>
            </div>
            <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800">
              <div class="text-slate-400 text-[11px]">Owner Direct Contact</div>
              <div class="text-base font-extrabold text-emerald-400 mt-0.5">info@duckac...</div>
              <div class="text-[10px] text-slate-400 mt-1">(817) 631-8281 Direct</div>
            </div>
          </div>

          <!-- Outbound Angle -->
          <div class="p-4 rounded-2xl bg-slate-900/90 border border-slate-800 text-xs space-y-2">
            <div class="font-bold text-cyan-400 flex items-center gap-1.5">
              <i data-lucide="mail" class="w-4 h-4"></i>
              <span>Outreach Email Angle:</span>
            </div>
            <p class="text-slate-300 italic leading-relaxed">
              "Hey Duck AC team — noticed when people search you on their iPhone during this heatwave, your phone number (817) 631-8281 isn't clickable on mobile, causing homeowners to bounce to competitors. Put together a high-speed emergency booking prototype with 1-click dialing. Take a look:"
            </p>
            <code class="text-[11px] text-cyan-400 bg-slate-950 px-2 py-1 rounded border border-slate-800 block">
              https://cakteam.github.io/texas-contractor-demos/duckac/
            </code>
          </div>
        </div>
      </div>
    </article>

    <!-- DEMO 5: AMERITEX FOUNDATION REPAIR -->
    <article id="ameritex-foundation" class="glass-card rounded-3xl p-6 sm:p-8 space-y-8">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-800 pb-6">
        <div>
          <div class="flex items-center gap-2 text-xs font-bold text-amber-400 uppercase tracking-wider mb-1">
            <i data-lucide="layers" class="w-4 h-4"></i> Target Candidate #5 • Steel Pier Foundation Underpinning
          </div>
          <h2 class="text-2xl font-extrabold text-white">AmeriTex Foundation Repair</h2>
          <p class="text-xs text-slate-400 mt-1">Keller & DFW, TX • AmeriTexFoundationRepair@gmail.com • (817) 703-9111 • 50+ Yrs DFW Exp</p>
        </div>
        <div class="flex flex-wrap items-center gap-2 sm:gap-3">
          <a href="./ameritex/" target="_blank" class="px-5 py-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-extrabold text-xs flex items-center gap-2 shadow-lg shadow-amber-500/20 transition-all">
            <i data-lucide="external-link" class="w-4 h-4"></i>
            <span>Open Mobile Demo</span>
          </a>
          <button onclick="copyDemoLink('ameritex')" class="px-3.5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700 flex items-center gap-1.5 transition-colors">
            <i data-lucide="copy" class="w-3.5 h-3.5"></i>
            <span>Copy Link</span>
          </button>
        </div>
      </div>

      <div class="grid lg:grid-cols-12 gap-8 items-start">
        <div class="lg:col-span-5 flex flex-col items-center">
          <div class="max-w-[320px] w-full rounded-2xl overflow-hidden border border-slate-700/60 shadow-2xl bg-slate-900">
            <img src="./assets/before_after/ameritex_after.jpg" alt="AmeriTex Preview" class="w-full h-auto block">
          </div>
        </div>

        <div class="lg:col-span-7 space-y-5">
          <div>
            <span class="text-xs font-bold uppercase tracking-wider text-rose-400">The Severe Mobile Leak:</span>
            <h3 class="text-lg font-bold text-white mt-1">Heavy engineering prowess hidden behind squished Wix mobile view</h3>
            <p class="text-xs text-slate-400 mt-2 leading-relaxed">
              AmeriTex owns impressive commercial equipment and dual hydraulic pier tech, but their Wix site squishes photos and lacks an interactive laser elevation assessment tool for homeowners with brick cracks.
            </p>
          </div>

          <div class="grid grid-cols-2 gap-3 text-xs">
            <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800">
              <div class="text-slate-400 text-[11px]">Avg Ticket Size</div>
              <div class="text-base font-extrabold text-white mt-0.5">$8,000 - $25,000</div>
              <div class="text-[10px] text-amber-400 mt-1">Residential Steel Underpinning</div>
            </div>
            <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800">
              <div class="text-slate-400 text-[11px]">Owner Direct Contact</div>
              <div class="text-base font-extrabold text-emerald-400 mt-0.5">AmeriTexFoundation...</div>
              <div class="text-[10px] text-slate-400 mt-1">(817) 703-9111 Owner Direct</div>
            </div>
          </div>

          <!-- Outbound Angle -->
          <div class="p-4 rounded-2xl bg-slate-900/90 border border-slate-800 text-xs space-y-2">
            <div class="font-bold text-amber-400 flex items-center gap-1.5">
              <i data-lucide="mail" class="w-4 h-4"></i>
              <span>Outreach Email Angle:</span>
            </div>
            <p class="text-slate-300 italic leading-relaxed">
              "Hey AmeriTex team — love seeing your Silverado Lone Star rigs around Tarrant County. Noticed your Wix mobile site doesn't let homeowners tap-to-call or self-assess brick stair-step cracks. Built a dedicated high-converting prototype highlighting your bedrock steel piers and lifetime warranty:"
            </p>
            <code class="text-[11px] text-amber-400 bg-slate-950 px-2 py-1 rounded border border-slate-800 block">
              https://cakteam.github.io/texas-contractor-demos/ameritex/
            </code>
          </div>
        </div>
      </div>
    </article>

    <!-- DEMO 6: D.A.D. HOME SERVICES -->
    <article id="dad-hvac" class="glass-card rounded-3xl p-6 sm:p-8 space-y-8">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-800 pb-6">
        <div>
          <div class="flex items-center gap-2 text-xs font-bold text-orange-400 uppercase tracking-wider mb-1">
            <i data-lucide="zap" class="w-4 h-4"></i> Target Candidate #6 • Licensed HVAC & Whole-Home Generators
          </div>
          <h2 class="text-2xl font-extrabold text-white">D.A.D. Home Services</h2>
          <p class="text-xs text-slate-400 mt-1">Dallas-Fort Worth, TX • Founder: David • david@calldadac.com • (682) 328-3700 • TACLA 116949C</p>
        </div>
        <div class="flex flex-wrap items-center gap-2 sm:gap-3">
          <a href="./calldadac/" target="_blank" class="px-5 py-2.5 rounded-xl bg-orange-500 hover:bg-orange-400 text-slate-950 font-extrabold text-xs flex items-center gap-2 shadow-lg shadow-orange-500/20 transition-all">
            <i data-lucide="external-link" class="w-4 h-4"></i>
            <span>Open Mobile Demo</span>
          </a>
          <button onclick="copyDemoLink('calldadac')" class="px-3.5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700 flex items-center gap-1.5 transition-colors">
            <i data-lucide="copy" class="w-3.5 h-3.5"></i>
            <span>Copy Link</span>
          </button>
        </div>
      </div>

      <div class="grid lg:grid-cols-12 gap-8 items-start">
        <div class="lg:col-span-5 flex flex-col items-center">
          <div class="max-w-[320px] w-full rounded-2xl overflow-hidden border border-slate-700/60 shadow-2xl bg-slate-900">
            <img src="./assets/before_after/dad_after.jpg" alt="D.A.D. Preview" class="w-full h-auto block">
          </div>
        </div>

        <div class="lg:col-span-7 space-y-5">
          <div>
            <span class="text-xs font-bold uppercase tracking-wider text-rose-400">The Severe Mobile Leak:</span>
            <h3 class="text-lg font-bold text-white mt-1">710KB WordPress script weight & buried emergency booking</h3>
            <p class="text-xs text-slate-400 mt-2 leading-relaxed">
              WordPress theme plugin bloat delays mobile page loads in emergency weather. No simple 60-second direct dispatch form for homeowners with AC outages.
            </p>
          </div>

          <div class="grid grid-cols-2 gap-3 text-xs">
            <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800">
              <div class="text-slate-400 text-[11px]">Avg Ticket Size</div>
              <div class="text-base font-extrabold text-white mt-0.5">$4,000 - $14,000</div>
              <div class="text-[10px] text-orange-400 mt-1">HVAC & Generator Backup</div>
            </div>
            <div class="p-3.5 rounded-xl bg-slate-900/80 border border-slate-800">
              <div class="text-slate-400 text-[11px]">Owner Direct Contact</div>
              <div class="text-base font-extrabold text-emerald-400 mt-0.5">david@calldadac...</div>
              <div class="text-[10px] text-slate-400 mt-1">Direct to David (Founder)</div>
            </div>
          </div>

          <!-- Outbound Angle -->
          <div class="p-4 rounded-2xl bg-slate-900/90 border border-slate-800 text-xs space-y-2">
            <div class="font-bold text-orange-400 flex items-center gap-1.5">
              <i data-lucide="mail" class="w-4 h-4"></i>
              <span>Outreach Email Angle:</span>
            </div>
            <p class="text-slate-300 italic leading-relaxed">
              "David — quick question regarding D.A.D. Home Services. Noticed your current WordPress site takes over 4 seconds to load on mobile due to old script plugins, which bleeds hot leads during summer heatwaves. Created a clean, instant-loading mobile prototype highlighting your TACLA 116949C license:"
            </p>
            <code class="text-[11px] text-orange-400 bg-slate-950 px-2 py-1 rounded border border-slate-800 block">
              https://cakteam.github.io/texas-contractor-demos/calldadac/
            </code>
          </div>
        </div>
      </div>
    </article>
'''

if '</main>' in content:
    new_content = content.replace('  </main>', wave2_html + '\n  </main>')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('index.html updated successfully with Wave 2 demos')
