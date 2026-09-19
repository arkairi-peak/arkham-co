#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds the KLS static site (bilingual: English + Bahasa Malaysia).
Run: python3 build.py  (prints usage; actual pages are written by the
page-builder scripts, pages_*.py for English, ms_pages_*.py for BM -
which import page()/breadcrumb() from this file.)

English pages live at the project root (e.g. index.html).
Bahasa Malaysia pages live under ms/ (e.g. ms/index.html), sharing the
same assets/ folder one level up.
"""
import os
from urllib.parse import quote_plus

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
MS_DIR = os.path.join(OUT_DIR, "ms")
os.makedirs(MS_DIR, exist_ok=True)

SITE_NAME = "Kejuruteraan Letrik Seri (M) Sdn Bhd"

# ---------------------------------------------------------------------------
# UI chrome strings, English / Bahasa Malaysia
# ---------------------------------------------------------------------------
UI = {
    "en": {
        "contact_us": "Contact Us",
        "menu": "Menu",
        "close_menu": "Close menu",
        "nav_dialog_label": "Site navigation",
        "kls_navigation": "KLS Navigation",
        "footer_desc": "Kejuruteraan Letrik Seri (M) Sdn Bhd, a Class A, CIDB G7 electrical engineering and renewable energy interconnection contractor, in business since 1984.",
        "footer_nav": "Navigation",
        "footer_hq": "Headquarters",
        "footer_branches": "Branch Offices",
        "footer_contact": "Contact",
        "footer_find_us": "Find Us",
        "google_maps": "Google Maps",
        "waze": "Waze",
        "rights": "All rights reserved.",
        "incorporated_line": "Incorporated 1984 &middot; Port Klang, Selangor, Malaysia",
        "back_to_top": "Back to top",
        "whatsapp_label": "Chat with us on WhatsApp",
        "breadcrumb_home": "Home",
        "footer_links": [
            ("Home", "index.html"),
            ("Company Overview", "company-overview.html"),
            ("Our People", "our-people.html"),
            ("Certifications &amp; Licenses", "certifications.html"),
            ("Our Services", "services.html"),
            ("Key Projects", "projects.html"),
            ("Careers", "careers.html"),
            ("Contact Us", "contact.html"),
        ],
    },
    "ms": {
        "contact_us": "Hubungi Kami",
        "menu": "Menu",
        "close_menu": "Tutup menu",
        "nav_dialog_label": "Navigasi laman",
        "kls_navigation": "Navigasi KLS",
        "footer_desc": "Kejuruteraan Letrik Seri (M) Sdn Bhd, sebuah kontraktor kejuruteraan elektrik dan interkoneksi tenaga boleh diperbaharui Kelas A, CIDB G7, beroperasi sejak 1984.",
        "footer_nav": "Navigasi",
        "footer_hq": "Ibu Pejabat",
        "footer_branches": "Pejabat Cawangan",
        "footer_contact": "Hubungi",
        "footer_find_us": "Lokasi Kami",
        "google_maps": "Google Maps",
        "waze": "Waze",
        "rights": "Hak cipta terpelihara.",
        "incorporated_line": "Diperbadankan 1984 &middot; Port Klang, Selangor, Malaysia",
        "back_to_top": "Kembali ke atas",
        "whatsapp_label": "Berbual dengan kami di WhatsApp",
        "breadcrumb_home": "Laman Utama",
        "footer_links": [
            ("Laman Utama", "index.html"),
            ("Ikhtisar Syarikat", "company-overview.html"),
            ("Warga Kerja Kami", "our-people.html"),
            ("Pensijilan &amp; Lesen", "certifications.html"),
            ("Perkhidmatan Kami", "services.html"),
            ("Projek Utama", "projects.html"),
            ("Kerjaya", "careers.html"),
            ("Hubungi Kami", "contact.html"),
        ],
    },
}

# label_en, label_ms, href, sub[(en,ms,href)], preview image, caption_en, caption_ms
NAV_ITEMS = [
    ("Home", "Laman Utama", "index.html", [],
     "https://www.klseri.com.my/wp-content/uploads/2021/03/sustainable_growth_istock.jpg",
     "Electrical engineering & renewable energy since 1984",
     "Kejuruteraan elektrik & tenaga boleh diperbaharui sejak 1984"),
    ("Company", "Syarikat Kami", "company-overview.html", [
        ("Company Overview", "Ikhtisar Syarikat", "company-overview.html"),
        ("Our Story & History", "Kisah & Sejarah Kami", "company-overview.html#our-story"),
        ("Mission & Vision", "Misi & Wawasan", "company-overview.html#mission-vision"),
        ("Core Values", "Nilai Teras", "company-overview.html#core-values"),
    ], "https://www.klseri.com.my/wp-content/uploads/2021/03/light-bulb-placed-on-soil-in-sun-light.jpg",
     "A Class A, CIDB G7 M&E Contractor, incorporated 1984",
     "Kontraktor M&E Kelas A, CIDB G7, diperbadankan pada 1984"),
    ("People", "Warga Kerja Kami", "our-people.html", [],
     "https://www.klseri.com.my/wp-content/uploads/2021/04/KLS-01.png",
     "Founders, technical leadership & business development",
     "Pengasas, kepimpinan teknikal & pembangunan perniagaan"),
    ("Services", "Perkhidmatan Kami", "services.html", [
        ("Electrical Power Distribution", "Pengagihan Kuasa Elektrik", "services.html#electrical-power-distribution"),
        ("Renewable Energy", "Tenaga Boleh Diperbaharui", "services.html#renewable-energy"),
        ("Biogas", "Biogas", "services.html#biogas"),
        ("Biomass", "Biojisim", "services.html#biomass"),
        ("Solar", "Suria", "services.html#solar"),
    ], "https://www.klseri.com.my/wp-content/uploads/2021/05/2021-05-10-015217938.jpg",
     "Power distribution, plus Biogas, Biomass & Solar interconnection",
     "Pengagihan kuasa, serta interkoneksi Biogas, Biojisim & Suria"),
    ("Projects", "Projek Utama", "projects.html", [
        ("Key Projects", "Projek Utama", "projects.html#key-projects"),
        ("Project Reference List", "Senarai Rujukan Projek", "projects.html#reference-list"),
    ], "https://www.klseri.com.my/wp-content/uploads/2021/03/sustainable_growth_istock.jpg",
     "Top Glove, Sime Darby, Telekom Malaysia & more",
     "Top Glove, Sime Darby, Telekom Malaysia & banyak lagi"),
    ("Certifications", "Pensijilan & Lesen", "certifications.html", [],
     "https://www.klseri.com.my/wp-content/uploads/2021/03/light-bulb-placed-on-soil-in-sun-light.jpg",
     "Class A, CIDB G7 credentials",
     "Kelayakan Kelas A, CIDB G7"),
    ("Careers", "Kerjaya", "careers.html", [],
     "https://www.klseri.com.my/wp-content/uploads/2021/04/KLS-01.png",
     "Join a young, dynamic technical team",
     "Sertai pasukan teknikal yang muda dan dinamik"),
    ("Contact", "Hubungi", "contact.html", [],
     "https://www.klseri.com.my/wp-content/uploads/2021/05/2021-05-10-015217938.jpg",
     "Port Klang HQ, plus Sabah & Sarawak branches",
     "Ibu pejabat Port Klang, serta cawangan Sabah & Sarawak"),
]

# ---------------------------------------------------------------------------
# Address / map helpers, real addresses only, no invented coordinates.
# Branch offices are geocoded live by Google from the text address; HQ keeps
# its previously-verified lat/lng (from the site's own Waze link).
# ---------------------------------------------------------------------------
ADDR_HQ = "Lot 10814, Jalan Petai, Pandamaran, 42000 Port Klang, Selangor"
ADDR_BRANCH1 = "Jalan Sahabat 16, Kompleks Bandar Sahabat, 91129 Lahad Datu, Sabah"
ADDR_BRANCH2 = "Parkcity Commerce Square, Jalan Tun Ahmad Zaidi, 97008 Bintulu, Sarawak"

def maps_search_url(address):
    return f"https://www.google.com/maps/search/?api=1&query={quote_plus(address)}"

def maps_embed_url(address):
    return f"https://www.google.com/maps?q={quote_plus(address)}&output=embed"

MAPS_HQ_SEARCH = "https://goo.gl/maps/w63mLVHk7L5xaHny7"
MAPS_HQ_EMBED = "https://www.google.com/maps?q=3.0133032185130992,101.41885042190553&output=embed"
MAPS_BRANCH1_SEARCH = maps_search_url(ADDR_BRANCH1)
MAPS_BRANCH1_EMBED = maps_embed_url(ADDR_BRANCH1)
MAPS_BRANCH2_SEARCH = maps_search_url(ADDR_BRANCH2)
MAPS_BRANCH2_EMBED = maps_embed_url(ADDR_BRANCH2)
WAZE_HQ = "https://www.waze.com/en-GB/live-map/directions?latlng=3.0133032185130992%2C101.41885042190553"

WHATSAPP_NUMBER = "60196203780"  # +6019 620 3780, as published on klseri.com.my
WHATSAPP_TEXT_EN = quote_plus("Hi KLS, I'd like to enquire about your services.")
WHATSAPP_TEXT_MS = quote_plus("Hai KLS, saya ingin bertanya tentang perkhidmatan anda.")

def whatsapp_url(lang):
    text = WHATSAPP_TEXT_MS if lang == "ms" else WHATSAPP_TEXT_EN
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={text}"

# ---------------------------------------------------------------------------
# Language-toggle flag icons (simplified but recognisable, inline SVG)
# ---------------------------------------------------------------------------
FLAG_GB = """<svg viewBox="0 0 28 20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <rect width="28" height="20" fill="#00247D"/>
  <path d="M0,0 L28,20 M28,0 L0,20" stroke="#fff" stroke-width="4"/>
  <path d="M0,0 L12,8.6 M28,0 L16,8.6 M0,20 L12,11.4 M28,20 L16,11.4" stroke="#CF142B" stroke-width="1.6"/>
  <rect x="11" width="6" height="20" fill="#fff"/>
  <rect y="7" width="28" height="6" fill="#fff"/>
  <rect x="12.5" width="3" height="20" fill="#CF142B"/>
  <rect y="8.5" width="28" height="3" fill="#CF142B"/>
