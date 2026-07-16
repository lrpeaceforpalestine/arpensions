---
layout: page
title: "Documents — Selected Primary Records"
description: "Privacy-reviewed anchor records supporting the principal findings on Arkansas public investment decisions."
permalink: /documents/
breadcrumb: "Documents"
mobile_cta_label: "Request a source locator"
mobile_cta_url: "mailto:info@arpensions.org?subject=Source%20locator%20request"
---

{% assign inv = site.data.investigation %}

## A curated source trail

This collection contains selected anchor records supporting the site's principal findings. Each record page identifies the agency source, date, exact page or locator, and any campaign-applied masking. The collection is not a complete mirror of every FOIA production.

Masking protects account numbers, transaction identifiers, user identifiers, direct contact information, and operational data that are not necessary to understand the public-interest finding. The underlying government records are not altered in the investigation corpus; the hosted excerpt is a separate publication copy.

Hosted PDFs include a searchable text layer, native or OCR, for accessibility. The visible page image remains the controlling publication excerpt, including every campaign-applied mask disclosed on its record page.

<div class="source-record-grid">
{% for pair in inv.sources %}
  {% assign source = pair[1] %}
  {% if source.record_url contains '/documents/records/' %}
  <article class="source-record-card">
    <span class="section-label">{{ source.agency }}</span>
    <h2><a href="{{ source.record_url | relative_url }}">{{ source.title }}</a></h2>
    <p>{{ source.locator }}</p>
    <p class="source-record-meta"><time datetime="{{ source.date }}">{{ source.date | date: "%B %-d, %Y" }}</time></p>
  </article>
  {% endif %}
{% endfor %}
</div>

## Official legal record

- [Act 498 of 2023 — Arkansas General Assembly]({{ inv.legislation.act_498_url }}) establishes the pension pecuniary-factor framework relevant to the campaign's proposal.

## Additional hosted records

Supplementary hosted records include Treasury purchase confirmations, investment policy, correspondence, and public news clippings. Read them with the [evidence ledger](/evidence/), status labels, and dated cutoffs.

- [Treasury May 2025 purchase confirmation](/assets/documents/sovereign-bond-purchase-confirmation-may2025.pdf)
- [Treasury November 2023 purchase confirmation](/assets/documents/sovereign-bond-purchase-confirmation-nov2023.pdf)
- [Treasury investment policy](/assets/documents/treasury-investment-policy-2022.pdf)
- [Selected 2025 institutional marketing email](/assets/documents/sovereign-bond-marketing-to-milligan-2025.pdf)

## How to cite these records

Name the agency, document title, document date, and physical PDF page. If you use a hosted excerpt, note that Arkansans for Pension Integrity applied privacy masks and link to the associated record page, which explains the excerpt boundary.

[Read the methodology](/methodology/) · [See the detailed findings](/findings/) · [Request a source locator](mailto:info@arpensions.org?subject=Source%20locator%20request)
