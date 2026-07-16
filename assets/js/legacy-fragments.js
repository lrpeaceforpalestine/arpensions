(function () {
  'use strict';

  var legacyId = decodeURIComponent(window.location.hash.slice(1));
  if (!legacyId) return;

  var alias = document.getElementById(legacyId);
  var currentId = alias && alias.getAttribute('data-legacy-target');
  var current = currentId && document.getElementById(currentId);
  if (!current) return;

  function alignLegacyFragment() {
    current.scrollIntoView({ block: 'start' });
  }

  if (document.readyState === 'complete') {
    requestAnimationFrame(alignLegacyFragment);
  } else {
    window.addEventListener('load', alignLegacyFragment, { once: true });
  }
})();
