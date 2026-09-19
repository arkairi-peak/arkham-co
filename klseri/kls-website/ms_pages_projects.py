from build import page, breadcrumb

BODY = f"""
<section class="page-hero">
  <div class="container">
    <h1>Projek Utama</h1>
    <p class="lead">Setiap projek yang kami ambil bermatlamat menyampaikan penyelesaian yang boleh dipercayai dan cekap tenaga, untuk tempat kerja, rumah dan komuniti yang akhirnya menggunakannya. Pengalaman berdekad membolehkan kami menggabungkan kepakaran praktikal dengan penyelesaian masalah sebenar ke arah masa depan tenaga yang lebih hijau.</p>
  </div>
</section>
{breadcrumb('projects.html','Projek', lang='ms')}

<section class="section" id="key-projects">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Pelanggan Terpilih</div>
      <h2>Disokong oleh nama industri &amp; tenaga utama Malaysia</h2>
    </div>
  </div>
  <div class="marquee" data-marquee data-marquee-speed="30">
    <div class="marquee-track">
      <a class="logo-plate logo-plate--text" href="https://www.topglove.com/" target="_blank" rel="noopener" aria-label="Top Glove Berhad">Top Glove<br>Berhad</a>
      <a class="logo-plate" href="https://www.cenergi-sea.com/" target="_blank" rel="noopener" aria-label="Cenergi SEA Sdn. Bhd."><img src="../assets/img/clients/cenergi.png" alt="Cenergi SEA logo" loading="lazy"></a>
      <a class="logo-plate" href="https://www.tm.com.my/Pages/Home.aspx" target="_blank" rel="noopener" aria-label="Telekom Malaysia Berhad"><img src="../assets/img/clients/telekom-malaysia.png" alt="Telekom Malaysia logo" loading="lazy"></a>
      <a class="logo-plate" href="https://www.simedarby.com/" target="_blank" rel="noopener" aria-label="Sime Darby Berhad"><img src="../assets/img/clients/sime-darby.png" alt="Sime Darby logo" loading="lazy"></a>
      <a class="logo-plate" href="http://cepatgroup.com/" target="_blank" rel="noopener" aria-label="Cepat Wawasan Sdn. Bhd."><img src="../assets/img/clients/cepat-wawasan.png" alt="Cepat Wawasan logo" loading="lazy"></a>
      <a class="logo-plate" href="https://www.klkoleo.com/" target="_blank" rel="noopener" aria-label="KLK Berhad"><img src="../assets/img/clients/klk-oleo.png" alt="KLK logo" loading="lazy"></a>
      <a class="logo-plate" href="https://www.cargill.com.my/" target="_blank" rel="noopener" aria-label="Cargill Palm Products Sdn. Bhd."><img src="../assets/img/clients/cargill.png" alt="Cargill logo" loading="lazy"></a>
    </div>
  </div>
</section>

<section class="section section--band" id="reference-list">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Senarai Rujukan Projek</div>
      <h2>Layari senarai rujukan projek penuh</h2>
      <p class="lead">Setiap baris di bawah datang terus daripada senarai rujukan projek KLS sendiri. Tapis mengikut kategori, cari mengikut pelanggan atau lokasi, atau buka mana-mana pelanggan untuk melihat entri projek individu berserta tahun dan lokasi.</p>
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
    "KLS menangani projek secara langsung, menyampaikan kerja interkoneksi elektrik dan tenaga boleh diperbaharui yang dibina untuk kebolehpercayaan dan kecekapan merentasi tetapan perniagaan, kediaman dan komuniti.",
    BODY,
    lang="ms",
    alt_url="https://www.klseri.com.my/projects.html",
)