</svg>"""

FLAG_MY = """<svg viewBox="0 0 28 20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <rect width="28" height="20" fill="#fff"/>
  <rect y="0" width="28" height="1.43" fill="#CC0001"/>
  <rect y="2.86" width="28" height="1.43" fill="#CC0001"/>
  <rect y="5.71" width="28" height="1.43" fill="#CC0001"/>
  <rect y="8.57" width="28" height="1.43" fill="#CC0001"/>
  <rect y="11.43" width="28" height="1.43" fill="#CC0001"/>
  <rect y="14.29" width="28" height="1.43" fill="#CC0001"/>
  <rect y="17.14" width="28" height="1.43" fill="#CC0001"/>
  <rect x="0" y="0" width="14" height="10" fill="#010066"/>
  <circle cx="7" cy="5" r="4" fill="#FFCC00"/>
  <circle cx="8.6" cy="5" r="4" fill="#010066"/>
  <polygon points="10.6,2 11.15,3.55 12.8,3.55 11.45,4.55 11.95,6.1 10.6,5.15 9.25,6.1 9.75,4.55 8.4,3.55 10.05,3.55" fill="#FFCC00"/>
</svg>"""

# ---------------------------------------------------------------------------
# Template builders
# ---------------------------------------------------------------------------
def nav_overlay_items(lang):
    out = []
    for i, (en, ms, href, sub, img, cap_en, cap_ms) in enumerate(NAV_ITEMS, start=1):
        label = ms if lang == "ms" else en
        caption = cap_ms if lang == "ms" else cap_en
        sub_html = ""
        if sub:
            links = "".join(f'<a href="{h}">{ms_s if lang == "ms" else en_s}</a>' for en_s, ms_s, h in sub)
            sub_html = f'<div class="nav-overlay-sub">{links}</div>'
        out.append(
            f'<li class="nav-overlay-item" data-nav-preview="{img}" data-nav-caption="{caption}">'
            f'<a class="nav-overlay-row" href="{href}" data-nav-link>'
            f'<span class="idx">{i:02d}</span><span class="label">{label}</span>'
            f'</a>{sub_html}</li>'
        )
    return "\n".join(out)

def nav_bg_images():
    seen, out = [], []
    for en, ms, href, sub, img, cap_en, cap_ms in NAV_ITEMS:
        if img in seen:
            continue
        seen.append(img)
        out.append(f'<img src="{img}" alt="" data-preview-src="{img}">')
    return "\n".join(out)

def head(title, description, canonical, extra_schema="", lang="en", asset_prefix="", alt_url=None):
    html_lang = "ms" if lang == "ms" else "en"
    canonical_prefix = "ms/" if lang == "ms" else ""
    alt_links = ""
    if alt_url:
        other_hreflang = "en" if lang == "ms" else "ms"
        alt_links = f'<link rel="alternate" hreflang="{other_hreflang}" href="{alt_url}">\n'
    return f"""<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://www.klseri.com.my/{canonical_prefix}{canonical}">
{alt_links}<meta property="og:type" content="website">
<meta property="og:site_name" content="KLS">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="{asset_prefix}assets/img/logo/kls-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{asset_prefix}assets/css/style.css">
{extra_schema}
</head>
"""

def header_html(lang, asset_prefix, page_file):
    t = UI[lang]
    switch_href = f"ms/{page_file}" if lang == "en" else f"../{page_file}"
    current_flag = FLAG_GB if lang == "en" else FLAG_MY
    toggle_label = "Switch to Bahasa Malaysia" if lang == "en" else "Tukar ke Bahasa Inggeris"
    return f"""<header class="site-header">
  <div class="container">
    <a href="index.html" class="brand" aria-label="KLS home">
      <img class="brand-mark" src="{asset_prefix}assets/img/logo/kls-icon.png" alt="" aria-hidden="true">
      <span class="brand-text"><strong>KLS</strong><span>Kejuruteraan Letrik Seri (M) Sdn Bhd</span></span>
    </a>
    <div class="nav-cta">
      <a href="{switch_href}" class="lang-toggle" aria-label="{toggle_label}" title="{toggle_label}">{current_flag}</a>
      <a href="contact.html" class="btn btn-outline">{t['contact_us']}</a>
      <button class="menu-trigger" data-menu-toggle aria-haspopup="dialog" aria-expanded="false">
        <span class="bars" aria-hidden="true"><span></span><span></span><span></span></span>
        {t['menu']}
      </button>
    </div>
  </div>
