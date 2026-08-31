// Mobile hamburger menu
document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.getElementById('navToggle');
  var nav = document.getElementById('primaryNav');
  if (!toggle || !nav) return;
  toggle.addEventListener('click', function () {
    var isOpen = nav.classList.toggle('open');
    toggle.classList.toggle('open', isOpen);
    toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  });
});

document.addEventListener('DOMContentLoaded', function () {
  var items = document.querySelectorAll('li.has-mega');
  if (!items.length) return;

  function closeAll(except) {
    items.forEach(function (li) {
      if (li === except) return;
      li.classList.remove('open');
      var b = li.querySelector('.navtop');
      if (b) b.setAttribute('aria-expanded', 'false');
    });
  }

  items.forEach(function (li) {
    var btn = li.querySelector('.navtop');
    if (!btn) return;
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var isOpen = li.classList.toggle('open');
      btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      closeAll(li);
    });
  });

  document.addEventListener('click', function (e) {
    var insideAny = Array.prototype.some.call(items, function (li) { return li.contains(e.target); });
    if (!insideAny) closeAll(null);
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeAll(null);
  });
});

// Journey tabs (Capture / Qualify / Nurture / Close)
document.addEventListener('DOMContentLoaded', function () {
  var tabs = document.querySelectorAll('.journey-tab');
  var panels = document.querySelectorAll('.journey-panel');
  if (!tabs.length) return;
  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      tabs.forEach(function (t) { t.classList.remove('active'); });
      panels.forEach(function (p) { p.classList.remove('active'); });
      tab.classList.add('active');
      var target = document.getElementById(tab.dataset.target);
      if (target) target.classList.add('active');
    });
  });
});

// Reveal-on-scroll
document.addEventListener('DOMContentLoaded', function () {
  var items = document.querySelectorAll('.reveal');
  if (!items.length) return;
  if (!('IntersectionObserver' in window)) {
    items.forEach(function (el) { el.classList.add('visible'); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });
  items.forEach(function (el) { io.observe(el); });
});
