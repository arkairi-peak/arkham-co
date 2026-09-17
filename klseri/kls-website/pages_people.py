from build import page, breadcrumb

def profile(name, role, image, initials, bio, facts):
    facts_html = "".join(f"<div><b>{k}</b>{v}</div>" for k, v in facts)
    img_html = f'<img src="{image}" alt="Photo of {name}" loading="lazy">' if image else f'<div class="initials">{initials}</div>'
    return f"""<div class="profile-row">
      <div class="profile-photo">{img_html}</div>
      <div class="profile-body">
        <span class="role">{role}</span>
        <h3>{name}</h3>
        <p>{bio}</p>
        <div class="profile-facts">{facts_html}</div>
      </div>
    </div>"""

FOUNDERS = "".join([
    profile(
        "Lim Cheng Lai", "Founder", "https://www.klseri.com.my/wp-content/uploads/2021/02/Lim-Cheng-Lai.jpg", "LCL",
        "Lim Cheng Lai is the founder of KLS and is the key person who led and transformed the company from a humble electrical motor wiring workshop into an established Class A, CIDB G7 M&amp;E Contractor. He sets the direction of the company and leads the charge of a young and dynamic technical team.",
        [
            ("Certification", "B4 33KV Chargeman (Energy Commission)"),
            ("Certification", "PW4 Wireman (Energy Commission)"),
            ("Focus", "Company direction &amp; technical leadership"),
        ],
    ),
    profile(
        "YDM Tengku Dato' Ardy Esfandiari Bin Tengku Hamid Shah Al Haj Tengku Seri Paduka Shahbandar (Selangor)",
        "Founder", "https://www.klseri.com.my/wp-content/uploads/2021/02/Team-03-797x1024.jpg", "TA",
        "One of the founders of KLS, YDM Tengku Dato' Ardy is instrumental in the company's public and government affairs liaison department. An established entrepreneur with extensive networking and excellent public relations skills, he helped build KLS into a company reputable amongst Government Linked Companies.",
        [
            ("Honour", "Darjah Kebesaran Dato' Sultan Sharafudin Idris Shah (D.S.I.S) — conferred 2012, for the 67th birthday of the Sultan of Selangor"),
            ("Board Position", "CB Industrial Products Bhd."),
            ("Focus", "Public affairs &amp; government affairs liaison"),
        ],
    ),
])

TECHNICAL = "".join([
    profile(
        "Ir. Lim Yee Chard", "Technical Leadership", "https://www.klseri.com.my/wp-content/uploads/2021/02/Team-02-796x1024.jpg", "LYC",
        "Ir. Lim currently oversees all projects undertaken by KLS. As a practising Professional Engineer and registered ASEAN Engineer, he is responsible for the overall tendering, execution and handing over of all major projects, leading an energetic and dedicated technical team to ensure projects are completed exceeding expectations and within budget.",
        [
            ("Education", "UMIST (University of Manchester Institute of Science and Technology), UK — graduated 2002"),
            ("Registration", "Practising Professional Engineer &middot; Registered ASEAN Engineer"),
            ("Responsibility", "Tendering, execution and handover of major projects"),
        ],
    ),
    profile(
        "Ir. Jeremy Goh Jing Wei", "Technical Leadership", "https://www.klseri.com.my/wp-content/uploads/2021/02/Jeremy.jpg", "JG",
        "Ir. Jeremy Goh joined KLS in 2014 and is the head engineer responsible for the technical and authorities liaison aspect of all KLS projects. An experienced and technical engineer, he has a proven track record in managing projects.",
        [
            ("Education", "UniTEN (Universiti Tenaga Nasional) — Degree in Electrical and Electronics Engineering (Hons.), 2013"),
            ("Registration", "Registered Professional Engineer"),
            ("Joined KLS", "2014 &middot; Head engineer, technical &amp; authorities liaison"),
        ],
    ),
])

BIZDEV = profile(
    "Ali Na'Azzam", "Business Development", "https://www.klseri.com.my/wp-content/uploads/2021/02/Team-01-796x1024.jpg", "AN",
    "Ali Na'Azzam is responsible for the business development of KLS. Equipped with strong PR skills and a vast network circle, he is also well versed in the construction industry with more than 25 years of experience.",
    [
        ("Education", "Bachelor of Law (LLB)"),
        ("Experience", "25+ years in the construction industry"),
        ("Position", "Nominated as Executive Director since 2018"),
    ],
)

BODY = f"""
<section class="page-hero">
  <div class="container">
    <h1>Our People</h1>
    <p class="lead">The founders, technical leadership and business development team behind KLS — organised by the role each plays in the company.</p>
  </div>
</section>
{breadcrumb('our-people.html','Our People')}

<section class="section">
  <div class="container">
    <div class="people-group">
      <div class="people-group-head"><h3>Founder &amp; Leadership</h3><span class="mono">01–02</span></div>
      {FOUNDERS}
    </div>
    <div class="people-group">
      <div class="people-group-head"><h3>Technical Leadership</h3><span class="mono">03–04</span></div>
      {TECHNICAL}
    </div>
    <div class="people-group">
      <div class="people-group-head"><h3>Business Development</h3><span class="mono">05</span></div>
      {BIZDEV}
    </div>
  </div>
</section>

<section class="section section--band">
  <div class="container grid grid-2" style="align-items:center;gap:48px;">
    <div>
      <div class="kicker">Our Team</div>
      <h2>A young and dynamic technical team</h2>
      <p class="lead">Beyond its key personnel, KLS is led by a young and dynamic technical team responsible for tendering, execution and handover of every project — from master rewiring works to multi-megawatt renewable energy interconnection facilities.</p>
    </div>
    <a href="https://www.klseri.com.my/wp-content/uploads/2021/04/KLS-01.png" target="_blank" rel="noopener">
      <img src="https://www.klseri.com.my/wp-content/uploads/2021/04/KLS-01.png" alt="The KLS team" style="border-radius:10px;border:1px solid var(--line-300);">
    </a>
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
    "our-people.html",
    "Our People | Key Personnel at KLS",
    "Meet KLS's key personnel, organised by role — founders, technical leadership and business development — who built a reputable electrical services provider.",
    BODY,
    alt_url="https://www.klseri.com.my/ms/our-people.html",
)
