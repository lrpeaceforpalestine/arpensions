---
layout: evidence
title: "How $115 Million Moved Through Arkansas"
description: "The money, decisions, and public officials behind Arkansas's Israel Bonds strategy—and the safeguards pension members are demanding."
permalink: /evidence/
charts: true
apexcharts: true
evidence_toc: true
scrollytelling: true
timeline_thread: true
---

{% assign inv = site.data.investigation %}
{% assign treasury = inv.agencies | where: "id", "treasury" | first %}
{% assign apers = inv.agencies | where: "id", "apers" | first %}
{% assign atrs = inv.agencies | where: "id", "atrs" | first %}

<div class="evidence-page" markdown="1">

## The bottom line

Arkansas put **at least {{ inv.metrics.confirmed_security_floor.display }} into completed Israel Bonds purchases**: {{ treasury.measure_display }} at the State Treasury and {{ apers.measure_display }} at APERS. ATRS separately moved **{{ atrs.measure_display }} into a manager account** created for an Israel Bonds strategy.

Together, those decisions placed **{{ inv.metrics.combined_tied_or_funded.display }} of public money** into Israel Bonds purchases or the dedicated ATRS account: {{ inv.metrics.confirmed_security_floor.display }} in completed purchases plus {{ inv.metrics.atrs_manager_funding.display }} in manager funding.

Treasury also initiated another {{ inv.metrics.treasury_conditional_payment.display }} payment. The February 17 report marked that instruction "Processing By Bank," placing it in a separate next stage of the story.

<div class="callout" markdown="1">

**Why it matters:** Teachers, public employees, retirees, and taxpayers deserve to see how credit risk, expected return, liquidity, and available alternatives were weighed before public money was committed.

</div>

<section class="scrolly" aria-label="Four-part overview of the money involved">
  <div class="scrolly__graphic" aria-hidden="true">
    <div class="scrolly__viz" id="scrolly-viz">
      <div class="scrolly__viz-inner">
        <div class="viz-stat viz-stat--accent" id="scrolly-stat">{{ inv.metrics.confirmed_security_floor.display }}</div>
        <hr class="viz-separator" aria-hidden="true">
        <div class="viz-subtitle" id="scrolly-subtitle">completed purchases at Treasury and APERS</div>
      </div>
    </div>
  </div>
  <div class="scrolly__text">
    <div class="scrolly__step" data-step="0" data-stat="{{ inv.metrics.confirmed_security_floor.display }}" data-subtitle="completed purchases at Treasury and APERS" data-color-class="viz-stat--accent">
      <div class="step__content">
        <h3>{{ inv.metrics.confirmed_security_floor.display }} in completed purchases</h3>
        <p>The State Treasury accounts for {{ treasury.measure_display }} of that amount. APERS accounts for {{ apers.measure_display }}.</p>
      </div>
    </div>
    <div class="scrolly__step" data-step="1" data-stat="{{ atrs.measure_display }}" data-subtitle="moved into the ATRS manager account" data-color-class="viz-stat--accent">
      <div class="step__content">
        <h3>{{ atrs.measure_display }} in an ATRS manager account</h3>
        <p>ATRS hired Reams Asset Management to carry out the strategy and later funded the account. ATRS's public account of the money currently ends at the transfer to Reams.</p>
      </div>
    </div>
    <div class="scrolly__step" data-step="2" data-stat="{{ inv.metrics.combined_tied_or_funded.display }}" data-subtitle="across completed purchases and manager funding" data-color-class="viz-stat--accent">
      <div class="step__content">
        <h3>{{ inv.metrics.combined_tied_or_funded.display }} across two kinds of transactions</h3>
        <p>This is the campaign's scale figure: {{ inv.metrics.confirmed_security_floor.display }} in completed purchases plus {{ inv.metrics.atrs_manager_funding.display }} placed under Reams management.</p>
      </div>
    </div>
    <div class="scrolly__step" data-step="3" data-stat="{{ inv.metrics.treasury_conditional_payment.display }}" data-subtitle="Treasury payment still moving through the bank" data-color-class="viz-stat--danger">
      <div class="step__content">
        <h3>A later {{ inv.metrics.treasury_conditional_payment.display }} Treasury payment</h3>
        <p>The payment report placed this transaction at the bank-processing stage, alongside the separately documented completed purchases.</p>
      </div>
    </div>
  </div>
</section>

---

## Where the money went

The chart keeps completed purchases, manager-account funding, and a payment still in process visually distinct. Hover or focus the bars for an explanation.

<div class="chart-container" data-aos="fade-up" style="position: relative; max-width: 720px; height: 260px; margin-bottom: 1.25rem;">
  <canvas id="exposure-chart"
    data-treasury="{{ treasury.measure_millions }}"
    data-apers="{{ apers.measure_millions }}"
    data-atrs="{{ atrs.measure_millions }}"
    data-processing="{{ inv.metrics.treasury_conditional_payment.value_millions }}"
    aria-label="Bar chart showing 50 million dollars in completed Treasury purchases, 15 million dollars in a completed APERS purchase, 50 million dollars funded to the ATRS manager account, and a separate 10 million dollar Treasury payment still shown as processing"
    role="img"></canvas>
