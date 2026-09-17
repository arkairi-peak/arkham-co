from build import page, breadcrumb

BODY = f"""
<section class="page-hero">
  <div class="container">
    <h1>Careers at KLS</h1>
    <p class="lead">Work with a team of experts in electrical engineering and renewable energy interconnection.</p>
  </div>
</section>
{breadcrumb('careers.html','Careers')}

<section class="section">
  <div class="container grid grid-2" style="gap:48px;align-items:center;">
    <div>
      <div class="kicker">JOIN US</div>
      <h2>Careers at KLS</h2>
      <p class="lead">We provide you with exciting opportunities to work with a team of experts in the industry. Working at KLS means being full of energy to learn, innovate and collaborate with our team, partners, advisors and clients. We pursue excellence and continuous innovation to keep up with the latest technologies and stay ahead of our competition.</p>
      <p>We offer a range of exciting career opportunities for dedicated and talented people at all stages of the career journey. If you are interested in joining the company, send us your resume.</p>
      <a href="mailto:info@klseri.com.my?subject=Career%20Enquiry%20-%20KLS" class="btn btn-primary">Email your resume</a>
    </div>
    <div class="card card-pad">
      <h4>Currently open roles</h4>
      <p class="small" style="margin-top:10px;">KLS does not currently have specific vacancies listed on its website. Talented candidates at every career stage are still encouraged to reach out — resumes are reviewed on an ongoing basis.</p>
      <hr class="rule" style="margin:22px 0;">
      <h4>How to apply</h4>
      <p class="small" style="margin-top:10px;">Send your resume to <a href="mailto:info@klseri.com.my" style="color:var(--brand-700);font-weight:600;">info@klseri.com.my</a>, or use the contact form to reach our HQ in Port Klang, Selangor.</p>
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
    "KLS offers a range of career opportunities where you'll work with an innovative team of people and the latest electrical engineering and renewable energy technologies.",
    BODY,
    alt_url="https://www.klseri.com.my/ms/careers.html",
)
