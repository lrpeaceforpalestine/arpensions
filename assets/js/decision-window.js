/* Interactive sequence chart for the 2025 agency decisions. */
(function () {
  'use strict';

  if (typeof ApexCharts === 'undefined') return;
  var chartEl = document.getElementById('decision-window-chart');
  if (!chartEl) return;

  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var instance = null;

  function d(value) { return new Date(value + 'T12:00:00').getTime(); }

  function palette() {
    var dark = document.documentElement.getAttribute('data-theme') === 'dark';
    return {
      treasury: dark ? '#82D8A8' : '#013237',
      apers: dark ? '#5FBF8B' : '#2F8F5B',
      atrs: dark ? '#F8C66A' : '#B45309',
      treasuryLight: dark ? 'rgba(130,216,168,0.32)' : 'rgba(1,50,55,0.22)',
      apersLight: dark ? 'rgba(95,191,139,0.32)' : 'rgba(47,143,91,0.22)',
      atrsLight: dark ? 'rgba(248,198,106,0.34)' : 'rgba(180,83,9,0.22)',
      text: dark ? '#E6F9E4' : '#25352B',
      muted: dark ? '#A9CDB8' : '#5C6B62',
      grid: dark ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.07)',
      tooltip: dark ? '#074750' : '#FFFFFF',
      annotation: dark ? '#C9F2D2' : '#2F8F5B'
    };
  }

  var descriptions = [
    'April 14–15 itinerary → May 2025 settled Treasury positions',
    'April 14–15 itinerary → May 15 APERS authorization',
    'April 14–15 itinerary → June 2 ATRS authorization',
    'May 15 authorization → October 15 APERS purchase',
    'June 2 authorization → December 29 ATRS manager funding'
  ];

  function build() {
    var c = palette();
    if (instance) instance.destroy();

    instance = new ApexCharts(chartEl, {
      chart: {
        type: 'rangeBar',
        height: 285,
        fontFamily: 'Mulish, system-ui, sans-serif',
        background: 'transparent',
        toolbar: { show: false },
        animations: { enabled: !reducedMotion, speed: 550, easing: 'easeinout' }
      },
      plotOptions: {
        bar: { horizontal: true, barHeight: '54%', rangeBarGroupRows: true, borderRadius: 2 }
      },
      colors: [c.treasury, c.apers, c.atrs, c.apersLight, c.atrsLight],
      series: [
        { name: 'Treasury decision sequence', data: [{ x: 'State Treasury', y: [d('2025-04-14'), d('2025-05-15')] }] },
        { name: 'APERS decision sequence', data: [{ x: 'APERS', y: [d('2025-04-14'), d('2025-05-15')] }] },
        { name: 'ATRS decision sequence', data: [{ x: 'ATRS', y: [d('2025-04-14'), d('2025-06-02')] }] },
        { name: 'APERS follow-through', data: [{ x: 'APERS', y: [d('2025-05-15'), d('2025-10-15')] }] },
        { name: 'ATRS follow-through', data: [{ x: 'ATRS', y: [d('2025-06-02'), d('2025-12-29')] }] }
      ],
      dataLabels: { enabled: false },
      stroke: { width: 0 },
      grid: { borderColor: c.grid, strokeDashArray: 3 },
      legend: { show: false },
      xaxis: {
        type: 'datetime',
        min: d('2025-04-01'),
        max: d('2026-01-10'),
        labels: {
          datetimeUTC: false,
          format: 'MMM yyyy',
          style: { colors: c.muted, fontFamily: 'IBM Plex Mono, monospace', fontSize: '10px' }
        },
        axisBorder: { show: false },
        axisTicks: { show: false }
      },
      yaxis: { labels: { style: { colors: [c.text], fontSize: '12px', fontWeight: 600 } } },
      tooltip: {
        theme: false,
        custom: function (context) {
          return '<div style="padding:10px 12px;max-width:290px;background:' + c.tooltip + ';color:' + c.text + ';border:1px solid ' + c.grid + ';border-radius:2px;font:12px/1.45 Mulish,system-ui,sans-serif">' +
            '<strong>' + context.w.globals.seriesNames[context.seriesIndex] + '</strong><br>' +
            '<span style="color:' + c.muted + '">' + descriptions[context.seriesIndex] + '</span></div>';
        }
      },
      annotations: {
        xaxis: [{
          x: d('2025-04-14'),
          strokeDashArray: 4,
          borderColor: c.annotation,
          label: {
            text: 'April itinerary',
            orientation: 'horizontal',
            borderColor: c.annotation,
            style: {
              color: c.text,
              background: c.tooltip,
              fontSize: '10px',
              fontFamily: 'IBM Plex Mono, monospace',
              fontWeight: 500
            },
            offsetY: -8
          }
        }]
      }
    });
    instance.render();
  }

  var legend = document.getElementById('decision-window-legend');
  if (legend) {
    legend.innerHTML =
      '<span class="dw-legend-item"><span class="dw-legend-swatch dw-legend-swatch--solid"></span>Outreach to agency decision</span>' +
      '<span class="dw-legend-item"><span class="dw-legend-swatch dw-legend-swatch--light"></span>Decision to purchase or manager funding</span>';
  }

  new MutationObserver(function (mutations) {
    mutations.forEach(function (mutation) {
      if (mutation.attributeName === 'data-theme') build();
    });
  }).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', build);
  else build();
})();
