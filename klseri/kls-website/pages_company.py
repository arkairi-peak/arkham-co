from build import page, breadcrumb

BODY = f"""
<section class="page-hero">
  <div class="container">
    <h1>Company Overview</h1>
    <p class="lead">Same company, same facts, same identity — four decades of electrical engineering and renewable energy interconnection work in Malaysia and beyond.</p>
  </div>
</section>
{breadcrumb('company-overview.html','Company Overview')}

<section class="section" id="we-are-kls">
  <div class="container grid grid-2" style="gap:56px;align-items:center;">
    <div>
      <div class="kicker">WE ARE KLS</div>
      <h2>Kejuruteraan Letrik Seri (M) Sdn Bhd</h2>
      <p class="lead">Kejuruteraan Letrik Seri (M) Sdn Bhd, also known as KLS, was incorporated in 1984, positioning ourselves as a master rewiring service provider. As we continued to grow, we diversified our services to providing supply, installation, testing, commissioning and warranty of High Voltage, Low Voltage and Extra Low Voltage electrical systems for residential, commercial, industrial, infrastructural and marine development.</p>
      <p>As one of the industry leaders in Malaysia, we embrace natural resources and recognise the need for sustainable development. We demonstrate our commitment by undertaking numerous Renewable Energy Interconnection contracts and initiatives encompassing Biogas, Biomass, Solar and Cogeneration Plants.</p>
    </div>
    <img src="https://www.klseri.com.my/wp-content/uploads/2021/05/2021-05-10-015217938.jpg" alt="KLS electrical engineering works" style="border-radius:10px;border:1px solid var(--line-300);">
  </div>
</section>

<section class="section section--band" id="our-story">
  <div class="container">
    <div class="section-head">
      <div class="kicker">OUR STORY</div>
      <h2>From a rewiring workshop to a regional M&amp;E contractor</h2>
      <p class="lead">Since our humble beginning in 1984, we have strived to provide quality work with an emphasis on client satisfaction. With over 30 years of experience, we have become one of the leading companies in the electrical engineering industry with numerous high-profile projects all over Malaysia.</p>
    </div>
    <div class="grid grid-2" style="gap:56px;">
      <div class="timeline">
        <div class="t-item">
          <div class="t-year">1984</div>
          <h4>Incorporated in Malaysia</h4>
          <p>KLS begins as a master rewiring service provider, growing out of a humble electrical motor wiring workshop.</p>
        </div>
        <div class="t-item">
          <div class="t-year">1984 — 2000s</div>
          <h4>Diversification &amp; specialisation</h4>
          <p>The company develops into an established Class A, CIDB G7 M&amp;E Contractor, gaining immense experience and professional specialisation that earned commendations from valued clients over three decades.</p>
        </div>
        <div class="t-item">
          <div class="t-year">2000</div>
          <h4>Expansion into East Malaysia</h4>
          <p>KLS expands its network by venturing into East Malaysia and opening a branch office in Lahad Datu, Sabah.</p>
        </div>
        <div class="t-item">
          <div class="t-year">Beyond Malaysia</div>
          <h4>Going global</h4>
          <p>Heeding the call for globalisation, KLS focuses beyond high-profile local projects and ventures out globally, securing international works in countries such as Indonesia, Papua New Guinea and Africa.</p>
        </div>
      </div>
      <div>
        <div class="card card-pad" style="background:var(--brand-800);color:#fff;border:0;">
          <img src="https://www.klseri.com.my/wp-content/uploads/2021/02/Icon-02.png" alt="" style="width:44px;filter:invert(1);margin-bottom:16px;">
          <h3 style="color:#fff;">Business Beyond Professionalism</h3>
          <p style="color:#DFF6E7;">At KLS, we deliver electrical and engineering solutions with excellent execution and responsibility. With every project undertaken, we provide solutions that endure and bring successful outcomes to their business. We aspire to exceed the expectations of our clients and showcase our commitment to excellence, accountability and professionalism.</p>
        </div>
        <div class="card card-pad" style="margin-top:24px;">
          <img src="https://www.klseri.com.my/wp-content/uploads/2021/02/Icon-01.png" alt="" style="width:44px;margin-bottom:16px;">
          <h3>Your Trusted Partner for Quality</h3>
          <p>At KLS, it is our technical expertise and understanding of the industry that makes us the trusted partner for quality-conscious companies in the nation. In line with our principles, we strive to provide electrical engineering solutions of the highest standards of quality to our valued clients. Our strong relationship with our clients is a testament to our quality work and solid reputation.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="mission-vision">
  <div class="container grid grid-2" style="gap:32px;">
    <div class="card card-pad">
      <div class="kicker">MISSION</div>
      <h3>Our Missions</h3>
      <ul class="svc-list" style="margin-top:16px;">
        <li>To deliver solutions and services that meet international standards.</li>
        <li>To provide excellent management of projects and quality workforce.</li>
        <li>To exceed customer expectations with exceptional expertise and performance.</li>
        <li>To deliver cost-efficient and quality electrical engineering services.</li>
      </ul>
    </div>
    <div class="card card-pad" style="background:var(--brand-800);color:#fff;border:0;">
      <div class="kicker" style="color:var(--amber-500);">VISION</div>
      <h3 style="color:#fff;">Our Vision</h3>
      <p style="color:#E9FBEF;font-size:1.08rem;margin-top:16px;">To be the engineering solution provider of choice in South East Asia (SEA) by delivering the best-in-class solution to our customers for them to succeed.</p>
    </div>
  </div>
</section>

<section class="section section--band" id="core-values">
  <div class="container">
    <div class="section-head">
      <div class="kicker">OUR CORE VALUES</div>
      <h2>What governs our people and our business</h2>
      <p class="lead">As a prominent company in the industry, we adhere to our core values as it governs our people and our business operations. These principles enable us to establish lasting and valuable relationships with clients as we deliver excellent solutions and services to help achieve their business goals.</p>
    </div>
    <div class="spec-list">
      <div class="value-row"><span class="idx mono">01</span><div><h4>Excellent Quality</h4><p>Our standards are unwavering. We ensure that quality is at the core of our work, management and entire company itself.</p></div></div>
      <div class="value-row"><span class="idx mono">02</span><div><h4>Innovation</h4><p>We strive to continually innovate and educate ourselves to keep up with state-of-the-art technology and the dynamic landscape of the industry.</p></div></div>
      <div class="value-row"><span class="idx mono">03</span><div><h4>Teamwork</h4><p>We build and foster connections between our people. Our culture is based on mutual respect and harmony between the management and technical departments.</p></div></div>
      <div class="value-row"><span class="idx mono">04</span><div><h4>Adaptability</h4><p>We adapt and embrace change as part and parcel of the business — resilient and steadfast against the ever-changing financial and economic situations in the world.</p></div></div>
      <div class="value-row"><span class="idx mono">05</span><div><h4>Professionalism</h4><p>We are consistent and reliable. Our team delivers quality infrastructure and services that exceed expectations in preparation, planning, design, implementation, testing and delivery.</p></div></div>
      <div class="value-row"><span class="idx mono">06</span><div><h4>Customer Satisfaction</h4><p>We provide continuous guarantee and excellent after-delivery services such as maintenance for all our projects, striving for 100% client satisfaction.</p></div></div>
    </div>
  </div>
</section>

<section class="section" id="key-clients">
  <div class="container">
    <div class="section-head">
      <div class="kicker">KEY CLIENTS</div>
      <h2>Organisations we work with</h2>
    </div>
    <div class="logo-strip" data-key-clients></div>
  </div>
</section>

<section class="section section--band" id="partners-suppliers">
  <div class="container">
    <div class="section-head">
      <div class="kicker">PARTNERS &amp; SUPPLIERS</div>
      <h2>Our partners &amp; suppliers</h2>
    </div>
    <div class="logo-strip" data-partners></div>
  </div>
</section>

<section class="section" id="advisors-consultants">
  <div class="container">
    <div class="section-head">
      <div class="kicker">ADVISORS &amp; CONSULTANTS</div>
      <h2>Our advisors &amp; consultants</h2>
    </div>
    <div class="logo-strip" data-advisors></div>
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
    "Company Overview | KLS — Kejuruteraan Letrik Seri (M) Sdn Bhd",
    "KLS embraces sustainable development and undertakes Renewable Energy Interconnection contracts, as well as electrical power offerings, since 1984.",
    BODY,
    alt_url="https://www.klseri.com.my/ms/company-overview.html",
)
