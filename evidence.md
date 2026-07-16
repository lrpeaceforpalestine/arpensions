---
layout: evidence
title: "Evidence — The Arkansas Public Investment Record"
description: "A source-led account of confirmed securities, ATRS manager funding, analytical materials, open record questions, and documented institutional routes."
permalink: /evidence/
evidence_toc: true
---

{% assign inv = site.data.investigation %}
{% assign apers = inv.agencies | where: "id", "apers" | first %}
{% assign atrs = inv.agencies | where: "id", "atrs" | first %}

<div class="evidence-page" markdown="1">

{% include evidence-ledger.html %}

{% include exposure-chart.html %}

The **{{ inv.metrics.pension_authorization_ceiling.display }} pension authorization ceiling** is a separate measure: {{ atrs.authorization_display }} at ATRS and {{ apers.authorization_display }} at APERS. The ceiling should be used to describe board authority, not holdings or cash already deployed.

## Agency-by-agency investment status {#agency-by-agency}

{% include agency-status.html %}

### How to read the labels

<div class="status-key">
{% for item in inv.status_labels %}
  <div><span class="evidence-status evidence-status--{{ item[0] | replace: '_', '-' }}">{{ item[0] | replace: '_', ' ' }}</span><p>{{ item[1] }}</p></div>
{% endfor %}
</div>

## The analysis record

<p class="record-lead">{{ inv.analysis_record.lead }}</p>

{% include analysis-record-matrix.html %}

### ATRS packet pages 149–150

Physical page 149 of the June 2, 2025 Board packet is a substantive Aon memorandum. It advises ATRS to use a manager, summarizes BlackRock and Reams, recommends Reams, and states that limited marketability reduces traditional active management. Physical page 150 defines Aon’s scope: it does not recommend whether ATRS should invest or which individual security it should buy.

The two pages document a division of responsibility between implementation advice and the underlying merits decision. [Open both rendered pages](/documents/records/atrs-aon-memo/).

### Treasury recommendation and later transaction

The October 8, 2024 internal overview recommends holding the existing positions, allowing scheduled maturities to roll off, and maintaining credit surveillance. The May 2025 transaction record documents a later {{ inv.transaction_figures.treasury_may_settled.display }} settled purchase. The documentary issue is the absence of an identified written reconciliation in the reviewed production—not a conclusion about who had final authority or why the purchase occurred.

## Open record questions

- Reams monthly valuations, transaction reports, CUSIP-level holdings, and deployment dates after ATRS funded the mandate.
- Any additional ATRS sovereign-credit or portfolio-fit work presented to trustees, including evidence of how the S&amp;P downgrade report was used.
- Any Callan or APERS staff sovereign-credit memorandum tied to the May 2025 authorization.
- APERS records clarifying whether the {{ apers.measure_display }} purchase was a first stage, a final amount, or an implementation requiring further board treatment.
- Treasury records showing whether the February 2026 payment settled and produced a beneficial holding.
- Any Treasury writing that superseded or reconciled the October 2024 HOLD recommendation.
- Meeting-specific evidence resolving which scheduled Capitol-tour stops occurred and who attended.

{% include evidence-boundary.html text="An unproduced record is a bounded finding about the reviewed release. It does not establish that no oral discussion, unproduced writing, or off-record communication existed." %}

## Scheduled, confirmed, reported, and unconfirmed events {#events-and-routes}

<ol class="record-timeline">
{% for event in inv.timeline %}
  <li><time datetime="{{ event.date }}">{{ event.date_display }}</time><p>{{ event.description }}</p><span class="evidence-status evidence-status--{{ event.status | replace: ' ', '-' }}">{{ event.status_display }}</span></li>
{% endfor %}
</ol>

{% include documented-routes.html %}

{% include citation.html source_id="capitol_itinerary" %}
{% include citation.html source_id="hudson_babbitt_confirmation" %}
{% include citation.html source_id="seller_reported_meetings" %}

## Primary records and findings

