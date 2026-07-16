---
layout: landing
title: "Press — Current Facts and Primary Records"
description: "Copy-ready facts, terminology, evidence cutoffs, and primary records for reporting on Arkansas public investment decisions and the Pension Investment Integrity Act."
permalink: /press/
audience_nav: true
breadcrumb: "Press"
hero_band: pine
---

{% assign inv = site.data.investigation %}

## Campaign summary

**Arkansans for Pension Integrity** is an Arkansas public-records and legislative campaign advancing issuer-neutral safeguards for public pension investment decisions. The campaign's principle is simple: **public money deserves a public investment record.**

The campaign supports the Pension Investment Integrity Act for the 2027 Arkansas legislative session. Citizens First Congress selected the proposal as a short-term priority. The Act would require written credit analysis, comparison with alternatives, liquidity disclosure, a fiduciary determination based on material financial risk and return, and public posting before covered pension acquisitions. It would not direct a board to buy, hold, or sell a security.

## Copy-ready current facts

- **{{ inv.metrics.confirmed_security_floor.display }} is the confirmed security-level floor.** It combines a {{ inv.agencies[0].measure }} and an {{ inv.agencies[1].measure }}.
- **{{ inv.metrics.atrs_manager_funding.display }} is ATRS manager funding.** ATRS documented that amount funded to the Reams mandate; the reviewed files do not identify the mandate's security-level holdings.
- **{{ inv.metrics.combined_tied_or_funded.display }} combines different measures.** It means {{ inv.metrics.confirmed_security_floor.display }} in confirmed securities plus {{ inv.metrics.atrs_manager_funding.display }} in manager funding. It is not a holdings total.
- **The additional Treasury {{ inv.metrics.treasury_conditional_payment.display }} is conditional.** The payment report was marked “Processing By Bank”; the production does not document settlement or resulting ownership.
- **{{ inv.metrics.pension_authorization_ceiling.display }} is an authorization ceiling.** It combines ATRS's and APERS's maximum authorizations and is not a purchased or held amount.

{% include exposure-chart.html %}

## Agency status

{% include agency-status.html %}

## The analytical record

{{ inv.analysis_record.lead }}

At ATRS, Aon's June 2, 2025 memorandum is substantive on implementation and manager selection. Page 149 recommends Reams and notes limited marketability. Page 150 says Aon is not recommending whether ATRS should invest or purchase an individual security.

At APERS, the reviewed authorization file contains no Callan sovereign-credit memorandum tied to the decision. At Treasury, an internal October 2024 overview recommends holding existing positions and continuing surveillance; the settled May 2025 purchase is not accompanied by an identified written reconciliation with that recommendation.

## Evidence terms

| Label | Meaning in this project |
|---|---|
{% for status in inv.status_labels %}| **{{ status[0] | replace: '_', ' ' }}** | {{ status[1] }} |
{% endfor %}

## Dates and scope

- **Transaction-record cutoff:** {{ inv.record_cutoff | date: "%B %-d, %Y" }}
- **Render-aware research review completed:** {{ inv.review_completed | date: "%B %-d, %Y" }}
- **Reviewed corpus:** {{ inv.corpus.raw_files_display }} raw files and {{ inv.corpus.pdf_pages_display }} PDF pages; {{ inv.corpus.render_jobs_complete }} of {{ inv.corpus.render_jobs_total }} render jobs complete
- **Hosted documents:** selected, privacy-reviewed anchor records supporting the site's principal findings; not a complete production mirror

## Primary links

- [Aon memorandum, ATRS packet pages 149–150](/documents/records/atrs-aon-memo/)
- [ATRS manager-funding record](/documents/records/atrs-manager-funding/)
- [APERS signed authorization minutes](/documents/records/apers-authorization/)
- [APERS confirmed purchase record](/documents/records/apers-purchase/)
- [Treasury internal credit overview](/documents/records/treasury-hold-overview/)
- [Treasury settled-position record](/documents/records/treasury-holdings/)
- [Treasury processing-stage payment](/documents/records/treasury-processing-payment/)
- [Act 498 of 2023]({{ inv.legislation.act_498_url }})

## Attribution and boundaries

The Auditor of State is an ex-officio ATRS trustee, and records identify Chief Deputy Auditor Jason Brady as a designee or proxy in ATRS and APERS proceedings. The Auditor's office also appears in scheduling, correspondence, presentation, and promotional records. The Auditor does not manage ATRS or APERS assets and is not their investment staff.

The April 2025 itinerary contains eight scheduled stops across distinct venues. The Hudson–Babbitt meeting is independently confirmed; Fecher and Treasury-team encounters are participant- or seller-reported; and the scheduled White encounter remains unconfirmed. Sequence and access do not establish decision causation.

ASHERS records document a pitch through DFA and no identified reply, authorization, or holding. They do not establish an affirmative decline or explain the different outcome.

## Media contact

**Arkansans for Pension Integrity**<br>
[info@arpensions.org](mailto:info@arpensions.org?subject=Media%20inquiry)<br>
[arpensions.org](https://arpensions.org)

Please include a deadline, outlet, and the records or claim you want to verify. The organization can provide source locators and privacy-reviewed excerpts.
