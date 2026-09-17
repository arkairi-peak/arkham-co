from build import page, breadcrumb

def profile(name, role, image, initials, bio, facts):
    facts_html = "".join(f"<div><b>{k}</b>{v}</div>" for k, v in facts)
    img_html = f'<img src="{image}" alt="Foto {name}" loading="lazy">' if image else f'<div class="initials">{initials}</div>'
    return f"""<div class="profile-row">
      <div class="profile-photo">{img_html}</div>
      <div class="profile-body">
        <span class="role">{role}</span>
        <h3>{name}</h3>
        <p>{bio}</p>
        <div class="profile-facts">{facts_html}</div>
      </div>
    </div>"""

FOUNDERS = "".join([
    profile(
        "Lim Cheng Lai", "Pengasas", "https://www.klseri.com.my/wp-content/uploads/2021/02/Lim-Cheng-Lai.jpg", "LCL",
        "Lim Cheng Lai ialah pengasas KLS dan merupakan individu utama yang menerajui serta mengubah syarikat daripada sebuah bengkel pendawaian motor elektrik yang kecil kepada Kontraktor M&amp;E Kelas A, CIDB G7 yang mantap. Beliau menetapkan hala tuju syarikat dan menerajui pasukan teknikal yang muda dan dinamik.",
        [
            ("Pensijilan", "B4 33KV Chargeman (Suruhanjaya Tenaga)"),
            ("Pensijilan", "PW4 Wireman (Suruhanjaya Tenaga)"),
            ("Fokus", "Hala tuju syarikat &amp; kepimpinan teknikal"),
        ],
    ),
    profile(
        "YDM Tengku Dato' Ardy Esfandiari Bin Tengku Hamid Shah Al Haj Tengku Seri Paduka Shahbandar (Selangor)",
        "Pengasas", "https://www.klseri.com.my/wp-content/uploads/2021/02/Team-03-797x1024.jpg", "TA",
        "Salah seorang pengasas KLS, YDM Tengku Dato' Ardy memainkan peranan penting dalam jabatan hubungan awam dan hubungan kerajaan syarikat. Seorang usahawan mapan dengan rangkaian yang luas dan kemahiran hubungan awam yang cemerlang, beliau membantu membina KLS menjadi syarikat yang disegani dalam kalangan Syarikat Berkaitan Kerajaan.",
        [
            ("Anugerah", "Darjah Kebesaran Dato' Sultan Sharafudin Idris Shah (D.S.I.S) — dianugerahkan 2012, sempena ulang tahun ke-67 kelahiran Sultan Selangor"),
            ("Jawatan Lembaga", "CB Industrial Products Bhd."),
            ("Fokus", "Hubungan awam &amp; hubungan kerajaan"),
        ],
    ),
])

TECHNICAL = "".join([
    profile(
        "Ir. Lim Yee Chard", "Kepimpinan Teknikal", "https://www.klseri.com.my/wp-content/uploads/2021/02/Team-02-796x1024.jpg", "LYC",
        "Ir. Lim kini menyelia semua projek yang diusahakan oleh KLS. Sebagai Jurutera Profesional yang bertugas dan Jurutera ASEAN berdaftar, beliau bertanggungjawab ke atas keseluruhan tender, pelaksanaan dan penyerahan semua projek utama, menerajui pasukan teknikal yang bertenaga dan berdedikasi bagi memastikan projek disiapkan melangkaui jangkaan dan dalam anggaran bajet.",
        [
            ("Pendidikan", "UMIST (University of Manchester Institute of Science and Technology), UK — bergraduat 2002"),
            ("Pendaftaran", "Jurutera Profesional bertugas &middot; Jurutera ASEAN berdaftar"),
            ("Tanggungjawab", "Tender, pelaksanaan dan penyerahan projek utama"),
        ],
    ),
    profile(
        "Ir. Jeremy Goh Jing Wei", "Kepimpinan Teknikal", "https://www.klseri.com.my/wp-content/uploads/2021/02/Jeremy.jpg", "JG",
        "Ir. Jeremy Goh menyertai KLS pada 2014 dan merupakan ketua jurutera yang bertanggungjawab ke atas aspek teknikal dan hubungan dengan pihak berkuasa bagi semua projek KLS. Seorang jurutera teknikal yang berpengalaman, beliau mempunyai rekod terbukti dalam menguruskan projek.",
        [
            ("Pendidikan", "UniTEN (Universiti Tenaga Nasional) — Ijazah Kejuruteraan Elektrik dan Elektronik (Kepujian), 2013"),
            ("Pendaftaran", "Jurutera Profesional berdaftar"),
            ("Menyertai KLS", "2014 &middot; Ketua jurutera, teknikal &amp; hubungan pihak berkuasa"),
        ],
    ),
])