</header>

<div class="nav-overlay-backdrop" data-nav-backdrop></div>
<div class="nav-overlay" data-nav-overlay role="dialog" aria-modal="true" aria-label="{t['nav_dialog_label']}">
  <div class="nav-overlay-bg" aria-hidden="true">
    {nav_bg_images()}
  </div>
  <div class="nav-overlay-head">
    <span class="brand-text"><strong style="font-family:var(--font-display);color:var(--brand-900);">{t['kls_navigation']}</strong></span>
    <button class="close-btn" data-nav-close aria-label="{t['close_menu']}">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M6 6l12 12M18 6L6 18"/></svg>
    </button>
  </div>
  <div class="nav-overlay-body">
    <nav aria-label="Primary"><ul class="nav-overlay-links">
      {nav_overlay_items(lang)}
    </ul></nav>
  </div>
  <div class="nav-overlay-foot">
    <span>{ADDR_HQ}</span>
    <span>info@klseri.com.my &middot; +603 3167 1818</span>
  </div>
</div>
"""

SCROLL_PROGRESS = '<div class="scroll-progress" data-scroll-progress></div>\n'

def footer_html(lang, asset_prefix):
    t = UI[lang]
    nav_links = "".join(f'<li><a href="{href}">{label}</a></li>' for label, href in t["footer_links"])
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="{asset_prefix}assets/img/logo/kls-logo-wide.png" alt="Kejuruteraan Letrik Seri (M) Sdn Bhd" style="height:42px;width:auto;">
        <p>{t['footer_desc']}</p>
      </div>
      <div>
        <h5>{t['footer_nav']}</h5>
        <ul>{nav_links}</ul>
      </div>
      <div>
        <h5>{t['footer_hq']}</h5>
        <p><a href="{MAPS_HQ_SEARCH}" target="_blank" rel="noopener">Lot 10814, Jalan Petai, Pandamaran,<br>42000 Port Klang, Selangor</a></p>
        <h5 style="margin-top:22px;">{t['footer_branches']}</h5>
        <p><a href="{MAPS_BRANCH1_SEARCH}" target="_blank" rel="noopener">Bengkel Felda Engineering Service Sdn. Bhd.<br>Jalan Sahabat 16, Kompleks Bandar Sahabat,<br>91129 Lahad Datu, Sabah</a></p>
        <p><a href="{MAPS_BRANCH2_SEARCH}" target="_blank" rel="noopener">No. 113, Lot 3399, 2nd Floor, Parkcity Commerce Square,<br>Jalan Tun Ahmad Zaidi, P.O. Box 90,<br>97008 Bintulu, Sarawak</a></p>
      </div>
      <div>
        <h5>{t['footer_contact']}</h5>
        <ul>
          <li><a href="tel:+60331671818">+603 3167 1818 / 1817</a></li>
          <li><a href="tel:+60331675204">Fax: +603 3167 5204</a></li>
          <li><a href="tel:+60196203780">+6019 620 3780</a></li>
          <li><a href="tel:+60192258667">+6019 225 8667</a></li>
          <li><a href="mailto:info@klseri.com.my">info@klseri.com.my</a></li>
        </ul>
        <h5 style="margin-top:22px;">{t['footer_find_us']}</h5>
        <ul>
          <li><a href="{MAPS_HQ_SEARCH}" target="_blank" rel="noopener">{t['google_maps']} &#8599;</a></li>
          <li><a href="{WAZE_HQ}" target="_blank" rel="noopener">{t['waze']} &#8599;</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> Kejuruteraan Letrik Seri (M) Sdn Bhd. {t['rights']}</span>
      <span>{t['incorporated_line']}</span>
    </div>
  </div>
</footer>

<a class="whatsapp-fab" href="{whatsapp_url(lang)}" target="_blank" rel="noopener" aria-label="{t['whatsapp_label']}">
  <span class="ping" aria-hidden="true"></span>
  <svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16.001 3C9.373 3 4 8.373 4 15c0 2.348.668 4.542 1.824 6.402L4 29l7.78-1.789A11.94 11.94 0 0 0 16.001 27C22.63 27 28 21.627 28 15S22.63 3 16.001 3Zm0 21.818a9.77 9.77 0 0 1-4.98-1.362l-.357-.213-4.62 1.062 1.08-4.518-.232-.365A9.77 9.77 0 0 1 5.182 15c0-5.973 4.846-10.818 10.819-10.818S26.818 9.027 26.818 15 21.973 24.818 16.001 24.818Zm5.6-8.09c-.307-.153-1.816-.897-2.098-1-.281-.102-.486-.153-.69.154-.205.307-.792 1-.972 1.205-.179.205-.358.23-.664.077-.307-.154-1.296-.478-2.47-1.524-.913-.814-1.529-1.82-1.708-2.127-.179-.307-.019-.473.135-.626.139-.138.307-.358.46-.537.154-.18.205-.307.307-.512.102-.205.051-.384-.026-.537-.077-.154-.69-1.665-.946-2.28-.249-.598-.502-.517-.69-.526l-.588-.01a1.13 1.13 0 0 0-.818.384c-.281.307-1.074 1.05-1.074 2.56s1.099 2.97 1.252 3.175c.154.205 2.163 3.303 5.24 4.632.732.316 1.303.505 1.748.646.734.234 1.402.201 1.931.122.589-.088 1.816-.742 2.072-1.46.256-.717.256-1.332.18-1.46-.078-.128-.283-.205-.59-.358Z"/></svg>
</a>

<button class="back-to-top" data-back-to-top aria-label="{t['back_to_top']}">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
</button>

<div class="modal-overlay" data-person-modal></div>
<div class="modal-overlay" data-cert-modal></div>
<div class="modal-overlay" data-list-modal></div>

<script>document.querySelector('[data-year]').textContent = new Date().getFullYear();</script>
<script src="{asset_prefix}assets/js/data.js"></script>
<script src="{asset_prefix}assets/js/main.js"></script>
"""

def breadcrumb(current, current_label, lang="en"):
    home_label = UI[lang]["breadcrumb_home"]
    return f"""<div class="container"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">{home_label}</a><span class="sep">/</span><span class="current">{current_label}</span></nav></div>"""

def page(filename, title, description, body, schema="", lang="en", alt_url=None):
    asset_prefix = "../" if lang == "ms" else ""
    out_dir = MS_DIR if lang == "ms" else OUT_DIR
    html = (
        head(title, description, filename, schema, lang=lang, asset_prefix=asset_prefix, alt_url=alt_url)
        + "<body>\n"
        + SCROLL_PROGRESS
        + header_html(lang, asset_prefix, filename)
        + "\n" + body + "\n"
        + footer_html(lang, asset_prefix)
        + "\n</body>\n</html>\n"
    )
    with open(os.path.join(out_dir, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", ("ms/" if lang == "ms" else "") + filename)

if __name__ == "__main__":
    print("Template engine ready. Run the pages_*.py (English) and ms_pages_*.py (Bahasa Malaysia) scripts to generate pages.")
