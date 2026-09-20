from build import page, breadcrumb, MAPS_HQ_SEARCH, MAPS_HQ_EMBED, MAPS_BRANCH1_SEARCH, MAPS_BRANCH1_EMBED, MAPS_BRANCH2_SEARCH, MAPS_BRANCH2_EMBED, WAZE_HQ
from urllib.parse import quote_plus

WAZE_BRANCH1 = f"https://www.waze.com/ul?q={quote_plus('Jalan Sahabat 16, Kompleks Bandar Sahabat, 91129 Lahad Datu, Sabah')}&navigate=yes"
WAZE_BRANCH2 = f"https://www.waze.com/ul?q={quote_plus('Parkcity Commerce Square, Jalan Tun Ahmad Zaidi, 97008 Bintulu, Sarawak')}&navigate=yes"

BODY = f"""
<section class="page-hero">
  <div class="container">
    <h1>Lokasi Kami</h1>
    <p class="lead">Satu ibu pejabat di Port Klang, Selangor, ditambah pejabat cawangan di Sabah dan Sarawak, merangkumi Semenanjung dan Malaysia Timur.</p>
  </div>
</section>
{breadcrumb('location.html','Lokasi', lang='ms')}

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

<section class="section section--forest text-center">
  <div class="container">
    <h2>Ada projek berhampiran salah satu pejabat kami?</h2>
    <a href="contact.html" class="btn btn-primary">Hubungi Kami</a>
  </div>
</section>
"""

page(
    "location.html",
    "Lokasi Kami | KLS, Kejuruteraan Letrik Seri (M) Sdn Bhd",
    "Ibu pejabat KLS di Port Klang, Selangor, ditambah pejabat cawangan di Lahad Datu, Sabah dan Bintulu, Sarawak.",
    BODY,
    lang="ms",
    alt_url="https://www.klseri.com.my/location.html",
)
