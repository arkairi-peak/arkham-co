/* Animated "power grid" page background: drifting nodes joined by faint lines,
   with amber pulses of energy travelling along them, and a soft response to
   the cursor. Fixed behind all content; sections with their own opaque
   background (photo bands, hero) simply cover it. Pauses when the tab is
   hidden; reduced-motion users get one static frame. */
(function () {
  const canvas = document.createElement("canvas");
  canvas.className = "grid-bg";
  canvas.setAttribute("aria-hidden", "true");
  document.body.insertBefore(canvas, document.body.firstChild);
  const ctx = canvas.getContext("2d");
  if (!ctx) return;

  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const LINK = 150;               // max link distance (px)
  const GREEN = "0,148,71";
  const AMBER = "227,167,59";
  let w = 0, h = 0, dpr = 1, nodes = [], pulses = [];
  const mouse = { x: -9999, y: -9999 };

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    w = window.innerWidth; h = window.innerHeight;
    canvas.width = w * dpr; canvas.height = h * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const count = Math.max(18, Math.min(70, Math.round((w * h) / (w < 700 ? 26000 : 20000))));
    nodes = Array.from({ length: count }, () => ({
      x: Math.random() * w, y: Math.random() * h,
      vx: (Math.random() - 0.5) * 0.22, vy: (Math.random() - 0.5) * 0.22,
      r: 1.4 + Math.random() * 1.6,
    }));
    pulses = [];
  }

  function spawnPulse() {
    const a = nodes[(Math.random() * nodes.length) | 0];
    const near = nodes.filter((b) => b !== a && Math.hypot(a.x - b.x, a.y - b.y) < LINK);
    if (!near.length) return;
    pulses.push({ a, b: near[(Math.random() * near.length) | 0], t: 0, speed: 0.008 + Math.random() * 0.01 });
  }

  function frame() {
    ctx.clearRect(0, 0, w, h);
    for (const n of nodes) {
      if (!reduced) {
        n.x += n.vx; n.y += n.vy;
        if (n.x < -20) n.x = w + 20; else if (n.x > w + 20) n.x = -20;
        if (n.y < -20) n.y = h + 20; else if (n.y > h + 20) n.y = -20;
      }
    }
    // links
    for (let i = 0; i < nodes.length; i++) {
      const a = nodes[i];
      for (let j = i + 1; j < nodes.length; j++) {
        const b = nodes[j];
        const d = Math.hypot(a.x - b.x, a.y - b.y);
        if (d < LINK) {
          ctx.strokeStyle = `rgba(${GREEN},${0.16 * (1 - d / LINK)})`;
          ctx.lineWidth = 1;
          ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
        }
      }
      // cursor: nodes near the pointer link to it and glow
      const dm = Math.hypot(a.x - mouse.x, a.y - mouse.y);
      if (dm < 190) {
        ctx.strokeStyle = `rgba(${AMBER},${0.35 * (1 - dm / 190)})`;
        ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(mouse.x, mouse.y); ctx.stroke();
      }
    }
    // nodes
    for (const n of nodes) {
      const dm = Math.hypot(n.x - mouse.x, n.y - mouse.y);
      const glow = dm < 190 ? 1 - dm / 190 : 0;
      ctx.fillStyle = glow ? `rgba(${AMBER},${0.35 + glow * 0.5})` : `rgba(${GREEN},0.34)`;
      ctx.beginPath(); ctx.arc(n.x, n.y, n.r + glow * 1.5, 0, 6.2832); ctx.fill();
    }
    // energy pulses
    if (!reduced) {
      if (pulses.length < 6 && Math.random() < 0.03) spawnPulse();
      for (let i = pulses.length - 1; i >= 0; i--) {
        const p = pulses[i];
        p.t += p.speed;
        if (p.t >= 1 || Math.hypot(p.a.x - p.b.x, p.a.y - p.b.y) > LINK * 1.3) { pulses.splice(i, 1); continue; }
        const x = p.a.x + (p.b.x - p.a.x) * p.t, y = p.a.y + (p.b.y - p.a.y) * p.t;
        const g = ctx.createRadialGradient(x, y, 0, x, y, 9);
        g.addColorStop(0, `rgba(${AMBER},0.95)`); g.addColorStop(1, `rgba(${AMBER},0)`);
        ctx.fillStyle = g; ctx.beginPath(); ctx.arc(x, y, 9, 0, 6.2832); ctx.fill();
      }
    }
  }

  let raf = 0;
  const loop = () => { frame(); raf = requestAnimationFrame(loop); };
  resize();
  if (reduced) { frame(); }
  else {
    raf = requestAnimationFrame(loop);
    document.addEventListener("visibilitychange", () => {
      cancelAnimationFrame(raf);
      if (!document.hidden) raf = requestAnimationFrame(loop);
    });
    window.addEventListener("pointermove", (e) => { mouse.x = e.clientX; mouse.y = e.clientY; }, { passive: true });
    window.addEventListener("pointerleave", () => { mouse.x = mouse.y = -9999; });
  }
  let rt;
  window.addEventListener("resize", () => { clearTimeout(rt); rt = setTimeout(() => { resize(); if (reduced) frame(); }, 150); });
})();
