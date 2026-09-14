document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.primary-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      nav.classList.toggle('open');
      var isOpen = nav.classList.contains('open');
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      toggle.textContent = isOpen ? 'Close' : 'Menu';
    });
  }

  initCountUp();
});

/* ---------- count-up effect for stat numbers ----------
   Add class="count-up" plus data-target="96" to any element.
   Optional: data-decimals="1", data-prefix="", data-suffix="%".
   Animates once, the first time the element scrolls into view. */
function initCountUp() {
  var els = document.querySelectorAll('.count-up');
  if (!els.length) return;

  var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function format(el, value) {
    var decimals = parseInt(el.dataset.decimals || '0', 10);
    var prefix = el.dataset.prefix || '';
    var suffix = el.dataset.suffix || '';
    return prefix + value.toFixed(decimals) + suffix;
  }

  function animate(el) {
    var target = parseFloat(el.dataset.target);
    if (isNaN(target)) return;

    if (prefersReduced) {
      el.textContent = format(el, target);
      return;
    }

    var duration = 1400;
    var start = null;

    function tick(now) {
      if (start === null) start = now;
      var progress = Math.min((now - start) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3); /* ease-out cubic */
      el.textContent = format(el, target * eased);
      if (progress < 1) {
        requestAnimationFrame(tick);
      } else {
        el.textContent = format(el, target);
      }
    }
    requestAnimationFrame(tick);
  }

  if (!('IntersectionObserver' in window)) {
    els.forEach(animate);
    return;
  }

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        animate(entry.target);
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.4 });

  els.forEach(function (el) { io.observe(el); });
}