BIZDEV = profile(
    "Ali Na'Azzam", "Pembangunan Perniagaan", "https://www.klseri.com.my/wp-content/uploads/2021/02/Team-01-796x1024.jpg", "AN",
    "Ali Na'Azzam bertanggungjawab ke atas pembangunan perniagaan KLS. Dilengkapi dengan kemahiran perhubungan awam yang kukuh dan rangkaian yang luas, beliau turut mahir dalam industri pembinaan dengan pengalaman lebih 25 tahun.",
    [
        ("Pendidikan", "Ijazah Sarjana Muda Undang-Undang (LLB)"),
        ("Pengalaman", "25+ tahun dalam industri pembinaan"),
        ("Jawatan", "Dilantik sebagai Pengarah Eksekutif sejak 2018"),
    ],
)

BODY = f"""
<section class="page-hero">
  <div class="container">
    <h1>Warga Kerja Kami</h1>
    <p class="lead">Pengasas, kepimpinan teknikal dan pasukan pembangunan perniagaan di sebalik KLS — disusun mengikut peranan masing-masing dalam syarikat.</p>
  </div>
</section>
{breadcrumb('our-people.html','Warga Kerja Kami', lang='ms')}

<section class="section">
  <div class="container">
    <div class="people-group">
      <div class="people-group-head"><h3>Pengasas &amp; Kepimpinan</h3><span class="mono">01–02</span></div>
      {FOUNDERS}
    </div>
    <div class="people-group">
      <div class="people-group-head"><h3>Kepimpinan Teknikal</h3><span class="mono">03–04</span></div>
      {TECHNICAL}
    </div>
    <div class="people-group">
      <div class="people-group-head"><h3>Pembangunan Perniagaan</h3><span class="mono">05</span></div>
      {BIZDEV}
    </div>
  </div>
</section>

<section class="section section--band">
  <div class="container grid grid-2" style="align-items:center;gap:48px;">
    <div>
      <div class="kicker">Pasukan Kami</div>
      <h2>Pasukan teknikal yang muda dan dinamik</h2>
      <p class="lead">Selain kakitangan utamanya, KLS diterajui oleh pasukan teknikal yang muda dan dinamik yang bertanggungjawab ke atas tender, pelaksanaan dan penyerahan setiap projek — daripada kerja pendawaian semula sehingga kemudahan interkoneksi tenaga boleh diperbaharui bermegawatt.</p>
    </div>
    <a href="https://www.klseri.com.my/wp-content/uploads/2021/04/KLS-01.png" target="_blank" rel="noopener">
      <img src="https://www.klseri.com.my/wp-content/uploads/2021/04/KLS-01.png" alt="Pasukan KLS" style="border-radius:10px;border:1px solid var(--line-300);">
    </a>
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
    "our-people.html",
    "Warga Kerja Kami | Kakitangan Utama KLS",
    "Kenali kakitangan utama KLS, disusun mengikut peranan — pengasas, kepimpinan teknikal dan pembangunan perniagaan — yang membina sebuah penyedia perkhidmatan elektrik yang disegani.",
    BODY,
    lang="ms",
    alt_url="https://www.klseri.com.my/our-people.html",
)
