/* Home page entrance (GSAP).
   1. A framed photo card develops on a dark field while a huge outlined year runs up to 1984.
   2. The card expands to full-bleed and the overlay dissolves.
   3. The hero photo settles, the headline rises out of masks, then the rest of the hero follows.
   Fail-safes: no GSAP / reduced motion => content simply shows; repeat visit => no overlay,
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
  const title = document.querySelector("[data-entrance-title]");
  const titleText = title ? title.textContent : "";

  if (title) {
    title.setAttribute("aria-label", titleText);
    title.innerHTML = titleText.split(/\s+/).map((w) => `<span class="w" aria-hidden="true"><span>${w}</span></span>`).join(" ");
  }
  const words = title ? title.querySelectorAll(".w > span") : [];
  const rest = document.querySelectorAll("[data-entrance-rest]");
  const header = document.querySelector(".site-header");
  const photos = document.querySelector("[data-entrance-photo]");

  gsap.set(words, { yPercent: 110 });
  gsap.set(rest, { autoAlpha: 0, y: 18 });
  if (header && showIntro) gsap.set(header, { yPercent: -100 });

  const contentIn = (tl, at) => {
    if (photos) tl.fromTo(photos, { scale: 1.06 }, { scale: 1, duration: 1.6, ease: "power3.out", clearProps: "transform" }, Math.max(0, at - 0.1));
    tl.to(words, { yPercent: 0, duration: 0.9, stagger: 0.045, ease: "power4.out" }, at)
      .to(rest, { autoAlpha: 1, y: 0, duration: 0.7, stagger: 0.06, ease: "power3.out" }, at + 0.35)
      .to(header, { yPercent: 0, duration: 0.6, ease: "power3.out" }, at + 0.2);
  };
  const finish = () => {
    clearTimeout(bail);
    if (title) { title.textContent = titleText; title.removeAttribute("aria-label"); }
    gsap.set([header, ...rest], { clearProps: "opacity,visibility,transform" });
    done();
  };
  const master = gsap.timeline({ paused: true, onComplete: finish });
  const bail = setTimeout(() => { master.kill(); finish(); }, 7000);

  if (!showIntro) {
    contentIn(master, 0.05);
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

  const load = gsap.timeline({ paused: true });
  load.fromTo(card, { clipPath: "inset(50% 50% 50% 50% round 6px)" }, { clipPath: "inset(0% 0% 0% 0% round 6px)", duration: 1.1, ease: "power4.inOut" }, 0.1)
      .fromTo(cardImg, { scale: 1.35 }, { scale: 1, duration: 1.4, ease: "power3.out" }, 0.1)
      .from(meta, { autoAlpha: 0, y: 12, duration: 0.6, stagger: 0.08, ease: "power3.out" }, 0.3)
      .to(line, { scaleX: 1, duration: 1.2, ease: "power2.inOut" }, 0.1)
      .to(y, { v: 1984, duration: 1.2, ease: "power3.out", onUpdate: () => { year.textContent = Math.round(y.v); } }, 0.1);
  load.eventCallback("onComplete", () => {
    master.to(meta, { autoAlpha: 0, duration: 0.25 }, 0)
      .to(year, { yPercent: -40, autoAlpha: 0, duration: 0.7, ease: "power3.in" }, 0.05)
      .to(card, { width: "100vw", height: "100vh", duration: 0.95, ease: "power4.inOut" }, 0.1)
      .set(card, { clipPath: "inset(0% round 0px)" }, 1.05)
      .to(intro, { autoAlpha: 0, duration: 0.45, ease: "power1.out" }, 1.0);
    contentIn(master, 1.05);
    master.play();
  });
  load.play();
})();
