# KLS Website Redesign, Kejuruteraan Letrik Seri (M) Sdn Bhd

A complete rebuild of https://www.klseri.com.my/, same company, same facts,
same green + gold identity, a modern premium engineering-firm UI/UX.

## Latest session: hero-jump fix v2, lighter photo overlay, value icons, tidier spacing

- **Hero jump fix, take two.** The previous fix (em-based min-heights on the
  title/lead individually) wasn't generous enough for every real-world line
  wrap. Replaced it with a single fixed-height wrapper (`.hero-copy`,
  `min-height:460px` desktop / `320px` mobile) around the whole title+lead
  block, sized with real buffer for the longest slide. This is a harder
  guarantee than the previous per-element estimate.
- **Re-block photos were too dark to read.** The green overlay on Solar/
  Biogas/Biomass/Grid Utilities/Semiconductor/Petrochem/Hospital panels was
  sitting at 90%/82% opacity, nearly blacking out the photo underneath.
  Dropped it to 52%/36% so the photo actually shows, and added a subtle
  text-shadow to the headline and project-example text so legibility holds
  up against brighter photos now that the overlay is lighter.
- **Core Values now has icons.** Added a small custom SVG icon (quality
  checkmark, lightbulb, two-person teamwork mark, refresh/adapt arrows,
  briefcase, heart) to each of the 6 value rows, sitting next to the
  existing numbered index rather than replacing it.
- **Project examples restyled as a tidy stacked card deck** instead of
  plain text lines separated by a divider, each example is now its own
  small rounded card, progressively inset to read as a stack (matching
  your sketch) rather than a flat list.
- **Tightened the gap between short subsections.** Grid Utilities,
  Semiconductor & Electronic, Petrochemical & Oleochemical, Hospital &
  Stadium, and Renovation & Restoration now use the tighter section padding
  (`section--tight`) since each holds only one re-block, the old full
  100px top/bottom padding was leaving a lot of dead space between them.

### Previous session: 4 bug fixes + Home page industries rebuilt into full subsections

