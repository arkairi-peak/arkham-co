from build import page, breadcrumb

BODY = f"""
<section class="page-hero">
  <div class="container">
    <h1>Key Projects</h1>
    <p class="lead">Every project we take on is aimed at delivering reliable, energy-efficient solutions, for the workplaces, homes and communities they ultimately serve. Decades of experience let us pair practical expertise with genuine problem-solving toward a greener energy future.</p>
  </div>
</section>
{breadcrumb('projects.html','Projects')}

<section class="section" id="key-projects">
  <div class="container">
    <div class="section-head">
      <div class="kicker">HIGHLIGHTED CLIENTS</div>
      <h2>Backed by major Malaysian industrial &amp; energy names</h2>
    </div>
  </div>
  <div class="marquee" data-marquee data-marquee-speed="30">
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
</section>

<section class="section" id="project-map">
  <div class="container">
    <div class="section-head">
      <div class="kicker">PROJECT MAP</div>
      <h2>Where we have worked across Malaysia</h2>
      <p class="lead">Every pin is built from the reference list below. Click a pin for its projects, or pick a location from the list.</p>
    </div>
    <div class="chip-group" style="margin-bottom:16px;"><button class="chip is-active" data-map-filter="all">All</button><button class="chip" data-map-filter="power">Electrical &amp; Power Distribution</button><button class="chip" data-map-filter="biogas">Biogas</button><button class="chip" data-map-filter="biomass">Biomass</button><button class="chip" data-map-filter="stadium">Stadium &amp; Infrastructure</button></div>
    <div class="map-wrap">
      <div class="map-canvas" data-project-map role="application" aria-label="PROJECT MAP"></div>
      <aside class="map-panel">
        <div class="map-panel-head" data-map-summary></div>
        <ul class="map-places" data-map-places></ul>
        <div class="map-note">* Pins for state-level entries are approximate. Diamonds mark KLS offices.</div>
      </aside>
    </div>
    <div class="map-legend"><span><i style="background:#009447"></i>Electrical &amp; power</span><span><i style="background:#E3A73B"></i>Biogas</span><span><i style="background:#7A5C2E"></i>Biomass</span><span><i style="background:#182922"></i>Stadium</span></div>
  </div>
</section>

<section class="section section--band" id="reference-list">
  <div class="container">
    <div class="section-head">
      <div class="kicker">PROJECT REFERENCE LIST</div>
      <h2>Browse the full project reference list</h2>
      <p class="lead">Every line below comes straight from KLS's own project reference list. Filter by category, search by client or location, or open up any client to see the individual project entries, year and location included.</p>
    </div>

    <div class="stat-band" data-project-stats></div>

    <div class="project-toolbar">
      <input type="search" placeholder="Search by client, project or location…" aria-label="Search projects" data-project-search>
      <div class="chip-group">
        <button class="chip is-active" data-project-filter="all">All</button>
        <button class="chip" data-project-filter="power">Electrical &amp; Power Distribution</button>
        <button class="chip" data-project-filter="biogas">Biogas</button>
        <button class="chip" data-project-filter="biomass">Biomass</button>
        <button class="chip" data-project-filter="stadium">Stadium &amp; Infrastructure</button>
      </div>
    </div>

    <div class="grid" style="gap:14px;" data-project-list></div>
  </div>
</section>

<section class="section section--forest text-center">
  <div class="container">
    <h2>Get In Touch with Us</h2>
    <a href="contact.html" class="btn btn-primary">Contact Us</a>
  </div>
</section>
"""

page(
    "projects.html",
    "Key Projects & Project Reference List | KLS",
    "KLS takes projects head-on, delivering electrical and renewable-energy interconnection work built for reliability and efficiency across business, residential and community settings.",
    BODY,
    scripts='<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.4/dist/leaflet.css">\n<script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.4/dist/leaflet.js"></script>\n<script src="assets/js/map.js"></script>\n',
    alt_url="https://www.klseri.com.my/ms/projects.html",
)
