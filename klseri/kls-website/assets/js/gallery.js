/* Project photo galleries (home page "Project sites").
   Each [data-gallery] button carries a JSON list of {src, caption}. Clicking
   opens a full-screen viewer: arrow buttons, keyboard (left/right/Esc), swipe
   on touch screens, and a photo counter. Focus returns to the card on close. */
(function () {
  const cards = document.querySelectorAll("[data-gallery]");
  if (!cards.length) return;
  const ms = document.documentElement.lang === "ms";
  const T = ms
    ? { close: "Tutup", prev: "Gambar sebelumnya", next: "Gambar seterusnya", of: "daripada" }
    : { close: "Close", prev: "Previous photo", next: "Next photo", of: "of" };

  const root = document.createElement("div");
  root.className = "modal-overlay gallery";
  root.setAttribute("role", "dialog");
  root.setAttribute("aria-modal", "true");
  root.setAttribute("data-lenis-prevent", "");
  root.innerHTML = `
    <div class="gallery-top">
      <p class="gallery-title"></p>
      <button type="button" class="gallery-close" aria-label="${T.close}">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 6l12 12M18 6L6 18"/></svg>
      </button>
    </div>
    <figure class="gallery-stage"><img alt=""><figcaption><span class="gallery-caption"></span><span class="gallery-count"></span></figcaption></figure>
    <button type="button" class="gallery-nav gallery-prev" aria-label="${T.prev}"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 6l-6 6 6 6"/></svg></button>
    <button type="button" class="gallery-nav gallery-next" aria-label="${T.next}"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 6l6 6-6 6"/></svg></button>`;
  document.body.appendChild(root);

  const img = root.querySelector(".gallery-stage img");
  const title = root.querySelector(".gallery-title");
  const caption = root.querySelector(".gallery-caption");
  const count = root.querySelector(".gallery-count");
  let photos = [], idx = 0, opener = null;

  function show(i) {
    idx = (i + photos.length) % photos.length;
    const ph = photos[idx];
    img.classList.remove("is-in");
    img.onload = () => img.classList.add("is-in");
    img.src = ph.src;
    img.alt = ph.caption || "";
    caption.textContent = ph.caption || "";
    count.textContent = `${idx + 1} ${T.of} ${photos.length}`;
    // warm the next photo so stepping through feels instant
    const next = photos[(idx + 1) % photos.length];
    if (next) { const pre = new Image(); pre.src = next.src; }
    root.classList.toggle("is-single", photos.length < 2);
  }
  function open(card) {
    try { photos = JSON.parse(card.getAttribute("data-gallery")); } catch (e) { return; }
    if (!photos.length) return;
    opener = card;
    title.textContent = card.getAttribute("data-gallery-title") || "";
    root.setAttribute("aria-label", title.textContent);
    show(0);
    root.classList.add("is-open");
    document.body.style.overflow = "hidden";
    if (window.__lenis) window.__lenis.stop();
    root.querySelector(".gallery-close").focus();
  }
  function close() {
    root.classList.remove("is-open");
    document.body.style.overflow = "";
    if (window.__lenis) window.__lenis.start();
    img.removeAttribute("src");
    if (opener) opener.focus();
  }

  cards.forEach((c) => c.addEventListener("click", () => open(c)));
  root.querySelector(".gallery-close").addEventListener("click", close);
  root.querySelector(".gallery-prev").addEventListener("click", () => show(idx - 1));
  root.querySelector(".gallery-next").addEventListener("click", () => show(idx + 1));
  root.addEventListener("click", (e) => { if (e.target === root) close(); });
  document.addEventListener("keydown", (e) => {
    if (!root.classList.contains("is-open")) return;
    if (e.key === "Escape") close();
    else if (e.key === "ArrowLeft") show(idx - 1);
    else if (e.key === "ArrowRight") show(idx + 1);
  });
  let x0 = null;
  root.addEventListener("touchstart", (e) => { x0 = e.touches[0].clientX; }, { passive: true });
  root.addEventListener("touchend", (e) => {
    if (x0 === null) return;
    const dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 40) show(idx + (dx < 0 ? 1 : -1));
    x0 = null;
  });
})();
