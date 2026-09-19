from build import page

BODY = """
<section class="page-hero" style="padding:90px 0 100px;text-align:center;">
  <div class="container">
    <div class="kicker" style="justify-content:center;">Error 404</div>
    <h1 style="max-width:none;font-size:clamp(3.5rem,10vw,6.5rem);">Page not found</h1>
    <p class="lead" style="margin:0 auto;max-width:52ch;">This page might have moved, been renamed, or just never existed in the first place. Let's point you somewhere useful instead.</p>
    <div class="hero-actions" style="justify-content:center;margin-top:30px;">
      <a href="index.html" class="btn btn-primary">Back to Home</a>
      <a href="contact.html" class="btn btn-outline">Contact Us</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center" style="margin:0 auto 40px;">
      <div class="kicker" style="justify-content:center;">Where would you like to go?</div>
      <h2>Popular pages</h2>
    </div>
    <div class="spec-list">
      <div class="spec-row">
        <span class="num mono">01</span>
        <div><h4><a href="company-overview.html" style="color:inherit;">Company Overview</a></h4><p style="margin-top:6px;">Our story, mission, vision and core values since 1984.</p></div>
      </div>
      <div class="spec-row">
        <span class="num mono">02</span>
        <div><h4><a href="services.html" style="color:inherit;">Our Services</a></h4><p style="margin-top:6px;">Electrical power distribution and Biogas, Biomass &amp; Solar renewable energy interconnection.</p></div>
      </div>
      <div class="spec-row">
        <span class="num mono">03</span>
        <div><h4><a href="projects.html" style="color:inherit;">Key Projects</a></h4><p style="margin-top:6px;">Browse the full, searchable project reference list.</p></div>
      </div>
      <div class="spec-row">
        <span class="num mono">04</span>
        <div><h4><a href="contact.html" style="color:inherit;">Contact Us</a></h4><p style="margin-top:6px;">Reach our Port Klang HQ, or our Sabah &amp; Sarawak branch offices.</p></div>
      </div>
    </div>
  </div>
</section>
"""

page(
    "404.html",
    "Page Not Found | KLS, Kejuruteraan Letrik Seri (M) Sdn Bhd",
    "This page couldn't be found. Head back to the KLS homepage or check out our most-visited pages instead.",
    BODY,
    alt_url="https://www.klseri.com.my/ms/404.html",
)
