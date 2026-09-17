from build import page, breadcrumb

BODY = f"""
<section class="page-hero">
  <div class="container">
    <h1>Projek Utama</h1>
    <p class="lead">Kami mengusahakan projek dan membantu menyediakan penyelesaian yang boleh dipercayai dan cekap tenaga untuk kerja, kehidupan dan komuniti. Dengan pengalaman berdekad, kami menggabungkan kepakaran dan kebijaksanaan untuk mencipta masa depan tenaga yang lebih hijau untuk semua.</p>
  </div>
</section>
{breadcrumb('projects.html','Projek', lang='ms')}

<section class="section" id="key-projects">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Pelanggan Terpilih</div>
      <h2>Dipercayai oleh pemain industri &amp; tenaga utama Malaysia</h2>
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
      <div class="kicker">Senarai Rujukan Projek</div>
      <h2>Layari senarai rujukan projek penuh</h2>
      <p class="lead">Setiap entri di bawah diambil daripada senarai rujukan projek KLS yang diterbitkan. Tapis mengikut kategori, cari mengikut pelanggan atau lokasi, atau kembangkan mana-mana pelanggan untuk melihat entri projek individu dengan tahun dan lokasi.</p>
    </div>

    <div class="stat-band" data-project-stats></div>

    <div class="project-toolbar">
      <input type="search" placeholder="Cari mengikut pelanggan, projek atau lokasi…" aria-label="Cari projek" data-project-search>
      <div class="chip-group">
        <button class="chip is-active" data-project-filter="all">Semua</button>
        <button class="chip" data-project-filter="power">Elektrik &amp; Pengagihan Kuasa</button>
        <button class="chip" data-project-filter="biogas">Biogas</button>
        <button class="chip" data-project-filter="biomass">Biojisim</button>
      </div>
    </div>

    <div class="grid" style="gap:14px;" data-project-list></div>
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
    "projects.html",
    "Projek Utama & Senarai Rujukan Projek | KLS",
    "KLS menangani projek secara langsung, menyediakan penyelesaian interkoneksi elektrik dan tenaga boleh diperbaharui yang boleh dipercayai dan cekap tenaga untuk tujuan perniagaan, kehidupan dan komuniti.",
    BODY,
    lang="ms",
    alt_url="https://www.klseri.com.my/projects.html",
)
