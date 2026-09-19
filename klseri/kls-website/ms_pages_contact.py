from build import page, breadcrumb, MAPS_HQ_SEARCH, MAPS_HQ_EMBED, MAPS_BRANCH1_SEARCH, MAPS_BRANCH1_EMBED, MAPS_BRANCH2_SEARCH, MAPS_BRANCH2_EMBED, WAZE_HQ
from urllib.parse import quote_plus

WAZE_BRANCH1 = f"https://www.waze.com/ul?q={quote_plus('Jalan Sahabat 16, Kompleks Bandar Sahabat, 91129 Lahad Datu, Sabah')}&navigate=yes"
WAZE_BRANCH2 = f"https://www.waze.com/ul?q={quote_plus('Parkcity Commerce Square, Jalan Tun Ahmad Zaidi, 97008 Bintulu, Sarawak')}&navigate=yes"

BODY = f"""
<section class="page-hero">
  <div class="container">
    <h1>Hubungi Kami</h1>
    <p class="lead">Cari kami di ibu pejabat Port Klang, Selangor, atau di pejabat cawangan kami di Sabah dan Sarawak.</p>
  </div>
</section>
{breadcrumb('contact.html','Hubungi', lang='ms')}

<section class="section">
  <div class="container">
    <div class="grid grid-3">
      <div class="loc-card">
        <h4><span class="dot"></span>Ibu Pejabat</h4>
        <address>Lot 10814, Jalan Petai, Pandamaran,<br>42000 Port Klang, Selangor</address>
        <div class="loc-map"><iframe title="Peta, Ibu Pejabat KLS, Port Klang" src="{MAPS_HQ_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
        <div class="loc-actions">
          <a href="{MAPS_HQ_SEARCH}" target="_blank" rel="noopener">Google Maps</a>
          <a href="{WAZE_HQ}" target="_blank" rel="noopener">Waze</a>
        </div>
      </div>
      <div class="loc-card">
        <h4><span class="dot"></span>Pejabat Cawangan I</h4>
        <p class="small mono" style="margin-bottom:4px;">Bengkel Felda Engineering Service Sdn. Bhd.</p>
        <address>Jalan Sahabat 16, Kompleks Bandar Sahabat,<br>91129 Lahad Datu, Sabah</address>
        <div class="loc-map"><iframe title="Peta, Pejabat Cawangan I KLS, Lahad Datu" src="{MAPS_BRANCH1_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
        <div class="loc-actions">
          <a href="{MAPS_BRANCH1_SEARCH}" target="_blank" rel="noopener">Google Maps</a>
          <a href="{WAZE_BRANCH1}" target="_blank" rel="noopener">Waze</a>
        </div>
      </div>
      <div class="loc-card">
        <h4><span class="dot"></span>Pejabat Cawangan II</h4>
        <address>No. 113, Lot 3399, Tingkat 2,<br>Parkcity Commerce Square, Jalan Tun Ahmad Zaidi,<br>P.O. Box 90, 97008 Bintulu, Sarawak</address>
        <div class="loc-map"><iframe title="Peta, Pejabat Cawangan II KLS, Bintulu" src="{MAPS_BRANCH2_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
        <div class="loc-actions">
          <a href="{MAPS_BRANCH2_SEARCH}" target="_blank" rel="noopener">Google Maps</a>
          <a href="{WAZE_BRANCH2}" target="_blank" rel="noopener">Waze</a>
        </div>
      </div>
    </div>
    <p class="small" style="margin-top:18px;">Peta bagi kedua-dua pejabat cawangan diletakkan menggunakan sistem geokod Google sendiri berdasarkan alamat yang diterbitkan, KLS belum menerbitkan koordinat tepat untuk kedua-dua lokasi ini.</p>
  </div>
</section>

<section class="section section--band">
  <div class="container grid grid-2" style="gap:48px;">
    <div class="card card-pad">
      <h3>Hantar mesej kepada kami</h3>
      <p class="small" style="margin-top:-8px;margin-bottom:20px;">Ruangan bertanda <span style="color:var(--danger-600);">*</span> wajib diisi.</p>
      <form class="form-grid" data-contact-form novalidate>
        <div class="field">
          <label for="name">Nama penuh <span class="req">*</span></label>
          <input type="text" id="name" name="name" autocomplete="name" required>
          <div class="field-error" role="alert"></div>
        </div>
        <div class="field">
          <label for="email">Alamat e-mel <span class="req">*</span></label>
          <input type="email" id="email" name="email" autocomplete="email" required>
          <div class="field-error" role="alert"></div>
        </div>
        <div class="field">
          <label for="phone">Nombor telefon</label>
          <input type="tel" id="phone" name="phone" autocomplete="tel" placeholder="+60 12-345 6789">
          <div class="field-error" role="alert"></div>
        </div>
        <div class="field">
          <label for="message">Mesej <span class="req">*</span></label>
          <textarea id="message" name="message" required></textarea>
          <div class="field-error" role="alert"></div>
        </div>
        <div>
          <button type="submit" class="btn btn-primary">Hantar mesej</button>
        </div>
        <div class="form-status" data-form-status role="status" aria-live="polite"></div>
      </form>
    </div>
    <div>
      <div class="card card-pad">
        <h4>Hubungan terus</h4>
        <ul style="margin-top:14px;">
          <li style="padding:8px 0;"><b>Telefon:</b> <a href="tel:+60331671818" style="color:var(--brand-700);">+603 3167 1818 / 1817</a></li>
          <li style="padding:8px 0;"><b>Faks:</b> +603 3167 5204</li>
          <li style="padding:8px 0;"><b>Mudah alih:</b> <a href="tel:+60196203780" style="color:var(--brand-700);">+6019 620 3780</a> / <a href="tel:+60192258667" style="color:var(--brand-700);">+6019 225 8667</a></li>
          <li style="padding:8px 0;"><b>E-mel:</b> <a href="mailto:info@klseri.com.my" style="color:var(--brand-700);">info@klseri.com.my</a></li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

page(
    "contact.html",
    "Hubungi Kami | KLS, Kejuruteraan Letrik Seri (M) Sdn Bhd",
    "Cari KLS di ibu pejabat Port Klang kami, atau di pejabat cawangan kami di Lahad Datu, Sabah dan Bintulu, Sarawak.",
    BODY,
    lang="ms",
    alt_url="https://www.klseri.com.my/contact.html",
)
