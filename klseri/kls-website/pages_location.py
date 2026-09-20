from build import page, breadcrumb, MAPS_HQ_SEARCH, MAPS_HQ_EMBED, MAPS_BRANCH1_SEARCH, MAPS_BRANCH1_EMBED, MAPS_BRANCH2_SEARCH, MAPS_BRANCH2_EMBED, WAZE_HQ
from urllib.parse import quote_plus

WAZE_BRANCH1 = f"https://www.waze.com/ul?q={quote_plus('Jalan Sahabat 16, Kompleks Bandar Sahabat, 91129 Lahad Datu, Sabah')}&navigate=yes"
WAZE_BRANCH2 = f"https://www.waze.com/ul?q={quote_plus('Parkcity Commerce Square, Jalan Tun Ahmad Zaidi, 97008 Bintulu, Sarawak')}&navigate=yes"

BODY = f"""
<section class="page-hero">
  <div class="container">
    <h1>Our Locations</h1>
    <p class="lead">One headquarters in Port Klang, Selangor, plus branch offices in Sabah and Sarawak, covering both Peninsular and East Malaysia.</p>
  </div>
</section>
{breadcrumb('location.html','Location')}

<section class="section">
  <div class="container">
    <div class="grid grid-3">
      <div class="loc-card">
        <h4><span class="dot"></span>Headquarters</h4>
        <address>Lot 10814, Jalan Petai, Pandamaran,<br>42000 Port Klang, Selangor</address>
        <div class="loc-map"><iframe title="Map, KLS Headquarters, Port Klang" src="{MAPS_HQ_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
        <div class="loc-actions">
          <a href="{MAPS_HQ_SEARCH}" target="_blank" rel="noopener">Google Maps</a>
          <a href="{WAZE_HQ}" target="_blank" rel="noopener">Waze</a>
        </div>
      </div>
      <div class="loc-card">
        <h4><span class="dot"></span>Branch Office I</h4>
        <p class="small mono" style="margin-bottom:4px;">Bengkel Felda Engineering Service Sdn. Bhd.</p>
        <address>Jalan Sahabat 16, Kompleks Bandar Sahabat,<br>91129 Lahad Datu, Sabah</address>
        <div class="loc-map"><iframe title="Map, KLS Branch Office I, Lahad Datu" src="{MAPS_BRANCH1_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
        <div class="loc-actions">
          <a href="{MAPS_BRANCH1_SEARCH}" target="_blank" rel="noopener">Google Maps</a>
          <a href="{WAZE_BRANCH1}" target="_blank" rel="noopener">Waze</a>
        </div>
      </div>
      <div class="loc-card">
        <h4><span class="dot"></span>Branch Office II</h4>
        <address>No. 113, Lot 3399, 2nd Floor,<br>Parkcity Commerce Square, Jalan Tun Ahmad Zaidi,<br>P.O. Box 90, 97008 Bintulu, Sarawak</address>
        <div class="loc-map"><iframe title="Map, KLS Branch Office II, Bintulu" src="{MAPS_BRANCH2_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
        <div class="loc-actions">
          <a href="{MAPS_BRANCH2_SEARCH}" target="_blank" rel="noopener">Google Maps</a>
          <a href="{WAZE_BRANCH2}" target="_blank" rel="noopener">Waze</a>
        </div>
      </div>
    </div>
    <p class="small" style="margin-top:18px;">Maps for both branch offices are placed using Google's own geocoding of the published address, KLS hasn't published exact coordinates for these two locations.</p>
  </div>
</section>

<section class="section section--forest text-center">
  <div class="container">
    <h2>Have a project near one of our offices?</h2>
    <a href="contact.html" class="btn btn-primary">Get In Touch</a>
  </div>
</section>
"""

page(
    "location.html",
    "Our Locations | KLS, Kejuruteraan Letrik Seri (M) Sdn Bhd",
    "KLS's headquarters in Port Klang, Selangor, plus branch offices in Lahad Datu, Sabah and Bintulu, Sarawak.",
    BODY,
    alt_url="https://www.klseri.com.my/ms/location.html",
)
