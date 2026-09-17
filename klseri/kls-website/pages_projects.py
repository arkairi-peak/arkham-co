from build import page, breadcrumb

BODY = f"""
<section class="page-hero">
  <div class="container">
    <h1>Key Projects</h1>
    <p class="lead">We take on projects and help provide reliable and energy-efficient solutions for work, living and community. With decades of experience, we combine expertise and ingenuity to create a greener energy future for people.</p>
  </div>
</section>
{breadcrumb('projects.html','Projects')}

<section class="section" id="key-projects">
  <div class="container">
    <div class="section-head">
      <div class="kicker">HIGHLIGHTED CLIENTS</div>
      <h2>Trusted by major Malaysian industrial &amp; energy players</h2>
    </div>
  </div>
  <div class="marquee" data-marquee data-marquee-speed="30">
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
</section>

<section class="section section--band" id="reference-list">
  <div class="container">
    <div class="section-head">
      <div class="kicker">PROJECT REFERENCE LIST</div>
      <h2>Browse the full project reference list</h2>
      <p class="lead">Every entry below is drawn from KLS's published project reference list. Filter by category, search by client or location, or expand any client to see individual project entries with year and location.</p>
    </div>

    <div class="stat-band" data-project-stats></div>

    <div class="project-toolbar">
      <input type="search" placeholder="Search by client, project or location…" aria-label="Search projects" data-project-search>
      <div class="chip-group">
        <button class="chip is-active" data-project-filter="all">All</button>
        <button class="chip" data-project-filter="power">Electrical &amp; Power Distribution</button>
        <button class="chip" data-project-filter="biogas">Biogas</button>
        <button class="chip" data-project-filter="biomass">Biomass</button>
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
    "KLS tackles projects head-on, providing reliable and energy-efficient electrical and renewable-energy interconnection solutions for business, living and community purposes.",
    BODY,
    alt_url="https://www.klseri.com.my/ms/projects.html",
)
