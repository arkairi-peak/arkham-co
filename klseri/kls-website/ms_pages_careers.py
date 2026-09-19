from build import page, breadcrumb

BODY = f"""
<section class="page-hero" style="--panel-img:url('https://www.klseri.com.my/wp-content/uploads/2021/04/KLS-01.png')">
  <div class="container">
    <h1>Kerjaya di KLS</h1>
    <p class="lead">Sertai pasukan pakar yang menerajui kejuruteraan elektrik dan interkoneksi tenaga boleh diperbaharui.</p>
  </div>
</section>
{breadcrumb('careers.html','Kerjaya', lang='ms')}

<section class="section">
  <div class="container grid grid-2" style="gap:48px;align-items:center;">
    <div>
      <div class="kicker">Sertai Kami</div>
      <h2>Kerjaya di KLS</h2>
      <p class="lead">Terdapat peluang sebenar untuk bekerja bersama individu berpengalaman dalam industri ini. Di KLS, itu bermakna sentiasa bersemangat untuk belajar, berinovasi, dan bekerjasama rapat dengan pasukan, rakan kongsi, penasihat dan pelanggan kami. Kami mengejar kecemerlangan dan terus berinovasi supaya kekal mendahului dari segi teknologi mahupun persaingan.</p>
      <p>Kami mencari individu yang berdedikasi dan berbakat pada setiap peringkat kerjaya, dan menyokongnya dengan peluang sebenar. Berminat menyertai kami? Hantarkan resume anda.</p>
      <a href="mailto:info@klseri.com.my?subject=Pertanyaan%20Kerjaya%20-%20KLS" class="btn btn-primary">E-mel resume anda</a>
    </div>
    <div class="card card-pad">
      <h4>Jawatan kosong semasa</h4>
      <p class="small" style="margin-top:10px;">Tiada kekosongan khusus disenaraikan di laman ini buat masa ini, tetapi calon berbakat pada mana-mana peringkat kerjaya tetap dialu-alukan untuk menghubungi kami. Resume disemak secara berterusan.</p>
      <hr class="rule" style="margin:22px 0;">
      <h4>Cara memohon</h4>
      <p class="small" style="margin-top:10px;">Hantar resume anda ke <a href="mailto:info@klseri.com.my" style="color:var(--brand-700);font-weight:600;">info@klseri.com.my</a>, atau hubungi ibu pejabat kami di Port Klang, Selangor melalui borang hubungan.</p>
      <a href="contact.html" class="btn-ghost" style="margin-top:6px;">Pergi ke Laman Hubungi</a>
    </div>
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
    "careers.html",
    "Kerjaya | Sertai Pasukan KLS",
    "KLS menawarkan peluang kerjaya bersama pasukan yang inovatif, bekerja dengan teknologi kejuruteraan elektrik dan tenaga boleh diperbaharui terkini.",
    BODY,
    lang="ms",
    alt_url="https://www.klseri.com.my/careers.html",
)
