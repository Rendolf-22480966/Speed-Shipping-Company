// ==========================================================================
//  Speed-Shipping and Security Company - site interactions
//  Page entrance, live adverts carousel, smooth-scroll nav,
//  animated stat counters, and the interactive global network map.
// ==========================================================================

(function () {
  var prefersReduced =
    window.matchMedia &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  document.addEventListener('DOMContentLoaded', function () {
    // ---- Page entrance ----
    if (prefersReduced) {
      document.documentElement.classList.add('is-loaded');
    } else {
      setTimeout(function () {
        document.documentElement.classList.add('is-loaded');
      }, 120);
    }

    setFooterYear();
    initAdverts();
    initSmoothNav();
    initCounters();
    initMap();
    initNetworkAccordion();
  });

  // ---- Footer year ----
  function setFooterYear() {
    var el = document.getElementById('footerYear');
    if (el) el.textContent = new Date().getFullYear();
  }

  // ---- Live adverts carousel ----
  function initAdverts() {
    var track = document.getElementById('advertTrack');
    var dotsWrap = document.getElementById('advertDots');
    if (!track) return;

    var slides = Array.prototype.slice.call(
      track.querySelectorAll('.advert-slide')
    );
    if (slides.length <= 1) return;

    var current = 0;
    var timer = null;

    // Build dots
    slides.forEach(function (_, i) {
      var dot = document.createElement('button');
      dot.setAttribute('aria-label', 'Show announcement ' + (i + 1));
      if (i === 0) dot.classList.add('active');
      dot.addEventListener('click', function () {
        show(i);
        restart();
      });
      dotsWrap.appendChild(dot);
    });

    var dots = Array.prototype.slice.call(dotsWrap.querySelectorAll('button'));

    function show(index) {
      current = (index + slides.length) % slides.length;
      slides.forEach(function (s, i) {
        s.classList.toggle('active', i === current);
      });
      dots.forEach(function (d, i) {
        d.classList.toggle('active', i === current);
      });
    }

    function next() {
      show(current + 1);
    }

    function start() {
      if (prefersReduced) return;
      timer = setInterval(next, 4500);
    }

    function restart() {
      if (timer) clearInterval(timer);
      start();
    }

    // Pause on hover for readability
    track.addEventListener('mouseenter', function () {
      if (timer) clearInterval(timer);
    });
    track.addEventListener('mouseleave', restart);

    start();
  }

  // ---- Smooth-scroll navigation (sidebar + buttons + footer links) ----
  function initSmoothNav() {
    var sideMenu = document.getElementById('sideMenu');
    var mainWrapper = document.getElementById('mainWrapper');

    document.querySelectorAll('[data-target]').forEach(function (el) {
      el.addEventListener('click', function (e) {
        var id = el.getAttribute('data-target');
        var target = document.getElementById(id);
        if (!target) return;
        e.preventDefault();

        // Close the sliding menu if it is open
        if (sideMenu) sideMenu.classList.remove('open');
        if (mainWrapper) mainWrapper.classList.remove('shift');

        target.scrollIntoView({
          behavior: prefersReduced ? 'auto' : 'smooth',
          block: 'start',
        });
      });
    });
  }

  // ---- Animated stat counters (run once on scroll into view) ----
  function initCounters() {
    var nums = Array.prototype.slice.call(
      document.querySelectorAll('.stat-num[data-count]')
    );
    if (!nums.length) return;

    function animate(el) {
      var target = parseInt(el.getAttribute('data-count'), 10) || 0;
      var suffix = el.getAttribute('data-suffix') || '';
      if (prefersReduced) {
        el.textContent = target + suffix;
        return;
      }
      var start = 0;
      var duration = 1400;
      var startTime = null;
      function step(ts) {
        if (!startTime) startTime = ts;
        var progress = Math.min((ts - startTime) / duration, 1);
        var eased = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.floor(eased * target) + suffix;
        if (progress < 1) requestAnimationFrame(step);
        else el.textContent = target + suffix;
      }
      requestAnimationFrame(step);
    }

    if (!('IntersectionObserver' in window)) {
      nums.forEach(animate);
      return;
    }

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            animate(entry.target);
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.4 }
    );

    nums.forEach(function (n) {
      observer.observe(n);
    });
  }

  // ---- Interactive global network map ----
  function initMap() {
    var mapEl = document.getElementById('networkMap');
    if (!mapEl || typeof L === 'undefined') return;

    var hubs = [
      { name: 'New York', role: 'Cash &amp; Bullion Hub', coords: [40.7128, -74.006] },
      { name: 'London', role: 'Global Custody Center', coords: [51.5074, -0.1278] },
      { name: 'Zurich', role: 'Bullion Vaulting', coords: [47.3769, 8.5417] },
      { name: 'Dubai', role: 'Secure Transit Hub', coords: [25.2048, 55.2708] },
      { name: 'Hong Kong', role: 'Precious Goods Gateway', coords: [22.3193, 114.1694] },
      { name: 'Singapore', role: 'Vault &amp; Freeport', coords: [1.3521, 103.8198] },
      { name: 'Johannesburg', role: 'Metals Origin Hub', coords: [-26.2041, 28.0473] },
      { name: 'Frankfurt', role: 'Cash Processing', coords: [50.1109, 8.6821] },
    ];

    var map = L.map(mapEl, {
      center: [25, 15],
      zoom: 2,
      scrollWheelZoom: false,
      worldCopyJump: true,
    });

    // Dark tile layer for the luxury look
    L.tileLayer(
      'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png',
      {
        attribution:
          '&copy; OpenStreetMap &copy; CARTO',
        subdomains: 'abcd',
        maxZoom: 19,
      }
    ).addTo(map);

    var goldIcon = L.divIcon({
      className: '',
      html: '<div class="map-pin"></div>',
      iconSize: [14, 14],
      iconAnchor: [7, 7],
    });

    var latlngs = [];
    hubs.forEach(function (hub) {
      latlngs.push(hub.coords);
      L.marker(hub.coords, { icon: goldIcon })
        .addTo(map)
        .bindPopup(
          '<strong style="color:#d4af37;letter-spacing:1px;">' +
            hub.name +
            '</strong><br>' +
            hub.role
        );
    });

    // Connecting arcs between hubs to imply an active network
    L.polyline(latlngs, {
      color: '#d4af37',
      weight: 1,
      opacity: 0.35,
      dashArray: '4 6',
    }).addTo(map);
  }

  // ---- Global network region accordion ----
  function initNetworkAccordion() {
    var container = document.getElementById('networkAccordion');
    var regions = window.RBH_NETWORK_REGIONS;

    if (!container || !regions || !regions.length) return;

    regions.forEach(function (region) {
      var sorted = region.countries.slice().sort(function (a, b) {
        return a.localeCompare(b);
      });

      var panel = document.createElement('div');
      panel.className = 'network-panel';
      panel.id = 'region-' + region.id;

      var toggle = document.createElement('button');
      toggle.type = 'button';
      toggle.className = 'network-node';
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-controls', region.id + '-countries');
      toggle.innerHTML =
        '<span class="region-label">' +
        region.label.toUpperCase() +
        '</span>' +
        '<span class="region-meta">' +
        sorted.length +
        ' Countries</span>' +
        '<span class="plus-icon" aria-hidden="true">+</span>';

      var body = document.createElement('div');
      body.className = 'network-countries';
      body.id = region.id + '-countries';

      var inner = document.createElement('div');
      inner.className = 'network-countries-inner';

      var summary = document.createElement('div');
      summary.className = 'network-summary';
      summary.textContent =
        'Active partner & custody nodes across ' + sorted.length + ' territories';

      var list = document.createElement('ul');
      list.className = 'country-grid';

      sorted.forEach(function (country) {
        var item = document.createElement('li');
        var chip = document.createElement('span');
        chip.className = 'country-chip';
        chip.textContent = country;
        item.appendChild(chip);
        list.appendChild(item);
      });

      inner.appendChild(summary);
      inner.appendChild(list);
      body.appendChild(inner);
      panel.appendChild(toggle);
      panel.appendChild(body);
      container.appendChild(panel);

      toggle.addEventListener('click', function () {
        var isOpen = panel.classList.contains('is-open');

        container.querySelectorAll('.network-panel.is-open').forEach(function (openPanel) {
          if (openPanel !== panel) {
            openPanel.classList.remove('is-open');
            var openBtn = openPanel.querySelector('.network-node');
            var openBody = openPanel.querySelector('.network-countries');
            if (openBtn) openBtn.setAttribute('aria-expanded', 'false');
            if (openBody) openBody.style.maxHeight = '0';
          }
        });

        if (isOpen) {
          panel.classList.remove('is-open');
          body.style.maxHeight = '0';
          toggle.setAttribute('aria-expanded', 'false');
        } else {
          panel.classList.add('is-open');
          body.style.maxHeight = body.scrollHeight + 'px';
          toggle.setAttribute('aria-expanded', 'true');
        }
      });
    });
  }
})();