<div class="source-card-grid">
  <a class="source-card" href="{{ inv.sources.atrs_aon.record_url }}"><span class="source-card-label">{{ inv.sources.atrs_aon.agency }} · pages 149–150</span><strong>{{ inv.sources.atrs_aon.title }}</strong><p>Implementation advice, manager comparison, Reams recommendation, and scope boundary.</p><span class="source-card-action">Open record →</span></a>
  <a class="source-card" href="{{ inv.sources.atrs_resolution.record_url }}"><span class="source-card-label">{{ inv.sources.atrs_resolution.agency }} · executed resolution</span><strong>{{ inv.sources.atrs_resolution.title }}</strong><p>Adoption, signature, authorization ceiling, manager selection, and delegated implementation authority.</p><span class="source-card-action">Open record →</span></a>
  <a class="source-card" href="{{ inv.sources.atrs_funding.record_url }}"><span class="source-card-label">{{ inv.sources.atrs_funding.agency }} · Board update</span><strong>{{ inv.sources.atrs_funding.title }}</strong><p>The distinct manager-account funding event documented in December 2025.</p><span class="source-card-action">Open record →</span></a>
  <a class="source-card" href="{{ inv.sources.apers_authorization.record_url }}"><span class="source-card-label">{{ inv.sources.apers_authorization.agency }} · signed minutes</span><strong>{{ inv.sources.apers_authorization.title }}</strong><p>The final motion, seconder, and recorded outcome.</p><span class="source-card-action">Open record →</span></a>
  <a class="source-card" href="{{ inv.sources.apers_analysis_email.record_url }}"><span class="source-card-label">{{ inv.sources.apers_analysis_email.agency }} · FOIA-search email</span><strong>{{ inv.sources.apers_analysis_email.title }}</strong><p>The chief investment officer's account of Board and consultant materials responsive to the request.</p><span class="source-card-action">Open record →</span></a>
  <a class="source-card" href="{{ inv.sources.apers_purchase.record_url }}"><span class="source-card-label">{{ inv.sources.apers_purchase.agency }} · purchase record</span><strong>{{ inv.sources.apers_purchase.title }}</strong><p>Transaction amount, date, beneficiary, and security identifier with operational fields masked.</p><span class="source-card-action">Open record →</span></a>
  <a class="source-card" href="{{ inv.sources.treasury_hold.record_url }}"><span class="source-card-label">{{ inv.sources.treasury_hold.agency }} · internal analysis</span><strong>{{ inv.sources.treasury_hold.title }}</strong><p>Credit summary, downgrade discussion, and portfolio recommendation.</p><span class="source-card-action">Open record →</span></a>
  <a class="source-card" href="{{ inv.sources.treasury_holdings.record_url }}"><span class="source-card-label">{{ inv.sources.treasury_holdings.agency }} · statement</span><strong>{{ inv.sources.treasury_holdings.title }}</strong><p>A dated security-level statement supporting the derived Treasury floor.</p><span class="source-card-action">Open record →</span></a>
  <a class="source-card" href="{{ inv.sources.treasury_maturity.record_url }}"><span class="source-card-label">{{ inv.sources.treasury_maturity.agency }} · cash-flow record</span><strong>{{ inv.sources.treasury_maturity.title }}</strong><p>The final maturity subtracted from the June statement to derive the current floor.</p><span class="source-card-action">Open record →</span></a>
  <a class="source-card" href="{{ inv.sources.treasury_processing.record_url }}"><span class="source-card-label">{{ inv.sources.treasury_processing.agency }} · payment state</span><strong>{{ inv.sources.treasury_processing.title }}</strong><p>The transaction state that keeps the additional amount conditional.</p><span class="source-card-action">Open record →</span></a>
</div>

<div class="finding-card-grid">
  <a class="finding-card" href="/findings/procedural-asymmetry/"><span class="finding-card-label">Finding</span><strong>Different roles in the ATRS decision file</strong><p>Staff supplied the merits conclusion while Aon advised on manager implementation.</p><span class="finding-card-action">Read finding →</span></a>
  <a class="finding-card" href="/findings/auditor-channel/"><span class="finding-card-label">Finding</span><strong>Documented access and coordination</strong><p>Board roles, proxy participation, scheduling, promotion, and media routing.</p><span class="finding-card-action">Read finding →</span></a>
  <a class="finding-card" href="/findings/control-case/"><span class="finding-card-label">Finding</span><strong>ASHERS non-adoption comparison</strong><p>The same sellers appear in a record with a different institutional outcome.</p><span class="finding-card-action">Read finding →</span></a>
</div>

For review method, record boundaries, and page-level validation, see [Methodology](/methodology/). For the complete curated public trail, see [Documents](/documents/).

</div>
