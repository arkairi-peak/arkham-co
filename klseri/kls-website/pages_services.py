from build import page, breadcrumb

BODY = f"""
<section class="page-hero">
  <div class="container">
    <h1>Our Services</h1>
    <p class="lead">Years of hands-on industry experience sit behind everything we deliver, quality services, products and work that help our clients reach their business goals. That covers supply, installation, testing and commissioning across:</p>
  </div>
</section>
{breadcrumb('services.html','Our Services')}

<section class="section" id="electrical-power-distribution">
  <div class="container">
    <div class="section-head">
      <div class="kicker">01 &middot; Electrical Power Distribution Systems</div>
      <h2>Electrical Power Distribution Systems</h2>
    </div>
    <div class="spec-list">
      <div class="spec-row">
        <span class="num mono">A</span>
        <div>
          <h4>Core Power Systems</h4>
          <ul class="svc-list">
            <li>Medium/High Voltage Power System</li>
            <li>Low Voltage Power System</li>
            <li>AMF Board and EMSB</li>
            <li>Motor Control Centre (MCC)</li>
            <li>Power transformers</li>
            <li>LV Power cabling</li>
            <li>MV Power cabling</li>
            <li>Cable support systems</li>
            <li>Diesel Generator System</li>
          </ul>
        </div>
      </div>
      <div class="spec-row">
        <span class="num mono">B</span>
        <div>
          <h4>Control, Instrumentation &amp; Lighting</h4>
          <ul class="svc-list">
            <li>Control and Instrumentation system &amp; cablings (control cables, instrument cables)</li>
            <li>Lighting and small power points &amp; fittings</li>
            <li>Explosion-proof lighting and power system</li>
          </ul>
        </div>
      </div>
      <div class="spec-row">
        <span class="num mono">C</span>
        <div>
          <h4>Telecommunications &amp; ICT</h4>
          <ul class="svc-list">
            <li>Telecommunication internal &amp; infrastructure works</li>
            <li>ICT solutions and data networking</li>
          </ul>
        </div>
      </div>
      <div class="spec-row">
        <span class="num mono">D</span>
        <div>
          <h4>Building Systems</h4>
          <ul class="svc-list">
            <li>HVAC / Ventilation systems</li>
            <li>Building Automation System and SCADA</li>
          </ul>
        </div>
      </div>
      <div class="spec-row">
        <span class="num mono">E</span>
        <div>
          <h4>Security &amp; AV</h4>
          <ul class="svc-list">
            <li>CCTV system</li>
            <li>SMATV</li>
            <li>AV and PA System</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--forest" id="renewable-energy" style="--panel-img:url('https://www.klseri.com.my/wp-content/uploads/2021/03/light-bulb-placed-on-soil-in-sun-light.jpg')">
  <div class="container">
    <div class="section-head">
      <div class="kicker">02 &middot; RENEWABLE ENERGY</div>
      <h2 style="max-width:18ch;">Renewable Energy Interconnection</h2>
      <p class="lead" style="color:#DFF6E7;">Our know-how in Renewable Energy (RE) Interconnection Facilities means we can supply and deliver electrical equipment and cabling built to last, keeping vital plant generation power flowing efficiently to the grid with as little downtime as possible.</p>
    </div>
  </div>
</section>

<section class="section" id="biogas">
  <div class="container">
    <div class="re-block">
      <div class="re-media" style="--panel-img:url('https://www.klseri.com.my/wp-content/uploads/2021/03/sustainable_growth_istock.jpg')">
        <div>
          <span class="tag">RENEWABLE ENERGY</span>
          <div class="headline">Biogas</div>
        </div>
        <div class="examples">
          <div>1.5MW Biogas for Cenergi FJP Sdn. Bhd.</div>
          <div>3.5MW Biogas for Mistral Engineering Sdn. Bhd.</div>
        </div>
      </div>
      <div class="re-body">
        <p>Because it's so closely tied to the palm oil industry, Malaysia is well placed to turn this into a genuinely clean source of power and heat. Biogas comes from anaerobic digestion of palm oil mill effluent (POME), a waste by-product of crude palm oil production, and using POME as a biomethane source cuts down both air pollution and the mills' carbon footprint.</p>
        <p>That biogas can generate renewable energy for export to the national grid. We support biogas plant rollouts with interconnection works and a full range of services that put methane gas to work as an efficient power source, covering the full supply and installation of electrical interconnection equipment, cabling, and control and instrumentation systems.</p>
        <a href="projects.html#reference-list" class="btn-ghost">See biogas projects in our reference list</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--band" id="biomass">
  <div class="container">
    <div class="re-block">
      <div class="re-media" style="--panel-img:url('https://www.klseri.com.my/wp-content/uploads/2021/05/2021-05-10-015217938.jpg')">
        <div>
          <span class="tag">RENEWABLE ENERGY</span>
          <div class="headline">Biomass</div>
        </div>
        <div class="examples">
          <div>10MW Biomass for Cepat Wawasan Sdn. Bhd.</div>
        </div>
      </div>
      <div class="re-body">
        <p>Biomass energy has several uses, but most biomass plants work the same basic way: burning organic material to produce high-pressure steam, which turns a turbine generator to make electricity.</p>
        <p>Agriculture, timber and general industry all generate large volumes of plant resources and residues that can be converted into renewable energy, cutting reliance on fossil fuels for power and heat. Tropical Southeast Asian countries are well positioned here too, given a hot, humid climate that holds year-round and strong agricultural sectors to draw on.</p>
        <p>Our renewable energy interconnection work here covers engineering, supply, installation and commissioning of the cables and electrical equipment biomass projects need, built to meet local utility authorities' strict requirements while keeping downtime low and generation output high.</p>
        <a href="projects.html#reference-list" class="btn-ghost">See biomass projects in our reference list</a>
      </div>
    </div>
  </div>
</section>

<section class="section" id="solar">
  <div class="container">
    <div class="re-block">
      <div class="re-media" style="--panel-img:url('https://www.klseri.com.my/wp-content/uploads/2021/03/light-bulb-placed-on-soil-in-sun-light.jpg')">
        <div>
          <span class="tag">RENEWABLE ENERGY</span>
          <div class="headline">Solar</div>
        </div>
        <div class="examples">
          <div>1MW Solar Energy for ERS Energy Sdn. Bhd.</div>
        </div>
      </div>
      <div class="re-body">
        <p>Solar remains the world's most widely used renewable energy source, and for good reason: it's clean, abundant and freely available. Panels capture and store energy straight from the sun with zero emissions and minimal environmental impact, which is exactly why solar matters so much to Malaysia's target of 20% renewable energy in its generation mix by 2025.</p>
        <p>Our solar work covers supply, installation and maintenance of the cables and electrical systems that interconnect solar panels, solar power plants and national grid facilities. We aim for solutions that are both cost-effective and built to last, tailored to each project's specific electrical and engineering needs.</p>
      </div>
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
    "services.html",
    "Our Services | Electrical Power Distribution & Renewable Energy, KLS",
    "KLS covers supply, installation, testing and commissioning for electrical power distribution systems, alongside Biogas, Biomass and Solar renewable energy interconnection work.",
    BODY,
    alt_url="https://www.klseri.com.my/ms/services.html",
)
