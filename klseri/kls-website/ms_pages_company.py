from build import page, breadcrumb

BODY = f"""
<section class="page-hero">
  <div class="container">
    <h1>Ikhtisar Syarikat</h1>
    <p class="lead">Satu syarikat, satu set fakta, satu identiti, dan hampir empat puluh tahun kerja kejuruteraan elektrik dan interkoneksi tenaga boleh diperbaharui secara langsung di seluruh Malaysia dan luar negara.</p>
  </div>
</section>
{breadcrumb('company-overview.html','Ikhtisar Syarikat', lang='ms')}

<section class="section" id="we-are-kls">
  <div class="container grid grid-2" style="gap:56px;align-items:center;">
    <div>
      <div class="kicker">Kami Adalah KLS</div>
      <h2>Kejuruteraan Letrik Seri (M) Sdn Bhd</h2>
      <p class="lead">Kejuruteraan Letrik Seri (M) Sdn Bhd, atau ringkasnya KLS, diperbadankan pada tahun 1984 dan bermula sebagai penyedia perkhidmatan pendawaian semula utama. Pertumbuhan membawa skop yang lebih luas: kini kami membekal, memasang, menguji, mentauliah dan memberi waranti sistem elektrik Voltan Tinggi, Voltan Rendah dan Voltan Sangat Rendah merentasi pembangunan kediaman, komersial, industri, infrastruktur dan marin.</p>
      <p>Sebagai salah sebuah nama industri yang mantap di Malaysia, kami mengambil serius sumber semula jadi negara dan keperluan pembangunan mampan, dan menyokongnya dengan kerja sebenar: satu senarai panjang kontrak Interkoneksi Tenaga Boleh Diperbaharui merangkumi loji Biogas, Biojisim, Suria dan Kogenerasi.</p>
    </div>
    <img src="https://www.klseri.com.my/wp-content/uploads/2021/05/2021-05-10-015217938.jpg" alt="Kerja kejuruteraan elektrik KLS" style="border-radius:10px;border:1px solid var(--line-300);">
  </div>
  <div class="container" style="margin-top:44px;">
    <div class="stat-band">
      <div class="stat-item"><b>1984</b><span>Tahun diperbadankan</span></div>
      <div class="stat-item"><b>Kelas A</b><span>Kontraktor M&amp;E CIDB G7</span></div>
      <div class="stat-item"><b>HV &middot; LV &middot; ELV</b><span>Sistem elektrik dibekal, dipasang &amp; ditauliah</span></div>
      <div class="stat-item"><b>5</b><span>Sektor pembangunan diservis</span></div>
    </div>
  </div>
</section>

<section class="section section--band" id="our-story">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Bagaimana Kami Sampai Ke Sini</div>
      <h2>Daripada operasi pendawaian kecil kepada kontraktor M&amp;E serantau</h2>
      <p class="lead">Satu perkara kekal sama sejak 1984: melakukan kerja dengan betul dan memastikan pelanggan berpuas hati. Tiga dekad kemudian, pendekatan itu membawa kami ke kedudukan terkemuka dalam industri kejuruteraan elektrik Malaysia, dengan senarai panjang projek berprofil tinggi sebagai bukti.</p>
    </div>
    <div class="timeline">
      <div class="t-item">
        <div class="t-year">1984</div>
        <h4>Diperbadankan di Malaysia</h4>
        <p>KLS bermula sebagai penyedia perkhidmatan pendawaian semula utama, berkembang daripada sebuah bengkel pendawaian motor elektrik yang kecil.</p>
      </div>
      <div class="t-item">
        <div class="t-year">1984-2000-an</div>
        <h4>Pertumbuhan dan pengkhususan</h4>
        <p>Sepanjang tiga dekad, syarikat berkembang menjadi Kontraktor M&amp;E Kelas A, CIDB G7 yang mantap, memperoleh pengalaman mendalam dan pengkhususan teknikal, disertai pengiktirafan berterusan daripada pelanggan yang dikhidmati.</p>
      </div>
      <div class="t-item">
        <div class="t-year">2000</div>
        <h4>Melangkah ke Malaysia Timur</h4>
        <p>KLS memperluas jangkauannya ke Malaysia Timur, membuka pejabat cawangan di Lahad Datu, Sabah.</p>
      </div>
      <div class="t-item">
        <div class="t-year">Luar Malaysia</div>
        <h4>Melihat ke luar</h4>
        <p>KLS melangkaui asas projek tempatan berprofil tinggi dan mengambil kerja antarabangsa, memperoleh kontrak di negara termasuk Indonesia, Papua New Guinea dan Afrika.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="philosophy">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Cara Kami Bekerja</div>
      <h2>Apa yang menerajui kerja seharian kami</h2>
    </div>
    <div class="grid grid-2" style="gap:24px;">
      <div class="card card-pad" style="background:var(--brand-800);color:#fff;border:0;">
        <img src="https://www.klseri.com.my/wp-content/uploads/2021/02/Icon-02.png" alt="" style="width:44px;filter:invert(1);margin-bottom:16px;">
        <h3 style="color:#fff;">Perniagaan Melangkaui Profesionalisme</h3>
        <p style="color:#DFF6E7;">Kami menyampaikan setiap penyelesaian elektrik dan kejuruteraan dengan pelaksanaan yang teliti dan rasa tanggungjawab sebenar terhadap hasilnya. Setiap projek dibina untuk bertahan lama dan terus memberi manfaat kepada perniagaan pelanggan selepas penyerahan. Kami sentiasa berusaha melangkaui jangkaan, disokong oleh komitmen sebenar terhadap kecemerlangan, akauntabiliti dan profesionalisme.</p>
      </div>
      <div class="card card-pad">
        <img src="https://www.klseri.com.my/wp-content/uploads/2021/02/Icon-01.png" alt="" style="width:44px;margin-bottom:16px;">
        <h3>Rakan Dipercayai Anda untuk Kualiti</h3>
        <p>Kepakaran teknikal dan pemahaman kami terhadap industri inilah yang menjadikan kami rakan dipercayai bagi syarikat yang mengutamakan kualiti di seluruh negara. Kami memastikan kerja kami sendiri memenuhi standard tertinggi yang boleh dicapai, dan hubungan yang kami bina dengan pelanggan sepanjang tahun mencerminkan itu, hasil langsung daripada kerja berkualiti yang konsisten dan reputasi yang diperoleh, bukan sekadar didakwa.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--band" id="mission-vision">
  <div class="container grid grid-2" style="gap:32px;">
    <div class="card card-pad">
      <div class="kicker">Misi</div>
      <h3>Misi Kami</h3>
      <ul class="svc-list" style="margin-top:16px;">
        <li>Menyampaikan penyelesaian dan perkhidmatan yang memenuhi standard antarabangsa.</li>
        <li>Menguruskan projek dengan baik, dengan tenaga kerja yang kami yakini.</li>
        <li>Melangkaui jangkaan pelanggan melalui kepakaran dan prestasi sebenar.</li>
        <li>Mengekalkan perkhidmatan kejuruteraan elektrik yang cekap kos tanpa menjejaskan kualiti.</li>
      </ul>
    </div>
    <div class="card card-pad" style="background:var(--brand-800);color:#fff;border:0;">
      <div class="kicker" style="background:rgba(255,255,255,.16);border-color:rgba(255,255,255,.3);color:#fff;">Wawasan</div>
      <h3 style="color:#fff;">Wawasan Kami</h3>
      <p style="color:#E9FBEF;font-size:1.08rem;margin-top:16px;">Menjadi penyedia penyelesaian kejuruteraan pilihan utama Asia Tenggara (SEA), dengan memberikan pelanggan penyelesaian terbaik dalam kelasnya untuk mereka berjaya.</p>
    </div>
  </div>
</section>

<section class="section" id="core-values">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Nilai Teras Kami</div>
      <h2>Apa yang membentuk warga kerja dan perniagaan kami</h2>
      <p class="lead">Sebagai syarikat yang menjaga reputasinya, kami berpegang kepada satu set nilai teras yang membentuk warga kerja dan cara kami menguruskan perniagaan. Nilai inilah yang membolehkan kami membina hubungan yang berkekalan dan bernilai dengan pelanggan, sambil membantu mereka mencapai matlamat masing-masing.</p>
    </div>
    <div class="spec-list">
      <div class="value-row"><span class="idx mono">01</span><div><h4>Kualiti Cemerlang</h4><p>Standard kami tidak berganjak. Kualiti kekal menjadi teras kepada cara kami bekerja, menguruskan projek, dan menjalankan syarikat secara keseluruhan.</p></div></div>
      <div class="value-row"><span class="idx mono">02</span><div><h4>Inovasi</h4><p>Kami terus belajar dan terus bergerak maju, kekal relevan dengan teknologi terkini dan tuntutan industri yang sentiasa berubah.</p></div></div>
      <div class="value-row"><span class="idx mono">03</span><div><h4>Kerja Berpasukan</h4><p>Kami melabur dalam hubungan antara warga kerja kami. Budaya kami berteraskan rasa hormat bersama dan kerjasama antara pihak pengurusan dan pasukan teknikal di lapangan.</p></div></div>
      <div class="value-row"><span class="idx mono">04</span><div><h4>Keupayaan Beradaptasi</h4><p>Perubahan adalah sebahagian daripada perniagaan, dan kami mengiktirafnya begitu, kekal tabah menghadapi keadaan kewangan dan ekonomi yang berubah, bukan terjejas olehnya.</p></div></div>
      <div class="value-row"><span class="idx mono">05</span><div><h4>Profesionalisme</h4><p>Kami konsisten dan boleh diharap. Daripada persediaan dan perancangan sehingga reka bentuk, pelaksanaan, pengujian dan penyerahan akhir, pasukan kami mengekalkan standard yang melangkaui jangkaan.</p></div></div>
      <div class="value-row"><span class="idx mono">06</span><div><h4>Kepuasan Pelanggan</h4><p>Komitmen kami tidak berakhir selepas penyerahan. Setiap projek disokong dengan jaminan berterusan dan sokongan selepas penyerahan, termasuk penyelenggaraan, dengan matlamat kepuasan penuh pelanggan.</p></div></div>
    </div>
  </div>
</section>

<section class="section section--band" id="key-clients">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Pelanggan Utama</div>
      <h2>Organisasi yang bekerjasama dengan kami</h2>
    </div>
    <div data-key-clients></div>
  </div>
</section>

<section class="section" id="partners-suppliers">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Rakan Kongsi &amp; Pembekal</div>
      <h2>Rakan kongsi &amp; pembekal kami</h2>
    </div>
    <div data-partners></div>
  </div>
</section>

<section class="section section--band" id="advisors-consultants">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Penasihat &amp; Perunding</div>
      <h2>Penasihat &amp; perunding kami</h2>
    </div>
    <div data-advisors></div>
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
    "company-overview.html",
    "Ikhtisar Syarikat | KLS, Kejuruteraan Letrik Seri (M) Sdn Bhd",
    "KLS telah menyokong pembangunan mampan dengan kontrak Interkoneksi Tenaga Boleh Diperbaharui sebenar, seiring dengan kerja kuasa elektrik terasnya, sejak 1984.",
    BODY,
    lang="ms",
    alt_url="https://www.klseri.com.my/company-overview.html",
)
