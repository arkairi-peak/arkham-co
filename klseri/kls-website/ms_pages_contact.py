from build import page, breadcrumb

BODY = f"""
<section class="page-hero">
  <div class="container">
    <h1>Hubungi Kami</h1>
    <p class="lead">Hantar mesej kepada kami dan pasukan kami akan menghubungi anda, atau hubungi kami terus menggunakan butiran di bawah.</p>
  </div>
</section>
{breadcrumb('contact.html','Hubungi', lang='ms')}

<section class="section">
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
      <div class="card card-pad" style="margin-top:20px;">
        <h4>Ibu pejabat &amp; pejabat cawangan</h4>
        <p class="small" style="margin-top:10px;">Port Klang, Selangor (Ibu Pejabat), ditambah pejabat cawangan di Lahad Datu, Sabah dan Bintulu, Sarawak.</p>
        <a href="location.html" class="btn-ghost" style="margin-top:6px;">Lihat peta &amp; alamat</a>
      </div>
    </div>
  </div>
</section>
"""

page(
    "contact.html",
    "Hubungi Kami | KLS, Kejuruteraan Letrik Seri (M) Sdn Bhd",
    "Hantar mesej kepada KLS, atau hubungi pasukan kami terus melalui telefon atau e-mel. Lihat lokasi ibu pejabat dan pejabat cawangan kami di laman Lokasi.",
    BODY,
    lang="ms",
    alt_url="https://www.klseri.com.my/contact.html",
)
