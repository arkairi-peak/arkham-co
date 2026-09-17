from build import page

BODY = """
<section class="hero">
  <div class="hero-slides">
    <div class="hero-slide is-active" data-hero-title="Menggerakkan Perniagaan Anda" data-hero-lead="Kejuruteraan Letrik Seri (M) Sdn Bhd, atau dikenali sebagai KLS, telah diperbadankan pada tahun 1984, bermula sebagai penyedia perkhidmatan pendawaian semula (rewiring) utama. Seiring perkembangan syarikat, kami mempelbagaikan perkhidmatan kepada bekalan, pemasangan, pengujian, pentauliahan dan waranti sistem elektrik Voltan Tinggi, Voltan Rendah dan Voltan Sangat Rendah untuk pembangunan kediaman, komersial, industri, infrastruktur dan marin.">
      <img src="https://www.klseri.com.my/wp-content/uploads/2021/03/sustainable_growth_istock.jpg" alt="Kejuruteraan elektrik KLS — menggerakkan perniagaan anda">
    </div>
    <div class="hero-slide" data-hero-title="Menyokong Penyelesaian Tenaga Bersih dan Mampan" data-hero-lead="Sebagai salah sebuah peneraju industri di Malaysia, kami menghargai sumber semula jadi dan mengiktiraf keperluan pembangunan mampan — melaksanakan pelbagai kontrak dan inisiatif Interkoneksi Tenaga Boleh Diperbaharui merangkumi Loji Biogas, Biojisim, Suria dan Kogenerasi.">
      <img src="https://www.klseri.com.my/wp-content/uploads/2021/03/light-bulb-placed-on-soil-in-sun-light.jpg" alt="Tenaga bersih — mentol lampu di atas tanah di bawah cahaya matahari">
    </div>
    <div class="hero-slide" data-hero-title="Kuasa Biojisim" data-hero-lead="Daripada kejuruteraan dan bekalan sehingga pemasangan dan pentauliahan kabel serta peralatan elektrik, KLS menyampaikan penyelesaian interkoneksi khusus untuk loji kuasa biojisim — termasuk projek 10MW untuk Cepat Wawasan Sdn. Bhd.">
      <img src="https://www.klseri.com.my/wp-content/uploads/2021/05/2021-05-10-015217938.jpg" alt="Kerja interkoneksi tenaga boleh diperbaharui KLS">
    </div>
  </div>
  <div class="container hero-inner">
    <div>
      <div class="hero-eyebrow">Kejuruteraan Elektrik &amp; Interkoneksi Tenaga Boleh Diperbaharui &middot; Sejak 1984</div>
      <h1 class="reveal" data-hero-title-el>Menggerakkan Perniagaan Anda</h1>
      <p class="lead reveal" data-hero-lead-el>Kejuruteraan Letrik Seri (M) Sdn Bhd, atau dikenali sebagai KLS, telah diperbadankan pada tahun 1984, bermula sebagai penyedia perkhidmatan pendawaian semula (rewiring) utama. Seiring perkembangan syarikat, kami mempelbagaikan perkhidmatan kepada bekalan, pemasangan, pengujian, pentauliahan dan waranti sistem elektrik Voltan Tinggi, Voltan Rendah dan Voltan Sangat Rendah untuk pembangunan kediaman, komersial, industri, infrastruktur dan marin.</p>
      <div class="hero-actions reveal">
        <a href="company-overview.html" class="btn btn-primary">Ketahui Lebih Lanjut Tentang KLS</a>
        <a href="services.html#renewable-energy" class="btn btn-outline">Kerja Tenaga Boleh Diperbaharui Kami</a>
      </div>
    </div>
    <div class="hero-stats reveal">
      <div class="hero-stat"><b data-count-to="1984" data-count-suffix="">0</b><span>Tahun diperbadankan</span></div>
      <div class="hero-stat"><b data-count-to="4" data-count-suffix="">0</b><span>Bidang tenaga boleh diperbaharui — Biogas, Biojisim, Suria, Kogenerasi</span></div>
      <div class="hero-stat"><b>Kelas A</b><span>Kontraktor M&amp;E CIDB G7</span></div>
      <div class="hero-stat"><b>3</b><span>Lokasi — Port Klang &middot; Lahad Datu &middot; Bintulu</span></div>
    </div>
  </div>
  <div class="hero-dots">
    <button data-hero-dot class="is-active" aria-label="Slaid 1: Menggerakkan Perniagaan Anda"></button>
    <button data-hero-dot aria-label="Slaid 2: Menyokong Penyelesaian Tenaga Bersih dan Mampan"></button>
    <button data-hero-dot aria-label="Slaid 3: Kuasa Biojisim"></button>
  </div>
</section>

<section class="section">
  <div class="container grid grid-2" style="align-items:center;gap:56px;">
    <div>
      <div class="kicker">Tentang KLS</div>
      <h2>Pakar pendawaian semula yang berkembang menjadi kontraktor elektrik &amp; tenaga boleh diperbaharui bersepadu</h2>
      <p class="lead">Sebagai salah sebuah peneraju industri di Malaysia, KLS menghargai sumber semula jadi dan mengiktiraf keperluan pembangunan mampan, dengan melaksanakan pelbagai kontrak dan inisiatif Interkoneksi Tenaga Boleh Diperbaharui merangkumi Loji Biogas, Biojisim, Suria dan Kogenerasi.</p>
      <a href="company-overview.html" class="btn-ghost">Baca Ikhtisar Syarikat Penuh</a>
    </div>
    <div class="grid" style="gap:16px;">
      <img src="https://www.klseri.com.my/wp-content/uploads/2021/03/sustainable_growth_istock.jpg" alt="Pertumbuhan mampan — KLS menerajui tenaga boleh diperbaharui dan pembangunan mampan" style="border-radius:10px;border:1px solid var(--line-300);">
      <img src="https://www.klseri.com.my/wp-content/uploads/2021/03/light-bulb-placed-on-soil-in-sun-light.jpg" alt="Mentol lampu di atas tanah di bawah cahaya matahari — tenaga bersih di KLS" style="border-radius:10px;border:1px solid var(--line-300);">
    </div>
  </div>
</section>

<section class="section section--band">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Apa Yang Kami Lakukan</div>
      <h2>Perkhidmatan Kami</h2>
      <p class="lead">Dengan pengetahuan dan pengalaman industri kami, kami menyediakan perkhidmatan, produk dan kerja berkualiti kepada pelanggan kami bagi membantu mereka mencapai matlamat perniagaan. Perkhidmatan kami merangkumi bekalan, pemasangan, pengujian dan pentauliahan untuk:</p>
    </div>
    <div class="spec-list">
      <div class="spec-row">
        <span class="num mono">01</span>
        <div>
          <h4>Sistem Pengagihan Kuasa Elektrik</h4>
          <p style="margin-top:8px;">Sistem kuasa Voltan Sederhana/Tinggi &amp; Voltan Rendah, papan AMF, MCC, transformer, kabel kuasa, sistem penjana diesel serta sistem ELV/ICT yang berkaitan.</p>
          <a href="services.html#electrical-power-distribution" class="btn-ghost">Ketahui Lebih Lanjut</a>
        </div>
      </div>
      <div class="spec-row">
        <span class="num mono">02</span>
        <div>
          <h4>Tenaga Boleh Diperbaharui</h4>
          <p style="margin-top:8px;">Kemudahan interkoneksi yang menyalurkan kuasa janaan loji Biogas, Biojisim dan Suria ke grid nasional dengan cekap dan gangguan yang minimum.</p>
          <a href="services.html#renewable-energy" class="btn-ghost">Ketahui Lebih Lanjut</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--forest">
  <div class="container">
    <div class="kicker">1984 — Kini</div>
    <h2 style="max-width:18ch;">Empat dekad pengalaman kejuruteraan Malaysia</h2>
    <p style="max-width:60ch;">Bermula daripada bengkel pendawaian motor elektrik yang kecil, kini menjadi Kontraktor M&amp;E Kelas A, CIDB G7 yang mantap, beroperasi di seluruh Malaysia dan luar negara.</p>
    <a href="company-overview.html#our-story" class="btn btn-outline" style="margin:6px 0 40px;">Kisah &amp; Garis Masa Kami</a>
  </div>
  <div class="marquee" data-marquee data-marquee-speed="26">
    <div class="marquee-track">
      <div class="milestone-chip"><b>1984</b><span>Diperbadankan di Malaysia, sebagai penyedia perkhidmatan pendawaian semula utama</span></div>
      <div class="milestone-chip"><b>1984–2000-an</b><span>Berkembang menjadi Kontraktor M&amp;E Kelas A, CIDB G7 yang mantap</span></div>
      <div class="milestone-chip"><b>2000</b><span>Pejabat cawangan dibuka di Lahad Datu, Sabah</span></div>
      <div class="milestone-chip"><b>Ke Luar Negara</b><span>Kerja antarabangsa di Indonesia, Papua New Guinea &amp; Afrika</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center" style="margin:0 auto 40px;">
      <div class="kicker" style="justify-content:center;">Projek Utama</div>
      <h2>Dipercayai oleh pemain industri &amp; tenaga utama Malaysia</h2>
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
    <a href="projects.html" class="btn btn-outline">Lihat Senarai Rujukan Projek Penuh</a>
  </div>
</section>

<section class="section section--band">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Warga Kerja Kami</div>
      <h2>Kepimpinan di Sebalik KLS</h2>
    </div>
    <div class="grid grid-4" data-people-preview></div>
    <div style="margin-top:30px;"><a href="our-people.html" class="btn btn-outline">Kenali Pasukan Penuh Kami</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center" style="margin:0 auto 40px;">
      <div class="kicker" style="justify-content:center;">Kelayakan</div>
      <h2>Pensijilan &amp; Lesen</h2>
      <p class="lead" style="margin:0 auto;">Kontraktor M&amp;E Kelas A, CIDB G7, diperakui merentasi bidang elektrik dan pembinaan yang diceburi.</p>
    </div>
    <div style="text-align:center;"><a href="certifications.html" class="btn btn-primary">Lihat Semua Pensijilan &amp; Lesen</a></div>
  </div>
</section>

<section class="section section--band">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Pelanggan Utama</div>
      <h2>Organisasi yang kami berurusan</h2>
    </div>
    <div class="logo-strip" data-key-clients></div>
  </div>
</section>

<section class="section section--forest">
  <div class="container text-center">
    <h2 style="max-width:20ch;margin:0 auto 16px;">Mari bincangkan projek elektrik atau tenaga boleh diperbaharui anda yang seterusnya</h2>
    <p style="margin:0 auto 30px;color:#DFF6E7;">Hubungi pasukan kami di ibu pejabat Port Klang, atau di pejabat cawangan kami di Sabah dan Sarawak.</p>
    <a href="contact.html" class="btn btn-primary">Hubungi Kami</a>
  </div>
</section>
"""

page(
    "index.html",
    "KLS — Kejuruteraan Elektrik & Interkoneksi Tenaga Boleh Diperbaharui | Kejuruteraan Letrik Seri",
    "Kejuruteraan Letrik Seri (M) Sdn Bhd (KLS), diperbadankan pada 1984 — kontraktor kejuruteraan elektrik Kelas A, CIDB G7 dan pakar interkoneksi tenaga boleh diperbaharui di Malaysia.",
    BODY,
    lang="ms",
    alt_url="https://www.klseri.com.my/index.html",
)
