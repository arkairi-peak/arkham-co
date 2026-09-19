from build import page

BODY = """
<div class="page-curtain" data-page-curtain aria-hidden="true">
  <div class="page-curtain-blobs"></div>
  <div class="page-curtain-tiles">
    <span style="animation-delay:0.550s"></span>
    <span style="animation-delay:0.595s"></span>
    <span style="animation-delay:0.640s"></span>
    <span style="animation-delay:0.685s"></span>
    <span style="animation-delay:0.595s"></span>
    <span style="animation-delay:0.640s"></span>
    <span style="animation-delay:0.685s"></span>
    <span style="animation-delay:0.730s"></span>
    <span style="animation-delay:0.640s"></span>
    <span style="animation-delay:0.685s"></span>
    <span style="animation-delay:0.730s"></span>
    <span style="animation-delay:0.775s"></span>
    <span style="animation-delay:0.685s"></span>
    <span style="animation-delay:0.730s"></span>
    <span style="animation-delay:0.775s"></span>
    <span style="animation-delay:0.820s"></span>
  </div>
  <div class="page-curtain-mark"><img src="../assets/img/logo/kls-icon.png" alt=""></div>
</div>
<script>try{if(sessionStorage.getItem('klsCurtainSeen')==='1'||window.matchMedia('(prefers-reduced-motion: reduce)').matches){document.currentScript.previousElementSibling.style.display='none';}else{sessionStorage.setItem('klsCurtainSeen','1');}}catch(e){}</script>
<section class="hero">
  <div class="hero-slides">
    <div class="hero-slide is-active" data-hero-title="Tenaga Yang Menggerakkan Perniagaan Anda" data-hero-lead="Kejuruteraan Letrik Seri (M) Sdn Bhd, atau ringkasnya KLS, diperbadankan pada tahun 1984 sebagai penyedia perkhidmatan pendawaian semula utama. Apabila perniagaan berkembang, skop perkhidmatan turut berkembang: kini kami membekal, memasang, menguji, mentauliah dan memberi waranti sistem elektrik Voltan Tinggi, Voltan Rendah dan Voltan Sangat Rendah merentasi projek kediaman, komersial, industri, infrastruktur dan marin.">
      <img src="https://www.klseri.com.my/wp-content/uploads/2021/03/sustainable_growth_istock.jpg" alt="Kejuruteraan elektrik KLS, menggerakkan perniagaan anda">
    </div>
    <div class="hero-slide" data-hero-title="Menyokong Tenaga Bersih dan Mampan" data-hero-lead="Sebagai salah sebuah nama industri yang mantap di Malaysia, kami memberikan sokongan sebenar kepada pembangunan mampan, melaksanakan kontrak dan inisiatif Interkoneksi Tenaga Boleh Diperbaharui merangkumi loji Biogas, Biojisim, Suria dan Kogenerasi.">
      <img src="https://www.klseri.com.my/wp-content/uploads/2021/03/light-bulb-placed-on-soil-in-sun-light.jpg" alt="Tenaga bersih, mentol lampu di atas tanah di bawah cahaya matahari">
    </div>
    <div class="hero-slide" data-hero-title="Kuasa Melalui Biojisim" data-hero-lead="Daripada kejuruteraan dan bekalan sehingga pemasangan dan pentauliahan kabel serta peralatan elektrik, KLS membina penyelesaian interkoneksi khusus untuk loji kuasa biojisim, termasuk projek 10MW untuk Cepat Wawasan Sdn. Bhd.">
      <img src="https://www.klseri.com.my/wp-content/uploads/2021/05/2021-05-10-015217938.jpg" alt="Kerja interkoneksi tenaga boleh diperbaharui KLS">
    </div>
  </div>
  <div class="container hero-inner">
    <div>
      <div class="hero-eyebrow reveal" style="animation-delay:.55s">Kejuruteraan Elektrik &amp; Tenaga Boleh Diperbaharui, Sejak 1984</div>
      <h1 class="reveal" style="animation-delay:.68s" data-hero-title-el>Tenaga Yang Menggerakkan Perniagaan Anda</h1>
      <p class="lead reveal" style="animation-delay:.8s" data-hero-lead-el>Kejuruteraan Letrik Seri (M) Sdn Bhd, atau ringkasnya KLS, diperbadankan pada tahun 1984 sebagai penyedia perkhidmatan pendawaian semula utama. Apabila perniagaan berkembang, skop perkhidmatan turut berkembang: kini kami membekal, memasang, menguji, mentauliah dan memberi waranti sistem elektrik Voltan Tinggi, Voltan Rendah dan Voltan Sangat Rendah merentasi projek kediaman, komersial, industri, infrastruktur dan marin.</p>
      <div class="hero-actions reveal" style="animation-delay:.95s">
        <a href="company-overview.html" class="btn btn-primary">Lihat Kisah Penuh Syarikat</a>
        <a href="services.html#renewable-energy" class="btn btn-outline">Kerja Tenaga Boleh Diperbaharui Kami</a>
      </div>
    </div>
    <div class="hero-stats reveal" style="animation-delay:1.05s">
      <div class="hero-stat"><b data-count-to="1984" data-count-suffix="">0</b><span>Tahun diperbadankan</span></div>
      <div class="hero-stat"><b data-count-to="4" data-count-suffix="">0</b><span>Bidang fokus tenaga boleh diperbaharui: Biogas, Biojisim, Suria, Kogenerasi</span></div>
      <div class="hero-stat"><b>Kelas A</b><span>Kontraktor M&amp;E CIDB G7</span></div>
      <div class="hero-stat"><b>3</b><span>Pejabat di Port Klang &middot; Lahad Datu &middot; Bintulu</span></div>
    </div>
  </div>
  <button class="hero-scroll-cue" data-scroll-cue aria-label="Tatal untuk terokai">
    <span class="hero-scroll-cue-track"><span></span></span>
    <em>Tatal</em>
  </button>
  <div class="hero-dots">
    <button data-hero-dot class="is-active" aria-label="Slaid 1: Tenaga Yang Menggerakkan Perniagaan Anda"></button>
    <button data-hero-dot aria-label="Slaid 2: Menyokong Tenaga Bersih dan Mampan"></button>
    <button data-hero-dot aria-label="Slaid 3: Kuasa Melalui Biojisim"></button>
  </div>
</section>

<section class="section">
  <div class="container grid grid-2" style="align-items:center;gap:56px;">
    <div>
      <div class="kicker">Tentang KLS</div>
      <h2>Daripada pakar pendawaian semula kepada kontraktor elektrik &amp; tenaga boleh diperbaharui bersepadu</h2>
      <p class="lead">KLS telah berkembang menjadi salah sebuah nama industri yang mantap di Malaysia, mengambil serius pembangunan mampan sehingga menyokongnya dengan projek sebenar: kontrak Interkoneksi Tenaga Boleh Diperbaharui merangkumi loji Biogas, Biojisim, Suria dan Kogenerasi.</p>
      <a href="company-overview.html" class="btn-ghost">Lihat Kisah Penuh Syarikat</a>
    </div>
    <div class="grid" style="gap:16px;">
      <img src="https://www.klseri.com.my/wp-content/uploads/2021/03/sustainable_growth_istock.jpg" alt="Pertumbuhan mampan, KLS menerajui tenaga boleh diperbaharui dan pembangunan mampan" style="border-radius:10px;border:1px solid var(--line-300);">
      <img src="https://www.klseri.com.my/wp-content/uploads/2021/03/light-bulb-placed-on-soil-in-sun-light.jpg" alt="Mentol lampu di atas tanah di bawah cahaya matahari, tenaga bersih di KLS" style="border-radius:10px;border:1px solid var(--line-300);">
    </div>
  </div>
</section>

<section class="section section--band">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Apa Yang Kami Lakukan</div>
      <h2>Perkhidmatan Kami</h2>
      <p class="lead">Berbekalkan pengalaman industri bertahun-tahun, kami menyampaikan perkhidmatan, produk dan kerja yang diperlukan pelanggan untuk mencapai matlamat perniagaan mereka, merangkumi bekalan, pemasangan, pengujian dan pentauliahan untuk:</p>
    </div>
    <div class="spec-list">
      <div class="spec-row">
        <span class="num mono">01</span>
        <div>
          <h4>Sistem Pengagihan Kuasa Elektrik</h4>
          <p style="margin-top:8px;">Sistem kuasa Voltan Sederhana/Tinggi dan Voltan Rendah, papan AMF, MCC, transformer, kabel kuasa, sistem penjana diesel, serta sistem ELV/ICT yang menghubungkan kesemuanya.</p>
          <a href="services.html#electrical-power-distribution" class="btn-ghost">Ketahui Lebih Lanjut</a>
        </div>
      </div>
      <div class="spec-row">
        <span class="num mono">02</span>
        <div>
          <h4>Tenaga Boleh Diperbaharui</h4>
          <p style="margin-top:8px;">Kemudahan interkoneksi yang menyalurkan kuasa Biogas, Biojisim dan Suria dengan cekap ke grid nasional, dengan gangguan yang seminimum mungkin.</p>
          <a href="services.html#renewable-energy" class="btn-ghost">Ketahui Lebih Lanjut</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--forest">
  <div class="container">
    <div class="section-head" style="margin-bottom:0;">
      <div class="kicker">1984-Kini</div>
      <h2 style="max-width:18ch;">Empat dekad dalam kejuruteraan Malaysia</h2>
      <p style="max-width:60ch;">Kami bermula sebagai bengkel pendawaian motor elektrik yang kecil dan berkembang menjadi Kontraktor M&amp;E Kelas A, CIDB G7 yang mantap, beroperasi di seluruh Malaysia dan luar negara.</p>
      <a href="company-overview.html#our-story" class="btn btn-outline" style="margin:6px 0 40px;display:inline-block;">Kisah &amp; Garis Masa Kami</a>
    </div>
  </div>
  <div class="marquee" data-marquee data-marquee-speed="26">
    <div class="marquee-track">
      <div class="milestone-chip"><b>1984</b><span>Diperbadankan di Malaysia sebagai penyedia perkhidmatan pendawaian semula utama</span></div>
      <div class="milestone-chip"><b>1984-2000-an</b><span>Menjadi Kontraktor M&amp;E Kelas A, CIDB G7 yang mantap</span></div>
      <div class="milestone-chip"><b>2000</b><span>Membuka pejabat cawangan di Lahad Datu, Sabah</span></div>
      <div class="milestone-chip"><b>Ke Luar Negara</b><span>Mengambil projek antarabangsa di Indonesia, Papua New Guinea &amp; Afrika</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center" style="margin:0 auto 40px;">
      <div class="kicker" style="justify-content:center;">Projek Utama</div>
      <h2>Disokong oleh nama industri &amp; tenaga utama Malaysia</h2>
    </div>
  </div>
  <div class="marquee" data-marquee data-marquee-speed="28">
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
  <div class="container" style="text-align:center;margin-top:36px;">
    <a href="projects.html" class="btn btn-outline">Lihat Senarai Rujukan Projek Penuh</a>
  </div>
</section>

<section class="section section--band">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Warga Kerja Kami</div>
      <h2>Individu yang menerajui KLS</h2>
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
      <p class="lead" style="margin:0 auto;">Kontraktor M&amp;E Kelas A, CIDB G7, memegang pensijilan merentasi setiap bidang elektrik dan pembinaan yang kami ceburi.</p>
    </div>
    <div style="text-align:center;"><a href="certifications.html" class="btn btn-primary">Lihat Semua Pensijilan &amp; Lesen</a></div>
  </div>
</section>

<section class="section section--band">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Pelanggan Utama</div>
      <h2>Organisasi yang bekerjasama dengan kami</h2>
    </div>
    <div data-key-clients></div>
  </div>
</section>

<section class="section section--forest">
  <div class="container text-center">
    <h2 style="max-width:20ch;margin:0 auto 16px;">Ada projek elektrik atau tenaga boleh diperbaharui? Mari berbincang</h2>
    <p style="margin:0 auto 30px;color:#DFF6E7;">Hubungi pasukan kami di ibu pejabat Port Klang, atau di salah satu pejabat cawangan kami di Sabah dan Sarawak.</p>
    <a href="contact.html" class="btn btn-primary">Hubungi Kami</a>
  </div>
</section>
"""

page(
    "index.html",
    "KLS | Kejuruteraan Elektrik & Interkoneksi Tenaga Boleh Diperbaharui, Kejuruteraan Letrik Seri",
    "Kejuruteraan Letrik Seri (M) Sdn Bhd (KLS) telah beroperasi sebagai kontraktor kejuruteraan elektrik Kelas A, CIDB G7 dan pakar interkoneksi tenaga boleh diperbaharui di Malaysia sejak 1984.",
    BODY,
    lang="ms",
    alt_url="https://www.klseri.com.my/index.html",
)
