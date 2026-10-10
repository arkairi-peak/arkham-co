"""Home page body, shared by pages_home.py (English) and ms_pages_home.py (BM).

One structure, two sets of copy, so the two languages cannot drift apart.
Section order:
  1. What we do: a pinned scroll story (opening photo, then one service per
     panel with a photo and a plain-language explanation)
  2. Figures band
  3. Industries we serve: a second pinned story (sector list + photo + projects)
  4. Project sites (photo galleries)
  5. Clients, 6. Four decades, 7. Certifications, 8. Call to action
Desktop pinning is driven by assets/js/scroll.js ([data-seq]); on phones, with
reduced motion or without JavaScript the panels simply stack.
"""
import json
from html import escape

IMG = "assets/img/"

# Project photo galleries: (file stem, EN caption, BM caption)
GALLERIES = {
    "sick": [
        ("projects/sick-01", "Building exterior", "Bahagian luar bangunan"),
        ("projects/sick-02", "Production hall", "Dewan pengeluaran"),
        ("projects/sick-03", "Production floor", "Lantai pengeluaran"),
        ("projects/sick-04", "Production hall", "Dewan pengeluaran"),
        ("projects/sick-05", "Production hall", "Dewan pengeluaran"),
        ("projects/sick-06", "Production equipment", "Peralatan pengeluaran"),
        ("projects/sick-07", "Utility room", "Bilik utiliti"),
        ("projects/sick-08", "Air handling units and chilled-water pumps", "Unit pengendalian udara dan pam air sejuk"),
        ("projects/sick-09", "Chiller plant", "Loji penyejuk"),
        ("projects/sick-10", "Plant room with hose reel and alarm point", "Bilik loji dengan gelung hos dan titik penggera"),
        ("projects/sick-11", "Electrical room", "Bilik elektrik"),
        ("projects/sick-13", "Meeting room", "Bilik mesyuarat"),
        ("projects/sick-14", "Open office", "Pejabat terbuka"),
        ("projects/sick-12", "Lobby", "Lobi"),
    ],
    "melexis": [
        ("projects/melexis-01", "Aerial view", "Pandangan udara"),
        ("projects/melexis-02", "Aerial view", "Pandangan udara"),
    ],
    "up": [
        ("projects/up-01", "Switchboard room", "Bilik papan suis"),
        ("projects/up-02", "Switchboards", "Papan suis"),
        ("projects/up-03", "Process hall", "Dewan proses"),
        ("projects/up-04", "Process hall", "Dewan proses"),
        ("projects/up-05", "Interior", "Ruang dalaman"),
        ("projects/up-06", "Dining hall", "Dewan makan"),
    ],
    "larkin": [
        ("projects/larkin-3", "Pitch and stands under floodlights", "Padang dan tempat duduk di bawah lampu limpah"),
        ("projects/larkin-1", "Aerial view at night", "Pandangan udara pada waktu malam"),
    ],
}
HAS_SMALL = ("sick", "melexis", "up")  # these have -sm.webp versions

EPD = "services.html#electrical-power-distribution"

