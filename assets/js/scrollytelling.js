// Scroll-driven summary on the Evidence page. The words and figures live in
// the page markup so the same explanation remains available without JavaScript.
(function () {
  'use strict';

  if (typeof scrollama === 'undefined') return;
  var section = document.querySelector('.scrolly');
  if (!section) return;

  var steps = Array.prototype.slice.call(section.querySelectorAll('.scrolly__step'));
  var statEl = document.getElementById('scrolly-stat');
  var subEl = document.getElementById('scrolly-subtitle');
  if (!steps.length || !statEl || !subEl) return;

  var scroller = scrollama();
  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var currentStep = -1;
  var transitionId = 0;

  function stateFor(step) {
    return {
      stat: step.getAttribute('data-stat') || '',
      subtitle: step.getAttribute('data-subtitle') || '',
      colorClass: step.getAttribute('data-color-class') || 'viz-stat--accent'
    };
  }

  function swap(stepIndex) {
    if (stepIndex === currentStep || !steps[stepIndex]) return;
    var next = stateFor(steps[stepIndex]);
    currentStep = stepIndex;
    transitionId += 1;
    var thisTransition = transitionId;

    function setContent() {
      if (thisTransition !== transitionId) return;
      statEl.textContent = next.stat;
      statEl.className = 'viz-stat ' + next.colorClass;
      subEl.textContent = next.subtitle;
      statEl.style.opacity = '1';
      subEl.style.opacity = '1';
    }

    if (reducedMotion) {
      setContent();
      return;
    }

    statEl.style.transition = 'opacity 0.18s ease';
    subEl.style.transition = 'opacity 0.18s ease';
    statEl.style.opacity = '0';
    subEl.style.opacity = '0';
    window.setTimeout(setContent, 190);
  }

  function enter(response) {
    steps.forEach(function (step) { step.classList.remove('is-active'); });
    response.element.classList.add('is-active');
    swap(response.index);
  }

  steps[0].classList.add('is-active');
  scroller.setup({ step: '.scrolly__step', offset: 0.5, debug: false }).onStepEnter(enter);
  window.addEventListener('resize', scroller.resize);
  section.classList.add('scrolly--initialized');
})();