- **Fixed unreadable industry-card tags**: the amber label text was sitting
  on an inherited near-white pill background (the global `.tag` class's
  background wasn't being overridden), making it nearly invisible. Now uses
  its own dark glass pill so the label is readable against any photo.
- **Logos now show full color by default everywhere**, the Trusted-by
  marquee and Key Clients river no longer gate color behind hover
  (`filter:grayscale(1)` removed from the default state), hover now only
  does the lift/scale.
- **Fixed the blank space in the menu** that pushed the HQ address/contact
  footer below the fold: `.nav-overlay-body` had a forced
  `min-height:calc(100vh - 86px)` regardless of how much content it held.
  Converted the panel to a proper flex column so the footer sits right
  after the nav links, with only the body scrolling if it ever needs to.
- **Fixed the homepage jump on hero slide change**: the title/lead text
  swap via JS was changing box height slightly differently per slide
  (different line-wrap counts), which shifted everything below it. Gave
  the title and lead a fixed `min-height` sized for the longest slide, so
  swapping slides no longer moves the page.
- **Home page industries rebuilt from a compact 5-card grid into full
  subsections**, matching your mind-map structure directly: Clean Energy
  (with Solar, Biogas and Biomass each getting their own mini re-block,
  brief description, project reference examples and a photo, same pattern
  already used on the Services page), then standalone subsections for Grid
  Utilities, Semiconductor & Electronic, Petrochemical & Oleochemical,
  Hospital & Stadium (featuring Larkin), and a lighter Renovation &
  Restoration callout. Each is its own named, anchored section rather than
  one dense grid.

### Previous session: nav overhaul, People removed, new Location page, Home rebuild

- **Navigation renewed to match your sketch**: 6 items (Home, Company,
  Certifications, Project Ref, Contact, Location), your uploaded icons in
  place of the old numbered index, People and Services/Careers dropped from
  the primary menu (Services and Careers pages still exist, just reachable
  via the footer instead).
- **People page removed entirely**, source files, generated HTML, footer
  links, and the homepage preview strip. No dangling references left.
- **New Location page** (EN + BM): pulled the HQ/branch maps out of Contact
  into their own dedicated page; Contact is now just the form + direct
  contact info, linking over to Location.
- **Kelington Group added as the featured partner**, confirmed their real
  site (kelington-group.com) before linking it, placed first in the
  Partners carousel with a distinct gold "Featured Partner" badge.
- **Larkin Stadium added as a project** (Stadium Tan Sri Dato' Haj Hassan
  Yunos, home of Johor Darul Ta'zim), lighting works, under a new "Stadium
  & Infrastructure" category with its own filter chip. Honest gap: no year
  was given for this project, so none was invented, it's listed undated
  until you confirm one.
- **Home page rebuilt** around your mind-map: a brief "What We Do" strip
  (HV/MV/LV, ACMV, fire fighting, ELV), then a photo-forward "Industries We
  Serve" grid (Renewable & Clean Energy shown wide/featured since biogas
  has the deepest project history in the data, Grid Utilities, Semiconductor
  & Electronic with an AI-growth framing, Petrochemical & Oleochemical,
  Hospital & Stadium featuring Larkin), then client logos and the trusted-by
  marquee moved up well before the historical milestone timeline, per
  "jump straight to clients and photos, cut the history." One honest note:
  Melexis (Kuching), Renesas and SICK AG (JB) are listed as clients per your
  sketch, but the accompanying photos are generic illustrative semiconductor
  photography, not verified photos of their specific facilities.
- **Projects page**: client logos now show next to the company name for
  every project group where I have a verified matching brand asset (Sime
  Darby, Telekom Malaysia, Cenergi, SESB, KLK, Cepat Wawasan, North Port,
  Cargill), giving each client group a more branded, detailed presence.
- Fixed a real bug along the way: a `const ASSET_PREFIX` was being used
  before its declaration executed (temporal dead zone), which would have
  thrown a runtime error on every Projects page load. Moved the declaration
  to the top of the script.

### Previous session: paraphrased copy, restructured Company Overview, RE card photos

- **Every piece of narrative copy on the English site has been paraphrased**,
  hero taglines, About/Company Overview text, service descriptions, all
  three renewable-energy write-ups (Biogas, Biomass, Solar), People bios,
  Careers, Contact and 404 copy, plus page titles and meta descriptions.
  The intent: read differently from the original klseri.com.my wording
  while keeping every fact, name, date, credential, and number exactly as
  published (nothing here changes what KLS says about itself, only how
  it's phrased). The one exception left untouched on purpose: the Project
  Reference List entries (client names, locations, years, categories),
  those are records, not prose, so they weren't reworded.
- **Company Overview restructured**, this was the page flagged as feeling
  "stacked." Specifically: the "Business Beyond Professionalism" and "Your
  Trusted Partner for Quality" cards used to sit crammed into a narrow
  column beside the timeline; they now have their own section as a proper
  side-by-side pair. A new quick-facts strip (Est. 1984, Class A CIDB G7,
  HV/LV/ELV systems, 5 sectors served) sits right under the opening
  paragraph too, so there's something scannable before the reader hits the
  denser text.
- **Biogas, Biomass and Solar cards now carry real photography** instead of
  a flat color panel, reusing KLS's own verified site images (the same
  honest tradeoff as the green-panel work earlier: I don't have three
  distinct on-topic photos, so some images repeat elsewhere on the site;
  send over dedicated Biogas/Biomass/Solar photos if you have any and I'll
  swap them in one at a time).

**Now done:** the Bahasa Malaysia pages (`ms/`) have been brought fully up
to date with the paraphrased English content above, matching page for
page: Home, Company Overview (including the restructured layout), Services
(with the same renewable-energy card images), People bios, Projects,
Certifications, Careers, Contact and 404. All 18 pages (9 English + 9 BM)
regenerated and validated together in this pass.

### Previous session: curtain restored on home, slide-up for everything else

My previous note said the glassmorphism curtain and 16-tile shatter were
removed entirely, that was a misread of the request. Corrected: the
curtain stays on the homepage only, exactly as before (glass blob panel,
shatters into a 4x4 grid on exit, hero content staggers in sync with it).
The "slide up" entrance is additive, not a replacement, it now covers
everything the curtain doesn't:
- Every `.page-hero` banner on every inner page (both languages)
- Every other `<section>` on the homepage itself, below the hero
- Every section on every inner page too

So: home page hero, curtain. Everything else, everywhere, slide-up.

### Also this session: kicker redesign, view-all fix

- **Redesigned the "kicker" eyebrow label.** The thin-rule-plus-tiny-spaced-
  caps treatment (small line + "SECTION LABEL") used above nearly every
  heading was replaced with a small pill badge (soft tinted background,
  colored dot, bold sentence-case text) instead. Applies everywhere the
  kicker is used, one CSS change, no page-by-page edits needed.
- **Fixed the View All button.** The actual bug: it was a `<button>` styled
  with `.btn-ghost` alone, which only overrides `border-bottom`, so the
  browser's default button border was still showing on the other three
  sides, that's what looked "cut." Fixed the underlying CSS (`.btn-ghost`
  now resets `border:0` first) and gave the carousel's View All button its
  own proper pill design with a small grid icon, rather than reusing the
  understated ghost-link style.

