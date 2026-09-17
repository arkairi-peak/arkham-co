/* ==========================================================================
   KLS site interactivity — vanilla JS, no build step required.
   Progressive: every page works without JS; this layers on the polish.
   ========================================================================== */
(function () {
  "use strict";

  /* ---------------- Interactive menu (half-screen sliding panel) ---------------- */
  const menuToggle = document.querySelector("[data-menu-toggle]");
  const navOverlay = document.querySelector("[data-nav-overlay]");
  const navBackdrop = document.querySelector("[data-nav-backdrop]");
  const navClose = document.querySelector("[data-nav-close]");
  const previewImgs = document.querySelectorAll("[data-preview-src]");
  const navItems = document.querySelectorAll(".nav-overlay-item");

  function setBgImage(img) {
    previewImgs.forEach((el) => el.classList.toggle("is-active", el.getAttribute("data-preview-src") === img));
  }
  navItems.forEach((item) => {
    const img = item.getAttribute("data-nav-preview");
    item.addEventListener("mouseenter", () => setBgImage(img));
    item.addEventListener("focusin", () => setBgImage(img));
  });

  function openNav() {
    if (!navOverlay) return;
    navOverlay.classList.add("is-open");
    navBackdrop && navBackdrop.classList.add("is-open");
    document.body.style.overflow = "hidden";
    menuToggle && menuToggle.setAttribute("aria-expanded", "true");
    const first = navItems[0];
    if (first) setBgImage(first.getAttribute("data-nav-preview"));
  }
  function closeNav() {
    if (!navOverlay) return;
    navOverlay.classList.remove("is-open");
    navBackdrop && navBackdrop.classList.remove("is-open");
    document.body.style.overflow = "";
    menuToggle && menuToggle.setAttribute("aria-expanded", "false");
  }
  menuToggle && menuToggle.addEventListener("click", openNav);
  navClose && navClose.addEventListener("click", closeNav);
  navBackdrop && navBackdrop.addEventListener("click", closeNav);
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && navOverlay && navOverlay.classList.contains("is-open")) closeNav();
  });
  // Close automatically when a nav link is followed (keeps same-page anchor jumps tidy too)
  document.querySelectorAll(".nav-overlay-row, .nav-overlay-sub a").forEach((a) => {
    a.addEventListener("click", () => closeNav());
  });

  /* ---------------- Infinite marquees — JS-driven for a smooth, eased ---------------- */
  /* hover pause/resume (an abrupt CSS animation-play-state toggle looks stiff; */
  /* this lerps the speed toward 0 on hover and back to full speed on leave).   */
  document.querySelectorAll("[data-marquee]").forEach((wrap) => {
    const track = wrap.querySelector(".marquee-track");
    if (!track) return;
    // Duplicate the track content once so a translateX loop is seamless.
    track.innerHTML = track.innerHTML + track.innerHTML;

    const baseSpeed = (parseFloat(wrap.getAttribute("data-marquee-speed")) || 45); // px/second
    const reverse = wrap.getAttribute("data-marquee-reverse") === "true";
    let pos = 0;
    let currentSpeed = baseSpeed;
    let targetSpeed = baseSpeed;
    let halfWidth = track.scrollWidth / 2 || 1;
    let lastTime = null;

    wrap.addEventListener("mouseenter", () => { targetSpeed = 0; });
    wrap.addEventListener("mouseleave", () => { targetSpeed = baseSpeed; });
    wrap.addEventListener("touchstart", () => { targetSpeed = 0; }, { passive: true });
    wrap.addEventListener("touchend", () => { targetSpeed = baseSpeed; }, { passive: true });
    window.addEventListener("resize", () => { halfWidth = track.scrollWidth / 2 || 1; });

    function frame(now) {
      if (lastTime == null) lastTime = now;
      const dt = Math.min(0.05, (now - lastTime) / 1000);
      lastTime = now;
      // Ease current speed toward target speed — this is what makes the
      // hover-to-stop (and resume) feel smooth instead of an abrupt cut.
      currentSpeed += (targetSpeed - currentSpeed) * Math.min(1, dt * 2.5);
      const dir = reverse ? 1 : -1;
      pos += dir * currentSpeed * dt;
      if (pos <= -halfWidth) pos += halfWidth;
      if (pos >= 0) pos -= halfWidth;
      track.style.transform = `translateX(${pos}px)`;
      requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  });

  /* ---------------- Hero crossfade slider ---------------- */
  (function heroSlider() {
    const slides = document.querySelectorAll(".hero-slide");
    const dots = document.querySelectorAll("[data-hero-dot]");
    const titleEl = document.querySelector("[data-hero-title-el]");
    const leadEl = document.querySelector("[data-hero-lead-el]");
    if (!slides.length) return;
    let idx = 0;
    function show(i) {
      slides.forEach((s, n) => s.classList.toggle("is-active", n === i));
      dots.forEach((d, n) => d.classList.toggle("is-active", n === i));
      const active = slides[i];
      if (active && titleEl && leadEl) {
        titleEl.style.opacity = "0";
        leadEl.style.opacity = "0";
        setTimeout(() => {
          titleEl.textContent = active.getAttribute("data-hero-title") || titleEl.textContent;
          leadEl.textContent = active.getAttribute("data-hero-lead") || leadEl.textContent;
          titleEl.style.opacity = "1";
          leadEl.style.opacity = "1";
        }, 260);
      }
      idx = i;
    }
    if (titleEl) titleEl.style.transition = "opacity .3s ease";
    if (leadEl) leadEl.style.transition = "opacity .3s ease";
    dots.forEach((d, n) => d.addEventListener("click", () => show(n)));
    setInterval(() => show((idx + 1) % slides.length), 6000);
  })();

  /* ---------------- Scroll progress bar + shrinking sticky header ---------------- */
  (function scrollChrome() {
    const progress = document.querySelector("[data-scroll-progress]");
    const header = document.querySelector(".site-header");
    let ticking = false;

    function update() {
      const doc = document.documentElement;
      const scrollTop = window.scrollY || doc.scrollTop;
      const max = doc.scrollHeight - doc.clientHeight;
      const pct = max > 0 ? (scrollTop / max) * 100 : 0;
      if (progress) progress.style.width = pct + "%";
      if (header) header.classList.toggle("is-scrolled", scrollTop > 8);
      ticking = false;
    }
    window.addEventListener(
      "scroll",
      () => {
        if (!ticking) {
          requestAnimationFrame(update);
          ticking = true;
        }
      },
      { passive: true }
    );
    update();
  })();

  /* ---------------- Generic scroll-reveal (smooth, staggered) ---------------- */
  (function scrollReveal() {
    if (!("IntersectionObserver" in window)) return;
    const selectors = [
      ".spec-row", ".value-row", ".re-block", ".t-item", ".logo-cell",
      ".stat-item", ".loc-card", ".hero-stat", ".card", ".section-head",
      ".profile-row",
    ];
    const groups = {};
    selectors.forEach((sel) => {
      document.querySelectorAll(sel).forEach((el) => {
        if (el.classList.contains("reveal") || el.classList.contains("reveal-io")) return;
        el.classList.add("reveal-io");
        const parent = el.parentElement;
        if (!groups[sel]) groups[sel] = new Map();
        const map = groups[sel];
        if (!map.has(parent)) map.set(parent, 0);
        const idx = map.get(parent);
        map.set(parent, idx + 1);
        el.style.transitionDelay = Math.min(idx * 70, 420) + "ms";
      });
    });
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );
    document.querySelectorAll(".reveal-io").forEach((el) => io.observe(el));
  })();

  /* ---------------- Active nav link (based on current path) ---------------- */
  (function markActiveNav() {
    const path = location.pathname.split("/").pop() || "index.html";
    document.querySelectorAll("[data-nav-link]").forEach((a) => {
      const href = a.getAttribute("href").split("#")[0] || "index.html";
      if (href === path || (path === "" && href === "index.html")) {
        a.classList.add("is-active");
      }
    });
  })();

  /* ---------------- Back to top ---------------- */
  const backToTop = document.querySelector("[data-back-to-top]");
  if (backToTop) {
    window.addEventListener(
      "scroll",
      () => {
        backToTop.classList.toggle("is-visible", window.scrollY > 640);
      },
      { passive: true }
    );
    backToTop.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  /* ---------------- Count-up stats (only real numeric data) ---------------- */
  const counters = document.querySelectorAll("[data-count-to]");
  if (counters.length && "IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          const el = entry.target;
          const target = parseFloat(el.getAttribute("data-count-to"));
          const suffix = el.getAttribute("data-count-suffix") || "";
          const duration = 900;
          const start = performance.now();
          function tick(now) {
            const p = Math.min(1, (now - start) / duration);
            const eased = 1 - Math.pow(1 - p, 3);
            el.textContent = Math.round(target * eased) + suffix;
            if (p < 1) requestAnimationFrame(tick);
          }
          requestAnimationFrame(tick);
          io.unobserve(el);
        });
      },
      { threshold: 0.4 }
    );
    counters.forEach((c) => io.observe(c));
  }

  /* ---------------- Certifications lightbox ---------------- */
  const certGrid = document.querySelector("[data-cert-grid]");
  if (certGrid && typeof KLS_CERTS !== "undefined") {
    const CERT_LANG = document.documentElement.getAttribute("lang") === "ms" ? "ms" : "en";
    const certLabel = CERT_LANG === "ms" ? "Sijil" : "Certificate";
    const certOf = CERT_LANG === "ms" ? "daripada 12" : "of 12";
    certGrid.innerHTML = KLS_CERTS.map(
      (c) => `<div class="cert-card reveal" data-cert="${c.n}" tabindex="0" role="button" aria-haspopup="dialog">
        <div class="cert-thumb"><img src="${c.image}" alt="KLS certification / licence document ${c.n}" loading="lazy"></div>
        <div class="cert-label">${certLabel} ${String(c.n).padStart(2, "0")}</div>
      </div>`
    ).join("");

    const certOverlay = document.querySelector("[data-cert-modal]");
    function openCert(n) {
      const c = KLS_CERTS.find((x) => x.n === Number(n));
      if (!c || !certOverlay) return;
      certOverlay.innerHTML = `<div class="modal" role="dialog" aria-modal="true" aria-label="${certLabel} ${c.n}" style="max-width:640px;">
        <div style="position:relative;padding:24px;">
          <button class="modal-close" type="button" data-modal-close aria-label="Close">&times;</button>
          <p class="small mono" style="margin-bottom:12px;">${certLabel} ${String(c.n).padStart(2, "0")} ${certOf}</p>
          <img src="${c.image}" alt="KLS certification / licence document ${c.n}" style="width:100%;border:1px solid var(--line-300);border-radius:6px;">
        </div>
      </div>`;
      certOverlay.classList.add("is-open");
      document.body.style.overflow = "hidden";
    }
    function closeCert() {
      if (!certOverlay) return;
      certOverlay.classList.remove("is-open");
      document.body.style.overflow = "";
    }
    certGrid.querySelectorAll("[data-cert]").forEach((card) => {
      card.addEventListener("click", () => openCert(card.getAttribute("data-cert")));
      card.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          openCert(card.getAttribute("data-cert"));
        }
      });
    });
    certOverlay &&
      certOverlay.addEventListener("click", (e) => {
        if (e.target === certOverlay || e.target.closest("[data-modal-close]")) closeCert();
      });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") closeCert();
    });
  }

  /* ---------------- Projects: stats, search, filters ---------------- */
  const projectList = document.querySelector("[data-project-list]");
  if (projectList && typeof KLS_PROJECTS !== "undefined") {
    const PAGE_LANG = document.documentElement.getAttribute("lang") === "ms" ? "ms" : "en";
    const PSTR = {
      en: {
        stat1: "Client organisations referenced",
        stat2: "Individual project entries",
        stat3: "Renewable energy interconnection works",
        stat4: "Years covered in this reference list",
        cat: { power: "Electrical & Power Distribution", biogas: "Biogas", biomass: "Biomass", solar: "Solar" },
        empty: "No projects match your search or filter. Try clearing the search box or choosing “All”.",
        listedOne: "project listed",
        listedMany: "projects listed",
      },
      ms: {
        stat1: "Organisasi pelanggan dirujuk",
        stat2: "Entri projek individu",
        stat3: "Kerja interkoneksi tenaga boleh diperbaharui",
        stat4: "Tahun yang diliputi dalam senarai rujukan ini",
        cat: { power: "Elektrik & Pengagihan Kuasa", biogas: "Biogas", biomass: "Biojisim", solar: "Suria" },
        empty: "Tiada projek sepadan dengan carian atau penapis anda. Cuba kosongkan kotak carian atau pilih “Semua”.",
        listedOne: "projek disenaraikan",
        listedMany: "projek disenaraikan",
      },
    }[PAGE_LANG];

    const flat = KLS_PROJECTS.flatMap((c) =>
      c.entries.map((e) => ({ ...e, client: c.client, short: c.short }))
    );
    const years = flat.map((e) => e.year).filter(Boolean);

    // Stats strip — computed directly from KLS_PROJECTS, nothing invented.
    const statsWrap = document.querySelector("[data-project-stats]");
    if (statsWrap) {
      const reCount = flat.filter((e) => ["biogas", "biomass", "solar"].includes(e.category)).length;
      statsWrap.innerHTML = `
        <div class="stat-item"><b data-count-to="${KLS_PROJECTS.length}">0</b><span>${PSTR.stat1}</span></div>
        <div class="stat-item"><b data-count-to="${flat.length}">0</b><span>${PSTR.stat2}</span></div>
        <div class="stat-item"><b data-count-to="${reCount}">0</b><span>${PSTR.stat3}</span></div>
        <div class="stat-item"><b>${Math.min(...years)}–${Math.max(...years)}</b><span>${PSTR.stat4}</span></div>`;
      statsWrap.querySelectorAll("[data-count-to]").forEach((el) => {
        if ("IntersectionObserver" in window) {
          const io2 = new IntersectionObserver(
            (entries) => {
              entries.forEach((entry) => {
                if (!entry.isIntersecting) return;
                const target = parseInt(el.getAttribute("data-count-to"), 10);
                const start = performance.now();
                function tick(now) {
                  const p = Math.min(1, (now - start) / 800);
                  el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3)));
                  if (p < 1) requestAnimationFrame(tick);
                }
                requestAnimationFrame(tick);
                io2.unobserve(el);
              });
            },
            { threshold: 0.4 }
          );
          io2.observe(el);
        }
      });
    }

    const catLabels = PSTR.cat;
    let activeFilter = "all";
    let searchTerm = "";

    function projectCategoryOfClient(client) {
      const cats = new Set(client.entries.map((e) => e.category));
      return Array.from(cats);
    }

    function renderProjects() {
      const term = searchTerm.trim().toLowerCase();
      const filteredClients = KLS_PROJECTS.map((c) => {
        const entries = c.entries.filter((e) => {
          const matchesCat = activeFilter === "all" || e.category === activeFilter;
          const haystack = `${c.client} ${e.desc} ${e.location}`.toLowerCase();
          const matchesTerm = !term || haystack.includes(term);
          return matchesCat && matchesTerm;
        });
        return { ...c, entries };
      }).filter((c) => c.entries.length > 0);

      if (!filteredClients.length) {
        projectList.innerHTML = `<div class="empty-state">${PSTR.empty}</div>`;
        return;
      }

      projectList.innerHTML = filteredClients
        .map((c, idx) => {
          const cats = projectCategoryOfClient(c);
          const tagHtml = cats
            .map((cat) => `<span class="tag ${cat !== "power" ? "re" : ""}">${catLabels[cat] || cat}</span>`)
            .join("");
          const entriesHtml = c.entries
            .slice()
            .sort((a, b) => (b.year || 0) - (a.year || 0))
            .map(
              (e) => `<div class="p-entry">
                <div>${escapeHtml(e.desc)}${e.capacity ? ` <span class="mono small">(${escapeHtml(e.capacity)})</span>` : ""}<div class="loc">${escapeHtml(e.location || "")}</div></div>
                <div class="yr">${e.year || "—"}</div>
              </div>`
            )
            .join("");
          return `<div class="project-card ${idx < 3 ? "is-open" : ""}">
            <div class="summary" role="button" tabindex="0" aria-expanded="${idx < 3 ? "true" : "false"}">
              <div>
                <div class="client">${escapeHtml(c.client)}</div>
                <div class="meta">${tagHtml}<span class="tag">${c.entries.length} ${c.entries.length > 1 ? PSTR.listedMany : PSTR.listedOne}</span></div>
              </div>
              <span class="chevron" aria-hidden="true"></span>
            </div>
            <div class="entries-outer"><div class="entries">${entriesHtml}</div></div>
          </div>`;
        })
        .join("");

      // Smooth expand/collapse via JS-driven max-height (native <details> jumps instantly).
      projectList.querySelectorAll(".project-card").forEach((card) => {
        const summary = card.querySelector(".summary");
        const outer = card.querySelector(".entries-outer");
        function setOpen(open) {
          card.classList.toggle("is-open", open);
          summary.setAttribute("aria-expanded", String(open));
          if (open) {
            outer.style.maxHeight = outer.scrollHeight + "px";
          } else {
            outer.style.maxHeight = outer.scrollHeight + "px"; // set current height first for a smooth close
            requestAnimationFrame(() => { outer.style.maxHeight = "0px"; });
          }
        }
        if (card.classList.contains("is-open")) outer.style.maxHeight = outer.scrollHeight + "px";
        summary.addEventListener("click", () => setOpen(!card.classList.contains("is-open")));
        summary.addEventListener("keydown", (e) => {
          if (e.key === "Enter" || e.key === " ") {
            e.preventDefault();
            setOpen(!card.classList.contains("is-open"));
          }
        });
      });
      // Recalculate open cards' heights after fonts/images settle and on resize.
      window.addEventListener("resize", () => {
        projectList.querySelectorAll(".project-card.is-open .entries-outer").forEach((outer) => {
          outer.style.maxHeight = outer.scrollHeight + "px";
        });
      });
    }

    document.querySelectorAll("[data-project-filter]").forEach((chip) => {
      chip.addEventListener("click", () => {
        document.querySelectorAll("[data-project-filter]").forEach((c) => c.classList.remove("is-active"));
        chip.classList.add("is-active");
        activeFilter = chip.getAttribute("data-project-filter");
        renderProjects();
      });
    });
    const searchInput = document.querySelector("[data-project-search]");
    searchInput &&
      searchInput.addEventListener("input", (e) => {
        searchTerm = e.target.value;
        renderProjects();
      });

    renderProjects();
  }

  /* ---------------- Data-driven strips (Key Clients / Partners / Advisors / People preview) ---------------- */
  /* Rendered here (not as inline <script> in page content) because this file */
  /* loads after assets/js/data.js — putting the render call inline in the    */
  /* page body ran it before KLS_KEY_CLIENTS etc. existed, leaving it empty.  */
  function renderLogoStrip(selector, list) {
    const el = document.querySelector(selector);
    if (!el || !list) return;
    el.innerHTML = list
      .map((c) => `<div class="logo-cell"><a href="${c.url}" target="_blank" rel="noopener">${escapeHtml(c.name)}</a></div>`)
      .join("");
  }
  renderLogoStrip("[data-key-clients]", typeof KLS_KEY_CLIENTS !== "undefined" ? KLS_KEY_CLIENTS : null);
  renderLogoStrip("[data-partners]", typeof KLS_PARTNERS !== "undefined" ? KLS_PARTNERS : null);
  renderLogoStrip("[data-advisors]", typeof KLS_ADVISORS !== "undefined" ? KLS_ADVISORS : null);

  const peoplePreview = document.querySelector("[data-people-preview]");
  if (peoplePreview && typeof KLS_PEOPLE !== "undefined") {
    peoplePreview.innerHTML = KLS_PEOPLE.slice(0, 4)
      .map(
        (p) => `<a href="our-people.html" class="person-card" style="text-decoration:none;">
        <div class="person-photo"><img src="${p.image}" alt="Photo of ${escapeHtml(p.name)}" loading="lazy"></div>
        <div class="person-info">
          <span class="role">${escapeHtml(p.role)}</span>
          <h3>${escapeHtml(p.shortName || p.name)}</h3>
        </div>
      </a>`
      )
      .join("");
  }

  /* ---------------- Contact form ---------------- */
  const form = document.querySelector("[data-contact-form]");
  if (form) {
    const FORM_LANG = document.documentElement.getAttribute("lang") === "ms" ? "ms" : "en";
    const FSTR = {
      en: {
        name: "Please enter your name.",
        email: "Please enter a valid email address.",
        phone: "Please enter a valid phone number.",
        message: "Please enter a message of at least 10 characters.",
        fixFields: "Please fix the highlighted fields before sending.",
        sending: "Sending…",
        success: "Thank you — your enquiry has been prepared. Connect this form to your email or API backend to deliver it to the KLS team.",
      },
      ms: {
        name: "Sila masukkan nama anda.",
        email: "Sila masukkan alamat e-mel yang sah.",
        phone: "Sila masukkan nombor telefon yang sah.",
        message: "Sila masukkan mesej sekurang-kurangnya 10 aksara.",
        fixFields: "Sila betulkan ruangan yang ditanda sebelum menghantar.",
        sending: "Menghantar…",
        success: "Terima kasih — pertanyaan anda telah disediakan. Sambungkan borang ini ke e-mel atau backend API anda untuk menghantarnya kepada pasukan KLS.",
      },
    }[FORM_LANG];

    const status = form.querySelector("[data-form-status]");
    function setError(field, message) {
      const wrap = field.closest(".field");
      if (!wrap) return;
      wrap.classList.toggle("has-error", Boolean(message));
      const errEl = wrap.querySelector(".field-error");
      if (errEl) errEl.textContent = message || "";
    }
    function validate() {
      let ok = true;
      const name = form.querySelector("#name");
      const email = form.querySelector("#email");
      const phone = form.querySelector("#phone");
      const message = form.querySelector("#message");

      if (!name.value.trim()) {
        setError(name, FSTR.name);
        ok = false;
      } else setError(name, "");

      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailPattern.test(email.value.trim())) {
        setError(email, FSTR.email);
        ok = false;
      } else setError(email, "");

      if (phone.value.trim() && !/^[0-9+\-\s()]{7,}$/.test(phone.value.trim())) {
        setError(phone, FSTR.phone);
        ok = false;
      } else setError(phone, "");

      if (!message.value.trim() || message.value.trim().length < 10) {
        setError(message, FSTR.message);
        ok = false;
      } else setError(message, "");

      return ok;
    }

    form.addEventListener("submit", (e) => {
      e.preventDefault();
      status.className = "form-status";
      status.textContent = "";
      if (!validate()) {
        status.className = "form-status is-error";
        status.textContent = FSTR.fixFields;
        return;
      }
      const submitBtn = form.querySelector('[type="submit"]');
      submitBtn.disabled = true;
      submitBtn.dataset.originalText = submitBtn.textContent;
      submitBtn.textContent = FSTR.sending;

      // Frontend-only placeholder. Wire this up to your email/API backend —
      // e.g. POST the FormData below to your endpoint of choice.
      const payload = Object.fromEntries(new FormData(form).entries());
      setTimeout(() => {
        console.log("KLS contact form — ready to submit to backend:", payload);
        submitBtn.disabled = false;
        submitBtn.textContent = submitBtn.dataset.originalText;
        status.className = "form-status is-success";
        status.textContent = FSTR.success;
        form.reset();
      }, 700);
    });
  }

  /* ---------------- utils ---------------- */
  function escapeHtml(str) {
    return String(str == null ? "" : str).replace(/[&<>"']/g, (m) => ({
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&#39;",
    }[m]));
  }
})();
