from build import page

BODY = """
<div class="page-curtain" data-page-curtain aria-hidden="true">
  <div class="page-curtain-blobs"></div>
  <div class="page-curtain-tiles">
    <span style="animation-delay:0.550s"></span>
    <span style="animation-delay:0.595s"></span>
    <span style="animation-delay:0.640s"></span>
    <span style="animation-delay:0.685s"></span>
    <span style="animation-delay:0.595s"></span>
    <span style="animation-delay:0.640s"></span>
    <span style="animation-delay:0.685s"></span>
    <span style="animation-delay:0.730s"></span>
    <span style="animation-delay:0.640s"></span>
    <span style="animation-delay:0.685s"></span>
    <span style="animation-delay:0.730s"></span>
    <span style="animation-delay:0.775s"></span>
    <span style="animation-delay:0.685s"></span>
    <span style="animation-delay:0.730s"></span>
    <span style="animation-delay:0.775s"></span>
    <span style="animation-delay:0.820s"></span>
  </div>
  <div class="page-curtain-mark"><img src="assets/img/logo/kls-icon.png" alt=""></div>
</div>
<script>try{if(sessionStorage.getItem('klsCurtainSeen')==='1'||window.matchMedia('(prefers-reduced-motion: reduce)').matches){document.currentScript.previousElementSibling.style.display='none';}else{sessionStorage.setItem('klsCurtainSeen','1');}}catch(e){}</script>
<section class="hero">
  <div class="hero-slides">
    <div class="hero-slide is-active" data-hero-title="Energy That Keeps Your Business Running" data-hero-lead="Kejuruteraan Letrik Seri (M) Sdn Bhd, known simply as KLS, was incorporated in 1984 as a master rewiring service provider. As the business grew, so did what we offered: today we supply, install, test, commission and warranty High Voltage, Low Voltage and Extra Low Voltage electrical systems across residential, commercial, industrial, infrastructure and marine projects.">
      <img src="https://www.klseri.com.my/wp-content/uploads/2021/03/sustainable_growth_istock.jpg" alt="KLS electrical engineering, powering your business">
    </div>
    <div class="hero-slide" data-hero-title="Backing Clean, Sustainable Energy" data-hero-lead="As one of Malaysia's established industry names, we put real weight behind sustainable development, taking on Renewable Energy Interconnection contracts and initiatives across Biogas, Biomass, Solar and Cogeneration plants.">
      <img src="https://www.klseri.com.my/wp-content/uploads/2021/03/light-bulb-placed-on-soil-in-sun-light.jpg" alt="Clean energy, light bulb placed on soil in sunlight">
    </div>
    <div class="hero-slide" data-hero-title="Powering Through Biomass" data-hero-lead="From engineering and supply through to installing and commissioning cables and electrical equipment, KLS builds specialised interconnection solutions for biomass power plants, including a 10MW project for Cepat Wawasan Sdn. Bhd.">
      <img src="https://www.klseri.com.my/wp-content/uploads/2021/05/2021-05-10-015217938.jpg" alt="KLS renewable energy interconnection works">
    </div>
  </div>
  <div class="container hero-inner">
    <div>
      <div class="hero-eyebrow reveal" style="animation-delay:.55s">Electrical Engineering &amp; Renewable Energy, Since 1984</div>
      <h1 class="reveal" style="animation-delay:.68s" data-hero-title-el>Energy That Keeps Your Business Running</h1>
      <p class="lead reveal" style="animation-delay:.8s" data-hero-lead-el>Kejuruteraan Letrik Seri (M) Sdn Bhd, known simply as KLS, was incorporated in 1984 as a master rewiring service provider. As the business grew, so did what we offered: today we supply, install, test, commission and warranty High Voltage, Low Voltage and Extra Low Voltage electrical systems across residential, commercial, industrial, infrastructure and marine projects.</p>
      <div class="hero-actions reveal" style="animation-delay:.95s">
        <a href="company-overview.html" class="btn btn-primary">See the full company story</a>
        <a href="services.html#renewable-energy" class="btn btn-outline">Our renewable energy work</a>
      </div>
    </div>
    <div class="hero-stats reveal" style="animation-delay:1.05s">
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

<section class="section">
  <div class="container grid grid-2" style="align-items:center;gap:56px;">
    <div>
      <div class="kicker">About KLS</div>
      <h2>From rewiring specialist to full-scope electrical &amp; renewable energy contractor</h2>
      <p class="lead">KLS has grown into one of Malaysia's established industry names, taking sustainable development seriously enough to back it with real projects: Renewable Energy Interconnection contracts across Biogas, Biomass, Solar and Cogeneration plants.</p>
      <a href="company-overview.html" class="btn-ghost">See the full company story</a>
    </div>
    <div class="grid" style="gap:16px;">
      <img src="https://www.klseri.com.my/wp-content/uploads/2021/03/sustainable_growth_istock.jpg" alt="Sustainable growth, KLS embraces renewable energy and sustainable development" style="border-radius:10px;border:1px solid var(--line-300);">
      <img src="https://www.klseri.com.my/wp-content/uploads/2021/03/light-bulb-placed-on-soil-in-sun-light.jpg" alt="Light bulb placed on soil in sunlight, clean energy at KLS" style="border-radius:10px;border:1px solid var(--line-300);">
    </div>
  </div>
</section>

<section class="section section--band">
  <div class="container">
    <div class="section-head">
      <div class="kicker">What We Do</div>
      <h2>Our Services</h2>
      <p class="lead">Drawing on years of hands-on industry experience, we deliver the services, products and work our clients need to hit their business goals, covering supply, installation, testing and commissioning across:</p>
    </div>
    <div class="spec-list">
      <div class="spec-row">
        <span class="num mono">01</span>
        <div>
          <h4>Electrical Power Distribution Systems</h4>
          <p style="margin-top:8px;">Medium/High Voltage and Low Voltage power systems, AMF boards, MCCs, transformers, power cabling, diesel generator systems, plus the ELV/ICT systems that tie it all together.</p>
          <a href="services.html#electrical-power-distribution" class="btn-ghost">Learn more</a>
        </div>
      </div>
      <div class="spec-row">
        <span class="num mono">02</span>
        <div>
          <h4>Renewable Energy</h4>
          <p style="margin-top:8px;">Interconnection facilities that move Biogas, Biomass and Solar power efficiently onto the national grid, with as little downtime as possible.</p>
          <a href="services.html#renewable-energy" class="btn-ghost">Learn more</a>
        </div>
      </div>
    </div>
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
      <div class="kicker">Our People</div>
      <h2>The people leading KLS</h2>
    </div>
    <div class="grid grid-4" data-people-preview></div>
    <div style="margin-top:30px;"><a href="our-people.html" class="btn btn-outline">Meet the full team</a></div>
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
    alt_url="https://www.klseri.com.my/ms/index.html",
)