### Previous session: real Partner/Advisor logos, glassmorphism load curtain
(note: the load curtain described below was replaced by the simpler
site-wide slide-up described above, this entry is kept as a historical
record of what was built and why.)

- **All 17 Partners & Advisors now have real logos**, not just Sime Darby.
  You uploaded 16 more files; every single one matched a company already on
  the site (UPC, Ekarat, Fuji Electric, OSK Group, Schneider Electric,
  INNIO Jenbacher, Sistem Konsult, SP Nergy, Tamco, Viscon, Terasaki,
  Duriane, ABB, ZP/Zeal Perunding, Grid Vision T&D, Malim), so the carousel
  now shows genuine logos across the board, no text plates left.
- **Homepage load curtain, done as glassmorphism.** A frosted-glass panel
  (backdrop-blur + saturation) with soft blurred green blobs drifting
  behind it, plus a small glass-card KLS mark in the center, covers the
  page for about half a second before lifting to reveal the hero, whose
  staggered entrance was retimed to start exactly as the curtain lifts so
  the two feel like one continuous motion rather than two effects stacked
  on top of each other.
  - It's pure-CSS timed (`animation-delay` + `forwards`), so it always
    lifts itself even if JavaScript never runs, it can't get anyone stuck.
  - A tiny synchronous inline script (not the main bundle) hides it
    instantly on repeat visits within the same browser session, and
    `prefers-reduced-motion` skips it entirely.
  - Scoped to the homepage only (both languages); inner pages are
    unaffected.

### Previous session: marquee fix, partner carousel, homepage motion

- **Marquee hover-clip bug fixed.** The logo plates' idle float animation
  and hover lift were being visually cut off by the row's `overflow:hidden`
  (needed for the horizontal scroll). Fixed by giving `.marquee` vertical
  padding, pausing the idle float on hover (`animation-play-state:paused`),
  and switching the hover shadow to a smaller one so it never exceeds that
  padding.
- **Partners & Suppliers / Advisors & Consultants** are no longer a plain
  text grid. They're now a center-focus slidable carousel (per your
  wireframe): active item large and in color, neighbours peeking at reduced
  scale/grayscale, prev/next arrows, dot indicators, gentle autoplay that
  pauses on hover, and a "View All" button that opens the full set in a
  grid lightbox. Sime Darby Berhad (which appears in both Key Clients and
  Partners) now uses the real logo you provided; the rest render as clean
  styled text plates since I don't have verified logo files for them.
  Upload real logos for any of these the same way you did for Key Clients
  and I'll wire them in the same way.
