---
layout: landing
title: "Press Kit — Arkansas Pension Investment Integrity"
description: "Current facts, dates, terminology, source documents, and contact information for reporting on Arkansas's Israel Bonds decisions."
permalink: /press/
audience_nav: true
breadcrumb: "For Media"
hero_band: pine
---

{% assign inv = site.data.investigation %}
{% assign treasury = inv.agencies | where: "id", "treasury" | first %}
{% assign apers = inv.agencies | where: "id", "apers" | first %}
{% assign atrs = inv.agencies | where: "id", "atrs" | first %}

## Campaign summary

Arkansans for Pension Integrity is a statewide campaign for transparent, financially sound stewardship of public retirement money. The campaign is advancing the **Pension Investment Integrity Act**, an issuer-neutral proposal that would require written credit, alternatives, liquidity, and fiduciary analysis for covered pension purchases of non-tradable sovereign debt.

The campaign can be reached at [info@arpensions.org](mailto:info@arpensions.org).

## Copy-ready overview

> Arkansas agencies put at least {{ inv.metrics.confirmed_security_floor.display }} into completed Israel Bonds purchases: {{ treasury.measure_display }} at the State Treasury and {{ apers.measure_display }} at APERS. ATRS separately moved {{ atrs.measure_display }} into a manager account created for the same strategy. Arkansans for Pension Integrity is asking the General Assembly to require a written, issuer-neutral financial analysis for future covered pension purchases of non-tradable sovereign debt. Citizens First Congress selected pension investment integrity as a short-term priority for the 2027 session.

## Figures to use

<div class="issue-agency-table issue-agency-table--fact-detail" markdown="1">

| Figure | Meaning |
|---:|---|
| **{{ inv.metrics.confirmed_security_floor.display }}** | Completed security purchases: {{ treasury.measure_display }} at Treasury plus {{ apers.measure_display }} at APERS. |
| **{{ atrs.measure_display }}** | Money funded to the ATRS Reams manager account for the strategy. This is manager funding, not a published list of individual holdings. |
| **{{ inv.metrics.combined_tied_or_funded.display }}** | Completed purchases plus ATRS manager funding. Use only with both transaction types stated. |
| **{{ inv.metrics.treasury_conditional_payment.display }}** | A later Treasury payment shown as still processing by the bank. It is not included in the completed total. |
| **{{ inv.metrics.pension_authorization_ceiling.display }}** | Combined pension authorization ceiling: ATRS up to $50M and APERS up to $50M. It is not a purchase or holdings total. |

</div>

## Agency-by-agency

### Arkansas State Treasury

- Treasury records support **{{ treasury.measure_display }} in completed purchases** after accounting for a {{ inv.transaction_figures.treasury_february_maturity.display }} maturity in February 2026.
- A **{{ inv.transaction_figures.treasury_may_settled.display }} purchase** settled in May 2025.
- An internal overview dated October 8, 2024 summarized rating downgrades and recommended holding existing positions while maturities rolled off.
- A later **{{ inv.metrics.treasury_conditional_payment.display }} payment** remained marked as processing by the bank.

### APERS

- The Investment Finance Subcommittee authorized a **$25&ndash;$50 million range** on May 15, 2025.
- APERS completed a **{{ apers.measure_display }} two-year bond purchase** on October 15, 2025.
- The purchase was **{{ inv.transaction_figures.apers_below_minimum_difference.display }} below the motion's stated minimum**.
- APERS's chief investment officer wrote that he prepared no Board material on the topic and believed the consultants had not either.

### ATRS

- ATRS authorized **{{ atrs.authorization_display | replace: 'Up to', 'up to' }}** through Resolution 2025-22 on June 2, 2025.
- Aon compared implementation options, recommended Reams, and noted limited marketability.
- Aon separately stated that it was not advising whether ATRS should invest or which bond to buy.
- ATRS reported **{{ atrs.measure_display }} funded to the Reams account** on December 29, 2025.
- The account records released by ATRS do not list individual security purchases or holdings.

## Short timeline

<div class="press-timeline" role="list" aria-label="Key dates">
  <div class="press-timeline-item" role="listitem"><time datetime="2024-10-08">Oct. 8, 2024</time><p>Treasury internal overview recommends holding existing positions and continued monitoring.</p></div>
  <div class="press-timeline-item" role="listitem"><time datetime="2025-04-14">Apr. 14&ndash;15, 2025</time><p>An eight-stop itinerary lists outreach across pension, executive, legislative, Treasury, and cabinet offices or settings.</p></div>
  <div class="press-timeline-item" role="listitem"><time datetime="2025-05">May 2025</time><p>{{ inv.transaction_figures.treasury_may_settled.display }} in Treasury positions settles.</p></div>
  <div class="press-timeline-item" role="listitem"><time datetime="2025-05-15">May 15, 2025</time><p>APERS authorizes a $25&ndash;$50 million range.</p></div>
  <div class="press-timeline-item" role="listitem"><time datetime="2025-06-02">June 2, 2025</time><p>ATRS authorizes {{ atrs.authorization_display | replace: 'Up to', 'up to' }} and receives Aon's implementation memo.</p></div>
  <div class="press-timeline-item" role="listitem"><time datetime="2025-10-15">Oct. 15, 2025</time><p>APERS completes its {{ apers.measure_display }} purchase.</p></div>
  <div class="press-timeline-item" role="listitem"><time datetime="2025-12-29">Dec. 29, 2025</time><p>ATRS reports {{ atrs.measure_display }} funded to the Reams account.</p></div>
  <div class="press-timeline-item" role="listitem"><time datetime="2026-06-27">June 27, 2026</time><p>Citizens First Congress selects pension investment integrity as a 2027 short-term priority.</p></div>
</div>

## Terminology

**Completed purchase:** A transaction supported by a completed security or cash-flow record.

**Manager funding:** Money moved into an investment manager's account. It does not, by itself, identify every security held in that account.

**Authorization ceiling:** The maximum amount a board allowed. It is not proof that the full amount was spent.

**Non-tradable sovereign debt:** Debt issued by a national government that does not trade on a secondary market and is generally held to maturity.

**Pension Investment Integrity Act:** A prospective, issuer-neutral proposal for covered pension acquisitions. It leaves investment outcomes with trustees and requires them to publish the financial work behind the decision.

## Primary documents

- [Aon implementation and manager-selection memo, ATRS packet pages 149&ndash;150]({{ inv.sources.atrs_aon.record_url }})
- [Executed ATRS Resolution 2025-22]({{ inv.sources.atrs_resolution.record_url }})
- [ATRS manager-funding notice]({{ inv.sources.atrs_funding.record_url }})
- [APERS signed authorization minutes]({{ inv.sources.apers_authorization.record_url }})
- [APERS chief investment officer email]({{ inv.sources.apers_analysis_email.record_url }})
- [APERS {{ apers.measure_display }} purchase record]({{ inv.sources.apers_purchase.record_url }})
- [Treasury internal credit overview]({{ inv.sources.treasury_hold.record_url }})
- [Treasury bondholder statement]({{ inv.sources.treasury_holdings.record_url }})
- [Treasury maturity record]({{ inv.sources.treasury_maturity.record_url }})
- [Treasury payment report]({{ inv.sources.treasury_processing.record_url }})

## Media contact

**Arkansans for Pension Integrity**<br>
[info@arpensions.org](mailto:info@arpensions.org)
[arpensions.org](https://arpensions.org/)
