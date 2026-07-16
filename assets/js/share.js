// Progressive share controls: ordinary email/Bluesky links work without JavaScript.
(function () {
  'use strict';

  var buttons = document.querySelectorAll('.share-copy[data-share-url]');
  if (!buttons.length) return;

  function fallbackCopy(value) {
    var area = document.createElement('textarea');
    area.value = value;
    area.setAttribute('readonly', '');
    area.style.position = 'fixed';
    area.style.opacity = '0';
    document.body.appendChild(area);
    area.select();
    document.execCommand('copy');
    area.remove();
  }

  buttons.forEach(function (button) {
    button.hidden = false;
    button.addEventListener('click', function () {
      var value = button.getAttribute('data-share-url');
      var copied = navigator.clipboard && navigator.clipboard.writeText
        ? navigator.clipboard.writeText(value)
        : Promise.resolve(fallbackCopy(value));

      copied.then(function () {
        var original = button.textContent;
        button.textContent = 'Link copied';
        window.setTimeout(function () { button.textContent = original; }, 1800);
      }).catch(function () {
        fallbackCopy(value);
        button.textContent = 'Link copied';
      });
    });
  });
})();
