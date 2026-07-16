---
layout: default
title: "Arkansans for Pension Integrity — Arkansas Pension Accountability"
description: "The current Arkansas public investment record, with confirmed securities, manager funding, and conditional transactions kept distinct."
---

{% assign inv = site.data.investigation %}
{% assign apers = inv.agencies | where: "id", "apers" | first %}
{% include hero.html %}

{% include stats-bar.html %}

<section class="home-record-section">
  <div class="container container-prose">
    <span class="section-label">The decision record</span>
    <h2>What the decision files address—and what they leave open</h2>
    <p class="record-lead">{{ inv.analysis_record.lead }}</p>

    <div class="analysis-matrix breakout">
      <div class="analysis-matrix-row analysis-matrix-head"><strong>Institution</strong><span>What the file contains</span><span>What remains open</span></div>
      <div class="analysis-matrix-row"><strong>ATRS</strong><p>Aon implementation and manager-selection advice, a Reams recommendation, marketability language, and an S&amp;P downgrade report elsewhere in the production.</p><p>The produced vote file does not connect a developed sovereign-credit and portfolio-fit evaluation to the invest-or-not decision.</p></div>
      <div class="analysis-matrix-row"><strong>APERS</strong><p>Authorization records, seller materials, operational correspondence, and the later {{ apers.measure }}.</p><p>The reviewed authorization file contains no Callan sovereign-credit memorandum tied to the decision.</p></div>
      <div class="analysis-matrix-row"><strong>Treasury</strong><p>An internal credit overview recommending HOLD and continued surveillance.</p><p>The settled May 2025 purchase is not accompanied by an identified written reconciliation with that recommendation.</p></div>
    </div>

    <p><a class="btn-primary" href="{{ '/evidence/' | relative_url }}">Follow the evidence trail</a></p>
  </div>
</section>

<hr class="section-divider section-divider--guilloche" aria-hidden="true">

{% include role-ctas.html %}

<section class="about-section">
  <div class="container container-prose">
    <span class="section-label">A 2027 legislative priority</span>
    <h2>The Pension Investment Integrity Act</h2>
    <p>The Integrity Act would require a written credit analysis, a comparison with available alternatives, plain-language liquidity disclosure, a documented fiduciary determination, and public posting before or shortly after an Arkansas pension plan acquires non-tradable sovereign debt.</p>
    <p>{{ inv.legislation.cfc_status }} The proposal is issuer-neutral: it governs the process used for this asset class, not the identity of a country or issuer.</p>
    <p><a href="{{ '/legislators/' | relative_url }}" class="about-link">Read the policy brief &rarr;</a></p>
  </div>
</section>

<section class="pathways" aria-label="Campaign actions">
  <div class="pathway-list">
    <a href="{{ '/documents/' | relative_url }}" class="pathway-row">
      <div class="container pathway-row-inner">
        <span class="pathway-title">Read the primary records</span>
        <span class="pathway-desc">Open the curated source trail and exact page locators</span>
        <span class="pathway-arrow" aria-hidden="true">&rarr;</span>
      </div>
    </a>
    <a href="{{ '/take-action/' | relative_url }}" class="pathway-row">
      <div class="container pathway-row-inner">
        <span class="pathway-title">Back the Integrity Act</span>
        <span class="pathway-desc">Sign on, contact legislators, and share the campaign</span>
        <span class="pathway-arrow" aria-hidden="true">&rarr;</span>
      </div>
    </a>
  </div>
</section>
