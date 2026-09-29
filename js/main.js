/* Arkham & Co — "Line to Gold"
   Every section begins as a gold hairline and is gilded into content as you scroll.
   GSAP (ScrollTrigger, SplitText, DrawSVG, ScrambleText, Flip, CustomEase) + Lenis + a WebGL gold shader (gold.js). */
(function () {
  "use strict";

  const root = document.documentElement;
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const fine = window.matchMedia("(pointer: fine)").matches;
  const skipIntro = new URLSearchParams(location.search).has("skip");
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
  const lerp = (a, b, t) => a + (b - a) * t;
  const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

  // The Google Fonts stylesheet loads without blocking the page, so "fonts ready" must first wait for the stylesheet
  // itself, then for Fraunces to arrive. Everything that measures text waits on this.
  const fontsLoaded = (() => {
    const link = document.querySelector('link[href*="fonts.googleapis.com/css2"]');
    const sheet = new Promise((resolve) => {
      if (!link || (link.rel === "stylesheet" && link.sheet)) return resolve();
      link.addEventListener("load", resolve, { once: true });
      link.addEventListener("error", resolve, { once: true });
    });
    if (!document.fonts) return sheet;
    return sheet
      .then(() => Promise.all([document.fonts.load('300 64px "Fraunces"'), document.fonts.load('400 16px "Inter"')]))
      .then(() => document.fonts.ready)
      .catch(() => {});
  })();
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);

  const INK = "#f3efe6";
  const GOLD = "#e4c282";
  const GHOST = "#2f2d29";

  gsap.registerPlugin(ScrollTrigger, SplitText, DrawSVGPlugin, ScrambleTextPlugin, Flip, CustomEase);
  CustomEase.create("silk", "M0,0 C0.7,0 0.2,1 1,1");
  ScrollTrigger.config({ ignoreMobileResize: true });

  const PROJECTS = [
    {
      title: "EESOY",
      idx: "Project 01",
      image: "img/eesoy.webp",
      link: "https://arkham-co.vercel.app/eesoy/index.html",
      desc: "A fresh soy business selling drinks and food. We built a cart system and a simpler way to order, so customers can buy in a few taps, and gave the shop a clean, fresh look that makes it feel distinct and professional.",
      meta: [["Industry", "Food & drink"], ["We built", "Design, development, cart & ordering"], ["Year", "2026"]],
    },
    {
      title: "KLS",
      idx: "Project 02",
      image: "img/kls.webp",
      link: "https://arkham-co.vercel.app/klseri/kls-website/index.html",
      desc: "A corporate website for Kejuruteraan Letrik Seri, a Malaysian electrical engineering and renewable-energy interconnection contractor in business since 1984. It covers the company story and timeline, the industries it serves, key projects and certifications, and opens with an animated year counter.",
      meta: [["Industry", "Electrical engineering"], ["We built", "Design, development, motion"], ["Status", "In progress, 2026"]],
    },
    {
      title: "Arkairi",
      idx: "Project 03",
      image: "img/arkairi.webp",
      link: "https://www.arkairi.lol",
      desc: "A portfolio for a web designer and developer: a real-time 3D logo you can press and hold, a sideways project gallery, and a terminal that types itself as you scroll.",
      meta: [["Industry", "Personal brand"], ["We built", "Design, development, WebGL"], ["Year", "2026"]],
    },
  ];

  /* ------------------------------------------------------------------ smooth scroll */
  let lenis = null;
  function initScroll() {
    if (reduced) return;
    lenis = new Lenis({ lerp: 0.09, wheelMultiplier: 0.95 });
    lenis.on("scroll", ScrollTrigger.update);
    gsap.ticker.add((t) => lenis.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);
  }
  const stopScroll = () => (lenis ? lenis.stop() : (root.style.overflow = "hidden"));
  const startScroll = () => (lenis ? lenis.start() : (root.style.overflow = ""));
  const yOf = (el) => el.getBoundingClientRect().top + window.scrollY;
  function scrollToY(y, opts = {}) {
    if (lenis) lenis.scrollTo(y, { immediate: Boolean(opts.immediate), duration: opts.duration || 1.4, force: true });
    else window.scrollTo({ top: y, behavior: opts.immediate || reduced ? "auto" : "smooth" });
  }

  /* ------------------------------------------------------------------ helpers */
  function makeGrain() {
    const el = $(".grain");
    if (!el) return;
    const c = document.createElement("canvas");
    c.width = c.height = 180;
    const ctx = c.getContext("2d");
    const img = ctx.createImageData(180, 180);
    for (let i = 0; i < img.data.length; i += 4) {
      const v = (Math.random() * 255) | 0;
      img.data[i] = img.data[i + 1] = img.data[i + 2] = v;
      img.data[i + 3] = 255;
    }
    ctx.putImageData(img, 0, 0);
    el.style.backgroundImage = `url(${c.toDataURL()})`;
  }

  // Wraps every character in a span (keeping nested elements like <em>), so two copies of a line split identically.
  function splitChars(el) {
    const out = [];
    const walk = (node) => {
      Array.from(node.childNodes).forEach((n) => {
        if (n.nodeType === 3) {
          const frag = document.createDocumentFragment();
          for (const c of n.textContent) {
            const s = document.createElement("span");
            s.className = c === " " ? "ch sp" : "ch";
            s.textContent = c;
            frag.appendChild(s);
            out.push(s);
          }
          n.replaceWith(frag);
        } else if (n.nodeType === 1) walk(n);
      });
    };
    walk(el);
    return out;
  }

  // An arch: straight sides, rounded top corners of radius r (r = w/2 gives a full semicircle).
  function archPath(x, y, w, h, r) {
    r = Math.max(0, Math.min(r, w / 2, h));
    const f = (v) => v.toFixed(2);
    return `M${f(x)} ${f(y + h)} V${f(y + r)} A${f(r)} ${f(r)} 0 0 1 ${f(x + r)} ${f(y)} H${f(x + w - r)} A${f(r)} ${f(r)} 0 0 1 ${f(x + w)} ${f(y + r)} V${f(y + h)}`;
  }

  /* ================================================================== 00 HERO */
  const hero = { expand: 0, cool: 0, fill: 0, visible: true, live: false, geom: null, cur: null, gold: null, st: null };

  function initHero() {
    const pin = $(".hero-pin");
    const archGold = $(".arch-gold");
    const fallback = $(".gold-fallback");
    const P = {
      baseL: $(".al-base-l"),
      baseR: $(".al-base-r"),
      outer: $(".al-outer"),
      inner: $(".al-inner"),
      dimW: $(".al-dim-w"),
      dimH: $(".al-dim-h"),
      labelW: $(".al-label-w"),
      labelH: $(".al-label-h"),
    };
    hero.pin = pin;
    hero.paths = P;

    if (window.GoldLiquid && GoldLiquid.supported()) {
      try {
        hero.gold = new GoldLiquid($(".gold-canvas"), { quality: fine ? 0.62 : 0.5, fill: 0, zoom: 0.95, wakeRadius: 88, wakeAmp: 0.2, static: reduced });
        hero.gold.onLost = () => root.classList.add("no-gl");
      } catch (err) {
        console.warn("Gold shader unavailable, using the still version.", err);
        hero.gold = null;
      }
    }
    if (!hero.gold) root.classList.add("no-gl");

    function apply() {
      const g = hero.geom;
      const e = hero.expand;
      const left = lerp(g.left, 0, e);
      const top = lerp(g.top, 0, e);
      const W = lerp(g.W, g.vw, e);
      const H = lerp(g.H, g.vh, e);
      const r = (g.W / 2) * (1 - clamp(e * 1.4, 0, 1));
      hero.cur = { left, top, W, H, r };
      const f = (v) => v.toFixed(2) + "px";
      archGold.style.clipPath = `inset(${f(top)} ${f(g.vw - left - W)} ${f(g.vh - top - H)} ${f(left)} round ${f(r)} ${f(r)} 0px 0px)`;

      P.outer.setAttribute("d", archPath(left - 10, top - 10, W + 20, H + 10, r + 10));
      P.inner.setAttribute("d", archPath(left - 22, top - 22, W + 44, H + 22, r + 22));
      const by = (top + H).toFixed(2);
      P.baseL.setAttribute("d", `M${(g.vw / 2).toFixed(2)} ${by} H0`);
      P.baseR.setAttribute("d", `M${(g.vw / 2).toFixed(2)} ${by} H${g.vw}`);

      const dy = g.top - 34;
      const dx = g.left + g.W + 40;
      P.dimW.setAttribute("d", `M${g.left} ${dy} H${g.left + g.W} M${g.left} ${dy - 6} V${dy + 6} M${g.left + g.W} ${dy - 6} V${dy + 6}`);
      P.dimH.setAttribute("d", `M${dx} ${g.top} V${g.top + g.H} M${dx - 6} ${g.top} H${dx + 6} M${dx - 6} ${g.top + g.H} H${dx + 6}`);
      P.labelW.setAttribute("x", g.left + g.W / 2);
      P.labelW.setAttribute("y", dy - 12);
      P.labelW.setAttribute("text-anchor", "middle");
      P.labelH.setAttribute("text-anchor", "middle");
      P.labelH.setAttribute("transform", `translate(${dx + 16} ${g.top + g.H / 2}) rotate(90)`);

      if (hero.gold) {
        hero.gold.arch = { left: g.left, top: g.top, width: g.W, height: g.H };
        hero.gold.clip = { left, top, width: W, height: H, radius: r };
        if (!hero.gold.running) hero.gold.render();
      }
      else fallback.style.clipPath = hero.fill >= 1 ? "none" : `inset(${(g.top + g.H * (1 - clamp(hero.fill, 0, 1))).toFixed(1)}px 0px 0px 0px)`;
    }

    function measure() {
      const vw = pin.clientWidth;
      const vh = pin.clientHeight;
      let W, H, top;
      if (vw < 760) {
        W = Math.min(vw * 0.7, 380);
        H = Math.min(vh * 0.48, W * 1.6);
        top = vh * 0.19;
      } else {
        H = vh * 0.72;
        W = Math.min(H * 0.62, vw * 0.34);
        top = vh * 0.15;
      }
      hero.geom = { vw, vh, W, H, top, left: (vw - W) / 2 };
      pin.style.setProperty("--al", hero.geom.left + "px");
      pin.style.setProperty("--at", top + "px");
      pin.style.setProperty("--aw", W + "px");
      pin.style.setProperty("--ah", H + "px");
      apply();
    }

    hero.apply = apply;
    hero.setFill = (v) => {
      hero.fill = v;
      if (hero.gold) hero.gold.fill = v;
      else apply();
    };
    hero.setCool = () => {
      if (hero.gold) hero.gold.cool = hero.cool;
      else fallback.style.filter = `brightness(${(1 - hero.cool * 0.85).toFixed(3)})`;
    };
    measure();
    window.addEventListener("resize", measure);
    // While pinned, the stage keeps its old size until ScrollTrigger refreshes, so measure again after every refresh.
    ScrollTrigger.addEventListener("refresh", measure);

    // Two copies of the headline: ivory on black, ink on gold (clipped to the arch). Split them identically.
    const lightChars = [];
    const inkChars = [];
    $$(".hero-title--light .ht-line").forEach((l) => lightChars.push(...splitChars(l)));
    $$(".hero-title--ink .ht-line").forEach((l) => inkChars.push(...splitChars(l)));
    hero.lightChars = lightChars;
    hero.inkChars = inkChars;
    hero.pairs = lightChars.map((el, i) => ({ light: el, ink: inkChars[i], k: 0, last: 0 }));
    hero.lcChars = splitChars($(".lc-word"));

    if (!reduced) {
      gsap.set(lightChars.concat(inkChars), { yPercent: 118, rotate: 7, transformOrigin: "0% 100%" });
      gsap.set([".hero-kicker span", ".hero-lede", ".hero-cta .btn", ".hero-scroll > *"], { autoAlpha: 0 });
    }

    // Is a point (viewport px) over the gold? The cursor turns dark there.
    hero.isOnGold = (x, y) => {
      if (!hero.visible || !hero.cur || hero.cool > 0.5 || hero.fill < 0.9) return false;
      const { left, top, W, H, r } = hero.cur;
      y -= pin.getBoundingClientRect().top;
      if (x < left || x > left + W || y < top || y > top + H) return false;
      if (y < top + r) {
        if (x < left + r) return Math.hypot(x - left - r, y - top - r) <= r;
        if (x > left + W - r) return Math.hypot(x - left - W + r, y - top - r) <= r;
      }
      return true;
    };

    // Staged states are set; stop hiding the hero with CSS before any scroll tween records its starting values.
    root.classList.add("ready");
    heroLetters();

    if (reduced) {
      ScrollTrigger.create({ trigger: ".hero", start: "top bottom", end: "bottom top", onToggle: (s) => (hero.visible = s.isActive) });
      return;
    }

    // Scroll story: the headline parts, the arch swallows the screen, the gold cools to black.
    const tl = gsap.timeline({
      defaults: { ease: "none" },
      scrollTrigger: {
        trigger: ".hero",
        start: "top top",
        end: () => "+=" + Math.round(window.innerHeight * 1.6),
        pin: pin,
        scrub: true,
        invalidateOnRefresh: true,
        onUpdate: () => root.classList.toggle("on-gold", Boolean(hero.cur) && hero.cur.top < 64 && hero.cool < 0.45),
      },
    });
    tl.fromTo(".hero-title .ht-1", { xPercent: 0, autoAlpha: 1 }, { xPercent: -24, autoAlpha: 0, duration: 0.3, ease: "power2.in", immediateRender: false }, 0.02)
      .fromTo(".hero-title .ht-2", { xPercent: 0, autoAlpha: 1 }, { xPercent: 24, autoAlpha: 0, duration: 0.3, ease: "power2.in", immediateRender: false }, 0.02)
      .fromTo([".hero-kicker", ".hero-foot", ".hero-scroll"], { autoAlpha: 1, y: 0 }, { autoAlpha: 0, y: -26, duration: 0.14, immediateRender: false }, 0.01)
      .fromTo(
        hero,
        { expand: 0 },
        {
          expand: 1,
          duration: 0.56,
          ease: "power2.inOut",
          immediateRender: false,
          onUpdate: () => {
            apply();
            if (hero.gold) hero.gold.zoom = 0.95 - 0.3 * hero.expand;
          },
        },
        0.1,
      )
      .fromTo(hero, { cool: 0 }, { cool: 1, duration: 0.34, ease: "power1.inOut", immediateRender: false, onUpdate: hero.setCool }, 0.64)
      .fromTo(".arch-lines", { autoAlpha: 1 }, { autoAlpha: 0, duration: 0.2, immediateRender: false }, 0.45)
      // "Keep scrolling" while the gold fills the screen and cools, gone before the studio arrives.
      .fromTo(".hero-keep", { autoAlpha: 0, y: 24 }, { autoAlpha: 1, y: 0, duration: 0.1, ease: "power2.out" }, 0.5)
      .fromTo(".hero-keep", { autoAlpha: 1, y: 0 }, { autoAlpha: 0, y: -24, duration: 0.08, ease: "power2.in", immediateRender: false }, 0.9)
      .set({}, {}, 1);
    hero.st = tl.scrollTrigger;

    ScrollTrigger.create({ trigger: ".hero", start: "top bottom", end: "bottom top", onToggle: (s) => (hero.visible = s.isActive) });
  }

  // Letters near the pointer grow heavier and softer, like warm metal, and blush gold.
  function heroLetters() {
    const pairs = hero.pairs;
    const pointer = { x: -1e4, y: -1e4, t: -1e4 };
    if (fine && !reduced) {
      window.addEventListener(
        "pointermove",
        (e) => {
          pointer.x = e.clientX;
          pointer.y = e.clientY;
          pointer.t = performance.now();
        },
        { passive: true },
      );
    }
    let radius = 300;
    const measure = () => (radius = parseFloat(getComputedStyle($(".hero-title--light")).fontSize) * 2.3);
    measure();
    window.addEventListener("resize", measure);
    const centres = pairs.map(() => [0, 0]);

    gsap.ticker.add(() => {
      if (!hero.live || !hero.visible) return;
      const calm = performance.now() - pointer.t > 2600 || (hero.st && hero.st.progress > 0.2);
      if (!calm) {
        // Read every position first, then write, so the browser lays out once per frame.
        for (let i = 0; i < pairs.length; i++) {
          const r = pairs[i].light.getBoundingClientRect();
          centres[i][0] = r.left + r.width / 2;
          centres[i][1] = r.top + r.height / 2;
        }
      }
      for (let i = 0; i < pairs.length; i++) {
        const p = pairs[i];
        let target = 0;
        if (!calm) target = Math.pow(clamp(1 - Math.hypot(pointer.x - centres[i][0], pointer.y - centres[i][1]) / radius, 0, 1), 1.5);
        p.k += (target - p.k) * 0.12;
        if (p.k < 0.002) p.k = 0;
        if (Math.abs(p.k - p.last) > 0.003 || (p.k === 0 && p.last !== 0)) {
          p.last = p.k;
          const v = p.k.toFixed(3);
          p.light.style.setProperty("--k", v);
          p.ink.style.setProperty("--k", v);
        }
      }
    });
  }

  function heroEnter(instant) {
    hero.live = true;
    if (instant) {
      gsap.set(hero.lightChars.concat(hero.inkChars), { yPercent: 0, rotate: 0 });
      gsap.set([".hero-kicker span", ".hero-lede", ".hero-cta .btn", ".hero-scroll > *", ".chrome", ".hud"], { autoAlpha: 1, y: 0 });
      return gsap.timeline();
    }
    const ledeSplit = SplitText.create(".hero-lede", { type: "lines", mask: "lines" });
    const tl = gsap.timeline();
    // Letters arrive swollen and gold, then settle to their resting weight.
    hero.pairs.forEach((p, i) => gsap.delayedCall(0.18 + i * 0.026, () => (p.k = 0.9)));
    tl.to(hero.lightChars, { yPercent: 0, rotate: 0, duration: 1.35, ease: "expo.out", stagger: 0.026 }, 0)
      .to(hero.inkChars, { yPercent: 0, rotate: 0, duration: 1.35, ease: "expo.out", stagger: 0.026 }, 0)
      .fromTo(".chrome", { autoAlpha: 0, y: -24 }, { autoAlpha: 1, y: 0, duration: 1.1, ease: "expo.out" }, 0.45)
      .fromTo(".hud", { autoAlpha: 0, y: 16 }, { autoAlpha: 1, y: 0, duration: 1.1, ease: "expo.out" }, 0.65)
      .set(".hero-lede", { autoAlpha: 1 }, 0.55)
      .from(ledeSplit.lines, { yPercent: 105, duration: 1.1, ease: "expo.out", stagger: 0.08 }, 0.55)
      .fromTo(".hero-cta .btn", { autoAlpha: 0, y: 24 }, { autoAlpha: 1, y: 0, duration: 1, ease: "expo.out", stagger: 0.1 }, 0.75)
      .to(".hero-scroll > *", { autoAlpha: 1, duration: 1 }, 1.1)
      // Hand the paragraph back to normal text flow, so it rewraps correctly if the font or width changes later.
      .add(() => ledeSplit.revert(), 1.9);
    $$(".hero-kicker span").forEach((s, i) => {
      const text = s.textContent;
      tl.set(s, { autoAlpha: 1 }, 0.4 + i * 0.18).to(s, { scrambleText: { text, chars: "ARKHAMCO&0123456789", speed: 0.6, revealDelay: 0.25 }, duration: 1.1 }, 0.4 + i * 0.18);
    });
    return tl;
  }

  // Loading: the arch is drafted in gold hairlines and measured, the counter runs, then molten gold pours in.
  async function runIntro() {
    const P = hero.paths;
    const lines = [P.baseL, P.baseR, P.outer, P.inner, P.dimW, P.dimH];
    const fontsReady = Promise.race([fontsLoaded, wait(3500)]);
    const cleanLines = () => lines.forEach((p) => {
      p.style.strokeDasharray = "";
      p.style.strokeDashoffset = "";
    });

    if (reduced || skipIntro) {
      hero.setFill(1.2);
      gsap.set([".al-dims", ".loader-center"], { autoAlpha: 0 });
      heroEnter(reduced);
      return;
    }

    const count = $("[data-count]");
    const counter = { v: 0 };
    const dim = { w: 0, h: 0 };
    const g = hero.geom;
    gsap.set(lines, { drawSVG: "0%" });
    gsap.set([P.labelW, P.labelH], { autoAlpha: 0 });
    gsap.set(hero.lcChars, { yPercent: 120 });
    gsap.set(".lc-count > span", { yPercent: 120 });

    const draw = gsap.timeline();
    draw
      .to([P.baseL, P.baseR], { drawSVG: "100%", duration: 1.3, ease: "silk" }, 0)
      .to(P.outer, { drawSVG: "100%", duration: 1.9, ease: "silk" }, 0.15)
      .to(P.inner, { drawSVG: "100%", duration: 1.9, ease: "silk" }, 0.3)
      .to([P.dimW, P.dimH], { drawSVG: "100%", duration: 1.1, ease: "power3.inOut", stagger: 0.15 }, 0.75)
      .to([P.labelW, P.labelH], { autoAlpha: 1, duration: 0.4 }, 1.2)
      .to(
        dim,
        {
          w: g.W,
          h: g.H,
          duration: 1.4,
          ease: "power2.out",
          onUpdate: () => {
            P.labelW.textContent = `W ${Math.round(dim.w)}`;
            P.labelH.textContent = `H ${Math.round(dim.h)}`;
          },
        },
        1.2,
      )
      .to(hero.lcChars, { yPercent: 0, duration: 1.2, ease: "expo.out", stagger: 0.04 }, 0.55)
      .to(".lc-count > span", { yPercent: 0, duration: 1, ease: "expo.out", stagger: 0.08 }, 0.8)
      .to(counter, { v: 100, duration: 2.4, ease: "power2.inOut", onUpdate: () => (count.textContent = String(Math.round(counter.v)).padStart(3, "0")) }, 0.4);

    await Promise.all([draw, fontsReady]);

    const out = gsap.timeline();
    out
      .to(hero.lcChars, { yPercent: -120, duration: 0.7, ease: "expo.in", stagger: 0.025 }, 0)
      .to(".lc-count > span", { yPercent: -120, duration: 0.6, ease: "expo.in", stagger: 0.05 }, 0.05)
      .to(".al-dims", { autoAlpha: 0, duration: 0.5 }, 0.1)
      .to(hero, { fill: 1.12, duration: 1.8, ease: "power2.inOut", onUpdate: () => hero.setFill(hero.fill) }, 0.45)
      .set(".loader-center", { autoAlpha: 0 }, 1)
      .add(() => heroEnter(false), 1.95);
    await out;
    cleanLines();
  }

  /* ================================================================== 01 STUDIO */
  function initStudio() {
    const text = $(".man-text");
    const split = SplitText.create(text, { type: "words", wordsClass: "mw" });
    const words = split.words.filter((w) => !w.closest(".pill"));
    words.forEach((w) => w.closest(".gw") && w.classList.add("mw-gold"));
    const target = (w) => (w.classList.contains("mw-gold") ? GOLD : INK);
    const pills = $$(".pill", text);
    const lineP = $(".pill-line path", text);

    if (reduced) {
      words.forEach((w) => (w.style.color = target(w)));
      pills.forEach((p) => p.style.setProperty("--o", "1"));
    } else {
      // The paragraph holds still and lights up word by word; small arches open inside the sentence.
      const n = words.length;
      const tl = gsap.timeline({
        defaults: { ease: "none" },
        scrollTrigger: {
          trigger: ".man-pin",
          start: "top top",
          end: () => "+=" + Math.round(window.innerHeight * 1.3),
          pin: true,
          scrub: 0.5,
          invalidateOnRefresh: true,
        },
      });
      words.forEach((w, i) => tl.fromTo(w, { color: GHOST }, { color: target(w), duration: 3 / n }, (i / n) * 0.9));
      pills.forEach((pill) => {
        let idx = 0;
        words.forEach((w, i) => {
          if (w.compareDocumentPosition(pill) & Node.DOCUMENT_POSITION_FOLLOWING) idx = i;
        });
        const at = (idx / n) * 0.9 + 1 / n;
        tl.fromTo(pill, { "--o": 0 }, { "--o": 1, duration: 0.09, ease: "power2.out" }, at);
        if (lineP && pill.contains(lineP)) tl.fromTo(lineP, { drawSVG: "0%" }, { drawSVG: "100%", duration: 0.1 }, at + 0.04);
      });
      tl.set({}, {}, 1.05);
    }

    // Facts: gold rules draw across, values scramble into place.
    const values = $$(".fact-v");
    if (reduced) return;
    gsap.set(".fact-rule", { scaleX: 0 });
    gsap.set([".fact-v", ".fact-k"], { autoAlpha: 0 });
    ScrollTrigger.create({
      trigger: ".facts",
      start: "top 88%",
      once: true,
      onEnter: () => {
        const tl = gsap.timeline();
        tl.to(".fact-rule", { scaleX: 1, duration: 1.3, ease: "silk", stagger: 0.12 }, 0);
        values.forEach((v, i) => {
          const text = v.textContent;
          tl.set(v, { autoAlpha: 1 }, 0.3 + i * 0.12).to(v, { scrambleText: { text, chars: "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", revealDelay: 0.25, speed: 0.7 }, duration: 1.2 }, 0.3 + i * 0.12);
        });
        tl.fromTo(".fact-k", { autoAlpha: 0, y: 10 }, { autoAlpha: 1, y: 0, duration: 0.9, ease: "expo.out", stagger: 0.12 }, 0.6);
      },
    });
  }

  /* ================================================================== 02 PROCESS */
  // A hand-drawn wireframe of the mock site, in the 1000 x 625 space of the browser view.
  function buildSketch(svg) {
    let seed = 11;
    const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
    const j = (v, a = 2.5) => +(v + (rnd() - 0.5) * a * 2).toFixed(1);
    const seg = (x1, y1, x2, y2) => `M${j(x1)} ${j(y1)} Q${j((x1 + x2) / 2, 5)} ${j((y1 + y2) / 2, 5)} ${j(x2)} ${j(y2)}`;
    const rect = (x, y, w, h) => [seg(x - 5, y, x + w + 6, y), seg(x + w, y - 5, x + w, y + h + 6), seg(x + w + 5, y + h, x - 6, y + h), seg(x, y + h + 5, x, y - 6)].join(" ");
    const wave = (x, y, w, amp = 9) => {
      let d = `M${j(x)} ${j(y)}`;
      let k = 0;
      for (let cx = x; cx < x + w - 1; cx += 26) d += ` Q${j(cx + 13, 2)} ${j(y + (k++ % 2 ? -amp : amp), 2)} ${j(Math.min(cx + 26, x + w), 1)} ${j(y, 1)}`;
      return d;
    };
    const arch = (x, y, w, h) => {
      const r = w / 2;
      return `M${j(x)} ${j(y + h)} L${j(x)} ${j(y + r)} A${r} ${r} 0 0 1 ${j(x + w)} ${j(y + r)} L${j(x + w)} ${j(y + h)} L${j(x - 4)} ${j(y + h)}`;
    };
    const loop = (cx, cy, rx, ry) => {
      let d = "";
      const n = 26;
      for (let i = 0; i <= n + 3; i++) {
        const a = (i / n) * Math.PI * 2 - 0.5;
        const x = cx + Math.cos(a) * rx * (1 + (rnd() - 0.5) * 0.08);
        const y = cy + Math.sin(a) * ry * (1 + (rnd() - 0.5) * 0.12);
        d += (i ? " L" : "M") + x.toFixed(1) + " " + y.toFixed(1);
      }
      return d;
    };
    const shapes = [
      rect(50, 34, 150, 31),
      seg(572, 50, 628, 51),
      seg(662, 50, 718, 49),
      seg(752, 51, 808, 50),
      rect(850, 31, 100, 38),
      wave(62, 157, 410),
      wave(62, 222, 330),
      seg(62, 292, 380, 294),
      seg(62, 322, 300, 321),
      rect(60, 362, 150, 50),
      loop(135, 387, 115, 48),
      "M252 440 Q236 420 216 414 M216 414 L227 409 M216 414 L225 422",
      arch(560, 106, 320, 325),
      seg(590, 205, 850, 425),
      seg(850, 205, 590, 425),
      rect(60, 475, 270, 112),
      rect(365, 475, 270, 112),
      rect(670, 475, 270, 112),
      seg(84, 507, 200, 507),
      seg(389, 507, 505, 507),
      seg(694, 507, 810, 507),
      seg(84, 540, 290, 541),
      seg(389, 540, 595, 539),
      seg(694, 540, 900, 541),
    ];
    const ns = "http://www.w3.org/2000/svg";
    return shapes.map((d) => {
      const p = document.createElementNS(ns, "path");
      p.setAttribute("d", d);
      svg.appendChild(p);
      return p;
    });
  }

  function initProcess() {
    const pin = $(".proc-pin");
    const paths = buildSketch($(".b-sketch"));
    const steps = $$(".step");
    const status = $(".b-status");
    const statusText = $(".b-status-text");
    const url = $(".b-url");
    const urlText = $(".b-url-text");
    const rev = $(".b-rev-text");
    const names = ["Brief", "Design", "Build", "Live"];
    const FINAL = "yourbrand.com.my";
    let stage = -1;
    let urlState = null;
    let revState = null;
    let burstArmed = true;

    const setStage = (i) => {
      if (i === stage) return;
      stage = i;
      steps.forEach((s, k) => s.classList.toggle("is-active", k === i));
      statusText.textContent = names[i];
      status.classList.toggle("is-live", i === 3);
    };

    function render(t) {
      setStage(t < 1 ? 0 : t < 2 ? 1 : t < 3 ? 2 : 3);
      let u;
      if (t < 1) u = "draft-01 · sketch";
      else if (t < 2) u = "draft-02 · layout";
      else if (t < 3.02) u = "localhost:3000";
      else u = FINAL.slice(0, Math.round(clamp((t - 3.05) / 0.35, 0, 1) * FINAL.length));
      if (u !== urlState) {
        urlState = u;
        urlText.textContent = u;
      }
      url.classList.toggle("is-typing", t >= 3.02 && t < 3.5);
      const r = t < 1.55 ? "Revision 1" : t < 1.85 ? "Revision 2" : "Approved ✓";
      if (r !== revState) {
        revState = r;
        rev.textContent = r;
      }
      if (t >= 3.84 && burstArmed) {
        burstArmed = false;
        burst();
      }
      if (t < 3.6) burstArmed = true;
    }

    if (reduced) {
      $(".steps").classList.add("is-all");
      gsap.set(".b-site", { clipPath: "none" });
      gsap.set([".b-wire", ".b-sketch", ".b-grid", ".b-notes", ".b-rev"], { autoAlpha: 0 });
      gsap.set(".phone", { autoAlpha: 1 });
      render(3.5);
      urlText.textContent = FINAL;
      return;
    }

    const codeScroll = $(".b-code-scroll");
    const codeBody = $(".b-code-body");
    const tl = gsap.timeline({
      defaults: { ease: "none" },
      onUpdate() {
        render(this.time());
      },
      scrollTrigger: {
        trigger: pin,
        start: "top top",
        end: () => "+=" + Math.round(window.innerHeight * (window.innerWidth < 900 ? 3.4 : 4.2)),
        pin: true,
        scrub: 0.8,
        invalidateOnRefresh: true,
      },
    });
    const later = { immediateRender: false };

    // 01 Brief: grid, then the sketch draws itself and gets annotated
    tl.fromTo(".b-grid", { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.3 }, 0)
      .fromTo(paths, { drawSVG: "0%" }, { drawSVG: "100%", duration: 0.3, stagger: 0.55 / paths.length }, 0.05)
      .fromTo(".b-note", { autoAlpha: 0, y: 6 }, { autoAlpha: 1, y: 0, duration: 0.12, stagger: 0.08 }, 0.45)
      // 02 Design: grey blocks settle over the sketch, two revisions, approved
      .fromTo(".b-sketch", { autoAlpha: 1 }, { autoAlpha: 0.18, duration: 0.2, ...later }, 1)
      .fromTo(".b-notes", { autoAlpha: 1 }, { autoAlpha: 0, duration: 0.15, ...later }, 1)
      .fromTo(".b-wire i", { scaleX: 0 }, { scaleX: 1, duration: 0.2, stagger: 0.035, ease: "power2.out" }, 1.05)
      .fromTo(".b-rev", { autoAlpha: 0, y: 8 }, { autoAlpha: 1, y: 0, duration: 0.1 }, 1.25)
      .fromTo(".b-wire i:nth-child(6)", { scaleX: 1 }, { scaleX: 0.84, duration: 0.12, ease: "power2.inOut", ...later }, 1.58)
      .fromTo(".b-wire .w-btn-wire", { backgroundColor: "#3b3222" }, { backgroundColor: "#c6a15b", duration: 0.1, ...later }, 1.86)
      // 03 Build: code runs, the real site sweeps in over the wireframe
      .fromTo(".b-rev", { autoAlpha: 1 }, { autoAlpha: 0, duration: 0.08, ...later }, 1.97)
      .fromTo(".b-code", { autoAlpha: 0, y: 40, rotate: -2 }, { autoAlpha: 1, y: 0, rotate: 0, duration: 0.2, ease: "power3.out" }, 2)
      .fromTo(codeScroll, { y: 0 }, { y: () => -Math.max(0, codeScroll.scrollHeight - codeBody.clientHeight + 24), duration: 0.95 }, 2.02)
      .fromTo(".b-site", { clipPath: "inset(0% 100% 0% 0%)" }, { clipPath: "inset(0% 0% 0% 0%)", duration: 0.32, ease: "power2.inOut" }, 2.05)
      .fromTo(".b-sketch", { autoAlpha: 0.18 }, { autoAlpha: 0, duration: 0.15, ...later }, 2.3)
      .fromTo([".b-wire", ".b-grid"], { autoAlpha: 1 }, { autoAlpha: 0, duration: 0.15, ...later }, 2.3)
      .fromTo(".bs-nav > *", { autoAlpha: 0, y: -8 }, { autoAlpha: 1, y: 0, duration: 0.12, stagger: 0.04 }, 2.22)
      .fromTo(".bs-l > span", { yPercent: 110 }, { yPercent: 0, duration: 0.22, stagger: 0.06, ease: "power3.out" }, 2.25)
      .fromTo(".bs-art", { clipPath: "inset(100% 0% 0% 0%)" }, { clipPath: "inset(0% 0% 0% 0%)", duration: 0.3, ease: "power2.out" }, 2.32)
      .fromTo(".bs-sun", { yPercent: 70 }, { yPercent: 0, duration: 0.4, ease: "power2.out" }, 2.36)
      .fromTo([".bs-sub", ".bs-btn"], { autoAlpha: 0, y: 12 }, { autoAlpha: 1, y: 0, duration: 0.15, stagger: 0.06 }, 2.42)
      .fromTo(".bs-card", { autoAlpha: 0, y: 18 }, { autoAlpha: 1, y: 0, duration: 0.18, stagger: 0.06, ease: "power3.out" }, 2.52)
      // 04 Launch: the address types itself, the phone version slides in, someone clicks the button
      .fromTo(".b-code", { autoAlpha: 1, y: 0 }, { autoAlpha: 0, y: 30, duration: 0.15, ...later }, 3)
      .fromTo(".phone", { autoAlpha: 0, y: 70, rotate: 7 }, { autoAlpha: 1, y: 0, rotate: 0, duration: 0.32, ease: "power3.out" }, 3.28)
      .fromTo(".b-cursor", { left: "88%", top: "98%", autoAlpha: 0 }, { left: "11.5%", top: "54.5%", autoAlpha: 1, duration: 0.36, ease: "power2.inOut" }, 3.38)
      .fromTo(".b-cursor svg", { scale: 1 }, { scale: 0.82, duration: 0.03, yoyo: true, repeat: 1, ...later }, 3.78)
      .fromTo(".bs-btn", { scale: 1 }, { scale: 0.93, duration: 0.03, yoyo: true, repeat: 1, ...later }, 3.78)
      .fromTo(".b-click", { scale: 0, autoAlpha: 1 }, { scale: 2.6, autoAlpha: 0, duration: 0.2, ease: "power2.out", ...later }, 3.8)
      .set({}, {}, 4.25);
    render(0);

    // Gold dust bursts from the button the moment the site goes live.
    const dust = $(".b-dust");
    const ctx = dust.getContext("2d");
    const btn = $(".bs-btn");
    let parts = [];
    let running = false;
    let scale = 1;
    function step() {
      const W = dust.width;
      const H = dust.height;
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, W, H);
      ctx.setTransform(scale, 0, 0, scale, 0, 0);
      let alive = 0;
      for (const p of parts) {
        if (p.life <= 0) continue;
        alive++;
        p.vx *= 0.975;
        p.vy = p.vy * 0.975 + 0.09;
        p.x += p.vx;
        p.y += p.vy;
        p.life -= p.decay;
        ctx.globalAlpha = Math.max(0, p.life);
        ctx.fillStyle = `rgb(${p.c})`;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fill();
      }
      if (!alive) {
        gsap.ticker.remove(step);
        running = false;
        ctx.setTransform(1, 0, 0, 1, 0, 0);
        ctx.clearRect(0, 0, W, H);
      }
    }
    function burst() {
      const cr = dust.getBoundingClientRect();
      const br = btn.getBoundingClientRect();
      if (!cr.width) return;
      scale = Math.min(window.devicePixelRatio || 1, 2);
      dust.width = Math.round(cr.width * scale);
      dust.height = Math.round(cr.height * scale);
      const ox = br.left + br.width / 2 - cr.left;
      const oy = br.top + br.height / 2 - cr.top;
      parts = Array.from({ length: 110 }, () => {
        const a = Math.random() * Math.PI * 2;
        const v = 1.2 + Math.random() * 6.5;
        return {
          x: ox,
          y: oy,
          vx: Math.cos(a) * v,
          vy: Math.sin(a) * v - 2.4,
          life: 1,
          decay: 0.01 + Math.random() * 0.018,
          r: 0.6 + Math.random() * 2.2,
          c: Math.random() < 0.7 ? "228,194,130" : "255,244,214",
        };
      });
      if (!running) {
        running = true;
        gsap.ticker.add(step);
      }
    }
  }

  /* ================================================================== 03 WORK */
  let caseOpen = false;
  let returnFocus = null;
  const work = { shown: false, hide: () => {} };

  function initWork() {
    const rows = $$(".w-row[data-project]");
    const list = $(".w-list");
    const preview = $(".w-preview");
    const frame = $(".w-preview-frame");
    const imgs = $$(".w-preview-img", preview);
    let active = -1;
    let mx = 0;
    let my = 0;

    // Rows rise into place as they arrive.
    if (!reduced) {
      $$(".w-row").forEach((row) => {
        const name = $(".w-name-a", row);
        const parts = [$(".w-idx", row), $(".w-type", row), $(".w-year", row), $(".w-arrow", row), $(".w-thumb", row)].filter(Boolean);
        gsap.set(name, { yPercent: 105 });
        gsap.set(parts, { autoAlpha: 0, y: 14 });
        ScrollTrigger.create({
          trigger: row,
          start: "top 92%",
          once: true,
          onEnter: () => {
            gsap.to(name, { yPercent: 0, duration: 1.2, ease: "expo.out", clearProps: "transform" });
            gsap.to(parts, { autoAlpha: 1, y: 0, duration: 1, ease: "expo.out", stagger: 0.06, delay: 0.15, clearProps: "transform" });
          },
        });
      });
    }

    function pan(img) {
      gsap.killTweensOf(img, "y");
      gsap.set(img, { y: 0 });
      const travel = img.offsetHeight - frame.offsetHeight;
      if (travel <= 0) return;
      gsap.to(img, { y: -travel, duration: Math.max(4, travel / 90), ease: "sine.inOut", yoyo: true, repeat: -1, delay: 0.6, repeatDelay: 0.8 });
    }

    function show(i) {
      if (!work.shown) {
        work.shown = true;
        gsap.set(preview, { x: mx, y: my });
        gsap.to(preview, { autoAlpha: 1, scale: 1, duration: 0.7, ease: "expo.out", overwrite: "auto" });
      }
      if (i === active) return;
      const prev = active;
      active = i;
      imgs.forEach((el, k) => (el.style.zIndex = k === i ? 3 : k === prev ? 2 : 1));
      gsap.fromTo(imgs[i], { clipPath: "inset(100% 0% 0% 0%)" }, { clipPath: "inset(0% 0% 0% 0%)", duration: 0.8, ease: "expo.out", overwrite: true });
      const img = imgs[i].firstElementChild;
      gsap.fromTo(img, { scale: 1.22 }, { scale: 1, duration: 1.2, ease: "expo.out" });
      pan(img);
    }

    function hide() {
      if (!work.shown) return;
      work.shown = false;
      active = -1;
      gsap.to(preview, {
        autoAlpha: 0,
        scale: 0.6,
        duration: 0.45,
        ease: "power3.out",
        overwrite: "auto",
        onComplete: () => {
          if (!work.shown) gsap.set(imgs, { clipPath: "inset(100% 0% 0% 0%)" });
        },
      });
    }
    work.hide = hide;

    // Desktop: an arch preview trails the pointer, leaning with its speed.
    if (fine && !reduced) {
      gsap.set(preview, { xPercent: -50, yPercent: -50, scale: 0.6, autoAlpha: 0 });
      const xTo = gsap.quickTo(preview, "x", { duration: 0.7, ease: "power3" });
      const yTo = gsap.quickTo(preview, "y", { duration: 0.7, ease: "power3" });
      const rTo = gsap.quickTo(frame, "rotation", { duration: 0.9, ease: "power3" });
      let vx = 0;
      let lastX = null;
      window.addEventListener(
        "pointermove",
        (e) => {
          mx = e.clientX;
          my = e.clientY;
          if (lastX !== null) vx += (e.clientX - lastX) * 0.35;
          lastX = e.clientX;
          if (work.shown) {
            xTo(mx);
            yTo(my);
          }
        },
        { passive: true },
      );
      gsap.ticker.add(() => {
        vx *= 0.86;
        if (work.shown) rTo(clamp(vx, -14, 14));
      });
      rows.forEach((row) => row.addEventListener("pointerenter", () => !caseOpen && show(Number(row.dataset.project))));
      list.addEventListener("pointerleave", hide);
      $(".w-row--next").addEventListener("pointerenter", hide);
      // Scrolling under a still pointer changes which row it is over.
      if (lenis) {
        lenis.on("scroll", () => {
          if (!work.shown || caseOpen) return;
          const el = document.elementFromPoint(mx, my);
          const row = el && el.closest(".w-row");
          if (!row || !row.dataset.project) hide();
          else show(Number(row.dataset.project));
        });
      }
    }

    rows.forEach((row) => {
      $(".w-btn", row).addEventListener("click", (e) => openCase(Number(row.dataset.project), row, e.currentTarget, work.shown ? frame : null));
    });
    setupCase();
  }

  const caseEl = $(".case");
  const caseParts = () => ({
    frame: $(".case-frame", caseEl),
    img: $(".case-img", caseEl),
    copy: [$(".case-idx", caseEl), $(".case-title", caseEl), $(".case-desc", caseEl), $(".case-meta", caseEl), $(".case-link", caseEl)],
    close: $(".case-close", caseEl),
    bg: $(".case-bg", caseEl),
  });
  let casePan = null;

  // Opening a project: the preview arch (or the row's thumbnail) grows into the case view.
  function openCase(i, row, btn, previewFrame) {
    if (caseOpen) return;
    caseOpen = true;
    returnFocus = btn;
    const p = PROJECTS[i];
    const c = caseParts();
    $(".case-idx", caseEl).textContent = p.idx;
    $(".case-title", caseEl).textContent = p.title;
    $(".case-desc", caseEl).textContent = p.desc;
    $(".case-meta", caseEl).innerHTML = p.meta.map(([k, v]) => `<div><dt>${esc(k)}</dt><dd>${esc(v)}</dd></div>`).join("");
    const link = $(".case-link", caseEl);
    link.href = p.link;
    link.setAttribute("aria-label", `Visit the ${p.title} website (opens in a new tab)`);
    c.img.src = p.image;
    c.img.alt = `Screenshot of the ${p.title} website`;

    const source = previewFrame || $(".w-thumb", row);
    caseEl.hidden = false;
    [$("#main"), $(".foot"), $(".chrome")].forEach((el) => (el.inert = true));
    stopScroll();
    gsap.set([c.frame, ...c.copy, c.close, c.bg, c.img], { clearProps: "all" });

    if (!reduced) {
      const rect = source ? source.getBoundingClientRect() : { width: 0 };
      if (rect.width > 4) {
        Flip.fit(c.frame, source, { scale: true });
        gsap.to(c.frame, { x: 0, y: 0, scaleX: 1, scaleY: 1, rotation: 0, duration: 1.15, ease: "expo.inOut" });
      } else {
        gsap.from(c.frame, { scale: 0.9, autoAlpha: 0, duration: 1, ease: "expo.out" });
      }
      if (previewFrame) gsap.set(".w-preview", { autoAlpha: 0 });
      gsap.fromTo(c.bg, { opacity: 0 }, { opacity: 1, duration: 0.6, ease: "power2.out" });
      gsap.fromTo(c.copy, { autoAlpha: 0, y: 36 }, { autoAlpha: 1, y: 0, duration: 1, ease: "expo.out", stagger: 0.07, delay: 0.45 });
      gsap.fromTo(c.close, { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.5, delay: 0.6 });
      const go = () => {
        if (!caseOpen) return;
        const travel = c.img.offsetHeight - c.frame.offsetHeight;
        if (travel > 0) casePan = gsap.to(c.img, { y: -travel, duration: Math.max(5, travel / 70), ease: "sine.inOut", yoyo: true, repeat: -1, delay: 1.3, repeatDelay: 1 });
      };
      if (c.img.complete && c.img.naturalWidth) go();
      else c.img.addEventListener("load", go, { once: true });
    }
    c.close.focus({ preventScroll: true });
  }

  function closeCase() {
    if (!caseOpen) return;
    caseOpen = false;
    const c = caseParts();
    const done = () => {
      caseEl.hidden = true;
      if (casePan) casePan.kill();
      gsap.set([c.frame, ...c.copy, c.close, c.bg, c.img], { clearProps: "all" });
      [$("#main"), $(".foot"), $(".chrome")].forEach((el) => (el.inert = false));
      work.shown = false;
      work.hide();
      startScroll();
      if (returnFocus) returnFocus.focus({ preventScroll: true });
    };
    if (reduced) return done();
    gsap.to([...c.copy, c.close], { autoAlpha: 0, y: -16, duration: 0.35, stagger: 0.03, ease: "power2.in" });
    gsap.to(c.frame, { scale: 0.86, autoAlpha: 0, duration: 0.55, ease: "power3.in" });
    gsap.to(c.bg, { opacity: 0, duration: 0.5, delay: 0.25, onComplete: done });
  }

  function setupCase() {
    $(".case-close", caseEl).addEventListener("click", closeCase);
    caseEl.addEventListener("keydown", (e) => {
      if (e.key !== "Tab") return;
      const items = $$("a[href], button", caseEl).filter((el) => el.offsetParent !== null);
      const first = items[0];
      const last = items[items.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    });
  }

  /* ================================================================== 04 PRICING */
  function initPricing() {
    $$(".plan").forEach((plan, i) => {
      const svg = $(".plan-trace", plan);
      const path = $("path", svg);
      const price = $("[data-price]", plan);
      const b = 16;

      // The card is an arch: its top radius is half its width. The gold trace starts at the apex.
      const shape = () => {
        const w = plan.offsetWidth;
        const h = plan.offsetHeight;
        const r = w / 2;
        plan.style.borderRadius = `${r}px ${r}px ${b}px ${b}px`;
        svg.setAttribute("viewBox", `0 0 ${w} ${h}`);
        const x0 = 0.5;
        const x1 = w - 0.5;
        const y1 = h - 0.5;
        path.setAttribute("d", `M${w / 2} ${y1} H${b} Q${x0} ${y1} ${x0} ${y1 - b} V${r} A${r - 0.5} ${r - 0.5} 0 0 1 ${x1} ${r} V${y1 - b} Q${x1} ${y1} ${w - b} ${y1} Z`);
      };
      shape();
      if ("ResizeObserver" in window) new ResizeObserver(shape).observe(plan);
      else window.addEventListener("resize", shape);

      if (reduced) return;
      gsap.set(path, { drawSVG: "50% 50%" });
      gsap.set(plan, { autoAlpha: 0, y: 70, rotationX: 10, transformPerspective: 1400 });
      ScrollTrigger.create({
        trigger: plan,
        start: "top 86%",
        once: true,
        onEnter: () => {
          const d = i * 0.14;
          gsap.to(plan, { autoAlpha: 1, y: 0, rotationX: 0, duration: 1.4, ease: "expo.out", delay: d });
          gsap.to(path, {
            drawSVG: "0% 100%",
            duration: 2.2,
            ease: "silk",
            delay: 0.2 + d,
            onComplete: () => {
              path.style.strokeDasharray = "";
              path.style.strokeDashoffset = "";
            },
          });
          gsap.to(price, { scrambleText: { text: price.textContent, chars: "0123456789", revealDelay: 0.4, speed: 0.5 }, duration: 1.6, delay: 0.5 + d });
          gsap.from($$("li", plan), { autoAlpha: 0, x: -12, duration: 0.8, stagger: 0.06, ease: "expo.out", delay: 0.55 + d });
        },
      });

      if (!fine) return;
      // Gold foil: the card tilts toward the pointer and a sheen follows it.
      const rx = gsap.quickTo(plan, "rotationX", { duration: 0.7, ease: "power3" });
      const ry = gsap.quickTo(plan, "rotationY", { duration: 0.7, ease: "power3" });
      plan.addEventListener("pointermove", (e) => {
        const r = plan.getBoundingClientRect();
        const nx = clamp((e.clientX - r.left) / r.width, 0, 1);
        const ny = clamp((e.clientY - r.top) / r.height, 0, 1);
        ry((nx - 0.5) * 10);
        rx(-(ny - 0.5) * 8);
        plan.style.setProperty("--mx", (nx * 100).toFixed(1) + "%");
        plan.style.setProperty("--my", (ny * 100).toFixed(1) + "%");
        plan.style.setProperty("--fa", (nx * 180 + ny * 90).toFixed(1) + "deg");
      });
      plan.addEventListener("pointerleave", () => {
        rx(0);
        ry(0);
      });
    });
  }

  /* ================================================================== Marquee */
  function initMarquee() {
    if (reduced) return;
    const items = $$(".mq-row").map((row) => ({ row, track: $(".mq-track", row), x: 0, w: 1, dir: Number(row.dataset.dir) || 1 }));
    const measure = () =>
      items.forEach((it) => {
        it.w = it.track.offsetWidth || 1;
        const need = Math.ceil((window.innerWidth * 2) / it.w) + 1;
        while (it.row.children.length < need) {
          const copy = it.track.cloneNode(true);
          copy.setAttribute("aria-hidden", "true");
          it.row.appendChild(copy);
        }
      });
    measure();
    fontsLoaded.then(measure);
    window.addEventListener("resize", measure);

    let active = false;
    let vel = 0;
    let sign = 1;
    let skew = 0;
    ScrollTrigger.create({
      trigger: ".marquee",
      start: "top bottom",
      end: "bottom top",
      onToggle: (s) => (active = s.isActive),
      onUpdate: (s) => {
        vel = s.getVelocity();
        if (vel) sign = Math.sign(vel);
      },
    });
    // Speed and lean follow the scroll; direction follows it too.
    gsap.ticker.add((time, dt) => {
      if (!active) return;
      const boost = clamp(Math.abs(vel) / 320, 0, 14);
      skew += (clamp(-vel / 260, -8, 8) - skew) * 0.1;
      vel *= 0.9;
      const k = dt / 16.7;
      items.forEach((it) => {
        it.x -= (0.6 + boost) * it.dir * sign * k;
        while (it.x <= -it.w) it.x += it.w;
        while (it.x > 0) it.x -= it.w;
        it.row.style.transform = `translate3d(${it.x.toFixed(2)}px,0,0) skewX(${skew.toFixed(2)}deg)`;
      });
    });
  }

  /* ================================================================== Threshold */
  // Between pricing and contact: a doorway draws itself around a line of copy, then the page walks through it.
  function initThreshold() {
    const pin = $(".th-pin");
    const door = $(".th-door");
    const svg = $(".th-arch");
    const a1 = $(".th-a1");
    const a2 = $(".th-a2");
    const glow = $(".th-glow");
    const copy = $$(".th-copy > p");
    const draw = $(".th-draw");
    const drawPath = $(".th-draw path");

    const shape = () => {
      const vw = pin.clientWidth;
      const vh = pin.clientHeight;
      const H = Math.min(vh * 0.66, 640);
      const W = Math.min(H * 0.64, vw * 0.78);
      const left = (vw - W) / 2;
      const top = (vh - H) / 2 + vh * 0.03;
      pin.style.setProperty("--tl", left + "px");
      pin.style.setProperty("--tt", top + "px");
      pin.style.setProperty("--tw", W + "px");
      pin.style.setProperty("--th", H + "px");
      svg.setAttribute("viewBox", `0 0 ${vw} ${vh}`);
      a1.setAttribute("d", archPath(left, top, W, H, W / 2));
      a2.setAttribute("d", archPath(left - 12, top - 12, W + 24, H + 12, W / 2 + 12));
      // Walk toward the middle of the doorway.
      gsap.set(door, { transformOrigin: `${vw / 2}px ${top + H * 0.58}px` });
    };
    shape();
    window.addEventListener("resize", shape);

    if (reduced) return;
    const later = { immediateRender: false };
    gsap
      .timeline({
        defaults: { ease: "none" },
        scrollTrigger: {
          trigger: ".threshold",
          start: "top top",
          end: () => "+=" + Math.round(window.innerHeight * 1.6),
          pin: pin,
          scrub: true,
          invalidateOnRefresh: true,
        },
      })
      // The arch draws out from its crown, and light comes up from the floor.
      .fromTo([a1, a2], { drawSVG: "50% 50%" }, { drawSVG: "0% 100%", duration: 0.3, ease: "power2.out", stagger: 0.04 }, 0)
      .fromTo(glow, { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.3 }, 0.05)
      .fromTo(copy[0], { autoAlpha: 0, y: 30 }, { autoAlpha: 1, y: 0, duration: 0.16, ease: "power2.out" }, 0.12)
      .fromTo(drawPath, { drawSVG: "0%" }, { drawSVG: "100%", duration: 0.18, ease: "power2.inOut" }, 0.2)
      .fromTo(copy[1], { autoAlpha: 0, y: 20 }, { autoAlpha: 1, y: 0, duration: 0.14, ease: "power2.out" }, 0.3)
      // Then walk through it.
      .fromTo([copy[0], draw, copy[1]], { autoAlpha: 1, y: 0 }, { autoAlpha: 0, y: -24, duration: 0.12, stagger: 0.03, ...later }, 0.56)
      .fromTo(door, { scale: 1 }, { scale: 9, duration: 0.44, ease: "power2.in" }, 0.56)
      .fromTo(glow, { autoAlpha: 1 }, { autoAlpha: 0, duration: 0.2, ...later }, 0.8);
  }

  /* ================================================================== 05 CONTACT */
  let contactGold = null;

  function initContact() {
    const mail = $(".c-mail");
    const status = $(".c-status");
    let clearTimer = 0;
    mail.addEventListener("click", async () => {
      const email = mail.dataset.copy;
      try {
        await navigator.clipboard.writeText(email);
        status.textContent = "Email copied. Talk soon.";
      } catch (err) {
        window.location.href = `mailto:${email}`;
        return;
      }
      if (!reduced) gsap.fromTo(status, { autoAlpha: 0, y: 8 }, { autoAlpha: 1, y: 0, duration: 0.5, ease: "expo.out" });
      clearTimeout(clearTimer);
      clearTimer = setTimeout(() => (status.textContent = ""), 3200);
    });

    // The closing headline is filled with the same liquid gold as the hero: a WebGL canvas masked by the text.
    const title = $(".c-title");
    const canvas = $(".c-gold");
    if (window.GoldLiquid && GoldLiquid.supported()) {
      try {
        contactGold = new GoldLiquid(canvas, { mask: true, quality: 1, maxDpr: 1.5, minQuality: 0.6, zoom: 1.15, bright: 0.18, wakeRadius: 46, wakeAmp: 0.3, static: reduced });
      } catch (err) {
        contactGold = null;
      }
    }
    if (!contactGold) {
      root.classList.add("no-cgold");
      canvas.remove();
      if (!reduced) {
        SplitText.create(title, {
          type: "lines",
          mask: "lines",
          autoSplit: true,
          onSplit: (self) => gsap.from(self.lines, { yPercent: 110, duration: 1.3, ease: "expo.out", stagger: 0.1, scrollTrigger: { trigger: title, start: "top 82%", once: true } }),
        });
      }
      return;
    }
    root.classList.add("has-cgold");

    const mask = document.createElement("canvas");
    const mctx = mask.getContext("2d");
    let lines = [];
    let revealed = reduced;
    const state = [];

    function draw() {
      const cr = canvas.getBoundingClientRect();
      if (!cr.width || !lines.length) return;
      const s = Math.min(window.devicePixelRatio || 1, 1.5);
      const W = Math.round(cr.width * s);
      const H = Math.round(cr.height * s);
      if (mask.width !== W || mask.height !== H) {
        mask.width = W;
        mask.height = H;
      }
      mctx.setTransform(1, 0, 0, 1, 0, 0);
      mctx.clearRect(0, 0, W, H);
      mctx.setTransform(s, 0, 0, s, 0, 0);
      const cs = getComputedStyle(title);
      const fs = parseFloat(cs.fontSize);
      const font = `${cs.fontStyle} ${cs.fontWeight} ${cs.fontSize} ${cs.fontFamily}`;
      // Drawing before Fraunces is ready would bake a wider fallback font into the mask.
      if (document.fonts && !document.fonts.check(font)) {
        document.fonts.load(font).then(draw);
        return;
      }
      mctx.font = font;
      if ("letterSpacing" in mctx) mctx.letterSpacing = cs.letterSpacing;
      mctx.textBaseline = "alphabetic";
      mctx.fillStyle = "#fff";
      lines.forEach((line, i) => {
        const st = state[i] || { y: 0, a: 1 };
        const r = line.getBoundingClientRect();
        const text = line.textContent.replace(/\s+$/, "");
        const m = mctx.measureText(text);
        const asc = m.fontBoundingBoxAscent || fs * 0.95;
        const desc = m.fontBoundingBoxDescent || fs * 0.25;
        const base = r.top - cr.top + (r.height - (asc + desc)) / 2 + asc;
        // Canvas text can't take the page's optical-size setting, so fit it to the real text box on the page.
        const range = document.createRange();
        range.selectNodeContents(line);
        const tr = range.getBoundingClientRect();
        const sx = tr.width && m.width ? clamp(tr.width / m.width, 0.8, 1.2) : 1;
        mctx.save();
        mctx.beginPath();
        mctx.rect(0, r.top - cr.top - fs * 0.12, cr.width, r.height + fs * 0.36);
        mctx.clip();
        mctx.globalAlpha = st.a;
        mctx.translate((tr.width ? tr.left : r.left) - cr.left, base + st.y * r.height);
        mctx.scale(sx, 1);
        mctx.fillText(text, 0, 0);
        mctx.restore();
      });
      contactGold.setMask(mask);
    }

    SplitText.create(title, {
      type: "lines",
      linesClass: "c-line",
      autoSplit: true,
      onSplit(self) {
        lines = self.lines;
        while (state.length < lines.length) state.push({ y: revealed ? 0 : 1.1, a: revealed ? 1 : 0 });
        draw();
      },
    });
    if ("ResizeObserver" in window) new ResizeObserver(draw).observe(canvas);
    fontsLoaded.then(draw);

    if (reduced) return;
    ScrollTrigger.create({
      trigger: title,
      start: "top 80%",
      once: true,
      onEnter: () => {
        gsap.to(state, {
          y: 0,
          a: 1,
          duration: 1.5,
          ease: "expo.out",
          stagger: 0.12,
          onUpdate: draw,
          onComplete: () => {
            revealed = true;
            draw();
          },
        });
      },
    });
  }

  /* ================================================================== Footer */
  function initFooter() {
    const chars = splitChars($(".foot-mark"));
    $("[data-to-top]").addEventListener("click", () => scrollToY(0, { duration: 2.6 }));
    if (reduced) return;
    gsap.fromTo(chars, { yPercent: 105 }, { yPercent: 0, ease: "none", stagger: 0.05, scrollTrigger: { trigger: ".foot", start: "top 85%", end: "bottom bottom", scrub: 0.6 } });
    gsap.fromTo(".foot-inner", { yPercent: -16 }, { yPercent: 0, ease: "none", scrollTrigger: { trigger: ".foot", start: "top bottom", end: "bottom bottom", scrub: true } });
  }

  /* ================================================================== Generic reveals */
  function initReveals() {
    if (reduced) return;
    $$(".sec-head").forEach((h) => {
      const idx = $(".sh-idx", h);
      const mark = $(".sh-arch path", h);
      const name = $(".sh-name", h);
      gsap.set(mark, { drawSVG: "0%" });
      gsap.set([idx, name], { autoAlpha: 0 });
      ScrollTrigger.create({
        trigger: h,
        start: "top 88%",
        once: true,
        onEnter: () => {
          gsap.to(mark, { drawSVG: "100%", duration: 1.2, ease: "silk" });
          gsap.set(idx, { autoAlpha: 1 });
          gsap.to(idx, { scrambleText: { text: idx.textContent, chars: "0123456789", speed: 0.5 }, duration: 0.8 });
          gsap.fromTo(name, { autoAlpha: 0, x: -14 }, { autoAlpha: 1, x: 0, duration: 1, ease: "expo.out", delay: 0.35 });
        },
      });
    });
    $$("[data-reveal]").forEach((el) => {
      SplitText.create(el, {
        type: "lines",
        mask: "lines",
        autoSplit: true,
        onSplit: (self) => gsap.from(self.lines, { yPercent: 108, duration: 1.3, ease: "expo.out", stagger: 0.1, scrollTrigger: { trigger: el, start: "top 86%", once: true } }),
      });
    });
    $$("[data-reveal-fade]").forEach((el) => {
      gsap.from(el, { autoAlpha: 0, y: 20, duration: 1.1, ease: "expo.out", scrollTrigger: { trigger: el, start: "top 92%", once: true } });
    });
  }

  /* ================================================================== Cursor */
  function initCursor() {
    if (!fine || reduced) return;
    const cur = $(".cursor");
    const ring = $(".cursor-ring");
    const dot = $(".cursor-dot");
    const label = $(".cursor-label");
    root.classList.add("has-cursor");
    cur.classList.add("is-hidden");
    const rx = gsap.quickTo(ring, "x", { duration: 0.45, ease: "power3" });
    const ry = gsap.quickTo(ring, "y", { duration: 0.45, ease: "power3" });
    const dx = gsap.quickTo(dot, "x", { duration: 0.1, ease: "power3" });
    const dy = gsap.quickTo(dot, "y", { duration: 0.1, ease: "power3" });
    let placed = false;
    let onGold = false;
    window.addEventListener(
      "pointermove",
      (e) => {
        if (e.pointerType !== "mouse") return;
        if (!placed) {
          placed = true;
          gsap.set([ring, dot], { x: e.clientX, y: e.clientY });
          cur.classList.remove("is-hidden");
        }
        rx(e.clientX);
        ry(e.clientY);
        dx(e.clientX);
        dy(e.clientY);
        const g = !caseOpen && hero.isOnGold ? hero.isOnGold(e.clientX, e.clientY) : false;
        if (g !== onGold) {
          onGold = g;
          cur.classList.toggle("on-gold", g);
        }
      },
      { passive: true },
    );
    document.addEventListener("pointerover", (e) => {
      const t = e.target instanceof Element ? e.target : null;
      if (!t) return;
      const labelled = t.closest("[data-cursor]");
      const text = labelled ? labelled.dataset.cursor : "";
      label.textContent = text;
      cur.classList.toggle("is-label", Boolean(text));
      cur.classList.toggle("is-link", !text && Boolean(t.closest("a, button")));
    });
    root.addEventListener("mouseleave", () => cur.classList.add("is-hidden"));
    root.addEventListener("mouseenter", () => placed && cur.classList.remove("is-hidden"));
    window.addEventListener("pointerdown", () => cur.classList.add("is-down"));
    window.addEventListener("pointerup", () => cur.classList.remove("is-down"));
  }

  /* ================================================================== Chrome: HUD, menu, transitions, buttons */
  const menuState = { open: false, busy: false };

  function setMenu(open, instant) {
    if (menuState.open === open) return;
    menuState.open = open;
    const menu = $("#menu");
    const btn = $(".menu-btn");
    btn.setAttribute("aria-expanded", String(open));
    $(".menu-label").textContent = open ? "Close" : "Menu";
    $("#main").inert = open;
    $(".foot").inert = open;
    root.classList.toggle("menu-open", open);
    const R = Math.hypot(window.innerWidth / 2, window.innerHeight) * 1.03;
    const d = instant || reduced ? 0 : 1;

    if (open) {
      stopScroll();
      gsap.set(menu, { visibility: "visible" });
      gsap.fromTo(".menu-bg", { clipPath: "circle(0px at 50% 100%)" }, { clipPath: `circle(${R}px at 50% 100%)`, duration: 0.95 * d, ease: "silk" });
      gsap.fromTo(".m-word", { yPercent: 112 }, { yPercent: 0, duration: 1.1 * d, ease: "expo.out", stagger: 0.06 * d, delay: 0.35 * d });
      gsap.fromTo([".m-i", ".menu-foot"], { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.6 * d, delay: 0.55 * d, stagger: 0.03 * d });
      gsap.fromTo(".menu-arch path", { drawSVG: "0%" }, { drawSVG: "100%", duration: 1.6 * d, ease: "silk", delay: 0.3 * d, stagger: 0.12 * d });
      gsap.delayedCall(0.4 * d, () => menuState.open && menu.focus({ preventScroll: true }));
    } else {
      if (!caseOpen) startScroll();
      gsap.to([".m-i", ".menu-foot", ".m-word"], { autoAlpha: 0, duration: 0.25 * d, overwrite: "auto", onComplete: () => gsap.set([".m-i", ".menu-foot", ".m-word"], { autoAlpha: 1 }) });
      gsap.to(".menu-bg", { clipPath: "circle(0px at 50% 100%)", duration: 0.75 * d, ease: "silk", overwrite: "auto", onComplete: () => gsap.set(menu, { visibility: "hidden" }) });
    }
  }

  // In-page links: a gold arch rises, the page jumps while covered, and the arch leaves through the top.
  function goTo(hash) {
    const id = hash.slice(1);
    const target = id ? document.getElementById(id) : null;
    if (!target || menuState.busy || caseOpen) return;
    // Pinned sections open a little way into their story, so the jump lands on something already drawing.
    const into = { studio: 0.12, process: 0.45 }[id] || 0;
    const y = id === "top" ? 0 : Math.round(yOf(target) + window.innerHeight * into);
    const jump = () => {
      setMenu(false, true);
      scrollToY(y, { immediate: true });
      history.replaceState(null, "", `#${id}`);
      ScrollTrigger.update();
    };
    if (reduced) return jump();

    menuState.busy = true;
    const wipe = $(".wipe");
    const label = $(".wipe-label");
    label.textContent = target.dataset.section || "";
    const R = Math.hypot(window.innerWidth / 2, window.innerHeight) * 1.03;
    gsap
      .timeline({ onComplete: () => (menuState.busy = false) })
      .set(wipe, { visibility: "visible", clipPath: "circle(0px at 50% 100%)" })
      .to(wipe, { clipPath: `circle(${R}px at 50% 100%)`, duration: 0.85, ease: "silk" })
      .fromTo(label, { yPercent: 50, autoAlpha: 0 }, { yPercent: 0, autoAlpha: 1, duration: 0.6, ease: "expo.out" }, "-=0.35")
      .add(jump)
      .set(wipe, { clipPath: `circle(${R}px at 50% 0%)` })
      .to(label, { yPercent: -50, autoAlpha: 0, duration: 0.45, ease: "power2.in" }, "+=0.2")
      .to(wipe, { clipPath: "circle(0px at 50% 0%)", duration: 0.85, ease: "silk" }, "-=0.2")
      .set(wipe, { visibility: "hidden" });
  }

  function initChrome() {
    // Malaysia time
    const clock = $("[data-clock]");
    let fmt;
    try {
      fmt = new Intl.DateTimeFormat("en-GB", { hour: "2-digit", minute: "2-digit", hour12: false, timeZone: "Asia/Kuala_Lumpur" });
    } catch (err) {
      fmt = new Intl.DateTimeFormat("en-GB", { hour: "2-digit", minute: "2-digit", hour12: false });
    }
    const tick = () => (clock.textContent = fmt.format(new Date()));
    tick();
    setInterval(tick, 15000);

    // HUD: which section, and how far through the page
    const hudIdx = $("[data-hud-idx]");
    const hudName = $("[data-hud-name]");
    const hudFill = $("[data-hud-progress]");
    // The current section is the last one whose top has passed the middle of the screen. Worked out on every scroll,
    // so a jump (menu, back to top) can't leave it stale the way enter/leave callbacks can.
    const sections = $$("[data-section]");
    const setSection = () => {
      const line = window.innerHeight * 0.55;
      let current = sections[0];
      for (const sec of sections) if (sec.getBoundingClientRect().top <= line) current = sec;
      if (hudIdx.textContent === current.dataset.index) return;
      hudIdx.textContent = current.dataset.index;
      hudName.textContent = current.dataset.section;
      if (!reduced) gsap.fromTo([hudIdx, hudName], { yPercent: 70, autoAlpha: 0 }, { yPercent: 0, autoAlpha: 1, duration: 0.6, ease: "expo.out", stagger: 0.05, overwrite: true });
    };
    ScrollTrigger.create({
      start: 0,
      end: "max",
      onUpdate: (s) => {
        hudFill.style.strokeDashoffset = (1 - s.progress).toFixed(4);
        setSection();
      },
      onRefresh: setSection,
    });
    ScrollTrigger.create({ trigger: "#studio", start: "top 90px", onToggle: (s) => root.classList.toggle("past-hero", s.isActive || s.progress > 0) , end: "max" });

    // Menu
    $(".menu-btn").addEventListener("click", () => setMenu(!menuState.open));
    document.addEventListener("keydown", (e) => {
      if (e.key !== "Escape") return;
      if (caseOpen) closeCase();
      else if (menuState.open) {
        setMenu(false);
        $(".menu-btn").focus();
      }
    });

    // Anchors
    document.addEventListener("click", (e) => {
      const link = e.target.closest('a[href^="#"]');
      if (!link || link.classList.contains("skip")) return;
      e.preventDefault();
      goTo(link.getAttribute("href"));
    });

    if (!fine || reduced) return;

    // Magnetic buttons
    $$("[data-magnetic]").forEach((el) => {
      const xTo = gsap.quickTo(el, "x", { duration: 0.55, ease: "power3" });
      const yTo = gsap.quickTo(el, "y", { duration: 0.55, ease: "power3" });
      el.addEventListener("pointermove", (e) => {
        const r = el.getBoundingClientRect();
        xTo((e.clientX - (r.left + r.width / 2)) * 0.3);
        yTo((e.clientY - (r.top + r.height / 2)) * 0.3);
      });
      el.addEventListener("pointerleave", () => {
        xTo(0);
        yTo(0);
      });
    });

    // Button fill grows from where the pointer came in, and leaves where it goes out.
    $$(".btn").forEach((btn) => {
      const fill = $(".btn-fill", btn);
      if (!fill) return;
      gsap.set(fill, { xPercent: -50, yPercent: -50, scale: 0 });
      const place = (e) => {
        const r = btn.getBoundingClientRect();
        const x = e.clientX - r.left;
        const y = e.clientY - r.top;
        const size = Math.hypot(Math.max(x, r.width - x), Math.max(y, r.height - y)) * 2.1;
        gsap.set(fill, { left: x, top: y, width: size, height: size });
      };
      btn.addEventListener("pointerenter", (e) => {
        place(e);
        gsap.to(fill, { scale: 1, duration: 0.6, ease: "power3.out", overwrite: true });
        btn.classList.add("is-filled");
      });
      btn.addEventListener("pointerleave", (e) => {
        place(e);
        gsap.to(fill, { scale: 0, duration: 0.5, ease: "power3.out", overwrite: true });
        btn.classList.remove("is-filled");
      });
    });
  }

  // The pointer stirs whichever pool of gold is on screen.
  function initStir() {
    window.addEventListener(
      "pointermove",
      (e) => {
        if (hero.gold && hero.visible && hero.gold.visible) hero.gold.poke(e.clientX, e.clientY);
        if (contactGold && contactGold.visible) contactGold.poke(e.clientX, e.clientY);
      },
      { passive: true },
    );
  }

  /* ================================================================== Boot */
  function boot() {
    makeGrain();
    initScroll();
    stopScroll();
    initCursor();
    // Pinned sections first, top to bottom, so everything below measures with their spacing.
    initHero();
    initStudio();
    initProcess();
    initWork();
    initPricing();
    initMarquee();
    initThreshold();
    initContact();
    initFooter();
    initReveals();
    initChrome();
    initStir();
    if (hero.gold) hero.gold.start();
    if (contactGold) contactGold.start();

    root.classList.add("ready");
    ScrollTrigger.refresh();
    fontsLoaded.then(() => ScrollTrigger.refresh());
    window.addEventListener("load", () => ScrollTrigger.refresh());

    runIntro().then(() => {
      root.classList.remove("is-loading");
      startScroll();
      ScrollTrigger.refresh();
      if (location.hash && location.hash.length > 1) goTo(location.hash);
    });
  }

  try {
    boot();
  } catch (err) {
    console.error(err);
    root.classList.add("fallback", "ready");
    root.classList.remove("is-loading");
    if (lenis) lenis.start();
  }
})();
