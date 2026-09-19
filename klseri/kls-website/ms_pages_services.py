from build import page, breadcrumb

BODY = f"""
<section class="page-hero">
  <div class="container">
    <h1>Perkhidmatan Kami</h1>
    <p class="lead">Pengalaman industri bertahun-tahun menjadi asas kepada segala yang kami sampaikan, perkhidmatan, produk dan kerja yang membantu pelanggan mencapai matlamat perniagaan mereka. Ini merangkumi bekalan, pemasangan, pengujian dan pentauliahan untuk:</p>
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

<section class="section section--forest" id="renewable-energy" style="--panel-img:url('https://www.klseri.com.my/wp-content/uploads/2021/03/light-bulb-placed-on-soil-in-sun-light.jpg')">
  <div class="container">
    <div class="section-head">
      <div class="kicker">02 &middot; Tenaga Boleh Diperbaharui</div>
      <h2 style="max-width:18ch;">Interkoneksi Tenaga Boleh Diperbaharui</h2>
      <p class="lead" style="color:#DFF6E7;">Pengetahuan dan kepakaran kami dalam Kemudahan Interkoneksi Tenaga Boleh Diperbaharui (RE) membolehkan kami membekal dan menyampaikan peralatan elektrik serta kabel yang tahan lama, memastikan kuasa janaan loji penting terus mengalir dengan cekap ke grid dengan gangguan yang seminimum mungkin.</p>
    </div>
  </div>
</section>

<section class="section" id="biogas">
  <div class="container">
    <div class="re-block">
      <div class="re-media" style="--panel-img:url('https://www.klseri.com.my/wp-content/uploads/2021/03/sustainable_growth_istock.jpg')">
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
        <p>Disebabkan hubung kaitnya yang rapat dengan industri kelapa sawit, Malaysia berada pada kedudukan baik untuk menjadikan ini sumber tenaga dan haba yang benar-benar bersih. Biogas terhasil daripada pencernaan anaerobik efluen kilang kelapa sawit (POME), hasil sampingan sisa daripada pengeluaran minyak sawit mentah, dan penggunaan POME sebagai sumber biometana mengurangkan kedua-dua pencemaran udara dan jejak karbon kilang.</p>
        <p>Biogas ini boleh menjana tenaga boleh diperbaharui untuk dieksport ke grid nasional. Kami menyokong pelaksanaan loji biogas dengan kerja interkoneksi dan pelbagai perkhidmatan yang memanfaatkan gas metana sebagai sumber kuasa yang cekap, merangkumi bekalan dan pemasangan penuh peralatan interkoneksi elektrik, kabel, serta sistem kawalan dan instrumentasi.</p>
        <a href="projects.html#reference-list" class="btn-ghost">Lihat projek biogas dalam senarai rujukan kami</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--band" id="biomass">
  <div class="container">
    <div class="re-block">
      <div class="re-media" style="--panel-img:url('https://www.klseri.com.my/wp-content/uploads/2021/05/2021-05-10-015217938.jpg')">
        <div>
          <span class="tag">TENAGA BOLEH DIPERBAHARUI</span>
          <div class="headline">Biojisim</div>
        </div>
        <div class="examples">
          <div>Biojisim 10MW untuk Cepat Wawasan Sdn. Bhd.</div>
        </div>
      </div>
      <div class="re-body">
        <p>Tenaga biojisim mempunyai pelbagai kegunaan, tetapi kebanyakan loji biojisim beroperasi dengan cara asas yang sama: membakar bahan organik untuk menghasilkan stim bertekanan tinggi, yang memutarkan turbin penjana untuk menghasilkan elektrik.</p>
        <p>Pertanian, balak dan industri am menghasilkan jumlah besar sumber dan sisa loji yang boleh ditukar kepada tenaga boleh diperbaharui, mengurangkan pergantungan kepada bahan api fosil untuk kuasa dan haba. Negara tropika Asia Tenggara turut berada pada kedudukan baik di sini, dengan iklim panas dan lembap sepanjang tahun serta sektor pertanian yang kukuh.</p>
        <p>Kerja interkoneksi tenaga boleh diperbaharui kami di sini merangkumi kejuruteraan, bekalan, pemasangan dan pentauliahan kabel serta peralatan elektrik yang diperlukan projek biojisim, dibina untuk memenuhi keperluan ketat pihak berkuasa utiliti tempatan sambil mengekalkan gangguan yang rendah dan output penjanaan yang tinggi.</p>
        <a href="projects.html#reference-list" class="btn-ghost">Lihat projek biojisim dalam senarai rujukan kami</a>
      </div>
    </div>
  </div>
</section>

<section class="section" id="solar">
  <div class="container">
    <div class="re-block">
      <div class="re-media" style="--panel-img:url('https://www.klseri.com.my/wp-content/uploads/2021/03/light-bulb-placed-on-soil-in-sun-light.jpg')">
        <div>
          <span class="tag">TENAGA BOLEH DIPERBAHARUI</span>
          <div class="headline">Suria</div>
        </div>
        <div class="examples">
          <div>Tenaga Suria 1MW untuk ERS Energy Sdn. Bhd.</div>
        </div>
      </div>
      <div class="re-body">
        <p>Suria kekal sebagai sumber tenaga boleh diperbaharui yang paling meluas digunakan di dunia, dan atas sebab yang baik: ia bersih, banyak dan tersedia secara percuma. Panel menangkap dan menyimpan tenaga terus daripada matahari tanpa pelepasan dan kesan alam sekitar yang minimum, justeru mengapa suria amat penting kepada sasaran Malaysia untuk mencapai 20% tenaga boleh diperbaharui dalam campuran penjanaannya menjelang 2025.</p>
        <p>Kerja suria kami merangkumi bekalan, pemasangan dan penyelenggaraan kabel serta sistem elektrik yang menghubungkan panel solar, loji kuasa solar dan kemudahan grid nasional. Kami mensasarkan penyelesaian yang kos efektif dan tahan lama, disesuaikan dengan keperluan elektrik dan kejuruteraan khusus setiap projek.</p>
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
    "Perkhidmatan Kami | Pengagihan Kuasa Elektrik & Tenaga Boleh Diperbaharui, KLS",
    "KLS menawarkan perkhidmatan yang merangkumi bekalan, pemasangan, pengujian dan pentauliahan sistem pengagihan kuasa elektrik, serta interkoneksi tenaga boleh diperbaharui Biogas, Biojisim dan Suria.",
    BODY,
    lang="ms",
    alt_url="https://www.klseri.com.my/services.html",
)
