/* Scroll-driven reveals (GSAP ScrollTrigger), every page.
   Content is visible by default; hidden states are applied here, so if GSAP
   or this file fails nothing stays invisible. Skipped entirely for
   prefers-reduced-motion (main.js keeps its plain IntersectionObserver reveal). */
(function () {
  const { gsap, ScrollTrigger } = window;
  if (!gsap || !ScrollTrigger) return;
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  gsap.registerPlugin(ScrollTrigger);

  const inHero = (el) => el.closest(".hero");
  const pick = (sel) => [...document.querySelectorAll(sel)].filter((el) => !inHero(el));
  const start = "top 88%";

  // 1. Section headings: masked word rise.
  pick(".section h2, .page-hero h1, .cta-band h2").forEach((h) => {
    if (h.children.length) return; // keep headings with inline markup untouched
    const text = h.textContent.trim();
    h.setAttribute("aria-label", text);
    h.innerHTML = text.split(/\s+/).map((w) => `<span class="w" aria-hidden="true"><span>${w}</span></span>`).join(" ");
    const words = h.querySelectorAll(".w > span");
    gsap.set(words, { yPercent: 115 });
    ScrollTrigger.create({
      trigger: h, start, once: true,
      onEnter: () => gsap.to(words, {
        yPercent: 0, duration: 0.85, stagger: 0.05, ease: "power4.out",
        onComplete: () => { h.textContent = text; h.removeAttribute("aria-label"); },
      }),
    });
  });

  // 2. Kickers, leads and short intro copy: fade + slide.
  const fadeTargets = pick(".kicker, .section .lead, .section-head > p, .svc-chip-row");
  gsap.set(fadeTargets, { autoAlpha: 0, y: 24 });
  ScrollTrigger.batch(fadeTargets, {
    start, once: true,
    onEnter: (els) => gsap.to(els, { autoAlpha: 1, y: 0, duration: 0.8, stagger: 0.08, ease: "power3.out", clearProps: "transform" }),
  });

  // 3. Repeating rows / cards: staggered rise per group.
  const items = pick(".spec-row, .value-row, .t-item, .logo-cell, .stat-item, .loc-card, .card, .profile-row, .quick-fact, .cert-card, .svc-chip");
  const fresh = items.filter((el) => !fadeTargets.includes(el));
  gsap.set(fresh, { autoAlpha: 0, y: 36 });
  ScrollTrigger.batch(fresh, {
    start, once: true, interval: 0.1, batchMax: 6,
    onEnter: (els) => gsap.to(els, { autoAlpha: 1, y: 0, duration: 0.8, stagger: 0.09, ease: "power3.out", clearProps: "transform" }),
  });

  // 4. Photo panels: clip-path unveil + slow background parallax.
  pick(".re-block").forEach((block) => {
    const media = block.querySelector(".re-media");
    if (!media) return;
    gsap.set(block, { autoAlpha: 0, y: 40 });
    ScrollTrigger.create({
      trigger: block, start: "top 86%", once: true,
      onEnter: () => {
        gsap.to(block, { autoAlpha: 1, y: 0, duration: 0.9, ease: "power3.out", clearProps: "transform" });
        gsap.fromTo(media, { clipPath: "inset(0 0 100% 0)" }, { clipPath: "inset(0 0 0% 0)", duration: 1.1, ease: "power4.out", clearProps: "clipPath" });
      },
    });
    gsap.fromTo(media, { backgroundPositionY: "35%" }, {
      backgroundPositionY: "65%", ease: "none",
      scrollTrigger: { trigger: block, start: "top bottom", end: "bottom top", scrub: true },
    });
  });

  // 5. Big section background photos (forest bands): gentle parallax.
  pick(".section--forest").forEach((sec) => {
    gsap.fromTo(sec, { backgroundPositionY: "30%" }, {
      backgroundPositionY: "70%", ease: "none",
      scrollTrigger: { trigger: sec, start: "top bottom", end: "bottom top", scrub: true },
    });
  });

  window.addEventListener("load", () => ScrollTrigger.refresh());
  window.addEventListener("kls:entrance-done", () => ScrollTrigger.refresh());
})();
