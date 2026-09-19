from build import page, breadcrumb

BODY = f"""
<section class="page-hero">
  <div class="container">
    <h1>Company Overview</h1>
    <p class="lead">One company, one set of facts, one identity, and roughly forty years of hands-on electrical engineering and renewable energy interconnection work across Malaysia and further afield.</p>
  </div>
</section>
{breadcrumb('company-overview.html','Company Overview')}

<section class="section" id="we-are-kls">
  <div class="container grid grid-2" style="gap:56px;align-items:center;">
    <div>
      <div class="kicker">We Are KLS</div>
      <h2>Kejuruteraan Letrik Seri (M) Sdn Bhd</h2>
      <p class="lead">Kejuruteraan Letrik Seri (M) Sdn Bhd, known to most simply as KLS, was incorporated in 1984 and began life as a master rewiring service provider. Growth brought a wider remit: today we supply, install, test, commission and warranty High Voltage, Low Voltage and Extra Low Voltage electrical systems across residential, commercial, industrial, infrastructure and marine developments.</p>
      <p>As one of Malaysia's established names in the field, we take the country's natural resources and the case for sustainable development seriously, and back that up with real work: a long line of Renewable Energy Interconnection contracts spanning Biogas, Biomass, Solar and Cogeneration plants.</p>
    </div>
    <img src="https://www.klseri.com.my/wp-content/uploads/2021/05/2021-05-10-015217938.jpg" alt="KLS electrical engineering works" style="border-radius:10px;border:1px solid var(--line-300);">
  </div>
  <div class="container" style="margin-top:44px;">
    <div class="stat-band">
      <div class="stat-item"><b>1984</b><span>Year incorporated</span></div>
      <div class="stat-item"><b>Class A</b><span>CIDB G7 M&amp;E Contractor</span></div>
      <div class="stat-item"><b>HV &middot; LV &middot; ELV</b><span>Electrical systems supplied, installed &amp; commissioned</span></div>
      <div class="stat-item"><b>5</b><span>Development sectors served</span></div>
    </div>
  </div>
</section>

<section class="section section--band" id="our-story">
  <div class="container">
    <div class="section-head">
      <div class="kicker">How We Got Here</div>
      <h2>From a small rewiring outfit to a regional M&amp;E contractor</h2>
      <p class="lead">We've kept one thing constant since 1984: doing the work properly and keeping clients satisfied. Three decades on, that approach has carried us to a leading position in Malaysia's electrical engineering industry, with a long list of high-profile projects to show for it.</p>
    </div>
    <div class="timeline">
      <div class="t-item">
        <div class="t-year">1984</div>
        <h4>Incorporated in Malaysia</h4>
        <p>KLS starts out as a master rewiring service provider, having grown from a small electrical motor wiring workshop.</p>
      </div>
      <div class="t-item">
        <div class="t-year">1984-2000s</div>
        <h4>Growth and specialisation</h4>
        <p>Over three decades, the company builds into an established Class A, CIDB G7 M&amp;E Contractor, picking up deep experience and technical specialisation along the way, along with steady commendation from the clients it serves.</p>
      </div>
      <div class="t-item">
        <div class="t-year">2000</div>
        <h4>Reaching East Malaysia</h4>
        <p>KLS extends its reach into East Malaysia, opening a branch office in Lahad Datu, Sabah.</p>
      </div>
      <div class="t-item">
        <div class="t-year">Beyond Malaysia</div>
        <h4>Looking outward</h4>
        <p>KLS looks past its local, high-profile project base and takes on international work, securing contracts in countries including Indonesia, Papua New Guinea and Africa.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="philosophy">
  <div class="container">
    <div class="section-head">
      <div class="kicker">How We Work</div>
      <h2>What guides the work day to day</h2>
    </div>
    <div class="grid grid-2" style="gap:24px;">
      <div class="card card-pad" style="background:var(--brand-800);color:#fff;border:0;">
        <img src="https://www.klseri.com.my/wp-content/uploads/2021/02/Icon-02.png" alt="" style="width:44px;filter:invert(1);margin-bottom:16px;">
        <h3 style="color:#fff;">Business Beyond Professionalism</h3>
        <p style="color:#DFF6E7;">We deliver every electrical and engineering solution with careful execution and a real sense of responsibility for the outcome. Each project is built to last and to serve the client's business well after handover. We aim to go beyond what's expected, backed by a genuine commitment to excellence, accountability and professionalism.</p>
      </div>
      <div class="card card-pad">
        <img src="https://www.klseri.com.my/wp-content/uploads/2021/02/Icon-01.png" alt="" style="width:44px;margin-bottom:16px;">
        <h3>Your Trusted Partner for Quality</h3>
        <p>It's our technical expertise and grasp of the industry that has made us a trusted partner for quality-conscious companies across the country. We hold our own work to the highest standard we can, and the relationships we've built with clients over the years reflect that, a direct result of consistent, quality work and a reputation earned rather than claimed.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--band" id="mission-vision">
  <div class="container grid grid-2" style="gap:32px;">
    <div class="card card-pad">
      <div class="kicker">Mission</div>
      <h3>Our Missions</h3>
      <ul class="svc-list" style="margin-top:16px;">
        <li>Deliver solutions and services that hold up to international standards.</li>
        <li>Run projects well, with a workforce we can stand behind.</li>
        <li>Go beyond what customers expect, through real expertise and performance.</li>
        <li>Keep electrical engineering services cost-efficient without cutting corners on quality.</li>
      </ul>
    </div>
    <div class="card card-pad" style="background:var(--brand-800);color:#fff;border:0;">
      <div class="kicker" style="background:rgba(255,255,255,.16);border-color:rgba(255,255,255,.3);color:#fff;">Vision</div>
      <h3 style="color:#fff;">Our Vision</h3>
      <p style="color:#E9FBEF;font-size:1.08rem;margin-top:16px;">To become the engineering solution provider South East Asia (SEA) turns to first, by giving customers the best-in-class solutions they need to succeed.</p>
    </div>
  </div>
</section>

<section class="section" id="core-values">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Our Core Values</div>
      <h2>What shapes our people and our business</h2>
      <p class="lead">As a company with a reputation to keep, we hold ourselves to a set of core values that shape both our people and how we run the business. They're what let us build lasting, worthwhile relationships with clients while helping them get where they're trying to go.</p>
    </div>
    <div class="spec-list">
      <div class="value-row"><span class="idx mono">01</span><div><h4>Excellent Quality</h4><p>Our standards don't bend. Quality sits at the center of how we work, how we manage projects, and how we run the company as a whole.</p></div></div>
      <div class="value-row"><span class="idx mono">02</span><div><h4>Innovation</h4><p>We keep learning and keep pushing forward, staying current with the latest technology and the industry's shifting demands.</p></div></div>
      <div class="value-row"><span class="idx mono">03</span><div><h4>Teamwork</h4><p>We invest in the relationships between our people. Our culture runs on mutual respect and cooperation between management and the technical teams on the ground.</p></div></div>
      <div class="value-row"><span class="idx mono">04</span><div><h4>Adaptability</h4><p>Change is part of doing business, and we treat it that way, staying resilient through shifting financial and economic conditions rather than being thrown by them.</p></div></div>
      <div class="value-row"><span class="idx mono">05</span><div><h4>Professionalism</h4><p>We're consistent and dependable. From preparation and planning through design, execution, testing and final delivery, our team holds itself to a standard that exceeds what's expected.</p></div></div>
      <div class="value-row"><span class="idx mono">06</span><div><h4>Customer Satisfaction</h4><p>Our commitment doesn't end at handover. We back every project with ongoing guarantees and after-delivery support, including maintenance, with full client satisfaction as the goal.</p></div></div>
    </div>
  </div>
</section>

<section class="section section--band" id="key-clients">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Key Clients</div>
      <h2>Organisations we work with</h2>
    </div>
    <div data-key-clients></div>
  </div>
</section>

<section class="section" id="partners-suppliers">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Partners &amp; Suppliers</div>
      <h2>Our partners &amp; suppliers</h2>
    </div>
    <div data-partners></div>
  </div>
</section>

<section class="section section--band" id="advisors-consultants">
  <div class="container">
    <div class="section-head">
      <div class="kicker">Advisors &amp; Consultants</div>
      <h2>Our advisors &amp; consultants</h2>
    </div>
    <div data-advisors></div>
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
    "company-overview.html",
    "Company Overview | KLS, Kejuruteraan Letrik Seri (M) Sdn Bhd",
    "KLS has backed sustainable development with real Renewable Energy Interconnection contracts, alongside its core electrical power work, since 1984.",
    BODY,
    alt_url="https://www.klseri.com.my/ms/company-overview.html",
)
