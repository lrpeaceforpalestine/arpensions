// Mobile nav toggle: Escape key, body-scroll lock, close on link click
// (the prior click-outside-to-close handler was dropped when the nav switched
// to a full-viewport overlay — clicking outside the menu = clicking the menu)
(function() {
  document.documentElement.classList.add('nav-js');
  var toggle = document.querySelector('.nav-toggle');
  var menu = document.getElementById('nav-menu');
  var nav = document.querySelector('.site-nav');
  var background = [
    document.querySelector('main'),
    document.querySelector('.site-footer'),
    document.querySelector('.mobile-cta-bar'),
    document.querySelector('.nav-logo'),
    document.querySelector('.theme-toggle-btn')
  ].filter(Boolean);

  if (!toggle || !menu || !nav) return;

  function closeMenu() {
    toggle.setAttribute('aria-expanded', 'false');
    menu.classList.remove('nav-open');
    document.body.style.overflow = '';
    background.forEach(function (element) { element.inert = false; });
  }

  function openMenu() {
    toggle.setAttribute('aria-expanded', 'true');
    menu.classList.add('nav-open');
    // Lock background scroll while the full-screen overlay is open
    document.body.style.overflow = 'hidden';
    background.forEach(function (element) { element.inert = true; });
    var firstItem = menu.querySelector('a');
    if (firstItem) firstItem.focus();
  }

  function isOpen() {
    return toggle.getAttribute('aria-expanded') === 'true';
  }

  toggle.addEventListener('click', function() {
    if (isOpen()) {
      closeMenu();
      toggle.focus();
    } else {
      openMenu();
    }
  });

  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && isOpen()) {
      closeMenu();
      toggle.focus();
      return;
    }

    if (e.key === 'Tab' && isOpen()) {
      var links = Array.prototype.slice.call(menu.querySelectorAll('a[href]'));
      var focusable = links.concat(toggle);
      var first = focusable[0];
      var last = focusable[focusable.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    }
  });

  // Close when a nav link is clicked (navigating away)
  menu.addEventListener('click', function(e) {
    if (e.target.tagName === 'A') {
      closeMenu();
    }
  });

  var desktop = window.matchMedia('(min-width: 769px)');
  function closeAtDesktop(event) {
    if (event.matches && isOpen()) closeMenu();
  }
  if (desktop.addEventListener) desktop.addEventListener('change', closeAtDesktop);
  else desktop.addListener(closeAtDesktop);
})();

// Scroll-triggered nav shadow — adds .is-scrolled when the page has scrolled
(function() {
  var nav = document.querySelector('.site-nav');
  if (!nav) return;

  function update() {
    if (window.scrollY > 4) nav.classList.add('is-scrolled');
    else nav.classList.remove('is-scrolled');
  }

  update();
  window.addEventListener('scroll', update, { passive: true });
})();

// Active nav highlighting — reinforce server-side aria-current with client-side path matching
(function() {
  var path = window.location.pathname.replace(/\/+$/, '') || '/';
  var links = document.querySelectorAll('.nav-links a');

  links.forEach(function(link) {
    var href = (link.getAttribute('href') || '').replace(/\/+$/, '') || '/';
    if (path === href || (href !== '/' && path.indexOf(href) === 0)) {
      link.setAttribute('aria-current', 'page');
    } else {
      link.removeAttribute('aria-current');
    }
  });
})();

// Static stat numbers; live count-up animation lives in scroll-animations.js ([data-countup]).

// External links — add target="_blank" and rel="noopener noreferrer" to off-site links
// Uses relList.add() to avoid clobbering existing rel values (WCAG 2.4.4)
(function() {
  var host = window.location.hostname;
  var links = document.querySelectorAll('a[href^="http"]');

  links.forEach(function(link) {
    if (link.hostname !== host) {
      link.setAttribute('target', '_blank');
      link.relList.add('noopener', 'noreferrer');

      if (!link.querySelector('.sr-only')) {
        var hint = document.createElement('span');
        hint.className = 'sr-only';
        hint.textContent = ' (opens in new tab)';
        link.appendChild(hint);
      }
    }
  });
})();
