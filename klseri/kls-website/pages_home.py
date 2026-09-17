from build import page

BODY = """
<section class="hero">
  <div class="hero-slides">
    <div class="hero-slide is-active" data-hero-title="Powering Your Business" data-hero-lead="Kejuruteraan Letrik Seri (M) Sdn Bhd, also known as KLS, was incorporated in 1984, positioning ourselves as a master rewiring service provider. As we continued to grow, we diversified our services to providing supply, installation, testing, commissioning and warranty of High Voltage, Low Voltage and Extra Low Voltage electrical systems for residential, commercial, industrial, infrastructural and marine development.">
      <img src="https://www.klseri.com.my/wp-content/uploads/2021/03/sustainable_growth_istock.jpg" alt="KLS electrical engineering — powering your business">
    </div>
    <div class="hero-slide" data-hero-title="Enabling Sustainable and Clean Energy Solutions" data-hero-lead="As one of the industry leaders in Malaysia, we embrace natural resources and recognise the need for sustainable development — undertaking numerous Renewable Energy Interconnection contracts and initiatives encompassing Biogas, Biomass, Solar and Cogeneration Plants.">
      <img src="https://www.klseri.com.my/wp-content/uploads/2021/03/light-bulb-placed-on-soil-in-sun-light.jpg" alt="Clean energy — light bulb placed on soil in sunlight">
    </div>
    <div class="hero-slide" data-hero-title="Biomass Power" data-hero-lead="From engineering and supply through to installation and commissioning of cables and electrical equipment, KLS delivers specialised interconnection solutions for biomass power plants — including 10MW for Cepat Wawasan Sdn. Bhd.">
      <img src="https://www.klseri.com.my/wp-content/uploads/2021/05/2021-05-10-015217938.jpg" alt="KLS renewable energy interconnection works">
    </div>
  </div>
  <div class="container hero-inner">
    <div>
      <div class="hero-eyebrow">Electrical Engineering &amp; Renewable Energy Interconnection &middot; Since 1984</div>
      <h1 class="reveal" data-hero-title-el>Powering Your Business</h1>
      <p class="lead reveal" data-hero-lead-el>Kejuruteraan Letrik Seri (M) Sdn Bhd, also known as KLS, was incorporated in 1984, positioning ourselves as a master rewiring service provider. As we continued to grow, we diversified our services to providing supply, installation, testing, commissioning and warranty of High Voltage, Low Voltage and Extra Low Voltage electrical systems for residential, commercial, industrial, infrastructural and marine development.</p>
      <div class="hero-actions reveal">
        <a href="company-overview.html" class="btn btn-primary">Learn more about KLS</a>
        <a href="services.html#renewable-energy" class="btn btn-outline">Our renewable energy work</a>
      </div>
    </div>
    <div class="hero-stats reveal">
      <div class="hero-stat"><b data-count-to="1984" data-count-suffix="">0</b><span>Year incorporated</span></div>
      <div class="hero-stat"><b data-count-to="4" data-count-suffix="">0</b><span>Renewable energy verticals — Biogas, Biomass, Solar, Cogeneration</span></div>
      <div class="hero-stat"><b>Class A</b><span>CIDB G7 M&amp;E Contractor</span></div>
      <div class="hero-stat"><b>3</b><span>Locations — Port Klang &middot; Lahad Datu &middot; Bintulu</span></div>
    </div>
  </div>
  <div class="hero-dots">
    <button data-hero-dot class="is-active" aria-label="Slide 1: Powering Your Business"></button>
    <button data-hero-dot aria-label="Slide 2: Enabling Sustainable and Clean Energy Solutions"></button>
    <button data-hero-dot aria-label="Slide 3: Biomass Power"></button>
  </div>
</section>

<section class="section">
  <div class="container grid grid-2" style="align-items:center;gap:56px;">
    <div>
      <div class="kicker">About KLS</div>
      <h2>A master rewiring specialist that grew into a full-scope electrical &amp; renewable energy contractor</h2>
      <p class="lead">As one of the industry leaders in Malaysia, KLS embraces natural resources and recognises the need for sustainable development, undertaking numerous Renewable Energy Interconnection contracts and initiatives encompassing Biogas, Biomass, Solar and Cogeneration Plants.</p>
      <a href="company-overview.html" class="btn-ghost">Read the full company overview</a>
    </div>
    <div class="grid" style="gap:16px;">
      <img src="https://www.klseri.com.my/wp-content/uploads/2021/03/sustainable_growth_istock.jpg" alt="Sustainable growth — KLS embraces renewable energy and sustainable development" style="border-radius:10px;border:1px solid var(--line-300);">
      <img src="https://www.klseri.com.my/wp-content/uploads/2021/03/light-bulb-placed-on-soil-in-sun-light.jpg" alt="Light bulb placed on soil in sunlight — clean energy at KLS" style="border-radius:10px;border:1px solid var(--line-300);">
    </div>
  </div>
</section>

<section class="section section--band">
  <div class="container">
    <div class="section-head">
      <div class="kicker">What We Do</div>
      <h2>Our Services</h2>
      <p class="lead">With our industry knowledge and experience, we provide quality services, products and works to our valued clients to assist them in achieving their business goals. We provide services which include the supply, installation, testing and commissioning for:</p>
    </div>
    <div class="spec-list">
      <div class="spec-row">
        <span class="num mono">01</span>
        <div>
          <h4>Electrical Power Distribution Systems</h4>
          <p style="margin-top:8px;">Medium/High Voltage &amp; Low Voltage power systems, AMF boards, MCCs, transformers, power cabling, diesel generator systems and the ELV/ICT systems that surround them.</p>
          <a href="services.html#electrical-power-distribution" class="btn-ghost">Learn more</a>
        </div>
      </div>
      <div class="spec-row">
        <span class="num mono">02</span>
        <div>
          <h4>Renewable Energy</h4>
          <p style="margin-top:8px;">Interconnection facilities that deliver Biogas, Biomass and Solar plant generation power to the national grid efficiently, with minimal downtime.</p>
          <a href="services.html#renewable-energy" class="btn-ghost">Learn more</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--forest">
  <div class="container">
    <div class="kicker">1984 — Today</div>
    <h2 style="max-width:18ch;">Four decades of Malaysian engineering experience</h2>
    <p style="max-width:60ch;">From a humble electrical motor wiring workshop to an established Class A, CIDB G7 M&amp;E Contractor working across Malaysia and abroad.</p>
    <a href="company-overview.html#our-story" class="btn btn-outline" style="margin:6px 0 40px;">Our story &amp; timeline</a>
  </div>
  <div class="marquee" data-marquee data-marquee-speed="26">
    <div class="marquee-track">
      <div class="milestone-chip"><b>1984</b><span>Incorporated in Malaysia, as a master rewiring service provider</span></div>
      <div class="milestone-chip"><b>1984–2000s</b><span>Grew into an established Class A, CIDB G7 M&amp;E Contractor</span></div>
      <div class="milestone-chip"><b>2000</b><span>Branch office opened in Lahad Datu, Sabah</span></div>
      <div class="milestone-chip"><b>Beyond MY</b><span>International works in Indonesia, Papua New Guinea &amp; Africa</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center" style="margin:0 auto 40px;">
      <div class="kicker" style="justify-content:center;">Key Projects</div>
      <h2>Trusted by major Malaysian industrial &amp; energy players</h2>
    </div>
  </div>
  <div class="marquee" data-marquee data-marquee-speed="28">
    <div class="marquee-track">
      <div class="client-chip">Top Glove Berhad</div>
      <div class="client-chip">Cenergi SEA Sdn. Bhd.</div>
      <div class="client-chip">Telekom Malaysia Berhad</div>
      <div class="client-chip">Sime Darby Berhad</div>
      <div class="client-chip">Cepat Wawasan Sdn. Bhd.</div>
      <div class="client-chip">KLK Berhad</div>
      <div class="client-chip">Cargill Palm Products Sdn. Bhd.</div>
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
      <h2>Leadership behind KLS</h2>
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
      <p class="lead" style="margin:0 auto;">A Class A, CIDB G7 M&amp;E Contractor, certified across the electrical and construction disciplines it operates in.</p>
    </div>
    <div style="text-align:center;"><a href="certifications.html" class="btn btn-primary">View all certifications &amp; licenses</a></div>
  </div>
</section>

<section class="section section--band">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Key Clients</div>
      <h2>Organisations we work with</h2>
    </div>
    <div class="logo-strip" data-key-clients></div>
  </div>
</section>

<section class="section section--forest">
  <div class="container text-center">
    <h2 style="max-width:20ch;margin:0 auto 16px;">Let's talk about your next electrical or renewable energy project</h2>
    <p style="margin:0 auto 30px;color:#DFF6E7;">Get in touch with our team at our Port Klang headquarters, or our branch offices in Sabah and Sarawak.</p>
    <a href="contact.html" class="btn btn-primary">Contact Us</a>
  </div>
</section>
"""

page(
    "index.html",
    "KLS — Electrical Engineering & Renewable Energy Interconnection | Kejuruteraan Letrik Seri",
    "Kejuruteraan Letrik Seri (M) Sdn Bhd (KLS), incorporated in 1984 — a Class A, CIDB G7 electrical engineering contractor and renewable energy interconnection specialist in Malaysia.",
    BODY,
    alt_url="https://www.klseri.com.my/ms/index.html",
)
