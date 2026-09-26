from build import page

BODY = """
<div class="intro" data-intro aria-hidden="true">
  <div class="intro-meta"><span>Kejuruteraan Letrik Seri (M) Sdn Bhd</span><span>Port Klang, Malaysia</span></div>
  <div class="intro-year" data-intro-count>1950</div>
  <div class="intro-card"><img src="assets/img/industries/biogas.webp" alt=""></div>
  <div class="intro-line"><i></i></div>
</div>
<script>try{var d=document.documentElement;if(window.matchMedia('(prefers-reduced-motion: reduce)').matches||sessionStorage.getItem('klsIntroSeen')==='1'){d.classList.add('no-intro');}else{sessionStorage.setItem('klsIntroSeen','1');d.classList.add('intro-lock');}}catch(e){}</script>
<section class="section">
  <div class="container">
    <div class="kicker">What We Do</div>
    <h2 style="max-width:26ch;">Electrical engineering and renewable energy interconnection, end to end</h2>
    <p class="lead" style="max-width:70ch;">From supply and installation through to testing, commissioning and warranty, across HV/MV/LV electrical work, ACMV, fire fighting and ELV systems.</p>
    <div class="svc-chip-row">
      <span class="svc-chip">HV / MV / LV Electrical Work</span>
      <span class="svc-chip">ACMV</span>
      <span class="svc-chip">Fire Fighting</span>
      <span class="svc-chip">ELV Systems</span>
    </div>
    <a href="services.html" class="btn-ghost" style="margin-top:16px;display:inline-block;">See all services</a>
  </div>
</section>


<section class="hero">
  <div class="hero-slides">
    <div class="hero-slide is-active" data-hero-title="Energy That Keeps Your Business Running" data-hero-lead="Kejuruteraan Letrik Seri (M) Sdn Bhd, known simply as KLS, was incorporated in 1984 as a master rewiring service provider. As the business grew, so did what we offered: today we supply, install, test, commission and warranty High Voltage, Low Voltage and Extra Low Voltage electrical systems across residential, commercial, industrial, infrastructure and marine projects.">
      <img src="assets/img/industries/biogas.webp" alt="KLS electrical engineering, powering your business">
    </div>
    <div class="hero-slide" data-hero-title="Backing Clean, Sustainable Energy" data-hero-lead="As one of Malaysia's established industry names, we put real weight behind sustainable development, taking on Renewable Energy Interconnection contracts and initiatives across Biogas, Biomass, Solar and Cogeneration plants.">
      <img src="assets/img/industries/solar.webp" alt="Clean energy, light bulb placed on soil in sunlight">
    </div>
    <div class="hero-slide" data-hero-title="Powering Through Biomass" data-hero-lead="From engineering and supply through to installing and commissioning cables and electrical equipment, KLS builds specialised interconnection solutions for biomass power plants, including a 10MW project for Cepat Wawasan Sdn. Bhd.">
      <img src="assets/img/industries/biomass.webp" alt="KLS renewable energy interconnection works">
    </div>
  </div>
  <div class="container hero-inner">
    <div class="hero-copy">
      <div class="hero-chips"><span>Est. 1984</span><span>CIDB G7</span><span>Class A</span></div>
      <h1 class="reveal" style="animation-delay:.68s" data-hero-title-el>Energy That Keeps Your Business Running</h1>
      <p class="lead" data-hero-lead-el>Kejuruteraan Letrik Seri (M) Sdn Bhd, known simply as KLS, was incorporated in 1984 as a master rewiring service provider. As the business grew, so did what we offered: today we supply, install, test, commission and warranty High Voltage, Low Voltage and Extra Low Voltage electrical systems across residential, commercial, industrial, infrastructure and marine projects.</p>
      <div class="hero-actions">
        <a href="company-overview.html" class="btn btn-primary">See the full company story</a>
        <a href="services.html#renewable-energy" class="btn btn-outline">Our renewable energy work</a>
      </div>
    </div>
    <div class="hero-stats">
      <div class="hero-stat"><b data-count-to="1984" data-count-suffix="">0</b><span>Year incorporated</span></div>
      <div class="hero-stat"><b data-count-to="4" data-count-suffix="">0</b><span>Renewable energy focus areas: Biogas, Biomass, Solar, Cogeneration</span></div>
      <div class="hero-stat"><b>Class A</b><span>CIDB G7 M&amp;E Contractor</span></div>
      <div class="hero-stat"><b>3</b><span>Offices across Port Klang &middot; Lahad Datu &middot; Bintulu</span></div>
    </div>
  </div>
  <button class="hero-scroll-cue" data-scroll-cue aria-label="Scroll to explore">
    <span class="hero-scroll-cue-track"><span></span></span>
    <em>Scroll</em>
  </button>
  <div class="hero-dots">
    <button data-hero-dot class="is-active" aria-label="Slide 1: Energy That Keeps Your Business Running"></button>
    <button data-hero-dot aria-label="Slide 2: Backing Clean, Sustainable Energy"></button>
    <button data-hero-dot aria-label="Slide 3: Powering Through Biomass"></button>
  </div>
</section>

<section class="trust-band">
  <div class="container trust-grid">
    <div class="trust-stat"><b data-count-to="42" data-count-suffix="+">0</b><span>Years in operation</span></div>
    <div class="trust-stat"><b data-count-to="35" data-count-suffix="+">0</b><span>Documented projects</span></div>
    <div class="trust-stat"><b data-count-to="12">0</b><span>Certificates &amp; licenses</span></div>
    <div class="trust-stat"><b data-count-to="3">0</b><span>Offices: Port Klang, Lahad Datu, Bintulu</span></div>
  </div>
</section>

<section class="showcase" id="industries" data-showcase>
  <div class="container showcase-head">
    <div class="kicker">Industries We Serve</div>
    <h2>Where our work shows up</h2>
    <p class="lead">Five sectors where KLS's electrical and interconnection work shows up most, from renewable energy plants to stadium lighting.</p>
  </div>
  <div class="container showcase-stage">
    <ol class="showcase-list">
      <li class="showcase-item" data-showcase-item><a href="#home-clean-energy"><span class="n">01</span><span class="t">Clean Energy</span><span class="d">Interconnection for solar, biogas and biomass plants, where our project history runs deepest.</span><img class="thumb" src="assets/img/industries/solar.webp" alt="" loading="lazy"></a></li>
      <li class="showcase-item" data-showcase-item><a href="#home-grid-utilities"><span class="n">02</span><span class="t">Substation &amp; Grid Utilities</span><span class="d">HV/MV/LV works for utility and telecommunications infrastructure.</span><img class="thumb" src="assets/img/industries/biomass.webp" alt="" loading="lazy"></a></li>
      <li class="showcase-item" data-showcase-item><a href="#home-semiconductor"><span class="n">03</span><span class="t">Semiconductor &amp; Electronic</span><span class="d">A growing focus, tracking the boom in chip manufacturing and electronics assembly.</span><img class="thumb" src="assets/img/industries/semiconductor-2.webp" alt="" loading="lazy"></a></li>
      <li class="showcase-item" data-showcase-item><a href="#home-petrochem"><span class="n">04</span><span class="t">Petrochemical &amp; Oleochemical</span><span class="d">Manufacturing plants, palm oil mills and process facilities.</span><img class="thumb" src="assets/img/industries/petrochem-1.webp" alt="" loading="lazy"></a></li>
      <li class="showcase-item" data-showcase-item><a href="#home-hospital-stadium"><span class="n">05</span><span class="t">Hospital &amp; Stadium</span><span class="d">From stadium lighting to healthcare facility electrical systems.</span><img class="thumb" src="assets/img/projects/larkin-2.webp" alt="" loading="lazy"></a></li>
    </ol>
    <div class="showcase-media" aria-hidden="true">
        <img src="assets/img/industries/solar.webp" alt="" loading="lazy">
        <img src="assets/img/industries/biomass.webp" alt="" loading="lazy">
        <img src="assets/img/industries/semiconductor-2.webp" alt="" loading="lazy">
        <img src="assets/img/industries/petrochem-1.webp" alt="" loading="lazy">
        <img src="assets/img/projects/larkin-2.webp" alt="" loading="lazy">
      <div class="showcase-bar"><i></i></div>
    </div>
  </div>
</section>

<section class="section section--band" id="home-clean-energy">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Clean Energy</div>
      <h2>Solar, Biogas &amp; Biomass Interconnection</h2>
      <p class="lead">Biogas is where our project history runs deepest, spanning palm oil mills across Peninsular and East Malaysia, alongside biomass and solar interconnection work.</p>
    </div>
    <div class="re-block">
      <div class="re-media" style="--panel-img:url('../img/industries/solar.webp')">
        <div><span class="tag">RENEWABLE ENERGY</span><div class="headline">Solar</div></div>
        <div class="examples"><div>1MW Solar Energy for ERS Energy Sdn. Bhd.</div></div>
      </div>
      <div class="re-body">
        <p>Supply, installation and maintenance of cables and electrical systems interconnecting solar panels, solar power plants and the national grid.</p>
        <a href="services.html#solar" class="btn-ghost">Full solar detail</a>
      </div>
    </div>
    <div class="re-block">
      <div class="re-media" style="--panel-img:url('../img/industries/biogas.webp')">
        <div><span class="tag">RENEWABLE ENERGY</span><div class="headline">Biogas</div></div>
        <div class="examples">
          <div>1.5MW Biogas for Cenergi FJP Sdn. Bhd.</div>
          <div>3.5MW Biogas for Mistral Engineering Sdn. Bhd.</div>
          <div>Plus multiple Cenergi EPC, Sime Darby &amp; Worldwide Holdings biogas projects</div>
        </div>
      </div>
      <div class="re-body">
        <p>Our most active renewable energy vertical: interconnection work that turns palm oil mill effluent (POME) into exportable grid power, across more documented projects than any other category we serve.</p>
        <a href="services.html#biogas" class="btn-ghost">Full biogas detail</a>
      </div>
    </div>
    <div class="re-block">
      <div class="re-media" style="--panel-img:url('../img/industries/biomass.webp')">
        <div><span class="tag">RENEWABLE ENERGY</span><div class="headline">Biomass</div></div>
        <div class="examples"><div>10MW Biomass for Cepat Wawasan Sdn. Bhd.</div></div>
      </div>
      <div class="re-body">
        <p>Engineering, supply, installation and commissioning of cables and electrical equipment for biomass power plants.</p>
        <a href="services.html#biomass" class="btn-ghost">Full biomass detail</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight" id="home-grid-utilities">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Grid Utilities</div>
      <h2>Substation &amp; Grid Utilities</h2>
      <p class="lead">HV/MV/LV works for utility and telecommunications infrastructure.</p>
    </div>
    <div class="re-block">
      <div class="re-media" style="--panel-img:url('../img/industries/biomass.webp')">
        <div><span class="tag">GRID UTILITIES</span><div class="headline">Substation Works</div></div>
        <div class="examples">
          <div>Remote Terminal Unit electrical works for SESB, Sabah</div>
          <div>Electrical upgrading works for Telekom Malaysia</div>
        </div>
      </div>
      <div class="re-body">
        <p>Substation and switchgear works for utility and telecommunications operators, including remote terminal unit installations and 11kV switchgear upgrades.</p>
        <a href="projects.html" class="btn-ghost">See project reference list</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight section--band" id="home-semiconductor">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Future Focus</div>
      <h2>Semiconductor &amp; Electronic</h2>
      <p class="lead">A growing focus for KLS, tracking the AI-driven boom in chip manufacturing and electronics assembly across Malaysia.</p>
    </div>
    <div class="re-block">
      <div class="re-media" style="--panel-img:url('../img/industries/semiconductor-1.webp')">
        <div><span class="tag">FUTURE FOCUS</span><div class="headline">Semiconductor &amp; Electronic</div></div>
        <div class="examples">
          <div>Melexis (Kuching)</div>
          <div>Renesas</div>
          <div>SICK AG (Johor Bahru)</div>
        </div>
      </div>
      <div class="re-body">
        <p>As Malaysia's semiconductor and electronics sector expands alongside global AI-driven demand, KLS is building out capability to serve chip manufacturing and electronics assembly facilities.</p>
        <a href="contact.html" class="btn-ghost">Talk to us about a project</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight" id="home-petrochem">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Manufacturing</div>
      <h2>Petrochemical &amp; Oleochemical</h2>
      <p class="lead">Manufacturing plants, palm oil mills and process facilities.</p>
    </div>
    <div class="re-block">
      <div class="re-media" style="--panel-img:url('../img/industries/petrochem-2.webp')">
        <div><span class="tag">MANUFACTURING</span><div class="headline">Petrochemical &amp; Oleochemical</div></div>
        <div class="examples">
          <div>Marine facilities works for Dialog Group, Pengerang</div>
          <div>Refinery electrical works for Cargill, Port Klang</div>
          <div>GTG Cogen works for KLK Berhad, Rawang</div>
        </div>
      </div>
      <div class="re-body">
        <p>Electrical, mechanical and ELV works for refineries, oleochemical plants and palm oil processing facilities.</p>
        <a href="projects.html" class="btn-ghost">See project reference list</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight section--band" id="home-hospital-stadium">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Public Infrastructure</div>
      <h2>Hospital &amp; Stadium</h2>
      <p class="lead">From stadium lighting to healthcare facility electrical systems.</p>
    </div>
    <div class="re-block">
      <div class="re-media" style="--panel-img:url('../img/projects/larkin-3.webp')">
        <div><span class="tag">PUBLIC INFRASTRUCTURE</span><div class="headline">Larkin Stadium</div></div>
        <div class="examples"><div>Stadium lighting works for Stadium Tan Sri Dato' Haj Hassan Yunos, Larkin</div></div>
      </div>
      <div class="re-body">
        <p>KLS delivered the stadium lighting for Stadium Tan Sri Dato' Haj Hassan Yunos in Larkin, Johor Bahru, home ground of Johor Darul Ta'zim (JDT).</p>
        <a href="location.html" class="btn-ghost">More about KLS</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight text-center" id="home-renovation">
  <div class="container">
    <div class="kicker" style="justify-content:center;">Renovation &amp; Restoration</div>
    <h3 style="max-width:40ch;margin:0 auto 10px;">Upgrades and restoration works for existing electrical infrastructure</h3>
    <a href="contact.html" class="btn-ghost">Get in touch to discuss a project</a>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center" style="margin:0 auto 40px;">
      <div class="kicker" style="justify-content:center;">Key Projects</div>
      <h2>Backed by major Malaysian industrial &amp; energy names</h2>
    </div>
  </div>
  <div class="marquee" data-marquee data-marquee-speed="28">
    <div class="marquee-track">
      <a class="logo-plate logo-plate--text" href="https://www.topglove.com/" target="_blank" rel="noopener" aria-label="Top Glove Berhad">Top Glove<br>Berhad</a>
      <a class="logo-plate" href="https://www.cenergi-sea.com/" target="_blank" rel="noopener" aria-label="Cenergi SEA Sdn. Bhd."><img src="assets/img/clients/cenergi.png" alt="Cenergi SEA logo" loading="lazy"></a>
      <a class="logo-plate" href="https://www.tm.com.my/Pages/Home.aspx" target="_blank" rel="noopener" aria-label="Telekom Malaysia Berhad"><img src="assets/img/clients/telekom-malaysia.png" alt="Telekom Malaysia logo" loading="lazy"></a>
      <a class="logo-plate" href="https://www.simedarby.com/" target="_blank" rel="noopener" aria-label="Sime Darby Berhad"><img src="assets/img/clients/sime-darby.png" alt="Sime Darby logo" loading="lazy"></a>
      <a class="logo-plate" href="http://cepatgroup.com/" target="_blank" rel="noopener" aria-label="Cepat Wawasan Sdn. Bhd."><img src="assets/img/clients/cepat-wawasan.png" alt="Cepat Wawasan logo" loading="lazy"></a>
      <a class="logo-plate" href="https://www.klkoleo.com/" target="_blank" rel="noopener" aria-label="KLK Berhad"><img src="assets/img/clients/klk-oleo.png" alt="KLK logo" loading="lazy"></a>
      <a class="logo-plate" href="https://www.cargill.com.my/" target="_blank" rel="noopener" aria-label="Cargill Palm Products Sdn. Bhd."><img src="assets/img/clients/cargill.png" alt="Cargill logo" loading="lazy"></a>
    </div>
  </div>
  <div class="container" style="text-align:center;margin-top:36px;">
    <a href="projects.html" class="btn btn-outline">View the full project reference list</a>
  </div>
</section>

<section class="section section--band">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Key Clients</div>
      <h2>Organisations that work with us</h2>
    </div>
    <div data-key-clients></div>
  </div>
</section>

<section class="section section--forest">
  <div class="container">
    <div class="section-head" style="margin-bottom:0;">
      <div class="kicker">1984-Today</div>
      <h2 style="max-width:18ch;">Four decades in Malaysian engineering</h2>
      <p style="max-width:60ch;">We started as a small electrical motor wiring workshop and grew into an established Class A, CIDB G7 M&amp;E Contractor working across Malaysia and beyond.</p>
      <a href="company-overview.html#our-story" class="btn btn-outline" style="margin:6px 0 40px;display:inline-block;">Our story &amp; timeline</a>
    </div>
  </div>
  <div class="marquee" data-marquee data-marquee-speed="26">
    <div class="marquee-track">
      <div class="milestone-chip"><b>1984</b><span>Incorporated in Malaysia as a master rewiring service provider</span></div>
      <div class="milestone-chip"><b>1984-2000s</b><span>Became an established Class A, CIDB G7 M&amp;E Contractor</span></div>
      <div class="milestone-chip"><b>2000</b><span>Opened a branch office in Lahad Datu, Sabah</span></div>
      <div class="milestone-chip"><b>Beyond MY</b><span>Took on international projects in Indonesia, Papua New Guinea &amp; Africa</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center" style="margin:0 auto 40px;">
      <div class="kicker" style="justify-content:center;">Credentials</div>
      <h2>Certifications &amp; Licenses</h2>
      <p class="lead" style="margin:0 auto;">A Class A, CIDB G7 M&amp;E Contractor, holding certification across every electrical and construction discipline we operate in.</p>
    </div>
    <div style="text-align:center;"><a href="certifications.html" class="btn btn-primary">View all certifications &amp; licenses</a></div>
  </div>
</section>

<section class="section section--forest">
  <div class="container text-center">
    <h2 style="max-width:20ch;margin:0 auto 16px;">Have an electrical or renewable energy project in mind? Let's talk</h2>
    <p style="margin:0 auto 30px;color:#DFF6E7;">Reach our team at the Port Klang headquarters, or at either of our branch offices in Sabah and Sarawak.</p>
    <a href="contact.html" class="btn btn-primary">Contact Us</a>
  </div>
</section>
"""

page(
    "index.html",
    "KLS | Electrical Engineering & Renewable Energy Interconnection, Kejuruteraan Letrik Seri",
    "Kejuruteraan Letrik Seri (M) Sdn Bhd (KLS) has operated as a Class A, CIDB G7 electrical engineering contractor and renewable energy interconnection specialist in Malaysia since 1984.",
    BODY,
    scripts='<script src="assets/js/entrance.js"></script>\n',
    alt_url="https://www.klseri.com.my/ms/index.html",
)
