# KLS Website Redesign — Kejuruteraan Letrik Seri (M) Sdn Bhd

A complete rebuild of https://www.klseri.com.my/ — same company, same facts,
same green + gold identity, a modern premium engineering-firm UI/UX.

## ⚠️ Work in progress — pick up here next session

This build includes new features requested in the latest session:
- ✅ WhatsApp click-to-chat button (floating, bottom-left, every page)
- ✅ Clickable footer addresses (HQ + both branches → Google Maps)
- ✅ Embedded maps for both branch offices on the Contact page (not just HQ)
- ✅ 404 error page (`404.html`)
- ✅ Bahasa Malaysia infrastructure: `build.py` is now a bilingual template
  engine (language-aware header/footer/nav, EN⇄BM toggle in the header,
  hreflang tags), with BM pages generating into `ms/`
- ✅ BM translations done: **Home, Company Overview, Our People, Services,
  Projects** (`ms_pages_home.py`, `ms_pages_company.py`, `ms_pages_people.py`,
  `ms_pages_services.py`, `ms_pages_projects.py`)
- ✅ Shared `main.js` is language-aware where it generates dynamic text
  (project stats, category tags, empty-state message, certificate labels,
  contact-form validation/status messages) — it reads `<html lang="...">`
  and switches strings automatically, so this doesn't need to be redone
  per page.

**Still to do:**
1. Write the remaining 4 BM pages, following the exact pattern of the
   existing `ms_pages_*.py` files (same structure as their English
   `pages_*.py` counterpart, translated body copy, `lang="ms"` and the
   matching `alt_url` passed to `page()`):
   - `ms_pages_certs.py` → `ms/certifications.html`
   - `ms_pages_careers.py` → `ms/careers.html`
   - `ms_pages_contact.py` → `ms/contact.html` (reuse the same
     `MAPS_*`/`WAZE_*` constants imported from `build.py`, same as the
     English `pages_contact.py`)
   - `ms_pages_404.py` → `ms/404.html`
2. Run all `ms_pages_*.py` scripts (including the 5 already written) to
   regenerate the full `ms/` folder in one pass.
3. Add matching `alt_url` hreflang values to the English
   certifications/careers/contact/404 `page()` calls once their BM
   counterparts exist (the other five EN pages already have this — same
   pattern: `alt_url="https://www.klseri.com.my/ms/<file>"`).
4. Re-run the full validation pass (the tag-balance script used throughout
   this build) across every file in both `/` and `/ms/`.
5. Consider a native-speaker review of the BM copy before this goes live —
   it was translated carefully but AI-translated corporate BM should get a
   human check before publishing, especially the Mission/Vision/Core Values
   wording.

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
`klseri.com.my` (the real, existing images — no fake portraits or invented
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
error states, but does **not** send email — there is no backend configured.
Wire `assets/js/main.js` (`data-contact-form` submit handler) to your email
service or API endpoint of choice; the code is structured so you only need
to replace the `setTimeout(...)` placeholder with a real `fetch()` call.

## Content accuracy

All company facts, people, mission/vision/values, service categories, the
full project reference list and contact details were sourced directly from
the live klseri.com.my pages (Home, Company Overview, Our People, Our
Services, Key Projects, Certifications & Licenses, Careers) at the time of
writing. Nothing has been invented — see `assets/js/data.js` for the
structured source data.

## Design notes (v2 — Sep 2026 revision)

- **Colour**: KLS's brand green `#009447` throughout (buttons, active states, links), light theme only — no dark-mode auto-switch. Hero/CTA sections use a bold green gradient block; header, footer and nav are light.
- **Type**: Source Sans 3 (body), Roboto Condensed / Arial (headings), Roboto Mono (technical labels — years, tags, spec numbers).
- **Cards de-templated**: services and core values now render as hairline "spec rows" with index numbers instead of uniform boxed/shadowed cards; stats render as a flowing divided band instead of a boxed grid.
- **Hero**: a crossfade image slider (3 real slides + taglines lifted from the source site's own homepage slider — "Powering Your Business", "Enabling Sustainable and Clean Energy Solutions", "Biomass Power") with a subtle Ken Burns zoom. Note: the original site uses an image slider, not an actual video file, so this is the closest honest equivalent — swap in real video files under `assets/` if you have them.
- **Interactive full-screen menu**: replaces the old dropdown/mobile-drawer nav. One "Menu" button at every breakpoint opens a full-screen overlay with large indexed links and a hover-swapped preview image/caption per section.
- **Infinite marquees**: the "Trusted by..." client strip and the "Four decades" milestone strip both scroll continuously (pause on hover), auto-duplicated in `main.js` (`[data-marquee]`) for a seamless loop.
- **Our People**: restructured into hierarchical profile sections (Founder & Leadership → Technical Leadership → Business Development) with full inline bios, rather than a uniform grid of short blurbs.
- **Motion**: one consistent easing curve (`cubic-bezier(.22,1,.36,1)`) site-wide, a scroll-progress bar, a shrinking sticky header, staggered scroll-reveals, and a JS-animated (non-native) accordion for the project reference list.

