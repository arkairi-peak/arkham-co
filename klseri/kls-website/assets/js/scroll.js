/* Scrolling behaviour, every page.
   - Smooth wheel scrolling (Lenis, lerp 0.1), synced with GSAP ScrollTrigger.
     Touch devices keep native scrolling. Paused during the home intro and
     while the menu or a modal is open.
   - Pinned scroll stories ([data-seq], home page, desktop only): the section
     holds still while one scrubbed timeline moves through its panels. Nothing
     switches abruptly: each photo wipes up over the last while the old one
     drifts away, text slides out and in, and scrub smoothing (0.8s) lets the
     motion ease in and out of the pin instead of stopping dead.
   - Quick photo unveils elsewhere. Text is never hidden waiting for a trigger.
   Everything here is skipped for prefers-reduced-motion. */
(function () {
  const { gsap, ScrollTrigger } = window;
  if (!gsap || !ScrollTrigger) return;
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  gsap.registerPlugin(ScrollTrigger);
  const root = document.documentElement;
  const header = document.querySelector(".site-header");
  const headerH = () => (header ? header.offsetHeight : 0);
  let lenis = null;

  // 1. Smooth scrolling
  if (window.Lenis) {
    lenis = new window.Lenis({ lerp: 0.1, smoothWheel: true });
    window.__lenis = lenis;
    lenis.on("scroll", ScrollTrigger.update);
    gsap.ticker.add((t) => lenis.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);

    // In-page anchors glide to their target, clear of the sticky header.
    document.addEventListener("click", (e) => {
      const a = e.target.closest('a[href*="#"]');
      if (!a || e.defaultPrevented) return;
      const url = new URL(a.href, location.href);
      if (url.pathname !== location.pathname || !url.hash || url.hash === "#") return;
      const target = document.getElementById(decodeURIComponent(url.hash.slice(1)));
      if (!target) return;
      e.preventDefault();
      lenis.scrollTo(target, { offset: -(headerH() + 16), duration: 1.2 });
      history.pushState(null, "", url.hash);
    });

    // Hold the page still while something sits on top of it.
    const sync = () => {
      const held = root.classList.contains("intro-lock") || document.querySelector(".nav-overlay.is-open, .modal-overlay.is-open");
      if (held) lenis.stop(); else lenis.start();
    };
    const watch = (el) => new MutationObserver(sync).observe(el, { attributes: true, attributeFilter: ["class"] });
    watch(root);
    document.querySelectorAll("[data-nav-overlay], .modal-overlay").forEach(watch);
    sync();
  }
  const scrollToY = (y) => (lenis ? lenis.scrollTo(y, { duration: 1.4, force: true }) : window.scrollTo({ top: y, behavior: "smooth" }));

  // 2. Pinned scroll stories
  const LEAD = 0.15;   // a short hold before the first change
  const TAIL = 0.3;    // and after the last, so the pin releases gently
  const PER = 0.75;    // viewport heights of scrolling per panel change
  document.querySelectorAll("[data-seq]").forEach((sec) => {
    const panels = [...sec.querySelectorAll("[data-seq-panel]")];
    const n = panels.length;
    if (n < 2) return;
    const media = panels.map((p) => p.querySelector("[data-seq-media]"));
    const pics = media.map((m) => m && m.querySelector("img"));
    const texts = panels.map((p) => p.querySelector("[data-seq-text]"));
    const navs = [...sec.querySelectorAll("[data-seq-nav]")];
    const bar = sec.querySelector("[data-seq-bar]");
    const total = LEAD + (n - 1) + TAIL;
    let current = -1;
    const setCurrent = (i) => {
      if (i === current) return;
      current = i;
      navs.forEach((b) => {
        const on = Number(b.getAttribute("data-seq-nav")) === i;
        b.classList.toggle("is-active", on);
        if (on) b.setAttribute("aria-current", "step"); else b.removeAttribute("aria-current");
      });
    };

    gsap.matchMedia().add("(min-width: 900px)", () => {
      sec.classList.add("is-seq");
      panels.forEach((p, i) => (p.style.zIndex = String(i + 1)));
      gsap.set(media.slice(1), { clipPath: "inset(100% 0% 0% 0%)" });
      gsap.set(texts.slice(1), { autoAlpha: 0, y: 48 });

      const tl = gsap.timeline({
        defaults: { ease: "none" },
        // follows the smoothed timeline, so the step names and bar match what is on screen
        onUpdate() {
          if (bar) gsap.set(bar, { scaleX: this.progress() });
          setCurrent(Math.min(n - 1, Math.max(0, Math.floor(this.time() - LEAD + 0.5))));
        },
        scrollTrigger: {
          trigger: sec,
          start: () => `top ${headerH()}px`,
          end: () => "+=" + Math.round(window.innerHeight * (PER * (n - 1) + 0.35)),
          pin: true,
          scrub: 0.8,
          anticipatePin: 1,
          invalidateOnRefresh: true,
        },
      });
      for (let i = 1; i < n; i++) {
        const t = LEAD + (i - 1);
        tl.to(texts[i - 1], { autoAlpha: 0, y: -48, duration: 0.4, ease: "power1.in" }, t + 0.05)
          .fromTo(media[i], { clipPath: "inset(100% 0% 0% 0%)" }, { clipPath: "inset(0% 0% 0% 0%)", duration: 0.7, ease: "power2.inOut" }, t + 0.12)
          .to(pics[i - 1], { scale: 1.08, yPercent: -5, duration: 0.7, ease: "power2.inOut" }, t + 0.12);
        if (pics[i]) tl.fromTo(pics[i], { scale: 1.22, yPercent: 6 }, { scale: 1, yPercent: 0, duration: 0.95, ease: "power2.out" }, t + 0.12);
        tl.fromTo(texts[i], { autoAlpha: 0, y: 48 }, { autoAlpha: 1, y: 0, duration: 0.45, ease: "power2.out" }, t + 0.5);
      }
      tl.to({}, { duration: TAIL }, LEAD + (n - 1));
      setCurrent(0);

      // The step names jump straight to their panel.
      const st = tl.scrollTrigger;
      const onNav = (e) => {
        const i = Number(e.currentTarget.getAttribute("data-seq-nav"));
        const time = i === 0 ? 0 : Math.min(total, LEAD + i - 1 + 0.98);
        scrollToY(st.start + (time / total) * (st.end - st.start));
      };
      navs.forEach((b) => b.addEventListener("click", onNav));

      return () => {
        navs.forEach((b) => b.removeEventListener("click", onNav));
        sec.classList.remove("is-seq");
        panels.forEach((p) => (p.style.zIndex = ""));
        gsap.set([...media, ...pics, ...texts].filter(Boolean), { clearProps: "all" });
      };
    });
  });

  // 3. Photos elsewhere: a short unveil that starts just before they come into view.
  document.querySelectorAll(".re-media, .site-card, .cert-feature, .spec-photo").forEach((el) => {
    gsap.fromTo(el, { clipPath: "inset(8% 0 0 0)", y: 16 }, {
      clipPath: "inset(0% 0 0 0)", y: 0, duration: 0.55, ease: "power2.out", clearProps: "clipPath,transform",
      scrollTrigger: { trigger: el, start: "top 98%", once: true },
    });
  });
  document.querySelectorAll(".re-media").forEach((m) => {
    gsap.fromTo(m, { backgroundPositionY: "38%" }, {
      backgroundPositionY: "62%", ease: "none",
      scrollTrigger: { trigger: m, start: "top bottom", end: "bottom top", scrub: true },
    });
  });

  window.addEventListener("load", () => ScrollTrigger.refresh());
  window.addEventListener("kls:entrance-done", () => ScrollTrigger.refresh());
})();
