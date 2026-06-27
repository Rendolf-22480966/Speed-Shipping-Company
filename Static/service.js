(function () {
  var loader = document.getElementById('serviceLoader');
  var header = document.getElementById('serviceHeader');
  var prefersReduced =
    window.matchMedia &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function hideLoader() {
    if (!loader) return;
    loader.classList.add('is-hidden');
    setTimeout(function () {
      if (loader.parentNode) loader.parentNode.removeChild(loader);
    }, 800);
  }

  function onScroll() {
    if (!header) return;
    if (window.scrollY > 60) {
      header.classList.add('is-solid');
    } else {
      header.classList.remove('is-solid');
    }
  }

  if (prefersReduced) {
    hideLoader();
  } else {
    window.addEventListener('load', function () {
      setTimeout(hideLoader, 1200);
    });
    setTimeout(hideLoader, 3500);
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();
