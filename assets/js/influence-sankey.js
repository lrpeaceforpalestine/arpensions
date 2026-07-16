/* Equal-weight D3 route map for the Issue page. */
(function () {
  'use strict';

  if (typeof d3 === 'undefined' || typeof d3.sankey === 'undefined') return;
  var container = document.getElementById('influence-sankey');
  if (!container) return;

  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasAnimated = false;

  function palette() {
    var dark = document.documentElement.getAttribute('data-theme') === 'dark';
    return {
      seller: dark ? '#A9CDB8' : '#3F4F46',
      office: dark ? '#82D8A8' : '#2F8F5B',
      route: dark ? '#F8C66A' : '#B45309',
      agency: dark ? '#5FBF8B' : '#0E6D50',
      action: dark ? '#C9F2D2' : '#013237',
      text: dark ? '#E6F9E4' : '#25352B',
      muted: dark ? '#A9CDB8' : '#5C6B62',
      base: dark ? 0.30 : 0.24,
      hover: dark ? 0.78 : 0.68
    };
  }

  var nodes = [
    { id: 'seller', label: 'Israel Bonds representatives', category: 'seller' },
    { id: 'auditor', label: 'Auditor of State office', category: 'office' },
    { id: 'dfa', label: 'DFA contact', category: 'office' },
    { id: 'itinerary', label: 'April 2025 itinerary', category: 'route' },
    { id: 'brady', label: 'Jason Brady', category: 'office' },
    { id: 'ashers-intro', label: 'ASHERS introduction', category: 'route' },
    { id: 'treasury', label: 'State Treasury', category: 'agency' },
    { id: 'apers', label: 'APERS', category: 'agency' },
    { id: 'atrs', label: 'ATRS', category: 'agency' },
    { id: 'ashers', label: 'ASHERS', category: 'agency' },
    { id: 'treasury-action', label: 'Treasury: $50M completed', category: 'action' },
    { id: 'apers-action', label: 'APERS: $15M purchased', category: 'action' },
    { id: 'atrs-action', label: 'ATRS: $50M account funded', category: 'action' }
  ];

  var links = [
    { source: 'seller', target: 'itinerary', desc: 'Seller representatives appear on the April 14–15 itinerary.' },
    { source: 'auditor', target: 'itinerary', desc: 'Auditor staff records document scheduling and coordination.' },
    { source: 'auditor', target: 'brady', desc: 'Brady served as the Auditor’s designee and proxy on pension boards.' },
    { source: 'dfa', target: 'ashers-intro', desc: 'DFA introduced the seller to ASHERS leadership.' },
    { source: 'seller', target: 'ashers-intro', desc: 'The introduction led to a documented seller presentation.' },
    { source: 'itinerary', target: 'treasury', desc: 'Treasury personnel were listed on the itinerary; a seller report later described the encounter.' },
    { source: 'itinerary', target: 'apers', desc: 'APERS leadership was listed among the itinerary stops.' },
    { source: 'itinerary', target: 'atrs', desc: 'ATRS leadership was listed among the itinerary stops.' },
    { source: 'ashers-intro', target: 'ashers', desc: 'ASHERS received the pitch; its available agency records show no later authorization or purchase.' },
    { source: 'brady', target: 'apers', desc: 'As the Auditor’s proxy, Brady presented and moved the APERS authorization.' },
    { source: 'brady', target: 'atrs', desc: 'Brady also appeared as the Auditor’s designee at ATRS.' },
    { source: 'treasury', target: 'treasury-action', desc: 'Treasury records support $50 million in completed purchases after a later maturity.' },
    { source: 'apers', target: 'apers-action', desc: 'APERS later completed a $15 million purchase.' },
    { source: 'atrs', target: 'atrs-action', desc: 'ATRS later reported $50 million funded to the Reams manager account.' }
  ];

  function width() { return Math.min(container.clientWidth || 760, 840); }
  function categoryColor(c, category) { return c[category] || c.office; }

  function syncLegend(c) {
    document.querySelectorAll('.sankey-legend-dot[data-category]').forEach(function (dot) {
      var category = dot.getAttribute('data-category');
      if (c[category]) dot.style.background = c[category];
    });
  }

  function render() {
    var c = palette();
    var chartWidth = width();
    var chartHeight = 470;
    var margin = { top: 18, right: 24, bottom: 18, left: 24 };

    d3.select(container).selectAll('*').remove();

    var svgRoot = d3.select(container).append('svg')
      .attr('viewBox', '0 0 ' + chartWidth + ' ' + chartHeight)
      .attr('width', '100%')
      .attr('height', chartHeight)
      .attr('role', 'img')
      .attr('aria-label', 'Equal-weight route map connecting Israel Bonds representatives, the Auditor of State office, DFA, the April 2025 itinerary, Arkansas agencies, and the later Treasury, APERS, and ATRS transactions.');

    var svg = svgRoot.append('g').attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');
    var map = {};
    nodes.forEach(function (node, index) { map[node.id] = index; });

    var sankey = d3.sankey()
      .nodeId(function (node) { return node.index; })
      .nodeWidth(18)
      .nodePadding(13)
      .nodeSort(null)
      .extent([[0, 0], [chartWidth - margin.left - margin.right, chartHeight - margin.top - margin.bottom]]);

    var graph = sankey({
      nodes: nodes.map(function (node) { return { id: node.id, name: node.label, category: node.category }; }),
      links: links.map(function (link) { return { source: map[link.source], target: map[link.target], value: 1, desc: link.desc }; })
    });

    var linkPaths = svg.append('g').attr('class', 'sankey-links').attr('fill', 'none')
      .selectAll('path').data(graph.links).join('path')
      .attr('d', d3.sankeyLinkHorizontal())
      .attr('stroke', function (link) { return categoryColor(c, link.source.category); })
      .attr('stroke-opacity', c.base)
      .attr('stroke-width', function (link) { return Math.max(3, link.width); })
      .attr('tabindex', '0')
      .attr('role', 'link')
      .attr('aria-label', function (link) { return link.source.name + ' to ' + link.target.name + '. ' + link.desc; });

    linkPaths.append('title').text(function (link) {
      return link.source.name + ' → ' + link.target.name + ': ' + link.desc;
    });

    var tooltip = d3.select(container).append('div')
      .attr('class', 'sankey-tooltip')
      .attr('role', 'tooltip')
      .style('display', 'none');

    function showTooltip(event, link) {
      d3.select(event.currentTarget).attr('stroke-opacity', c.hover);
      var tip = tooltip.node();
      tip.textContent = '';
      var heading = document.createElement('strong');
      heading.textContent = link.source.name + ' → ' + link.target.name;
      var detail = document.createElement('span');
      detail.style.display = 'block';
      detail.style.color = palette().muted;
      detail.textContent = link.desc;
      tip.appendChild(heading);
      tip.appendChild(detail);
      tooltip.style('display', 'block');
      moveTooltip(event);
    }

    function moveTooltip(event) {
      var rect = container.getBoundingClientRect();
      var x = typeof event.clientX === 'number' && event.clientX ? event.clientX - rect.left + 12 : 18;
      var y = typeof event.clientY === 'number' && event.clientY ? event.clientY - rect.top - 8 : 18;
      var tipWidth = tooltip.node().offsetWidth;
      if (x + tipWidth > rect.width) x = Math.max(8, x - tipWidth - 24);
      tooltip.style('left', x + 'px').style('top', Math.max(8, y) + 'px');
    }

    function hideTooltip(event) {
      d3.select(event.currentTarget).attr('stroke-opacity', c.base);
      tooltip.style('display', 'none');
    }

    linkPaths
      .on('mouseenter focus', showTooltip)
      .on('mousemove', moveTooltip)
      .on('mouseleave blur', hideTooltip);

    var nodeGroups = svg.append('g').attr('class', 'sankey-nodes').selectAll('g')
      .data(graph.nodes).join('g');

    nodeGroups.append('rect')
      .attr('x', function (node) { return node.x0; })
      .attr('y', function (node) { return node.y0; })
      .attr('width', function (node) { return node.x1 - node.x0; })
      .attr('height', function (node) { return Math.max(5, node.y1 - node.y0); })
      .attr('fill', function (node) { return categoryColor(c, node.category); })
      .attr('rx', 2);

    nodeGroups.append('text')
      .attr('x', function (node) { return node.x0 < (chartWidth - margin.left - margin.right) / 2 ? node.x1 + 8 : node.x0 - 8; })
      .attr('y', function (node) { return (node.y0 + node.y1) / 2; })
      .attr('dy', '0.35em')
      .attr('text-anchor', function (node) { return node.x0 < (chartWidth - margin.left - margin.right) / 2 ? 'start' : 'end'; })
      .attr('font-family', 'Mulish, system-ui, sans-serif')
      .attr('font-size', '10.5px')
      .attr('font-weight', '600')
      .attr('fill', c.text)
      .text(function (node) { return node.name; });

    nodeGroups
      .on('mouseenter', function (event, node) {
        linkPaths.attr('stroke-opacity', c.base * 0.35);
        linkPaths.filter(function (link) { return link.source === node || link.target === node; }).attr('stroke-opacity', c.hover);
      })
      .on('mouseleave', function () { linkPaths.attr('stroke-opacity', c.base); });

    if (!reducedMotion && !hasAnimated && 'IntersectionObserver' in window) {
      linkPaths
        .attr('stroke-dasharray', function () { return this.getTotalLength() + ' ' + this.getTotalLength(); })
        .attr('stroke-dashoffset', function () { return this.getTotalLength(); });
      nodeGroups.attr('opacity', 0);
    }

    syncLegend(c);
  }

  function animate() {
    if (hasAnimated || reducedMotion) return;
    hasAnimated = true;
    var svg = d3.select(container).select('svg');
    svg.selectAll('.sankey-links path').transition().duration(1100).ease(d3.easeCubicOut).attr('stroke-dashoffset', 0);
    svg.selectAll('.sankey-nodes g').transition().delay(260).duration(550).attr('opacity', 1);
  }

  render();

  if (!reducedMotion && 'IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animate();
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.2 });
    observer.observe(container);
  }

  new MutationObserver(function (mutations) {
    mutations.forEach(function (mutation) {
      if (mutation.attributeName === 'data-theme') render();
    });
  }).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });

  var resizeTimer;
  window.addEventListener('resize', function () {
    window.clearTimeout(resizeTimer);
    resizeTimer = window.setTimeout(render, 220);
  });
})();
