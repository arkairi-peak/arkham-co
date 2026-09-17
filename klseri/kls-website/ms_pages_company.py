from build import page, breadcrumb

BODY = f"""
<section class="page-hero">
  <div class="container">
    <h1>Ikhtisar Syarikat</h1>
    <p class="lead">Syarikat yang sama, fakta yang sama, identiti yang sama — empat dekad kerja kejuruteraan elektrik dan interkoneksi tenaga boleh diperbaharui di Malaysia dan luar negara.</p>
  </div>
</section>
{breadcrumb('company-overview.html','Ikhtisar Syarikat', lang='ms')}

<section class="section" id="we-are-kls">
  <div class="container grid grid-2" style="gap:56px;align-items:center;">
    <div>
      <div class="kicker">Kami Adalah KLS</div>
      <h2>Kejuruteraan Letrik Seri (M) Sdn Bhd</h2>
      <p class="lead">Kejuruteraan Letrik Seri (M) Sdn Bhd, atau dikenali sebagai KLS, telah diperbadankan pada tahun 1984, bermula sebagai penyedia perkhidmatan pendawaian semula (rewiring) utama. Seiring perkembangan syarikat, kami mempelbagaikan perkhidmatan kepada bekalan, pemasangan, pengujian, pentauliahan dan waranti sistem elektrik Voltan Tinggi, Voltan Rendah dan Voltan Sangat Rendah untuk pembangunan kediaman, komersial, industri, infrastruktur dan marin.</p>
      <p>Sebagai salah sebuah peneraju industri di Malaysia, kami menghargai sumber semula jadi dan mengiktiraf keperluan pembangunan mampan. Kami menzahirkan komitmen ini dengan melaksanakan pelbagai kontrak dan inisiatif Interkoneksi Tenaga Boleh Diperbaharui merangkumi Loji Biogas, Biojisim, Suria dan Kogenerasi.</p>
    </div>
    <img src="https://www.klseri.com.my/wp-content/uploads/2021/05/2021-05-10-015217938.jpg" alt="Kerja kejuruteraan elektrik KLS" style="border-radius:10px;border:1px solid var(--line-300);">
  </div>
</section>

<section class="section section--band" id="our-story">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Kisah Kami</div>
      <h2>Daripada bengkel pendawaian semula kepada kontraktor M&amp;E serantau</h2>
      <p class="lead">Sejak permulaan kami yang sederhana pada tahun 1984, kami sentiasa berusaha menyampaikan kerja berkualiti dengan penekanan kepada kepuasan pelanggan. Dengan pengalaman lebih 30 tahun, kami telah menjadi salah sebuah syarikat peneraju dalam industri kejuruteraan elektrik dengan pelbagai projek berprofil tinggi di seluruh Malaysia.</p>
    </div>
    <div class="grid grid-2" style="gap:56px;">
      <div class="timeline">
        <div class="t-item">
          <div class="t-year">1984</div>
          <h4>Diperbadankan di Malaysia</h4>
          <p>KLS bermula sebagai penyedia perkhidmatan pendawaian semula utama, berkembang daripada sebuah bengkel pendawaian motor elektrik yang kecil.</p>
        </div>
        <div class="t-item">
          <div class="t-year">1984 — 2000-an</div>
          <h4>Pempelbagaian &amp; pengkhususan</h4>
          <p>Syarikat berkembang menjadi Kontraktor M&amp;E Kelas A, CIDB G7 yang mantap, memperoleh pengalaman luas dan kepakaran profesional yang mendapat pengiktirafan daripada pelanggan sepanjang tiga dekad.</p>
        </div>
        <div class="t-item">
          <div class="t-year">2000</div>
          <h4>Pengembangan ke Malaysia Timur</h4>
          <p>KLS memperluas rangkaiannya dengan melangkah ke Malaysia Timur dan membuka pejabat cawangan di Lahad Datu, Sabah.</p>
        </div>
        <div class="t-item">
          <div class="t-year">Luar Malaysia</div>
          <h4>Melangkah ke peringkat global</h4>
          <p>Menyahut seruan globalisasi, KLS memperluas fokus melangkaui projek tempatan berprofil tinggi dan melangkah ke persada antarabangsa, memperoleh kerja di negara seperti Indonesia, Papua New Guinea dan Afrika.</p>
        </div>
      </div>
      <div>
        <div class="card card-pad" style="background:var(--brand-800);color:#fff;border:0;">
          <img src="https://www.klseri.com.my/wp-content/uploads/2021/02/Icon-02.png" alt="" style="width:44px;filter:invert(1);margin-bottom:16px;">
          <h3 style="color:#fff;">Perniagaan Melangkaui Profesionalisme</h3>
          <p style="color:#DFF6E7;">Di KLS, kami menyampaikan penyelesaian elektrik dan kejuruteraan dengan pelaksanaan dan tanggungjawab yang cemerlang. Bagi setiap projek yang diusahakan, kami menyediakan penyelesaian yang tahan lasak serta membawa hasil perniagaan yang berjaya kepada pelanggan. Kami berhasrat untuk melangkaui jangkaan pelanggan dan menonjolkan komitmen kami terhadap kecemerlangan, akauntabiliti dan profesionalisme.</p>
        </div>
        <div class="card card-pad" style="margin-top:24px;">
          <img src="https://www.klseri.com.my/wp-content/uploads/2021/02/Icon-01.png" alt="" style="width:44px;margin-bottom:16px;">
          <h3>Rakan Dipercayai Anda untuk Kualiti</h3>
          <p>Di KLS, kepakaran teknikal dan kefahaman kami terhadap industri inilah yang menjadikan kami rakan dipercayai bagi syarikat yang mengutamakan kualiti di negara ini. Selaras dengan prinsip kami, kami berusaha menyediakan penyelesaian kejuruteraan elektrik bertaraf kualiti tertinggi kepada pelanggan kami. Hubungan erat kami dengan pelanggan adalah bukti kepada kerja berkualiti dan reputasi kukuh kami.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="mission-vision">
  <div class="container grid grid-2" style="gap:32px;">
    <div class="card card-pad">
      <div class="kicker">Misi</div>
      <h3>Misi Kami</h3>
      <ul class="svc-list" style="margin-top:16px;">
        <li>Menyampaikan penyelesaian dan perkhidmatan yang memenuhi standard antarabangsa.</li>
        <li>Menyediakan pengurusan projek yang cemerlang dan tenaga kerja yang berkualiti.</li>
        <li>Melangkaui jangkaan pelanggan dengan kepakaran dan prestasi yang luar biasa.</li>
        <li>Menyampaikan perkhidmatan kejuruteraan elektrik yang cekap kos dan berkualiti.</li>
      </ul>
    </div>
    <div class="card card-pad" style="background:var(--brand-800);color:#fff;border:0;">
      <div class="kicker" style="color:var(--amber-500);">Wawasan</div>
      <h3 style="color:#fff;">Wawasan Kami</h3>
      <p style="color:#E9FBEF;font-size:1.08rem;margin-top:16px;">Menjadi penyedia penyelesaian kejuruteraan pilihan di Asia Tenggara (SEA) dengan menyampaikan penyelesaian terbaik dalam kelasnya kepada pelanggan kami untuk mereka berjaya.</p>
    </div>
  </div>
</section>

<section class="section section--band" id="core-values">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Nilai Teras Kami</div>
      <h2>Apa yang menerajui warga kerja dan perniagaan kami</h2>
      <p class="lead">Sebagai syarikat terkemuka dalam industri, kami berpegang teguh kepada nilai teras kami kerana ia menerajui warga kerja dan operasi perniagaan kami. Prinsip ini membolehkan kami membina hubungan yang berkekalan dan bernilai dengan pelanggan sambil menyampaikan penyelesaian dan perkhidmatan cemerlang bagi membantu mencapai matlamat perniagaan mereka.</p>
    </div>
    <div class="spec-list">
      <div class="value-row"><span class="idx mono">01</span><div><h4>Kualiti Cemerlang</h4><p>Standard kami tidak berganjak. Kami memastikan kualiti menjadi teras kepada kerja, pengurusan dan keseluruhan syarikat kami.</p></div></div>
      <div class="value-row"><span class="idx mono">02</span><div><h4>Inovasi</h4><p>Kami berusaha untuk terus berinovasi dan memperkasakan diri bagi mengikuti teknologi terkini dan landskap industri yang sentiasa berubah.</p></div></div>
      <div class="value-row"><span class="idx mono">03</span><div><h4>Kerja Berpasukan</h4><p>Kami membina dan memupuk hubungan antara warga kerja kami. Budaya kami berteraskan rasa hormat bersama dan keharmonian antara pihak pengurusan dan jabatan teknikal.</p></div></div>
      <div class="value-row"><span class="idx mono">04</span><div><h4>Keupayaan Beradaptasi</h4><p>Kami beradaptasi dan menerima perubahan sebagai sebahagian daripada perniagaan — tabah dan tekun menghadapi keadaan kewangan dan ekonomi dunia yang sentiasa berubah.</p></div></div>
      <div class="value-row"><span class="idx mono">05</span><div><h4>Profesionalisme</h4><p>Kami konsisten dan boleh dipercayai. Pasukan kami menyampaikan infrastruktur dan perkhidmatan berkualiti yang melangkaui jangkaan dalam persediaan, perancangan, reka bentuk, pelaksanaan, pengujian dan penyerahan.</p></div></div>
      <div class="value-row"><span class="idx mono">06</span><div><h4>Kepuasan Pelanggan</h4><p>Kami menyediakan jaminan berterusan dan perkhidmatan selepas penyerahan yang cemerlang seperti penyelenggaraan bagi semua projek kami, dengan matlamat kepuasan pelanggan 100%.</p></div></div>
    </div>
  </div>
</section>

<section class="section" id="key-clients">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Pelanggan Utama</div>
      <h2>Organisasi yang kami berurusan</h2>
    </div>
    <div class="logo-strip" data-key-clients></div>
  </div>
</section>

<section class="section section--band" id="partners-suppliers">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Rakan Kongsi &amp; Pembekal</div>
      <h2>Rakan kongsi &amp; pembekal kami</h2>
    </div>
    <div class="logo-strip" data-partners></div>
  </div>
</section>

<section class="section" id="advisors-consultants">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Penasihat &amp; Perunding</div>
      <h2>Penasihat &amp; perunding kami</h2>
    </div>
    <div class="logo-strip" data-advisors></div>
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
    "Ikhtisar Syarikat | KLS — Kejuruteraan Letrik Seri (M) Sdn Bhd",
    "KLS menerajui pembangunan mampan dan melaksanakan kontrak Interkoneksi Tenaga Boleh Diperbaharui, serta tawaran kuasa elektrik, sejak 1984.",
    BODY,
    lang="ms",
    alt_url="https://www.klseri.com.my/company-overview.html",
)