</div>

<div class="issue-agency-table issue-agency-table--fact-detail" markdown="1">

| Agency action | Amount | What it means |
|---|---:|---|
| State Treasury purchases | **{{ treasury.measure_display }}** | A security-level total derived from completed transaction records after a later maturity. |
| APERS purchase | **{{ apers.measure_display }}** | A completed two-year institutional bond purchase dated October 15, 2025. |
| ATRS manager account | **{{ atrs.measure_display }}** | Money transferred to Reams for the strategy; security-by-security public reporting remains due to ATRS members. |
| Later Treasury payment | **$10M** | The payment report showed the transaction still being processed by the bank. |

</div>

---

## What each agency did

### State Treasury

Treasury held Israel Bonds before the 2025 pension decisions. Its records support a {{ treasury.measure_display }} completed-purchase total after accounting for a February 2026 maturity. A separate {{ inv.transaction_figures.treasury_may_settled.display }} purchase settled in May 2025.

An internal Treasury credit overview had already summarized sovereign-rating downgrades and recommended holding the existing positions while maturities rolled off. Six months later, Treasury settled {{ inv.transaction_figures.treasury_may_settled.display }} in new positions. Arkansans deserve the written reasoning behind that change in course.

[Read the Treasury credit overview]({{ inv.sources.treasury_hold.record_url }}) and [Treasury transaction documents]({{ inv.sources.treasury_holdings.record_url }}).

### APERS

The APERS Investment Finance Subcommittee authorized a **$25&ndash;$50 million range** on May 15, 2025. APERS later bought **{{ apers.measure_display }}** on October 15&mdash;{{ inv.transaction_figures.apers_below_minimum_difference.display }} below the minimum named in the motion.

A February 2026 email from APERS's chief investment officer makes the transparency problem concrete. Members received a motion, operational correspondence, and a transaction record, leaving them to reconstruct the investment case.

[Read the signed APERS minutes]({{ inv.sources.apers_authorization.record_url }}), [the staff email]({{ inv.sources.apers_analysis_email.record_url }}), and [the purchase record]({{ inv.sources.apers_purchase.record_url }}).

### ATRS

ATRS authorized {{ atrs.authorization_display | replace: 'Up to', 'up to' }} on June 2, 2025, hired Reams Asset Management, and reported funding the Reams account with **{{ atrs.measure_display }}** in December.

Aon's two-page memo compared implementation options, recommended Reams, and warned that Israel Bonds have limited marketability. Aon owned the implementation work; trustees owned the investment decision.

ATRS members deserve the Board's sovereign-credit case, expected-return comparison, liquidity judgment, and explanation of how the strategy fit the wider portfolio.

