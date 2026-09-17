from build import page, breadcrumb

BODY = f"""
<section class="page-hero">
  <div class="container">
    <h1>Certifications &amp; Licenses</h1>
    <p class="lead">Peruse KLS's complete set of certifications &amp; licenses so you can place total confidence in us to provide the best solutions for your business.</p>
  </div>
</section>
{breadcrumb('certifications.html','Certifications &amp; Licenses')}

<section class="section">
  <div class="container">
    <div class="grid grid-4" data-cert-grid></div>
    <p class="small" style="margin-top:28px;">Certificate images are reproduced from KLS's published Certifications &amp; Licenses page. Select any certificate to view it enlarged.</p>
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
    "certifications.html",
    "Certifications & Licenses | KLS",
    "KLS's complete set of certifications and licenses — a Class A, CIDB G7 M&E Contractor certified to deliver electrical engineering and renewable energy interconnection works.",
    BODY,
    alt_url="https://www.klseri.com.my/ms/certifications.html",
)
