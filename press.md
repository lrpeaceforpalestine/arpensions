---
layout: landing
title: "Press — Current Facts and Primary Records"
description: "Copy-ready facts, terminology, evidence cutoffs, and primary records for reporting on Arkansas public investment decisions and the Pension Investment Integrity Act."
permalink: /press/
audience_nav: true
breadcrumb: "Press"
hero_band: pine
mobile_cta_label: "Media inquiry"
mobile_cta_url: "mailto:info@arpensions.org?subject=Media%20inquiry"
---

{% assign inv = site.data.investigation %}
{% assign terms = site.data.terminology %}
{% assign treasury = inv.agencies | where: "id", "treasury" | first %}
{% assign apers = inv.agencies | where: "id", "apers" | first %}

## Campaign summary

**Arkansans for Pension Integrity** is an Arkansas public-records and legislative campaign advancing issuer-neutral safeguards for public pension investment decisions. The campaign's principle is simple: **public money deserves a public investment record.**

The campaign supports the Pension Investment Integrity Act for the 2027 Arkansas legislative session. {{ inv.legislation.cfc_status }} {{ inv.legislation.full_summary }} It would not direct a board to buy, hold, or sell a security. The proposal is at the **{{ inv.legislation.stage | downcase }}** stage; no bill number has been assigned.

## Copy-ready current facts

- **{{ inv.metrics.confirmed_security_floor.display }} is the confirmed security-level floor.** It combines a {{ treasury.measure }} and an {{ apers.measure }}. [Treasury statement](/documents/records/treasury-holdings/) · [maturity](/documents/records/treasury-maturity/) · [APERS purchase](/documents/records/apers-purchase/)
- **{{ inv.metrics.atrs_manager_funding.display }} is ATRS manager funding.** ATRS documented that amount funded to the Reams mandate; the reviewed files do not identify the mandate's security-level holdings. [Funding record](/documents/records/atrs-manager-funding/)
- **{{ inv.metrics.combined_tied_or_funded.display }} combines different measures.** It means {{ inv.metrics.confirmed_security_floor.display }} in confirmed securities plus {{ inv.metrics.atrs_manager_funding.display }} in manager funding. It is not a holdings total. [Evidence ledger](/evidence/)
- **The additional Treasury {{ inv.metrics.treasury_conditional_payment.display }} is conditional.** The payment report was marked “Processing By Bank”; the production does not document settlement or resulting ownership. [Payment-stage record](/documents/records/treasury-processing-payment/)
- **{{ inv.metrics.pension_authorization_ceiling.display }} is an authorization ceiling.** It combines ATRS's and APERS's maximum authorizations and is not a purchased or held amount. [ATRS resolution](/documents/records/atrs-resolution/) · [APERS minutes](/documents/records/apers-authorization/)

{% include exposure-chart.html %}

## Agency status

{% include agency-status.html %}

## The analytical record

{{ inv.analysis_record.lead }}

At ATRS, Aon's June 2, 2025 memorandum is substantive on implementation and manager selection. Page 149 recommends Reams and notes limited marketability. Page 150 says Aon is not recommending whether ATRS should invest or purchase an individual security.

At APERS, the reviewed authorization file contains no Callan sovereign-credit memorandum tied to the decision. At Treasury, an internal October 2024 overview recommends holding existing positions and continuing surveillance; the settled May 2025 purchase is not accompanied by an identified written reconciliation with that recommendation.

## Evidence terms

**Instrument:** {{ terms.instrument_name }}, issued by {{ terms.issuer_formal }} and offered in the United States through {{ terms.broker_dealer }}. The site's formal asset-class phrase is **{{ terms.instrument_formal }}**; its plain-language phrase is **{{ terms.instrument_accessible }}**. “Limited marketability” describes the practical liquidity constraint without implying an ordinary secondary market.

| Label | Meaning in this project |
|---|---|
{% for status in inv.status_labels %}| **{{ status[0] | replace: '_', ' ' }}** | {{ status[1] }} |
{% endfor %}

## Dates and scope

- **Transaction-record cutoff:** {{ inv.record_cutoff | date: "%B %-d, %Y" }}
- **PDF render gate completed:** {{ inv.review_completed | date: "%B %-d, %Y" }}
- **Render-gate scope:** {{ inv.corpus.raw_files_display }} raw files and {{ inv.corpus.pdf_pages_display }} PDF pages; {{ inv.corpus.render_jobs_complete }} of {{ inv.corpus.render_jobs_total }} render jobs complete
- **Hosted documents:** selected, privacy-reviewed anchor records supporting the site's principal findings; not a complete production mirror
- **Bill prefiling opens:** {{ inv.legislation.prefiling_opens_display }}
- **Regular session convenes:** {{ inv.legislation.session_convenes_display }}
- **Ordinary retirement-legislation filing deadline:** {{ inv.legislation.retirement_filing_deadline_display }} ([official calendar]({{ inv.legislation.important_dates_url }}))

## Primary links

- [Aon memorandum, ATRS packet pages 149–150](/documents/records/atrs-aon-memo/)
- [ATRS manager-funding record](/documents/records/atrs-manager-funding/)
- [APERS signed authorization minutes](/documents/records/apers-authorization/)
- [APERS analytical-record search email](/documents/records/apers-analysis-email/)
- [APERS confirmed purchase record](/documents/records/apers-purchase/)
- [Treasury internal credit overview](/documents/records/treasury-hold-overview/)
- [Treasury settled-position record](/documents/records/treasury-holdings/)
- [Treasury final-maturity record](/documents/records/treasury-maturity/)
- [Treasury processing-stage payment](/documents/records/treasury-processing-payment/)
- [Act 498 of 2023]({{ inv.legislation.act_498_url }})

## Attribution and boundaries

The Auditor of State is an ex-officio ATRS trustee, and records identify Chief Deputy Auditor Jason Brady as a designee or proxy in ATRS and APERS proceedings. The Auditor's office also appears in scheduling, correspondence, presentation, and promotional records. The Auditor does not manage ATRS or APERS assets and is not their investment staff.

The April 2025 itinerary contains eight scheduled stops across pension, legislative, Treasury, and cabinet offices. The Hudson–Babbitt meeting is independently confirmed; Fecher and Treasury-team encounters are participant- or seller-reported; and the scheduled White encounter remains unconfirmed. Sequence and access do not establish decision causation.

ASHERS records document a pitch through DFA and no identified reply, authorization, or holding. They do not establish an affirmative decline or explain the different outcome.

## Downloads and brand assets

- [Pension Investment Integrity Act one-page brief, dated PDF]({{ inv.legislation.brief_pdf_url }})
- [Printable HTML version of the brief](/legislators/one-page/)
- [Current facts as CSV](/assets/data/current-facts.csv)
- [Campaign logo, SVG](/assets/images/api-badge.svg)
- [Campaign logo, 512-pixel PNG](/assets/images/api-badge-512.png)
- [Current social-preview image](/assets/images/og-default.png)

## Organization boilerplate

**Arkansans for Pension Integrity** is an Arkansas public-records and legislative campaign advancing documented, issuer-neutral safeguards for public pension decisions. Its research separates authorizations, manager funding, processing-stage payments, settled transactions, and holdings, and publishes selected privacy-reviewed primary records with exact locators. Its principle is: **Public money deserves a public investment record.**

## Media contact

**Arkansans for Pension Integrity**<br>
[info@arpensions.org](mailto:info@arpensions.org?subject=Media%20inquiry)<br>
[arpensions.org](https://arpensions.org)

Please include a deadline, outlet, and the records or claim you want to verify. The organization can provide source locators and privacy-reviewed excerpts.