COPY = {
    "en": dict(
        chips=["Est. 1984", "CIDB G7", "Class A"],
        title="Electrical engineering and renewable energy interconnection, end to end",
        lead="Since 1984 KLS has supplied, installed, tested and commissioned high, low and extra-low voltage systems for industrial, commercial, infrastructure and marine projects across Malaysia.",
        btn1=("projects.html", "See our projects"), btn2=("contact.html", "Contact us"),
        hero_img=("projects/sick-02", "Production hall with overhead cable trays and lighting at SICK, Senai", "SICK, Senai, Johor"),
        wwd_h2="What we do", scope_label="Our scope",
        services=[
            dict(rail="HV / MV / LV", title="HV / MV / LV electrical work",
                 text="Power reaches a site in stages. In Malaysia the national grid carries it at high voltage (132 kV and above), steps it down to medium voltage (usually 11, 22 or 33 kV) for distribution, and finally to low voltage (400/230 V) for lighting, sockets and machines. We build that chain inside a site and make sure every part of it is tested before it is switched on.",
                 scope=["Medium and high voltage power systems", "Low voltage power systems and switchboards", "Power transformers", "AMF boards and emergency main switchboards (EMSB)", "Motor control centres (MCC)", "MV and LV power cabling and cable support", "Diesel generator systems"],
                 link=(EPD, "Read more on our services"), img="projects/sick-11", cap="Electrical room, SICK, Senai"),
            dict(rail="ACMV", title="ACMV",
                 text="Air-conditioning and mechanical ventilation keeps a building at the right temperature, humidity and air quality. A typical system pairs chillers or condensing units with air handling units, fan coil units, ducting and exhaust fans. Behind each one sits electrical work: power supply, motor starters and control panels, and links to the building automation system that schedules and monitors it all.",
                 scope=["HVAC and ventilation systems", "Power and controls for chiller plant and air handling units", "Building automation system (BAS) and SCADA", "Testing and commissioning"],
                 link=(EPD, "Read more on our services"), img="projects/sick-08", cap="Air handling units and chilled-water pumps, SICK, Senai"),
            dict(rail="Fire fighting", title="Fire fighting",
                 text="Active fire protection detects a fire, raises the alarm and fights it until help arrives: sprinklers, hose reels, hydrants, wet and dry risers, fire pumps, and the alarm and detection systems that set them off. In Malaysia these systems follow the Uniform Building By-Laws and need approval from the Fire and Rescue Department (BOMBA). The electrical side matters as much as the pipework: fire pump control panels, alarm panels, and power supplies that must keep running when everything else is off.",
                 scope=["Fire fighting system installations for buildings and plants", "Power supply and controls for fire pumps and alarm panels"],
                 link=("contact.html", "Discuss a project with us"), img="projects/sick-10", cap="Hose reel, alarm point and sprinkler pipework, SICK, Senai"),
            dict(rail="ELV", title="ELV systems",
                 text="Extra-low voltage covers systems that run below 50 V AC (or 120 V DC): the networks that carry data, pictures and sound rather than power. CCTV, access control, structured cabling and data networks, telephones, public address and AV, and SMATV for shared satellite and TV reception are all ELV. They are installed alongside the power systems, so planning both together saves rework later.",
                 scope=["CCTV", "SMATV", "AV and PA systems", "Telecommunication internal and infrastructure works", "ICT solutions and data networking"],
                 link=(EPD, "Read more on our services"), img="projects/sick-13", cap="Meeting room with video conferencing, SICK, Senai"),
            dict(rail="Renovation", title="Renovation & restoration",
                 text="Electrical installations age: insulation wears, loads grow and older switchboards fall behind current standards. Renovation brings an existing building up to date without starting over, from rewiring and switchboard replacement to capacity upgrades, while restoration of older buildings means fitting new services carefully around the original structure. KLS began in 1984 as a master rewiring service provider, so this is where we started.",
                 scope=["Rewiring of existing installations", "Switchboard replacement and upgrades", "Capacity upgrades for added load", "Restoration works for older buildings"],
                 link=("contact.html", "Discuss a project with us"), img="projects/up-03", cap="Process hall, United Plantations seed plant"),
        ],
        stats=[("42", "+", "Years in operation"), ("35", "+", "Documented projects"), ("12", "", "Certificates &amp; licenses"), ("3", "", "Offices: Port Klang, Lahad Datu, Bintulu")],
        ind_h2="Industries we serve",
        ind_lead="Five sectors where our electrical and interconnection work shows up most.",
        industries=[
            ("Clean energy", "Electrical interconnection for biogas, biomass and solar plants, linking them to the national grid. It is where our project history runs deepest.",
             ["10 MW biomass plant, Cepat Wawasan", "3.5 MW biogas plant, Mistral Engineering", "1.5 MW biogas plant, Cenergi FJP", "1 MW solar plant, ERS Energy"],
             "industries/biomass", "Renewable energy interconnection works"),
            ("Substation & grid utilities", "HV, MV and LV works for utility and telecommunications infrastructure, including remote terminal units and 11kV switchgear upgrades.",
             ["Remote terminal unit electrical works, SESB, Sabah", "Electrical upgrading works, Telekom Malaysia"],
             "projects/up-02", "Switchboards, United Plantations seed plant"),
            ("Semiconductor & electronics", "A growing focus as chip and electronics manufacturing in Malaysia expands with global demand.",
             ["SICK, Senai, Johor", "Melexis, Kuching, Sarawak", "Renesas"],
             "projects/sick-03", "Production floor, SICK, Senai"),
            ("Petrochemical & oleochemical", "Electrical, mechanical and ELV works for refineries, oleochemical plants and palm oil processing facilities.",
             ["Marine facilities works, Dialog Group, Pengerang", "Refinery electrical works, Cargill, Port Klang", "GTG cogen works, KLK Berhad, Rawang", "Palm oil mill, refinery and biogas electrical works, United Plantations, Ulu Bernam"],
             "projects/up-04", "Process hall, United Plantations seed plant"),
            ("Hospital & stadium", "Lighting and electrical systems for public buildings, from stadiums to healthcare facilities.",
             ["Stadium lighting, Stadium Tan Sri Dato' Haj Hassan Yunos (Larkin), home ground of Johor Darul Ta'zim"],
             "projects/larkin-3", "Larkin Stadium, Johor Bahru"),
        ],
        refs_label="Selected projects",
        ind_more="See the full project reference list",
        sites_h2="Project sites",
        sites_lead="Photos from sites we have worked on. Select a project to look through its photos.",
        sites=[
            ("sick", "SICK", "Senai, Johor", "Semiconductor & electronics"),
            ("melexis", "Melexis", "Kuching, Sarawak", "Semiconductor & electronics"),
            ("up", "United Plantations", "Seed plant", "Palm oil processing"),
            ("larkin", "Larkin Stadium", "Johor Bahru, Johor", "Stadium lighting"),
        ],
        photos="photos",
        clients_h2="Clients we have worked with",
        clients_more="View the full project reference list",
        decades_h2="Four decades in Malaysian engineering",
        decades_p="We started as a small electrical motor wiring workshop and grew into an established Class A, CIDB G7 M&amp;E Contractor working across Malaysia and beyond.",
        decades_btn="Our story &amp; timeline",
        milestones=[("1984", "Incorporated in Malaysia as a master rewiring service provider"),
                    ("1984-2000s", "Became an established Class A, CIDB G7 M&amp;E Contractor"),
                    ("2000", "Opened a branch office in Lahad Datu, Sabah"),
                    ("Beyond MY", "Took on international projects in Indonesia, Papua New Guinea &amp; Africa")],
        certs_h2="Certifications &amp; licenses",
        certs_lead="A Class A, CIDB G7 M&amp;E Contractor, holding certification across every electrical and construction discipline we operate in.",
        certs_btn="View all certifications &amp; licenses",
        cert_alt="One of KLS's certificates",
        cta_h2="Have an electrical or renewable energy project in mind? Let's talk",
        cta_p="Reach our team at the Port Klang headquarters, or at either of our branch offices in Sabah and Sarawak.",
        cta_btn="Contact us", call="Call +603 3167 1818",
    ),
    "ms": dict(
        chips=["Sejak 1984", "CIDB G7", "Kelas A"],
        title="Kejuruteraan elektrik dan interkoneksi tenaga boleh diperbaharui, hujung ke hujung",
        lead="Sejak 1984, KLS membekal, memasang, menguji dan mentauliah sistem voltan tinggi, voltan rendah dan voltan sangat rendah untuk projek industri, komersial, infrastruktur dan marin di seluruh Malaysia.",
        btn1=("projects.html", "Lihat projek kami"), btn2=("contact.html", "Hubungi kami"),
        hero_img=("projects/sick-02", "Dewan pengeluaran dengan dulang kabel dan lampu di atas, SICK, Senai", "SICK, Senai, Johor"),
        wwd_h2="Apa yang kami lakukan", scope_label="Skop kami",
        services=[
            dict(rail="HV / MV / LV", title="Kerja elektrik HV / MV / LV",
                 text="Bekalan kuasa sampai ke tapak secara berperingkat. Di Malaysia, grid nasional menghantar kuasa pada voltan tinggi (132 kV dan ke atas), menurunkannya ke voltan sederhana (biasanya 11, 22 atau 33 kV) untuk pengagihan, dan akhirnya ke voltan rendah (400/230 V) untuk lampu, soket dan mesin. Kami membina rangkaian itu di dalam tapak dan memastikan setiap bahagiannya diuji sebelum dihidupkan.",
                 scope=["Sistem kuasa voltan sederhana dan tinggi", "Sistem kuasa dan papan suis voltan rendah", "Pengubah kuasa", "Papan AMF dan papan suis utama kecemasan (EMSB)", "Pusat kawalan motor (MCC)", "Pengkabelan kuasa MV dan LV serta sokongan kabel", "Sistem penjana diesel"],
                 link=(EPD, "Baca lanjut tentang perkhidmatan kami"), img="projects/sick-11", cap="Bilik elektrik, SICK, Senai"),
            dict(rail="ACMV", title="ACMV",
                 text="Penyaman udara dan pengudaraan mekanikal mengekalkan suhu, kelembapan dan kualiti udara yang sesuai dalam bangunan. Sistem biasa menggabungkan penyejuk (chiller) atau unit pemeluwap dengan unit pengendalian udara, unit gegelung kipas, saluran udara dan kipas ekzos. Di sebalik setiap satunya ada kerja elektrik: bekalan kuasa, pemula motor dan panel kawalan, serta sambungan ke sistem automasi bangunan yang menjadualkan dan memantau semuanya.",
                 scope=["Sistem HVAC dan pengudaraan", "Kuasa dan kawalan untuk loji penyejuk dan unit pengendalian udara", "Sistem automasi bangunan (BAS) dan SCADA", "Pengujian dan pentauliahan"],
                 link=(EPD, "Baca lanjut tentang perkhidmatan kami"), img="projects/sick-08", cap="Unit pengendalian udara dan pam air sejuk, SICK, Senai"),
            dict(rail="Kebakaran", title="Pencegahan kebakaran",
                 text="Perlindungan kebakaran aktif mengesan kebakaran, membunyikan penggera dan memadamkannya sehingga bantuan tiba: pemercik, gelung hos, pili bomba, paip naik basah dan kering, pam kebakaran, serta sistem penggera dan pengesanan yang mengaktifkannya. Di Malaysia, sistem ini mengikut Undang-Undang Kecil Bangunan Seragam (UBBL) dan memerlukan kelulusan Jabatan Bomba dan Penyelamat (BOMBA). Bahagian elektriknya sama penting dengan paipnya: panel kawalan pam kebakaran, panel penggera, dan bekalan kuasa yang mesti terus berfungsi walaupun semua yang lain dimatikan.",
                 scope=["Pemasangan sistem pencegahan kebakaran untuk bangunan dan loji", "Bekalan kuasa dan kawalan untuk pam kebakaran dan panel penggera"],
                 link=("contact.html", "Bincang projek dengan kami"), img="projects/sick-10", cap="Gelung hos, titik penggera dan paip pemercik, SICK, Senai"),
            dict(rail="ELV", title="Sistem ELV",
                 text="Voltan sangat rendah (ELV) merangkumi sistem yang beroperasi di bawah 50 V AU (atau 120 V AT): rangkaian yang membawa data, gambar dan bunyi, bukan kuasa. CCTV, kawalan akses, pengkabelan berstruktur dan rangkaian data, telefon, sistem siaraya dan AV, serta SMATV untuk penerimaan satelit dan TV bersama, semuanya tergolong dalam ELV. Sistem ini dipasang bersama sistem kuasa, jadi merancang kedua-duanya serentak mengelakkan kerja semula kemudian.",
                 scope=["CCTV", "SMATV", "Sistem AV dan PA", "Kerja telekomunikasi dalaman dan infrastruktur", "Penyelesaian ICT dan rangkaian data"],
                 link=(EPD, "Baca lanjut tentang perkhidmatan kami"), img="projects/sick-13", cap="Bilik mesyuarat dengan sidang video, SICK, Senai"),
            dict(rail="Naik taraf", title="Naik taraf & pemulihan",
                 text="Pemasangan elektrik semakin usang: penebat haus, beban bertambah dan papan suis lama ketinggalan berbanding piawaian semasa. Kerja naik taraf membawa bangunan sedia ada ke tahap terkini tanpa bermula semula, daripada pendawaian semula dan penggantian papan suis hingga peningkatan kapasiti, manakala pemulihan bangunan lama bermaksud memuatkan perkhidmatan baharu dengan teliti di sekitar struktur asal. KLS bermula pada 1984 sebagai penyedia perkhidmatan pendawaian semula utama, jadi di sinilah kami bermula.",
                 scope=["Pendawaian semula pemasangan sedia ada", "Penggantian dan naik taraf papan suis", "Peningkatan kapasiti untuk beban tambahan", "Kerja pemulihan untuk bangunan lama"],
                 link=("contact.html", "Bincang projek dengan kami"), img="projects/up-03", cap="Dewan proses, loji benih United Plantations"),
        ],
        stats=[("42", "+", "Tahun beroperasi"), ("35", "+", "Projek didokumenkan"), ("12", "", "Sijil &amp; lesen"), ("3", "", "Pejabat: Port Klang, Lahad Datu, Bintulu")],
        ind_h2="Industri yang kami khidmati",
        ind_lead="Lima sektor di mana kerja elektrik dan interkoneksi kami paling banyak dilihat.",
        industries=[
            ("Tenaga bersih", "Interkoneksi elektrik untuk loji biogas, biojisim dan suria, menyambungkannya ke grid nasional. Bidang inilah yang mempunyai sejarah projek paling mendalam bagi kami.",
             ["Loji biojisim 10 MW, Cepat Wawasan", "Loji biogas 3.5 MW, Mistral Engineering", "Loji biogas 1.5 MW, Cenergi FJP", "Loji suria 1 MW, ERS Energy"],
             "industries/biomass", "Kerja interkoneksi tenaga boleh diperbaharui"),
            ("Pencawang & utiliti grid", "Kerja HV, MV dan LV untuk infrastruktur utiliti dan telekomunikasi, termasuk unit terminal jauh dan naik taraf suis gear 11kV.",
             ["Kerja elektrik unit terminal jauh, SESB, Sabah", "Kerja naik taraf elektrik, Telekom Malaysia"],
             "projects/up-02", "Papan suis, loji benih United Plantations"),
            ("Semikonduktor & elektronik", "Fokus yang berkembang seiring pertumbuhan pembuatan cip dan elektronik di Malaysia untuk permintaan global.",
             ["SICK, Senai, Johor", "Melexis, Kuching, Sarawak", "Renesas"],
             "projects/sick-03", "Lantai pengeluaran, SICK, Senai"),
            ("Petrokimia & oleokimia", "Kerja elektrik, mekanikal dan ELV untuk loji penapisan, loji oleokimia dan kemudahan pemprosesan kelapa sawit.",
             ["Kerja kemudahan marin, Dialog Group, Pengerang", "Kerja elektrik loji penapisan, Cargill, Port Klang", "Kerja kogenerasi GTG, KLK Berhad, Rawang", "Kerja elektrik kilang sawit, loji penapisan dan biogas, United Plantations, Ulu Bernam"],
             "projects/up-04", "Dewan proses, loji benih United Plantations"),
            ("Hospital & stadium", "Sistem pencahayaan dan elektrik untuk bangunan awam, daripada stadium hingga kemudahan kesihatan.",
             ["Pencahayaan stadium, Stadium Tan Sri Dato' Haj Hassan Yunos (Larkin), gelanggang Johor Darul Ta'zim"],
             "projects/larkin-3", "Stadium Larkin, Johor Bahru"),
        ],
        refs_label="Projek terpilih",
        ind_more="Lihat senarai rujukan projek penuh",
        sites_h2="Tapak projek",
        sites_lead="Gambar dari tapak yang pernah kami usahakan. Pilih projek untuk melihat gambarnya.",
        sites=[
            ("sick", "SICK", "Senai, Johor", "Semikonduktor & elektronik"),
            ("melexis", "Melexis", "Kuching, Sarawak", "Semikonduktor & elektronik"),
            ("up", "United Plantations", "Loji benih", "Pemprosesan kelapa sawit"),
            ("larkin", "Stadium Larkin", "Johor Bahru, Johor", "Pencahayaan stadium"),
        ],
        photos="gambar",
        clients_h2="Pelanggan yang pernah bekerjasama dengan kami",
        clients_more="Lihat senarai rujukan projek penuh",
        decades_h2="Empat dekad dalam kejuruteraan Malaysia",
        decades_p="Kami bermula sebagai bengkel pendawaian motor elektrik yang kecil dan berkembang menjadi Kontraktor M&amp;E Kelas A, CIDB G7 yang mantap, beroperasi di seluruh Malaysia dan luar negara.",
        decades_btn="Kisah &amp; garis masa kami",
        milestones=[("1984", "Diperbadankan di Malaysia sebagai penyedia perkhidmatan pendawaian semula utama"),
                    ("1984-2000-an", "Menjadi Kontraktor M&amp;E Kelas A, CIDB G7 yang mantap"),
                    ("2000", "Membuka pejabat cawangan di Lahad Datu, Sabah"),
                    ("Ke luar negara", "Mengambil projek antarabangsa di Indonesia, Papua New Guinea &amp; Afrika")],
        certs_h2="Pensijilan &amp; lesen",
        certs_lead="Kontraktor M&amp;E Kelas A, CIDB G7, memegang pensijilan merentasi setiap bidang elektrik dan pembinaan yang kami ceburi.",
        certs_btn="Lihat semua pensijilan &amp; lesen",
        cert_alt="Salah satu sijil KLS",
        cta_h2="Ada projek elektrik atau tenaga boleh diperbaharui? Mari berbincang",
        cta_p="Hubungi pasukan kami di ibu pejabat Port Klang, atau di salah satu pejabat cawangan kami di Sabah dan Sarawak.",
        cta_btn="Hubungi kami", call="Telefon +603 3167 1818",
    ),
}


