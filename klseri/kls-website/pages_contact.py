from build import page, breadcrumb

BODY = f"""
<section class="page-hero">
  <div class="container">
    <h1>Contact Us</h1>
    <p class="lead">Send us a message and our team will get back to you, or reach us directly using the details below.</p>
  </div>
</section>
{breadcrumb('contact.html','Contact')}

<section class="section">
  <div class="container grid grid-2" style="gap:48px;">
    <div class="card card-pad">
      <h3>Send us a message</h3>
      <p class="small" style="margin-top:-8px;margin-bottom:20px;">Fields marked <span style="color:var(--danger-600);">*</span> are required.</p>
      <form class="form-grid" data-contact-form novalidate>
        <div class="field">
          <label for="name">Full name <span class="req">*</span></label>
          <input type="text" id="name" name="name" autocomplete="name" required>
          <div class="field-error" role="alert"></div>
        </div>
        <div class="field">
          <label for="email">Email address <span class="req">*</span></label>
          <input type="email" id="email" name="email" autocomplete="email" required>
          <div class="field-error" role="alert"></div>
        </div>
        <div class="field">
          <label for="phone">Phone number</label>
          <input type="tel" id="phone" name="phone" autocomplete="tel" placeholder="+60 12-345 6789">
          <div class="field-error" role="alert"></div>
        </div>
        <div class="field">
          <label for="message">Message <span class="req">*</span></label>
          <textarea id="message" name="message" required></textarea>
          <div class="field-error" role="alert"></div>
        </div>
        <div>
          <button type="submit" class="btn btn-primary">Send message</button>
        </div>
        <div class="form-status" data-form-status role="status" aria-live="polite"></div>
      </form>
    </div>
    <div>
      <div class="card card-pad">
        <h4>Direct contact</h4>
        <ul style="margin-top:14px;">
          <li style="padding:8px 0;"><b>Telephone:</b> <a href="tel:+60331671818" style="color:var(--brand-700);">+603 3167 1818 / 1817</a></li>
          <li style="padding:8px 0;"><b>Fax:</b> +603 3167 5204</li>
          <li style="padding:8px 0;"><b>Mobile:</b> <a href="tel:+60196203780" style="color:var(--brand-700);">+6019 620 3780</a> / <a href="tel:+60192258667" style="color:var(--brand-700);">+6019 225 8667</a></li>
          <li style="padding:8px 0;"><b>Email:</b> <a href="mailto:info@klseri.com.my" style="color:var(--brand-700);">info@klseri.com.my</a></li>
        </ul>
      </div>
      <div class="card card-pad" style="margin-top:20px;">
        <h4>Headquarters &amp; branch offices</h4>
        <p class="small" style="margin-top:10px;">Port Klang, Selangor (HQ), plus branch offices in Lahad Datu, Sabah and Bintulu, Sarawak.</p>
        <a href="location.html" class="btn-ghost" style="margin-top:6px;">View maps &amp; addresses</a>
      </div>
    </div>
  </div>
</section>
"""

page(
    "contact.html",
    "Contact Us | KLS, Kejuruteraan Letrik Seri (M) Sdn Bhd",
    "Send KLS a message, or reach our team directly by phone or email. See our Port Klang headquarters and branch office locations on the Location page.",
    BODY,
    alt_url="https://www.klseri.com.my/ms/contact.html",
)
