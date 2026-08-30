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
