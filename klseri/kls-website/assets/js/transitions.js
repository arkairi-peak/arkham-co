/* Page-to-page wipe. A dark panel rises over the page on internal link clicks,
   the next page starts covered (flag in sessionStorage + html.wipe-in set by an
   inline script) and the panel lifts away. Falls back to a normal navigation
   if GSAP is missing; skipped for reduced motion. */
(function () {
  const wipe = document.querySelector("[data-page-wipe]");
  const root = document.documentElement;
  const gsap = window.gsap;
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!wipe || !gsap || reduced) { root.classList.remove("wipe-in"); return; }

  const reveal = () => {
    if (!root.classList.contains("wipe-in")) return;
    try { sessionStorage.removeItem("klsWipe"); } catch (e) {}
    gsap.set(wipe, { yPercent: 0 });
    root.classList.remove("wipe-in");
    gsap.to(wipe, { yPercent: -100, duration: 0.7, ease: "power4.inOut", delay: 0.05, onComplete: () => gsap.set(wipe, { clearProps: "all" }) });
  };
  reveal();
  // Back/forward cache restore: make sure the panel is not left covering the page.
  window.addEventListener("pageshow", (e) => { if (e.persisted) gsap.set(wipe, { clearProps: "all" }); });

  document.addEventListener("click", (e) => {
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    const a = e.target.closest("a[href]");
    if (!a || a.target === "_blank" || a.hasAttribute("download")) return;
    const url = new URL(a.href, location.href);
    if (url.origin !== location.origin || !/^https?:$/.test(url.protocol)) return;
    if (url.pathname === location.pathname && url.search === location.search) return; // same page / hash jump
    e.preventDefault();
    try { sessionStorage.setItem("klsWipe", "1"); } catch (err) {}
    gsap.fromTo(wipe, { yPercent: 100 }, { yPercent: 0, duration: 0.55, ease: "power4.inOut", onComplete: () => { location.href = a.href; } });
    setTimeout(() => { location.href = a.href; }, 1500); // safety net
  });
})();
