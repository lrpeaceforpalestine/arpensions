/* Interactive charts used by the evidence and audience pages. */
(function () {
  'use strict';

  if (typeof Chart === 'undefined') return;

  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var instances = {};
  var exposureReady = false;

  function colors() {
    var dark = document.documentElement.getAttribute('data-theme') === 'dark';
    return {
      pine: dark ? '#5FBF8B' : '#013237',
      jade: dark ? '#82D8A8' : '#2F8F5B',
      amber: dark ? '#F8C66A' : '#B45309',
      processing: dark ? 'rgba(248,198,106,0.14)' : 'rgba(180,83,9,0.10)',
      gray: dark ? '#14555C' : '#DCE8DC',
      text: dark ? '#E6F9E4' : '#25352B',
      muted: dark ? '#A9CDB8' : '#5C6B62',
      tooltip: dark ? '#074750' : '#FFFFFF',
      grid: dark ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.07)'
    };
  }

  function numberFrom(canvas, name, fallback) {
    var parsed = Number(canvas.getAttribute(name));
    return Number.isFinite(parsed) ? parsed : fallback;
  }

  function initExposureChart() {
    var canvas = document.getElementById('exposure-chart');
    if (!canvas) return;

    var c = colors();
    var values = [
      numberFrom(canvas, 'data-treasury', 50),
      numberFrom(canvas, 'data-apers', 15),
      numberFrom(canvas, 'data-atrs', 50),
      numberFrom(canvas, 'data-processing', 10)
    ];
    var details = [
      'Completed Treasury purchases after the documented maturity',
      'Completed APERS purchase dated October 15, 2025',
      'Money funded to the ATRS manager account for the strategy',
      'Separate Treasury payment shown as still processing by the bank'
    ];

    if (instances.exposure) instances.exposure.destroy();
    instances.exposure = new Chart(canvas.getContext('2d'), {
      type: 'bar',
      data: {
        labels: ['Treasury purchases', 'APERS purchase', 'ATRS manager account', 'Treasury payment in process'],
        datasets: [{
          data: values,
          backgroundColor: [c.pine, c.jade, c.amber, c.processing],
          borderColor: [c.pine, c.jade, c.amber, c.amber],
          borderWidth: [0, 0, 0, 2],
          borderRadius: 2,
          barPercentage: 0.62,
          categoryPercentage: 0.82
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true,
        maintainAspectRatio: false,
        animation: { duration: reducedMotion ? 0 : 1000, easing: 'easeOutQuart' },
        plugins: {
          legend: { display: false },
          tooltip: {
            backgroundColor: c.tooltip,
            titleColor: c.text,
            bodyColor: c.muted,
            borderColor: c.grid,
            borderWidth: 1,
            padding: 12,
            titleFont: { family: 'Mulish, system-ui, sans-serif', size: 13, weight: '600' },
            bodyFont: { family: 'Mulish, system-ui, sans-serif', size: 12 },
            callbacks: {
              label: function (context) {
                return '$' + values[context.dataIndex] + 'M — ' + details[context.dataIndex];
              }
            }
          }
        },
        scales: {
          x: {
            beginAtZero: true,
            suggestedMax: 60,
            ticks: {
              callback: function (value) { return '$' + value + 'M'; },
              color: c.muted,
              font: { family: 'IBM Plex Mono, monospace', size: 11 }
            },
            grid: { color: c.grid },
            border: { display: false }
          },
          y: {
            ticks: { color: c.text, font: { family: 'Mulish, system-ui, sans-serif', size: 12, weight: '500' } },
            grid: { display: false }
          }
        }
      }
    });
  }

  function initFundedGauge(canvasId, fallbackRatio, fallbackLabel) {
    var canvas = document.getElementById(canvasId);
    if (!canvas) return;
    var ratio = numberFrom(canvas, 'data-ratio', fallbackRatio);
    var label = canvas.getAttribute('data-label') || fallbackLabel;
    var c = colors();

    if (instances[canvasId]) instances[canvasId].destroy();
    var centerText = {
      id: 'gaugeCenter_' + canvasId,
      afterDraw: function (chart) {
        var ctx = chart.ctx;
        var current = colors();
        ctx.save();
        ctx.font = '600 ' + Math.max(28, Math.round(chart.width * 0.13)) + 'px Mulish, system-ui, sans-serif';
        ctx.fillStyle = current.text;
        ctx.textAlign = 'center';
        ctx.textBaseline = 'bottom';
        ctx.fillText(ratio + '%', chart.width / 2, chart.height * 0.82);
        ctx.font = '500 ' + Math.max(10, Math.round(chart.width * 0.045)) + 'px "IBM Plex Mono", monospace';
        ctx.fillStyle = current.muted;
        ctx.textBaseline = 'top';
        ctx.fillText(label, chart.width / 2, chart.height * 0.82 + 4);
        ctx.restore();
      }
    };

    instances[canvasId] = new Chart(canvas.getContext('2d'), {
      type: 'doughnut',
      data: {
        labels: ['Funded', 'Unfunded gap'],
        datasets: [{
          data: [ratio, 100 - ratio],
          backgroundColor: [c.pine, c.gray],
          borderWidth: 0,
          circumference: 180,
          rotation: 270
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: true,
        aspectRatio: 2,
        cutout: '72%',
        animation: { duration: reducedMotion ? 0 : 900, easing: 'easeOutCubic' },
        plugins: {
          legend: { display: false },
          tooltip: {
            backgroundColor: c.tooltip,
            titleColor: c.text,
            bodyColor: c.muted,
            borderColor: c.grid,
            borderWidth: 1,
            padding: 10,
            callbacks: {
              label: function (context) {
                return context.dataIndex === 0 ? ratio + '% funded' : (100 - ratio) + '% funding gap';
              }
            }
          }
        }
      },
      plugins: [centerText]
    });
  }

  function initExposureOnScroll() {
    var canvas = document.getElementById('exposure-chart');
    if (!canvas || exposureReady) return;
    if (!('IntersectionObserver' in window)) {
      exposureReady = true;
      initExposureChart();
      return;
    }
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        exposureReady = true;
        initExposureChart();
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.25 });
    observer.observe(canvas);
  }

  function initAll() {
    initExposureOnScroll();
    initFundedGauge('atrs-funded-gauge', 84, 'ATRS funded ratio');
    initFundedGauge('apers-funded-gauge', 83, 'APERS funded ratio');
  }

  new MutationObserver(function (mutations) {
    mutations.forEach(function (mutation) {
      if (mutation.attributeName !== 'data-theme') return;
      if (exposureReady) initExposureChart();
      initFundedGauge('atrs-funded-gauge', 84, 'ATRS funded ratio');
      initFundedGauge('apers-funded-gauge', 83, 'APERS funded ratio');
    });
  }).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll);
  else initAll();
})();
