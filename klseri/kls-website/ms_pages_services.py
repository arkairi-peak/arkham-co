from build import page, breadcrumb

BODY = f"""
<section class="page-hero">
  <div class="container">
    <h1>Perkhidmatan Kami</h1>
    <p class="lead">Dengan pengetahuan dan pengalaman industri kami, kami menyediakan perkhidmatan, produk dan kerja berkualiti kepada pelanggan kami bagi membantu mereka mencapai matlamat perniagaan. Perkhidmatan kami merangkumi bekalan, pemasangan, pengujian dan pentauliahan untuk:</p>
  </div>
</section>
{breadcrumb('services.html','Perkhidmatan Kami', lang='ms')}

<section class="section" id="electrical-power-distribution">
  <div class="container">
    <div class="section-head">
      <div class="kicker">01 &middot; Sistem Pengagihan Kuasa Elektrik</div>
      <h2>Sistem Pengagihan Kuasa Elektrik</h2>
    </div>
    <div class="spec-list">
      <div class="spec-row">
        <span class="num mono">A</span>
        <div>
          <h4>Sistem Kuasa Teras</h4>
          <ul class="svc-list">
            <li>Sistem Kuasa Voltan Sederhana/Tinggi</li>
            <li>Sistem Kuasa Voltan Rendah</li>
            <li>Papan AMF dan EMSB</li>
            <li>Pusat Kawalan Motor (MCC)</li>
            <li>Transformer kuasa</li>
            <li>Pendawaian kuasa LV</li>
            <li>Pendawaian kuasa MV</li>
            <li>Sistem sokongan kabel</li>
            <li>Sistem Penjana Diesel</li>
          </ul>
        </div>
      </div>
      <div class="spec-row">
        <span class="num mono">B</span>
        <div>
          <h4>Kawalan, Instrumentasi &amp; Pencahayaan</h4>
          <ul class="svc-list">
            <li>Sistem Kawalan dan Instrumentasi &amp; pendawaian (kabel kawalan, kabel instrumen)</li>
            <li>Pencahayaan dan titik kuasa kecil &amp; kelengkapan</li>
            <li>Sistem pencahayaan dan kuasa kalis letupan</li>
          </ul>
        </div>
      </div>
      <div class="spec-row">
        <span class="num mono">C</span>
        <div>
          <h4>Telekomunikasi &amp; ICT</h4>
          <ul class="svc-list">
            <li>Kerja telekomunikasi dalaman &amp; infrastruktur</li>
            <li>Penyelesaian ICT dan rangkaian data</li>
          </ul>
        </div>
      </div>
      <div class="spec-row">
        <span class="num mono">D</span>
        <div>
          <h4>Sistem Bangunan</h4>
          <ul class="svc-list">
            <li>Sistem HVAC / Pengudaraan</li>
            <li>Sistem Automasi Bangunan dan SCADA</li>
          </ul>
        </div>
      </div>
      <div class="spec-row">
        <span class="num mono">E</span>
        <div>
          <h4>Keselamatan &amp; AV</h4>
          <ul class="svc-list">
            <li>Sistem CCTV</li>
            <li>SMATV</li>
            <li>Sistem AV dan PA</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--forest" id="renewable-energy">
  <div class="container">
    <div class="section-head">
      <div class="kicker">02 &middot; Tenaga Boleh Diperbaharui</div>
      <h2 style="max-width:18ch;">Interkoneksi Tenaga Boleh Diperbaharui</h2>
      <p class="lead" style="color:#DFF6E7;">Dengan menggabungkan pengetahuan dan kepakaran kami dalam Kemudahan Interkoneksi Tenaga Boleh Diperbaharui (RE), kami membekal dan menyampaikan peralatan elektrik serta kabel yang berkualiti tinggi dan boleh dipercayai bagi memastikan kuasa janaan loji penting disalurkan dengan cekap ke grid dengan gangguan yang minimum.</p>
    </div>
  </div>
</section>

<section class="section" id="biogas">
  <div class="container">
    <div class="re-block">
      <div class="re-media">
        <div>
          <span class="tag">TENAGA BOLEH DIPERBAHARUI</span>
          <div class="headline">Biogas</div>
        </div>
        <div class="examples">
          <div>Biogas 1.5MW untuk Cenergi FJP Sdn. Bhd.</div>
          <div>Biogas 3.5MW untuk Mistral Engineering Sdn. Bhd.</div>
        </div>
      </div>
      <div class="re-body">
        <p>Didorong terutamanya oleh industri kelapa sawit, Malaysia berada di kedudukan unik untuk menyediakan sumber tenaga bersih bagi penjanaan kuasa dan haba. Biogas dihasilkan melalui pencernaan anaerobik efluen kilang kelapa sawit (POME), sisa dan hasil sampingan pengeluaran minyak sawit mentah. Penggunaan POME sebagai sumber tenaga biometana mengurangkan pencemaran udara dan jejak karbon kilang.</p>
        <p>Biogas ini boleh dimanfaatkan untuk menjana tenaga boleh diperbaharui yang boleh dieksport ke grid kuasa nasional untuk pengedaran ke seluruh negara. Di KLS, kami menyokong pelaksanaan loji biogas dengan kerja interkoneksi dan perkhidmatan menyeluruh yang membantu memanfaatkan gas metana sebagai sumber kuasa yang cekap tenaga. Kerja kami merangkumi bekalan dan pemasangan menyeluruh peralatan interkoneksi elektrik, kabel, serta sistem kawalan dan instrumentasi.</p>
        <a href="projects.html#reference-list" class="btn-ghost">Lihat projek biogas dalam senarai rujukan kami</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--band" id="biomass">
  <div class="container">
    <div class="re-block">
      <div class="re-media">
        <div>
          <span class="tag">TENAGA BOLEH DIPERBAHARUI</span>
          <div class="headline">Biojisim</div>
        </div>
        <div class="examples">
          <div>Biojisim 10MW untuk Cepat Wawasan Sdn. Bhd.</div>
        </div>
      </div>
      <div class="re-body">
        <p>Tenaga biojisim boleh digunakan dalam pelbagai cara. Loji biojisim umumnya menggunakan stim bertekanan tinggi yang dihasilkan daripada pembakaran bahan organik untuk memutarkan turbin penjana bagi menghasilkan elektrik.</p>
        <p>Industri termasuk pertanian, balak dan perindustrian mempunyai sumber dan sisa loji yang besar yang boleh ditukar kepada tenaga boleh diperbaharui, mengurangkan pergantungan kepada bahan api fosil untuk penjanaan kuasa dan haba. Negara-negara tropika di rantau Asia Tenggara boleh memanfaatkan iklim panas dan lembap sepanjang tahun serta sektor pertanian mereka.</p>
        <p>Sebagai pakar interkoneksi tenaga boleh diperbaharui, kami menjalankan kejuruteraan, bekalan, pemasangan dan pentauliahan kabel serta peralatan elektrik yang diperlukan untuk projek biojisim, menyampaikan penyelesaian khusus bagi memenuhi keperluan ketat pihak berkuasa utiliti tempatan dan loji penjana penting — meminimumkan gangguan untuk memaksimumkan output penjanaan.</p>
        <a href="projects.html#reference-list" class="btn-ghost">Lihat projek biojisim dalam senarai rujukan kami</a>
      </div>
    </div>
  </div>
</section>

<section class="section" id="solar">
  <div class="container">
    <div class="re-block">
      <div class="re-media">
        <div>
          <span class="tag">TENAGA BOLEH DIPERBAHARUI</span>
          <div class="headline">Suria</div>
        </div>
        <div class="examples">
          <div>Tenaga Suria 1MW untuk ERS Energy Sdn. Bhd.</div>
        </div>
      </div>
      <div class="re-body">
        <p>Tenaga suria adalah bentuk tenaga boleh diperbaharui yang paling popular di dunia kerana ia paling bersih, paling banyak dan mudah didapati secara semula jadi. Tenaga suria daripada matahari ditangkap dan disimpan oleh panel solar serta tidak mempunyai pelepasan dengan kesan yang minimum terhadap alam sekitar. Bagi memastikan Malaysia mencapai sasaran 20% Tenaga Boleh Diperbaharui dalam campuran penjanaannya menjelang 2025, tenaga suria amat penting bagi negara.</p>
        <p>Skop perkhidmatan kami untuk tenaga suria merangkumi bekalan, pemasangan dan penyelenggaraan kabel serta sistem elektrik bagi interkoneksi antara panel solar, loji kuasa solar dan kemudahan interkoneksi grid nasional. Sebagai pakar interkoneksi tenaga boleh diperbaharui, kami menyediakan penyelesaian yang kos efektif dan tahan lama bagi memenuhi keperluan elektrik dan kejuruteraan khusus setiap projek.</p>
      </div>
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
    "services.html",
    "Perkhidmatan Kami | Pengagihan Kuasa Elektrik & Tenaga Boleh Diperbaharui — KLS",
    "KLS menawarkan perkhidmatan yang merangkumi bekalan, pemasangan, pengujian dan pentauliahan sistem pengagihan kuasa elektrik, serta interkoneksi tenaga boleh diperbaharui Biogas, Biojisim dan Suria.",
    BODY,
    lang="ms",
    alt_url="https://www.klseri.com.my/services.html",
)
