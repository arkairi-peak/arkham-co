/* Interactive projects map (Leaflet + OpenStreetMap tiles).
   Pins are built at runtime from KLS_PROJECTS (assets/js/data.js), so the map
   always matches the reference list. Coordinates come from the PLACES table
   below; state-level entries (e.g. just "Perak") are shown at the state's
   approximate centre and flagged as approximate. */
(function () {
  const el = document.querySelector("[data-project-map]");
  if (!el || !window.L || typeof KLS_PROJECTS === "undefined") return;

  const ms = document.documentElement.lang === "ms";
  const T = ms
    ? { proj: "projek", projs: "projek", places: "lokasi", approx: "Kedudukan pin peringkat negeri adalah anggaran.", hq: "Ibu Pejabat", branch: "Pejabat Cawangan", more: "lagi", all: "Semua lokasi", office: "Pejabat KLS" }
    : { proj: "project", projs: "projects", places: "locations", approx: "Pins for state-level entries are approximate.", hq: "Headquarters", branch: "Branch Office", more: "more", all: "All locations", office: "KLS office" };

  // Ordered: specific places first, state-level fallbacks last.
  const PLACES = [
    ["larkin", "Larkin, Johor Bahru", 1.4927, 103.7414],
    ["pengerang", "Pengerang, Johor", 1.3773, 104.2226],
    ["carey island", "Carey Island, Selangor", 2.8617, 101.4172],
    ["bestari jaya", "Bestari Jaya, Selangor", 3.3846, 101.4217],
    ["kuala selangor", "Kuala Selangor", 3.3389, 101.2503],
    ["rawang", "Rawang, Selangor", 3.3213, 101.5767],
    ["klang utara", "Klang Utara (Kapar), Klang", 3.1000, 101.4000],
    ["westport", "Westport, Pulau Indah", 2.9970, 101.3100],
    ["port klang", "Port Klang, Selangor", 3.0000, 101.3900],
    ["kuala lumpur", "Kuala Lumpur / Selangor", 3.1390, 101.6869, true],
    ["ulu bernam", "Ulu Bernam", 3.7000, 101.4200],
    ["kuantan", "Kuantan, Pahang", 3.8077, 103.3260],
    ["lahad datu", "Lahad Datu, Sabah", 5.0267, 118.3270],
    ["sandakan", "Sandakan, Sabah", 5.8402, 118.1179],
    ["sabah", "Sabah", 5.4200, 116.9500, true],
    ["perak", "Perak", 4.5921, 101.0901, true],
    ["pahang", "Pahang", 3.9500, 102.6000, true],
    ["johor", "Johor", 1.9500, 103.3000, true],
  ];
  const OFFICES = [
    { name: "Port Klang", role: T.hq, lat: 3.0000, lng: 101.3900 },
    { name: "Lahad Datu", role: T.branch, lat: 5.0267, lng: 118.3270 },
    { name: "Bintulu", role: T.branch, lat: 3.1700, lng: 113.0360 },
  ];
  const COLORS = { power: "#009447", biogas: "#E3A73B", biomass: "#7A5C2E", stadium: "#182922", solar: "#3CBE72" };
  const NAMES = {
    power: ms ? "Elektrik & Pengagihan Kuasa" : "Electrical & Power Distribution",
    biogas: "Biogas", biomass: ms ? "Biojisim" : "Biomass", stadium: ms ? "Stadium & Infrastruktur" : "Stadium & Infrastructure",
  };
  const esc = (s) => String(s == null ? "" : s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

  // Flatten to entries with a resolved place.
  const entries = [];
  KLS_PROJECTS.forEach((c) => c.entries.forEach((e) => {
    const loc = (e.location || "").toLowerCase();
    const hit = PLACES.find((p) => loc.includes(p[0]));
    if (hit) entries.push({ client: c.short || c.client, desc: e.desc, year: e.year, capacity: e.capacity, category: e.category, place: hit });
  }));

  const map = L.map(el, { scrollWheelZoom: false, minZoom: 4, maxZoom: 12, zoomControl: true }).setView([4.2, 109.5], 5);
  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: "&copy; OpenStreetMap contributors", maxZoom: 19,
  }).addTo(map);
  // Wheel zoom only after the map is clicked, so page scrolling never gets hijacked.
  map.on("click", () => map.scrollWheelZoom.enable());
  map.on("mouseout", () => map.scrollWheelZoom.disable());

  OFFICES.forEach((o) => {
    L.marker([o.lat, o.lng], {
      icon: L.divIcon({ className: "", html: '<div class="kls-office"><i>KLS</i></div>', iconSize: [26, 26], iconAnchor: [13, 13] }),
      zIndexOffset: -100, keyboard: false,
    }).bindTooltip(`${T.office}: ${o.name} (${o.role})`, { direction: "top", offset: [0, -12] }).addTo(map);
  });

  const layer = L.layerGroup().addTo(map);
  const list = document.querySelector("[data-map-places]");
  const summary = document.querySelector("[data-map-summary]");
  let filter = "all";

  function render() {
    layer.clearLayers();
    const groups = new Map();
    entries.filter((e) => filter === "all" || e.category === filter).forEach((e) => {
      const k = e.place[1];
      if (!groups.has(k)) groups.set(k, { place: e.place, items: [] });
      groups.get(k).items.push(e);
    });
    const arr = [...groups.values()].sort((a, b) => b.items.length - a.items.length);
    const bounds = [];
    if (list) list.innerHTML = "";
    arr.forEach((g) => {
      const [, label, lat, lng, approx] = g.place;
      const counts = {};
      g.items.forEach((i) => { counts[i.category] = (counts[i.category] || 0) + 1; });
      const dom = Object.keys(counts).sort((a, b) => counts[b] - counts[a])[0];
      const size = 26 + Math.min(18, g.items.length * 2);
      const marker = L.marker([lat, lng], {
        icon: L.divIcon({
          className: "",
          html: `<div class="kls-pin" style="width:${size}px;height:${size}px;background:${COLORS[dom] || "#009447"};${approx ? "opacity:.75;border-style:dashed;" : ""}">${g.items.length}</div>`,
          iconSize: [size, size], iconAnchor: [size / 2, size / 2],
        }),
        title: `${label}: ${g.items.length}`,
      });
      const shown = g.items.slice(0, 8).map((i) =>
        `<li>${i.year ? `<b>${esc(i.year)}</b> · ` : ""}${esc(i.client)}: ${esc(i.desc.length > 90 ? i.desc.slice(0, 88) + "…" : i.desc)}${i.capacity ? ` (${esc(i.capacity)})` : ""}</li>`).join("");
      const extra = g.items.length > 8 ? `<li>+${g.items.length - 8} ${T.more}</li>` : "";
      marker.bindPopup(`<div class="map-pop"><h4>${esc(label)}${approx ? " *" : ""}</h4><ul>${shown}${extra}</ul></div>`, { maxWidth: 320 });
      marker.addTo(layer);
      bounds.push([lat, lng]);
      if (list) {
        const li = document.createElement("li");
        li.innerHTML = `<button type="button"><span class="dot" style="background:${COLORS[dom] || "#009447"}"></span><span>${esc(label)}${approx ? " *" : ""}</span><span class="c">${g.items.length}</span></button>`;
        li.firstChild.addEventListener("click", () => { map.flyTo([lat, lng], Math.max(map.getZoom(), 8), { duration: 0.9 }); marker.openPopup(); });
        list.appendChild(li);
      }
    });
    const total = arr.reduce((n, g) => n + g.items.length, 0);
    if (summary) summary.innerHTML = `<b>${total} ${total === 1 ? T.proj : T.projs}</b>${arr.length} ${T.places}`;
    if (bounds.length) map.flyToBounds(L.latLngBounds(bounds.concat(OFFICES.map((o) => [o.lat, o.lng]))).pad(0.15), { duration: 0.8, maxZoom: 9 });
  }

  document.querySelectorAll("[data-map-filter]").forEach((b) => b.addEventListener("click", () => {
    filter = b.getAttribute("data-map-filter");
    document.querySelectorAll("[data-map-filter]").forEach((x) => x.classList.toggle("is-active", x === b));
    render();
  }));
  render();
  // Leaflet needs a size recalculation when the section is revealed/laid out late.
  window.addEventListener("load", () => map.invalidateSize());
})();
