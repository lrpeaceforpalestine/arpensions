---
layout: default
title: "Arkansans for Pension Integrity — Arkansas Pension Accountability"
description: "The evidence-led Arkansas Israel Bonds record: confirmed securities, ATRS manager funding, conditional transactions, primary documents, and issuer-neutral safeguards."
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

    <div class="breakout">{% include analysis-record-matrix.html %}</div>

    <p><a class="btn-primary" href="{{ '/evidence/' | relative_url }}">Follow the evidence trail</a></p>
  </div>
</section>

<hr class="section-divider section-divider--guilloche" aria-hidden="true">

{% include role-ctas.html %}

<section class="about-section">
  <div class="container container-prose">
    <span class="section-label">A 2027 legislative priority</span>
    <h2>The Pension Investment Integrity Act</h2>
    <p>{{ inv.legislation.full_summary }}</p>
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
