document.addEventListener('DOMContentLoaded', function () {
  var li = document.getElementById('featuresLi');
  var btn = document.getElementById('featuresBtn');
  if (!li || !btn) return;

  function closeMenu() {
    li.classList.remove('open');
    btn.setAttribute('aria-expanded', 'false');
  }
  function toggleMenu() {
    var isOpen = li.classList.toggle('open');
    btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  }

  btn.addEventListener('click', function (e) {
    e.stopPropagation();
    toggleMenu();
  });
  document.addEventListener('click', function (e) {
    if (!li.contains(e.target)) closeMenu();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeMenu();
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
