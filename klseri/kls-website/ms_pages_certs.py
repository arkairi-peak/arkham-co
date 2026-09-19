from build import page, breadcrumb

BODY = f"""
<section class="page-hero">
  <div class="container">
    <h1>Pensijilan &amp; Lesen</h1>
    <p class="lead">Layari koleksi penuh pensijilan &amp; lesen KLS, kelayakan di sebalik dakwaan kami untuk menyampaikan penyelesaian yang tepat bagi perniagaan anda.</p>
  </div>
</section>
{breadcrumb('certifications.html','Pensijilan &amp; Lesen', lang='ms')}

<section class="section">
  <div class="container">
    <div class="grid grid-4" data-cert-grid></div>
    <p class="small" style="margin-top:28px;">Imej sijil ini dipaparkan semula daripada laman Pensijilan &amp; Lesen KLS yang diterbitkan. Pilih mana-mana satu untuk melihatnya pada saiz penuh.</p>
  </div>
</section>

<section class="section section--forest text-center">
  <div class="container">
    <h2>Hubungi Kami</h2>
    <a href="contact.html" class="btn btn-primary">Hubungi Kami</a>
  </div>
</section>
"""

page(
    "certifications.html",
    "Pensijilan & Lesen | KLS",
    "Koleksi penuh pensijilan dan lesen di sebalik KLS, Kontraktor M&E Kelas A, CIDB G7 yang berkelayakan menyampaikan kerja kejuruteraan elektrik dan interkoneksi tenaga boleh diperbaharui.",
    BODY,
    lang="ms",
    alt_url="https://www.klseri.com.my/certifications.html",
)
