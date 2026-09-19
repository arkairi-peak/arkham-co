from build import page

BODY = """
<section class="page-hero" style="padding:90px 0 100px;text-align:center;">
  <div class="container">
    <div class="kicker" style="justify-content:center;">Ralat 404</div>
    <h1 style="max-width:none;font-size:clamp(3.5rem,10vw,6.5rem);">Laman tidak ditemui</h1>
    <p class="lead" style="margin:0 auto;max-width:52ch;">Laman ini mungkin telah dipindahkan, ditukar nama, atau memang tidak pernah wujud sejak awal. Mari kami bawa anda ke tempat yang berguna.</p>
    <div class="hero-actions" style="justify-content:center;margin-top:30px;">
      <a href="index.html" class="btn btn-primary">Kembali ke Laman Utama</a>
      <a href="contact.html" class="btn btn-outline">Hubungi Kami</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center" style="margin:0 auto 40px;">
      <div class="kicker" style="justify-content:center;">Ke mana anda ingin pergi?</div>
      <h2>Laman popular</h2>
    </div>
    <div class="spec-list">
      <div class="spec-row">
        <span class="num mono">01</span>
        <div><h4><a href="company-overview.html" style="color:inherit;">Ikhtisar Syarikat</a></h4><p style="margin-top:6px;">Kisah, misi, wawasan dan nilai teras kami sejak 1984.</p></div>
      </div>
      <div class="spec-row">
        <span class="num mono">02</span>
        <div><h4><a href="services.html" style="color:inherit;">Perkhidmatan Kami</a></h4><p style="margin-top:6px;">Pengagihan kuasa elektrik dan interkoneksi tenaga boleh diperbaharui Biogas, Biojisim &amp; Suria.</p></div>
      </div>
      <div class="spec-row">
        <span class="num mono">03</span>
        <div><h4><a href="projects.html" style="color:inherit;">Projek Utama</a></h4><p style="margin-top:6px;">Layari senarai rujukan projek penuh yang boleh dicari.</p></div>
      </div>
      <div class="spec-row">
        <span class="num mono">04</span>
        <div><h4><a href="contact.html" style="color:inherit;">Hubungi Kami</a></h4><p style="margin-top:6px;">Hubungi ibu pejabat Port Klang, atau pejabat cawangan Sabah &amp; Sarawak kami.</p></div>
      </div>
    </div>
  </div>
</section>
"""

page(
    "404.html",
    "Laman Tidak Ditemui | KLS, Kejuruteraan Letrik Seri (M) Sdn Bhd",
    "Laman ini tidak dapat ditemui. Kembali ke laman utama KLS atau semak laman kami yang paling banyak dikunjungi.",
    BODY,
    lang="ms",
    alt_url="https://www.klseri.com.my/404.html",
)
