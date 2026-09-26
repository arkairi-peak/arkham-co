/* Home page entrance (GSAP).
   1. A framed photo card develops on a dark field while a huge outlined year runs up to 1984.
   2. The card expands to full-bleed, the overlay dissolves.
   3. Headline words rise out of masks, chips / copy / stats follow, header drops in.
   Fail-safes: no GSAP / reduced motion => hero simply shows; repeat visit => no overlay,
   short reveal only; a 7s bail-out shows the page if the animation stalls. */
(function () {
  const root = document.documentElement;
  const intro = document.querySelector("[data-intro]");
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const done = () => {
    root.classList.remove("intro-lock");
    if (intro) intro.style.display = "none";
    window.__klsEntranceDone = true;
    window.dispatchEvent(new Event("kls:entrance-done"));
  };
  if (!window.gsap || reduced) return done();

  const gsap = window.gsap;
  const showIntro = intro && !root.classList.contains("no-intro");
  const h1 = document.querySelector("[data-hero-title-el]");
  const h1Text = h1 ? h1.textContent : "";

  if (h1) {
    h1.setAttribute("aria-label", h1Text);
    h1.innerHTML = h1Text.split(/\s+/).map((w) => `<span class="w" aria-hidden="true"><span>${w}</span></span>`).join(" ");
  }
  const words = h1 ? h1.querySelectorAll(".w > span") : [];
  const chips = document.querySelectorAll(".hero-chips span");
  const rest = document.querySelectorAll("[data-hero-lead-el], .hero-actions, .hero-stats, .hero-dots, .hero-scroll-cue");
  const header = document.querySelector(".site-header");
  const slides = document.querySelector(".hero-slides");

  gsap.set(words, { yPercent: 115 });
  gsap.set(chips, { autoAlpha: 0, x: -18 });
  gsap.set(rest, { autoAlpha: 0, y: 22 });
  if (header) gsap.set(header, { yPercent: -100 });
  if (slides) gsap.set(slides, { scale: 1.1, transformOrigin: "50% 50%" });

  const heroIn = (tl, at) => {
    tl.to(slides, { scale: 1, duration: 1.8, ease: "power3.out" }, at)
      .to(words, { yPercent: 0, duration: 0.9, stagger: 0.07, ease: "power4.out" }, at + 0.05)
      .to(chips, { autoAlpha: 1, x: 0, duration: 0.6, stagger: 0.08, ease: "power3.out" }, at)
      .to(rest, { autoAlpha: 1, y: 0, duration: 0.7, stagger: 0.1, ease: "power3.out" }, at + 0.4)
      .to(header, { yPercent: 0, duration: 0.7, ease: "power3.out" }, at + 0.5);
  };
  const finish = () => {
    clearTimeout(bail);
    if (h1) { h1.textContent = h1Text; h1.removeAttribute("aria-label"); }
    gsap.set([slides, header, ...chips, ...rest], { clearProps: "opacity,visibility,transform" });
    done();
  };
  const master = gsap.timeline({ paused: true, onComplete: finish });
  const bail = setTimeout(() => { master.kill(); finish(); }, 7000);

  if (!showIntro) {
    heroIn(master, 0);
    master.play();
    return;
  }

  const q = (s) => intro.querySelector(s);
  const year = q("[data-intro-count]");
  const card = q(".intro-card");
  const cardImg = q(".intro-card img");
  const line = q(".intro-line i");
  const meta = intro.querySelectorAll(".intro-meta span");
  const y = { v: 1950 };

  const firstImg = document.querySelector(".hero-slide.is-active img");
  const imgReady = firstImg && !firstImg.complete
    ? new Promise((r) => { firstImg.addEventListener("load", r, { once: true }); setTimeout(r, 1600); })
    : Promise.resolve();

  const load = gsap.timeline({ paused: true });
  load.fromTo(card, { clipPath: "inset(50% 50% 50% 50% round 18px)" }, { clipPath: "inset(0% 0% 0% 0% round 18px)", duration: 1.1, ease: "power4.inOut" }, 0.1)
      .fromTo(cardImg, { scale: 1.35 }, { scale: 1, duration: 1.4, ease: "power3.out" }, 0.1)
      .from(meta, { autoAlpha: 0, y: 12, duration: 0.6, stagger: 0.08, ease: "power3.out" }, 0.3)
      .to(line, { scaleX: 1, duration: 1.2, ease: "power2.inOut" }, 0.1)
      .to(y, { v: 1984, duration: 1.2, ease: "power3.out", onUpdate: () => { year.textContent = Math.round(y.v); } }, 0.1);
  load.play();

  Promise.all([imgReady, new Promise((r) => load.eventCallback("onComplete", r))]).then(() => {
    master.to(meta, { autoAlpha: 0, duration: 0.25 }, 0)
      .to(year, { yPercent: -40, autoAlpha: 0, duration: 0.8, ease: "power3.in" }, 0.05)
      .to(card, { width: "100vw", height: "100vh", duration: 1.0, ease: "power4.inOut" }, 0.1)
      .set(card, { clipPath: "inset(0% round 0px)" }, 1.1)
      .to(intro, { autoAlpha: 0, duration: 0.45, ease: "power1.out" }, 1.1);
    heroIn(master, 1.0);
    master.play();
  });
})();