def home_body(lang):
    c = COPY[lang]
    p = "../" if lang == "ms" else ""
    img = lambda stem, small=False: f"{p}{IMG}{stem}{'-sm' if small else ''}.webp"
    e = lambda s: escape(s, quote=False)  # copy may already contain &amp; entities
    a = lambda s: escape(s, quote=True)

    # 1. What we do: opening panel + one panel per service
    h_stem, h_alt, h_cap = c["hero_img"]
    panels = [f'''    <article class="seq-panel seq-panel--hero" data-seq-panel>
      <figure class="seq-media" data-seq-media><img src="{img(h_stem)}" alt="{a(h_alt)}" data-entrance-photo><figcaption>{e(h_cap)}</figcaption></figure>
      <div class="seq-text container" data-seq-text>
        <div class="hero-chips" data-entrance-rest>{"".join(f"<span>{x}</span>" for x in c["chips"])}</div>
        <h1 class="hero-title" data-entrance-title>{e(c["title"])}</h1>
        <p class="lead" data-entrance-rest>{e(c["lead"])}</p>
        <div class="hero-actions" data-entrance-rest>
          <a href="{c["btn1"][0]}" class="btn btn-primary">{c["btn1"][1]}</a>
          <a href="{c["btn2"][0]}" class="btn btn-outline">{c["btn2"][1]}</a>
        </div>
      </div>
    </article>
    <h2 class="seq-mobile-head container">{c["wwd_h2"]}</h2>''']
    for s in c["services"]:
        scope = "".join(f"<li>{e(x)}</li>" for x in s["scope"])
        panels.append(f'''    <article class="seq-panel" data-seq-panel>
      <figure class="seq-media" data-seq-media><img src="{img(s["img"])}" alt="" loading="lazy"><figcaption>{e(s["cap"])}</figcaption></figure>
      <div class="seq-text container" data-seq-text>
        <h3>{e(s["title"])}</h3>
        <p class="seq-lead">{e(s["text"])}</p>
        <p class="seq-scope-label">{c["scope_label"]}</p>
        <ul class="seq-scope">{scope}</ul>
        <a href="{s["link"][0]}" class="btn-ghost">{s["link"][1]}</a>
      </div>
    </article>''')
    rail = "".join(f'<li><button type="button" data-seq-nav="{i + 1}">{e(s["rail"])}</button></li>' for i, s in enumerate(c["services"]))

    # 3. Industries: sector list + one photo/project panel per sector
    ind_nav, ind_panels = [], []
    for i, (title, desc, refs, stem, cap) in enumerate(c["industries"]):
        ind_nav.append(f'<li><button type="button" data-seq-nav="{i}">{e(title)}</button></li>')
        refs_html = "".join(f"<li>{e(r)}</li>" for r in refs)
        ind_panels.append(f'''        <article class="seq-panel" data-seq-panel>
          <figure class="seq-media" data-seq-media><img src="{img(stem)}" alt="" loading="lazy"><figcaption>{e(cap)}</figcaption></figure>
          <div class="seq-text ind-card" data-seq-text>
            <h3>{e(title)}</h3>
            <p>{e(desc)}</p>
            <p class="ind-refs-label">{c["refs_label"]}</p>
            <ul class="ind-refs">{refs_html}</ul>
          </div>
        </article>''')

    # 4. Project sites: cover cards that open a photo gallery
    cards = []
    for key, name, loc, sector in c["sites"]:
        g = GALLERIES[key]
        payload = json.dumps([{"src": img(stem), "caption": cap_en if lang == "en" else cap_ms} for stem, cap_en, cap_ms in g], ensure_ascii=False)
        cover = img("projects/sick-02" if key == "sick" else g[0][0], key in HAS_SMALL)
        cards.append(f'''      <button type="button" class="site-card site-card--{key}" data-gallery="{a(payload)}" data-gallery-title="{a(name)}, {a(loc)}">
        <img src="{cover}" alt="" loading="lazy">
        <span class="site-meta"><span class="site-name">{e(name)}</span><span class="site-loc">{e(loc)}</span><span class="site-sector">{e(sector)}</span><span class="site-count">{len(g)} {c["photos"]}</span></span>
      </button>''')

    stats = "\n".join(
        f'    <div class="trust-stat"><b data-count-to="{n}"{f" data-count-suffix=\"{s}\"" if s else ""}>{n}{s}</b><span>{label}</span></div>'
        for n, s, label in c["stats"])
    milestones = "\n".join(f'      <div class="milestone-chip"><b>{y}</b><span>{t}</span></div>' for y, t in c["milestones"])
    nl = "\n"

    return f'''
<div class="intro" data-intro aria-hidden="true">
  <div class="intro-meta"><span>Kejuruteraan Letrik Seri (M) Sdn Bhd</span><span>Port Klang, Malaysia</span></div>
  <div class="intro-year" data-intro-count>1950</div>
  <div class="intro-card"><img src="{img(h_stem)}" alt=""></div>
  <div class="intro-line"><i></i></div>
</div>
<script>try{{var d=document.documentElement;if(window.matchMedia('(prefers-reduced-motion: reduce)').matches||sessionStorage.getItem('klsIntroSeen')==='1'){{d.classList.add('no-intro');}}else{{sessionStorage.setItem('klsIntroSeen','1');d.classList.add('intro-lock');}}}}catch(e){{}}</script>

<section class="seq seq--wwd" id="what-we-do" data-seq>
  <div class="seq-stage">
{nl.join(panels)}
  </div>
  <div class="seq-rail">
    <div class="container seq-rail-inner">
      <p class="seq-rail-title">{c["wwd_h2"]}</p>
      <ol class="seq-nav">{rail}</ol>
    </div>
    <div class="seq-bar"><i data-seq-bar></i></div>
  </div>
</section>

<section class="trust-band">
  <div class="container trust-grid">
{stats}
  </div>
</section>

<section class="seq seq--ind industries" id="industries" data-seq>
  <div class="container ind-wrap">
    <div class="ind-side">
      <h2>{c["ind_h2"]}</h2>
      <p class="lead">{c["ind_lead"]}</p>
      <ol class="seq-nav ind-nav">{"".join(ind_nav)}</ol>
      <div class="seq-bar ind-bar"><i data-seq-bar></i></div>
      <a href="projects.html" class="btn btn-outline btn-on-dark ind-more">{c["ind_more"]}</a>
    </div>
    <div class="seq-stage ind-stage">
{nl.join(ind_panels)}
    </div>
    <a href="projects.html" class="btn btn-outline btn-on-dark ind-more ind-more--end">{c["ind_more"]}</a>
  </div>
</section>

<section class="section" id="project-sites">
  <div class="container">
    <div class="section-head">
      <h2>{c["sites_h2"]}</h2>
      <p class="lead">{c["sites_lead"]}</p>
    </div>
    <div class="site-grid">
{nl.join(cards)}
    </div>
  </div>
</section>

<section class="section section--band" id="clients">
  <div class="container">
    <div class="section-head">
      <h2>{c["clients_h2"]}</h2>
    </div>
    <div data-key-clients></div>
    <a href="projects.html" class="btn-ghost clients-more">{c["clients_more"]}</a>
  </div>
</section>

<section class="section section--forest">
  <div class="container">
    <div class="section-head">
      <h2>{c["decades_h2"]}</h2>
      <p>{c["decades_p"]}</p>
      <a href="company-overview.html#our-story" class="btn btn-outline btn-on-dark">{c["decades_btn"]}</a>
    </div>
  </div>
  <div class="marquee" data-marquee data-marquee-speed="26">
    <div class="marquee-track">
{milestones}
    </div>
  </div>
</section>

<section class="section">
  <div class="container certs-home">
    <div>
      <h2>{c["certs_h2"]}</h2>
      <p class="lead">{c["certs_lead"]}</p>
      <a href="certifications.html" class="btn btn-primary">{c["certs_btn"]}</a>
    </div>
    <a href="certifications.html" class="cert-feature"><img src="{p}{IMG}certs/cert-1.webp" alt="{c["cert_alt"]}" loading="lazy"></a>
  </div>
</section>

<section class="section section--forest cta-final">
  <div class="container cta-grid">
    <div>
      <h2>{c["cta_h2"]}</h2>
      <p>{c["cta_p"]}</p>
    </div>
    <div class="cta-actions">
      <a href="contact.html" class="btn btn-primary">{c["cta_btn"]}</a>
      <a href="tel:+60331671818" class="cta-phone">{c["call"]}</a>
    </div>
  </div>
</section>
'''
