from build import page, breadcrumb

BODY = f"""
<section class="page-hero">
  <div class="container">
    <h1>Our Services</h1>
    <p class="lead">With our industry knowledge and experience, we provide quality services, products and works to our valued clients to assist them in achieving their business goals. We provide services which include the supply, installation, testing and commissioning for:</p>
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

<section class="section section--forest" id="renewable-energy">
  <div class="container">
    <div class="section-head">
      <div class="kicker">02 &middot; RENEWABLE ENERGY</div>
      <h2 style="max-width:18ch;">Renewable Energy Interconnection</h2>
      <p class="lead" style="color:#DFF6E7;">By combining our knowledge and expertise of Renewable Energy (RE) Interconnection Facilities, we supply and deliver high-quality and reliable electrical equipment and cabling to ensure vital plant generation power is efficiently delivered to the grid with minimal downtime.</p>
    </div>
  </div>
</section>

<section class="section" id="biogas">
  <div class="container">
    <div class="re-block">
      <div class="re-media">
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
        <p>Driven primarily by the palm oil industry, Malaysia is uniquely positioned to provide a clean source of energy for power and heat generation. Biogas is generated from anaerobic digestion of palm oil mill effluent (POME), a waste and by-product of the production of crude palm oil. The usage of POME as a biomethane energy source reduces air pollution and the carbon footprint of the mills.</p>
        <p>The biogas can be utilised to generate renewable energy that can be exported to the national power grid for nationwide distribution. At KLS, we support the implementation of biogas plants with interconnection works and comprehensive services that help successfully utilise methane gas as an energy-efficient power source. Our works involve the total supply and installation of electrical interconnection equipment, cabling, and control and instrumentation systems.</p>
        <a href="projects.html#reference-list" class="btn-ghost">See biogas projects in our reference list</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--band" id="biomass">
  <div class="container">
    <div class="re-block">
      <div class="re-media">
        <div>
          <span class="tag">RENEWABLE ENERGY</span>
          <div class="headline">Biomass</div>
        </div>
        <div class="examples">
          <div>10MW Biomass for Cepat Wawasan Sdn. Bhd.</div>
        </div>
      </div>
      <div class="re-body">
        <p>Biomass energy can be used in different ways. Biomass plants generally utilise the high-pressure steam produced by the combustion of organic materials to turn a turbine generator to produce electricity.</p>
        <p>Industries including agricultural, timber and industrial have tremendous plant resources and residues that can be converted to renewable energy, reducing dependency on fossil fuels for power and heat generation. Tropical countries in the Southeast Asia region can leverage their hot and humid climate all year round as well as their agricultural sectors.</p>
        <p>As a renewable energy interconnection expert, we carry out engineering, supply, installation and commissioning of cables and electrical equipment required for biomass projects, delivering specialised solutions to meet the strict requirements of local utility authorities and vital generating plants — minimising downtime to maximise generation output.</p>
        <a href="projects.html#reference-list" class="btn-ghost">See biomass projects in our reference list</a>
      </div>
    </div>
  </div>
</section>

<section class="section" id="solar">
  <div class="container">
    <div class="re-block">
      <div class="re-media">
        <div>
          <span class="tag">RENEWABLE ENERGY</span>
          <div class="headline">Solar</div>
        </div>
        <div class="examples">
          <div>1MW Solar Energy for ERS Energy Sdn. Bhd.</div>
        </div>
      </div>
      <div class="re-body">
        <p>Solar energy is the world's most popular form of renewable energy because it is the cleanest, most abundant and readily available in nature. Solar energy from the sun is captured and stored by solar panels and has zero emissions with little to no impact on the environment. To ensure Malaysia achieves its target of 20% Renewable Energy in its generation mix by 2025, solar energy is vital to the country.</p>
        <p>Our scope of services for solar energy includes supplying, installation and maintenance of cables and electrical systems for interconnection between solar panels, solar power plants and national grid interconnection facilities. As experts in renewable energy interconnection, we provide cost-effective and durable solutions to meet every project's specific electrical and engineering requirements.</p>
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
    "Our Services | Electrical Power Distribution & Renewable Energy — KLS",
    "KLS offers services that include supplying, installing, testing and commissioning for electrical power distribution systems, plus Biogas, Biomass and Solar renewable energy interconnection.",
    BODY,
    alt_url="https://www.klseri.com.my/ms/services.html",
)