- **Homepage load and scroll animation:**
  - Hero content now enters in a choreographed stagger (eyebrow, then
    headline, then lead, then buttons, then the stats strip) instead of
    all at once.
  - A small animated scroll-cue in the bottom-right of the hero invites
    scrolling and smooth-scrolls to the next section on click.
  - The hero slides now have a subtle parallax drift as you scroll past
    them (separate from, and not fighting, the existing Ken Burns zoom on
    the images themselves).
  - The "Four decades" milestone section now gets the same scroll-triggered
    reveal treatment as the rest of the page (it was previously skipped
    because its heading wasn't wrapped in `.section-head`).

### Previous session: logos, full BM site, style cleanup

- All 18 pages now exist: 9 English (root) + 9 Bahasa Malaysia (`ms/`).
  The Bahasa Malaysia site is complete (Home, Company Overview, Our People,
  Services, Projects, Certifications, Careers, Contact, 404).
- Real client logos are now wired in under `assets/img/clients/` (Sime Darby,
  Sabah Electricity, Northport, Telekom Malaysia, FELCRA, Cargill, Cenergi,
  Cepat Wawasan, FGV Holdings, Hap Seng, KLK Oleo), sourced from the files
  you uploaded. Top Glove Berhad (used only in the "Trusted by" strip, not
  the main Key Clients list) has no verifiable logo file available to me, so
  it renders as a styled text plate matching the others rather than a guessed
  or low-quality image.
- The Key Clients section is now an animated "logo river": two rows of logos
  scrolling in opposite directions, each logo idly floating on its own
  offset timer (not synchronised), grayscale by default and revealing full
  colour with a lift on hover. The same hover-to-smooth-stop easing from the
  milestone/client marquees applies here too (see `initMarquee()` in
  `assets/js/main.js`, now a single reusable function).
- Every visible em dash ("--") has been removed site-wide (all EN/BM page
  content, JS-generated strings, and doc comments) and replaced with commas,
  plain hyphens, or restructured phrasing, whichever read most naturally.

## Running it locally

No build step, no dependencies. Just open `index.html` in a browser, or
serve the folder with any static server, e.g.:

```bash
cd kls
python3 -m http.server 8080
# then visit http://localhost:8080
```

## Structure

```
kls/
├── index.html                 Home
├── company-overview.html      Company Overview, Our Story, Mission, Vision, Core Values,
│                               Key Clients, Partners & Suppliers, Advisors & Consultants
├── our-people.html             Key personnel directory
├── services.html               Electrical Power Distribution + Renewable Energy
│                               (Biogas / Biomass / Solar)
├── projects.html               Key Projects + filterable/searchable Project Reference List
├── certifications.html         Certifications & Licenses
├── careers.html                Careers
├── contact.html                Contact form, HQ + branch offices, map
├── assets/
│   ├── css/style.css           Design system (colour tokens, type, components)
│   ├── js/data.js              Structured data: people, projects, clients, partners, certs
│   └── js/main.js              Nav, modals, filters, search, counters, form validation
└── build.py + pages_*.py       Python generator that produced the HTML above
                                 (re-run `python3 build.py` after editing pages_*.py
                                 to regenerate the header/nav/footer consistently)
```

## Important: images are currently hot-linked from klseri.com.my

I could not download binary image files in this environment, so every
photo, icon and certificate scan currently points at its original URL on
`klseri.com.my` (the real, existing images, no fake portraits or invented
certificates). This keeps the site 100% content-accurate, but for a
production deployment you should:

1. Download each image referenced in `assets/js/data.js` and the `pages_*.py`
   / generated `.html` files (search for `klseri.com.my/wp-content/uploads`).
2. Save them under `assets/img/` (people, certs, projects folders are
   pre-created).
3. Update the `src`/`image` paths to the local copies.

This also removes the dependency on the old site staying online.

## Contact form

The form in `contact.html` validates client-side (required fields, email
format, phone format, minimum message length) and shows loading/success/
error states, but does **not** send email, there is no backend configured.
Wire `assets/js/main.js` (`data-contact-form` submit handler) to your email
service or API endpoint of choice; the code is structured so you only need
to replace the `setTimeout(...)` placeholder with a real `fetch()` call.

## Content accuracy

All company facts, people, mission/vision/values, service categories, the
full project reference list and contact details were sourced directly from
the live klseri.com.my pages (Home, Company Overview, Our People, Our
Services, Key Projects, Certifications & Licenses, Careers) at the time of
writing. Nothing has been invented, see `assets/js/data.js` for the
structured source data.

## Design notes (v2, Sep 2026 revision)

- **Colour**: KLS's brand green `#009447` throughout (buttons, active states, links), light theme only, no dark-mode auto-switch. Hero/CTA sections use a bold green gradient block; header, footer and nav are light.
- **Type**: Source Sans 3 (body), Roboto Condensed / Arial (headings), Roboto Mono (technical labels, years, tags, spec numbers).
- **Cards de-templated**: services and core values now render as hairline "spec rows" with index numbers instead of uniform boxed/shadowed cards; stats render as a flowing divided band instead of a boxed grid.
- **Hero**: a crossfade image slider (3 real slides + taglines lifted from the source site's own homepage slider, "Powering Your Business", "Enabling Sustainable and Clean Energy Solutions", "Biomass Power") with a subtle Ken Burns zoom. Note: the original site uses an image slider, not an actual video file, so this is the closest honest equivalent, swap in real video files under `assets/` if you have them.
- **Interactive full-screen menu**: replaces the old dropdown/mobile-drawer nav. One "Menu" button at every breakpoint opens a full-screen overlay with large indexed links and a hover-swapped preview image/caption per section.
- **Infinite marquees**: the "Trusted by..." client strip and the "Four decades" milestone strip both scroll continuously (pause on hover), auto-duplicated in `main.js` (`[data-marquee]`) for a seamless loop.
- **Our People**: restructured into hierarchical profile sections (Founder & Leadership → Technical Leadership → Business Development) with full inline bios, rather than a uniform grid of short blurbs.
- **Motion**: one consistent easing curve (`cubic-bezier(.22,1,.36,1)`) site-wide, a scroll-progress bar, a shrinking sticky header, staggered scroll-reveals, and a JS-animated (non-native) accordion for the project reference list.

