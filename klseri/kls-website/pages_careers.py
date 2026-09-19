from build import page, breadcrumb

BODY = f"""
<section class="page-hero" style="--panel-img:url('https://www.klseri.com.my/wp-content/uploads/2021/04/KLS-01.png')">
  <div class="container">
    <h1>Careers at KLS</h1>
    <p class="lead">Join a team of specialists working across electrical engineering and renewable energy interconnection.</p>
  </div>
</section>
{breadcrumb('careers.html','Careers')}

<section class="section">
  <div class="container grid grid-2" style="gap:48px;align-items:center;">
    <div>
      <div class="kicker">Join Us</div>
      <h2>Careers at KLS</h2>
      <p class="lead">There's real opportunity here to work alongside experienced people in the industry. At KLS, that means staying energised, learning, innovating, and collaborating closely with our team, partners, advisors and clients. We chase excellence and keep innovating so we stay ahead of the curve on technology and the competition alike.</p>
      <p>We look for dedicated, talented people at every stage of their career, and back that with genuine opportunity. Interested in joining us? Send through your resume.</p>
      <a href="mailto:info@klseri.com.my?subject=Career%20Enquiry%20-%20KLS" class="btn btn-primary">Email your resume</a>
    </div>
    <div class="card card-pad">
      <h4>Currently open roles</h4>
      <p class="small" style="margin-top:10px;">There are no specific vacancies listed on this site right now, but talented candidates at any career stage are still welcome to get in touch. Resumes are reviewed on an ongoing basis.</p>
      <hr class="rule" style="margin:22px 0;">
      <h4>How to apply</h4>
      <p class="small" style="margin-top:10px;">Send your resume to <a href="mailto:info@klseri.com.my" style="color:var(--brand-700);font-weight:600;">info@klseri.com.my</a>, or reach our Port Klang, Selangor HQ through the contact form.</p>
      <a href="contact.html" class="btn-ghost" style="margin-top:6px;">Go to Contact page</a>
    </div>
  </div>
</section>

<section class="section section--forest text-center">
  <div class="container">
    <h2>Get In Touch with Us</h2>
    <a href="contact.html" class="btn btn-primary">Contact Us</a>
  </div>
</section>
"""

page(
    "careers.html",
    "Careers | Join the KLS Team",
    "KLS offers career opportunities alongside an innovative team, working with current electrical engineering and renewable energy technology.",
    BODY,
    alt_url="https://www.klseri.com.my/ms/careers.html",
)