[Read Aon's two-page memo]({{ inv.sources.atrs_aon.record_url }}), [the ATRS resolution]({{ inv.sources.atrs_resolution.record_url }}), and [the manager-funding notice]({{ inv.sources.atrs_funding.record_url }}).

---

## The case for a decision memo {#what-the-financial-record-shows}

The public trail includes a Treasury credit overview, Aon's implementation advice, manager comparisons, a warning about limited marketability, an S&amp;P downgrade report in ATRS files, authorization records, purchase records, and manager-funding records.

A decision memo would connect those pieces in one place: credit risk, expected return, liquidity, reasonable alternatives, and the reason each pension board chose to proceed.

That distinction matters because Israel Bonds cannot be sold on a secondary market. A pension fund that buys one generally holds it to maturity. When an investment cannot be readily sold, trustees should show how they priced that loss of flexibility and why the expected return justified it.

<div class="pull-quote">
  <p>Every covered sovereign-debt purchase should come with a public financial case.</p>
</div>

---

<div class="decision-window-section" data-aos="fade-up" markdown="1">

## How the decisions unfolded

<p class="decision-window-sub">This chart follows the April 2025 outreach through the agency decisions and the later purchases or manager funding.</p>

<div class="decision-window-container">
  <div id="decision-window-chart" aria-label="Interactive timeline showing the April 2025 outreach followed by a May Treasury purchase, the May 15 APERS authorization and October 15 purchase, and the June 2 ATRS authorization and December 29 manager funding" role="img"></div>
  <div id="decision-window-legend" class="decision-window-legend" aria-hidden="true"></div>
</div>

<p class="decision-window-note">Solid bars run from the April itinerary to each agency's decision. Lighter bars continue to the later purchase or manager-funding event. Hover over a bar for the dates.</p>

</div>

<div class="timeline-wrapper" aria-label="Timeline of Arkansas Israel Bonds decisions">

<div class="timeline-section">
<div class="timeline-year">2024</div>
<ol class="timeline" role="list" aria-label="2024 events">
  <li class="timeline-event timeline-event--highlight" data-aos="fade-left">
    <time>October 8, 2024</time>
    <h3>Treasury's internal overview recommends holding</h3>
    <p>The overview summarizes credit-rating pressure, recommends holding the existing positions, and calls for continued monitoring as scheduled maturities roll off.</p>
  </li>
</ol>
</div>

<div class="timeline-section">
<div class="timeline-year">2025</div>
<ol class="timeline" role="list" aria-label="2025 events">
  <li class="timeline-event" data-aos="fade-left">
    <time>April 14&ndash;15</time>
    <h3>Eight stops appear on a Capitol-area itinerary</h3>
    <p>The itinerary scheduled eight stops across pension, executive, legislative, Treasury, and cabinet offices. DFA records confirm the Hudson&ndash;Babbitt meeting, while seller correspondence recounts encounters with APERS and Treasury personnel.</p>
  </li>
  <li class="timeline-event timeline-event--highlight" data-aos="fade-left">
    <time>May 2025</time>
    <h3>Treasury adds {{ inv.transaction_figures.treasury_may_settled.display }}</h3>
    <p>Two Treasury positions settle and later appear on a June bondholder statement.</p>
  </li>
  <li class="timeline-event timeline-event--highlight" data-aos="fade-left">
    <time>May 15</time>
    <h3>APERS authorizes a $25&ndash;$50 million range</h3>
    <p>The Investment Finance Subcommittee adopts the motion recorded in its signed minutes.</p>
  </li>
  <li class="timeline-event timeline-event--highlight" data-aos="fade-left">
    <time>June 2</time>
    <h3>ATRS authorizes {{ atrs.authorization_display | replace: 'Up to', 'up to' }}</h3>
    <p>The Board adopts Resolution 2025-22. Its packet includes Aon's manager-selection and implementation memo.</p>
  </li>
  <li class="timeline-event timeline-event--highlight" data-aos="fade-left">
    <time>October 15</time>
    <h3>APERS buys {{ apers.measure_display }}</h3>
    <p>The transaction record identifies a two-year institutional bond.</p>
  </li>
  <li class="timeline-event timeline-event--highlight" data-aos="fade-left">
    <time>December 29</time>
    <h3>ATRS reports {{ atrs.measure_display }} in manager funding</h3>
    <p>A Board update reports that the Reams account created for the strategy has been funded.</p>
  </li>
</ol>
</div>

<div class="timeline-section">
<div class="timeline-year">2026</div>
<ol class="timeline" role="list" aria-label="2026 events">
  <li class="timeline-event" data-aos="fade-left">
    <time>February 2</time>
    <h3>A {{ inv.transaction_figures.treasury_february_maturity.display }} Treasury bond reaches maturity</h3>
    <p>The maturity reduces the Treasury total derived from its June 2025 statement to {{ treasury.measure_display }}.</p>
  </li>
  <li class="timeline-event" data-aos="fade-left">
    <time>February 17</time>
    <h3>Treasury instructs another {{ inv.metrics.treasury_conditional_payment.display }}</h3>
    <p>Treasury's outgoing-payment report marks the instruction "Processing By Bank."</p>
  </li>
  <li class="timeline-event timeline-event--highlight" data-aos="fade-left">
    <time>June 27</time>
    <h3>Pension investment integrity becomes a 2027 priority</h3>
    <p>Citizens First Congress selects the Pension Investment Integrity Act as one of its short-term legislative priorities.</p>
  </li>
</ol>
</div>

</div>

---

## Read the key documents

The document library publishes the records most useful for understanding the decisions: signed minutes, resolutions, financial memoranda, transaction records, and the ATRS manager-funding notice.

- [Aon manager-selection memo, ATRS packet pages 149&ndash;150]({{ inv.sources.atrs_aon.record_url }})
- [Executed ATRS Resolution 2025-22]({{ inv.sources.atrs_resolution.record_url }})
- [ATRS manager-funding notice]({{ inv.sources.atrs_funding.record_url }})
- [APERS signed authorization minutes]({{ inv.sources.apers_authorization.record_url }})
- [APERS {{ apers.measure_display }} purchase record]({{ inv.sources.apers_purchase.record_url }})
- [Treasury internal credit overview]({{ inv.sources.treasury_hold.record_url }})
- [Treasury bondholder statement]({{ inv.sources.treasury_holdings.record_url }})
- [Treasury payment report]({{ inv.sources.treasury_processing.record_url }})

[Browse all published documents &rarr;](/documents/)

---

## What the Integrity Act would do

The Pension Investment Integrity Act creates a public financial process while keeping every investment outcome with the pension board. Before a covered purchase of non-tradable sovereign debt, it would require:

1. A written credit analysis prepared by pension staff or an independent adviser.
2. A comparison of risk, expected return, and liquidity against reasonable fixed-income alternatives.
3. A plain-language explanation of transfer restrictions and the absence of a secondary market.
4. A written finding that the decision serves the financial interests of pension members.
5. Public posting of the analysis and finding within 30 days after the purchase.

[Read the legislative brief &rarr;](/legislators/) or [ask your legislator to support the Integrity Act &rarr;](/take-action/).

</div>
