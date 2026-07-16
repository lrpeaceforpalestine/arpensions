(function () {
  'use strict';

  var host = document.getElementById('can-petition-area-stand-for-pension-integrity');
  if (!host) return;

  function enhanceForm() {
    var form = host.querySelector('#can_embed_form');
    if (!form) return false;

    form.querySelectorAll('input.required, select.required, textarea.required').forEach(function (field) {
      field.required = true;
      field.setAttribute('aria-required', 'true');
    });

    var country = form.querySelector('#form-country');
    if (country) {
      country.setAttribute('aria-label', 'Country (required)');
      country.setAttribute('autocomplete', 'country');
    }

    host.setAttribute('data-a11y-enhanced', 'true');
    return true;
  }

  if (enhanceForm()) return;

  var observer = new MutationObserver(function () {
    if (enhanceForm()) observer.disconnect();
  });
  observer.observe(host, { childList: true, subtree: true });
})();
