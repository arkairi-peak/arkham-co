/* Page background: a faint single-line wiring diagram.
   Cable runs are routed at right angles on a fixed grid (like a schematic),
   with square terminals at their ends and small junction dots at the bends.
   Amber current pulses travel along the runs, and runs near the cursor light
   up. The static drawing is rendered once per resize to an offscreen canvas,
   so each frame only paints pulses and highlights. Pauses when the tab is
   hidden; reduced-motion users get the still drawing. */
(function () {
  const canvas = document.createElement("canvas");
  canvas.className = "grid-bg";
  canvas.setAttribute("aria-hidden", "true");
  document.body.insertBefore(canvas, document.body.firstChild);
  const ctx = canvas.getContext("2d");
  if (!ctx) return;

  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const GREEN = "0,148,71";
  const AMBER = "227,167,59";
  const base = document.createElement("canvas");
  const bctx = base.getContext("2d");
  let w = 0, h = 0, dpr = 1, cell = 96, runs = [], pulses = [];
  const mouse = { x: -9999, y: -9999 };
  const rand = (a, b) => a + Math.random() * (b - a);
  const pick = (arr) => arr[(Math.random() * arr.length) | 0];

  // A run: a polyline of grid points, alternating horizontal and vertical legs.
  function makeRun(cols, rows) {
    let x = (Math.random() * cols) | 0, y = (Math.random() * rows) | 0;
    const pts = [[x, y]];
    let horizontal = Math.random() < 0.6;
    const legs = 2 + ((Math.random() * 4) | 0);
    for (let i = 0; i < legs; i++) {
      const len = pick([1, 2, 2, 3, 4]) * (Math.random() < 0.5 ? -1 : 1);
      if (horizontal) x = Math.max(0, Math.min(cols, x + len));
      else y = Math.max(0, Math.min(rows, y + len));
      const last = pts[pts.length - 1];
      if (last[0] !== x || last[1] !== y) pts.push([x, y]);
      horizontal = !horizontal;
    }
    if (pts.length < 2) return null;
    const path = pts.map(([gx, gy]) => [gx * cell + 0.5, gy * cell + 0.5]);
    let length = 0;
    const segs = [];
    for (let i = 1; i < path.length; i++) {
      const [ax, ay] = path[i - 1], [bx, by] = path[i];
      const l = Math.abs(bx - ax) + Math.abs(by - ay);
      segs.push({ ax, ay, bx, by, l, at: length });
      length += l;
    }
    return { path, segs, length, glow: 0 };
  }

  function drawBase() {
    base.width = w * dpr; base.height = h * dpr;
    bctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    bctx.clearRect(0, 0, w, h);
    // faint drafting grid ticks at every intersection
    bctx.fillStyle = `rgba(${GREEN},0.07)`;
    for (let x = 0; x <= w + cell; x += cell) for (let y = 0; y <= h + cell; y += cell) bctx.fillRect(x - 1, y - 1, 2, 2);
    for (const r of runs) {
      bctx.strokeStyle = `rgba(${GREEN},0.085)`;
      bctx.lineWidth = 1;
      bctx.beginPath();
      r.path.forEach(([x, y], i) => (i ? bctx.lineTo(x, y) : bctx.moveTo(x, y)));
      bctx.stroke();
      bctx.fillStyle = `rgba(${GREEN},0.2)`;
      for (let i = 1; i < r.path.length - 1; i++) { bctx.beginPath(); bctx.arc(r.path[i][0], r.path[i][1], 2, 0, 6.2832); bctx.fill(); }
      for (const [x, y] of [r.path[0], r.path[r.path.length - 1]]) {
        bctx.strokeStyle = `rgba(${GREEN},0.24)`;
        bctx.strokeRect(x - 3.5, y - 3.5, 7, 7);
      }
    }
  }

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    w = window.innerWidth; h = window.innerHeight;
    canvas.width = w * dpr; canvas.height = h * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    cell = w < 700 ? 72 : 96;
    const cols = Math.ceil(w / cell), rows = Math.ceil(h / cell);
    const count = Math.max(6, Math.min(16, Math.round((w * h) / 90000)));
    runs = [];
    for (let i = 0; i < count * 3 && runs.length < count; i++) { const r = makeRun(cols, rows); if (r && r.length >= cell * 2) runs.push(r); }
    pulses = [];
    drawBase();
  }

  function pointAt(r, d) {
    for (const s of r.segs) {
      if (d <= s.at + s.l) { const t = s.l ? (d - s.at) / s.l : 0; return [s.ax + (s.bx - s.ax) * t, s.ay + (s.by - s.ay) * t]; }
    }
    const last = r.path[r.path.length - 1];
    return [last[0], last[1]];
  }

  function nearCursor(r) {
    for (const s of r.segs) {
      const minx = Math.min(s.ax, s.bx) - 120, maxx = Math.max(s.ax, s.bx) + 120;
      const miny = Math.min(s.ay, s.by) - 120, maxy = Math.max(s.ay, s.by) + 120;
      if (mouse.x > minx && mouse.x < maxx && mouse.y > miny && mouse.y < maxy) return true;
    }
    return false;
  }

  let last = performance.now();
  function frame(now) {
    const dt = Math.min(0.05, (now - last) / 1000); last = now;
    ctx.clearRect(0, 0, w, h);
    ctx.drawImage(base, 0, 0, w, h);
    // runs near the pointer brighten, then fade back
    for (const r of runs) {
      r.glow += ((nearCursor(r) ? 1 : 0) - r.glow) * Math.min(1, dt * 6);
      if (r.glow > 0.02) {
        ctx.strokeStyle = `rgba(${GREEN},${0.45 * r.glow})`;
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        r.path.forEach(([x, y], i) => (i ? ctx.lineTo(x, y) : ctx.moveTo(x, y)));
        ctx.stroke();
        const [ex, ey] = r.path[r.path.length - 1];
        ctx.fillStyle = `rgba(${AMBER},${0.8 * r.glow})`;
        ctx.fillRect(ex - 3.5, ey - 3.5, 7, 7);
      }
    }
    // current pulses: a short bright trace running along a cable
    if (pulses.length < 4 && Math.random() < dt * 0.9) {
      const r = pick(runs);
      if (r) pulses.push({ r, d: 0, speed: rand(90, 150) });
    }
    for (let i = pulses.length - 1; i >= 0; i--) {
      const p = pulses[i];
      p.d += p.speed * dt;
      if (p.d > p.r.length + 40) { pulses.splice(i, 1); continue; }
      ctx.lineWidth = 2;
      ctx.lineCap = "round";
      for (let k = 0; k < 8; k++) {
        const d0 = Math.max(0, p.d - k * 6), d1 = Math.max(0, p.d - (k + 1) * 6);
        if (d0 > p.r.length) continue;
        const [x0, y0] = pointAt(p.r, d0), [x1, y1] = pointAt(p.r, d1);
        ctx.strokeStyle = `rgba(${AMBER},${0.85 * (1 - k / 8)})`;
        ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x1, y1); ctx.stroke();
      }
    }
    raf = requestAnimationFrame(frame);
  }

  let raf = 0;
  resize();
  if (reduced) ctx.drawImage(base, 0, 0, w, h);
  else {
    raf = requestAnimationFrame(frame);
    document.addEventListener("visibilitychange", () => {
      cancelAnimationFrame(raf);
      if (!document.hidden) { last = performance.now(); raf = requestAnimationFrame(frame); }
    });
    window.addEventListener("pointermove", (e) => { mouse.x = e.clientX; mouse.y = e.clientY; }, { passive: true });
    document.addEventListener("pointerleave", () => { mouse.x = mouse.y = -9999; });
  }
  let rt;
  window.addEventListener("resize", () => {
    clearTimeout(rt);
    rt = setTimeout(() => { resize(); if (reduced) ctx.drawImage(base, 0, 0, w, h); }, 150);
  });
})();
