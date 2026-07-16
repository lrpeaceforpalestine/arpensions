---
layout: evidence
title: "What the Public Record Shows"
description: "A plain-language account of Arkansas's Israel Bonds decisions, the money involved, and the safeguards the Pension Investment Integrity Act would add."
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

Together, those decisions placed **{{ inv.metrics.combined_tied_or_funded.display }} of public money** into completed purchases or the dedicated ATRS account. Those are different kinds of transactions, so the site keeps them separate wherever the figures appear.

Treasury also initiated another {{ inv.metrics.treasury_conditional_payment.display }} payment. The bank report still showed it being processed, so it is not included in the {{ inv.metrics.confirmed_security_floor.display }} completed-purchase total.

<div class="callout" markdown="1">

**Why it matters:** Teachers, public employees, retirees, and taxpayers should not have to take a major investment decision on faith. They should be able to see how credit risk, expected return, liquidity, and available alternatives were weighed before public money was committed.

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
        <p>ATRS hired Reams Asset Management to carry out the strategy and later reported funding the account. The released account documents do not list the individual bonds Reams bought or held.</p>
      </div>
    </div>
    <div class="scrolly__step" data-step="2" data-stat="{{ inv.metrics.combined_tied_or_funded.display }}" data-subtitle="across completed purchases and manager funding" data-color-class="viz-stat--accent">
      <div class="step__content">
        <h3>{{ inv.metrics.combined_tied_or_funded.display }} across two kinds of transactions</h3>
        <p>This combined figure is useful for understanding the scale of the decisions. It is not a claim that all {{ inv.metrics.combined_tied_or_funded.display }} appears as individual bonds on agency statements.</p>
      </div>
    </div>
    <div class="scrolly__step" data-step="3" data-stat="{{ inv.metrics.treasury_conditional_payment.display }}" data-subtitle="Treasury payment still moving through the bank" data-color-class="viz-stat--danger">
      <div class="step__content">
        <h3>A later {{ inv.metrics.treasury_conditional_payment.display }} Treasury payment</h3>
        <p>The payment report showed the bank still processing this transaction. It belongs in the story, but not in the completed-purchase total unless a completed settlement is documented.</p>
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
| ATRS manager account | **{{ atrs.measure_display }}** | Money funded to the Reams account for the strategy; the account records released by ATRS do not list its individual bonds. |
| Later Treasury payment | **$10M** | The payment report showed the transaction still being processed by the bank. |

</div>

---

## What each agency did

### State Treasury

Treasury held Israel Bonds before the 2025 pension decisions. Its records support a {{ treasury.measure_display }} completed-purchase total after accounting for a February 2026 maturity. A separate {{ inv.transaction_figures.treasury_may_settled.display }} purchase settled in May 2025.

An internal Treasury credit overview had already summarized sovereign-rating downgrades and recommended holding the existing positions while maturities rolled off. The later purchase records do not include a written explanation connecting the new purchase to that recommendation.

[Read the Treasury credit overview]({{ inv.sources.treasury_hold.record_url }}) and [Treasury transaction documents]({{ inv.sources.treasury_holdings.record_url }}).

### APERS

The APERS Investment Finance Subcommittee authorized a **$25&ndash;$50 million range** on May 15, 2025. APERS later bought **{{ apers.measure_display }}** on October 15&mdash;{{ inv.transaction_figures.apers_below_minimum_difference.display }} below the minimum named in the motion.

In response to the records request, APERS's chief investment officer wrote that he had not prepared material for the Board on the investment and believed its consultants had not prepared any either. That leaves a straightforward governance question: what written financial work supported the authorization and the later purchase?

[Read the signed APERS minutes]({{ inv.sources.apers_authorization.record_url }}), [the staff email]({{ inv.sources.apers_analysis_email.record_url }}), and [the purchase record]({{ inv.sources.apers_purchase.record_url }}).

### ATRS

ATRS authorized {{ atrs.authorization_display | replace: 'Up to', 'up to' }} on June 2, 2025, hired Reams Asset Management, and reported funding the Reams account with **{{ atrs.measure_display }}** in December.

Aon's two-page memo did real work: it compared implementation options, recommended Reams, and warned that Israel Bonds have limited marketability. Aon also drew a clear line around its role. It did not advise trustees whether ATRS should make the investment or which individual bond to buy.

The public can therefore see how ATRS chose a manager. The remaining question is how trustees weighed the sovereign-credit case, expected return, liquidity, and fit with the wider portfolio before approving the strategy.

[Read Aon's two-page memo]({{ inv.sources.atrs_aon.record_url }}), [the ATRS resolution]({{ inv.sources.atrs_resolution.record_url }}), and [the manager-funding notice]({{ inv.sources.atrs_funding.record_url }}).

---

## What the financial record shows

The documents are not silent. They include a Treasury credit overview, Aon's implementation advice, manager comparisons, a warning about limited marketability, an S&amp;P downgrade report in ATRS files, authorization records, purchase records, and manager-funding records.

What they do not provide in one place is the basic decision memo the public should expect: a written comparison of credit risk, expected return, liquidity, and reasonable alternatives tied to each pension board's decision to proceed.

That distinction matters because Israel Bonds cannot be sold on a secondary market. A pension fund that buys one generally holds it to maturity. When an investment cannot be readily sold, trustees should show how they priced that loss of flexibility and why the expected return justified it.

<div class="pull-quote">
  <p>The issue is not whether a board may ever buy a sovereign bond. The issue is whether Arkansans can see the financial case before retirement money is committed.</p>
</div>

---

<div class="decision-window-section" data-aos="fade-up" markdown="1">

## How the decisions unfolded

<p class="decision-window-sub">This chart places the April 2025 outreach, the agency decisions, and the later purchases or funding on one timeline. It shows sequence. The source documents should be read before drawing conclusions about why any official acted.</p>

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
    <p>The itinerary lists meetings or introductions across pension, executive, legislative, Treasury, and cabinet offices. Other records show that at least one meeting occurred and describe two additional encounters.</p>
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
    <h3>A later {{ inv.metrics.treasury_conditional_payment.display }} payment is still processing</h3>
    <p>Treasury's outgoing-payment report shows the instruction moving through the bank.</p>
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

The Pension Investment Integrity Act is a process bill. It would leave every investment outcome with the pension board. Before a covered purchase of non-tradable sovereign debt, it would require:

1. A written credit analysis prepared by pension staff or an independent adviser.
2. A comparison of risk, expected return, and liquidity against reasonable fixed-income alternatives.
3. A plain-language explanation of transfer restrictions and the absence of a secondary market.
4. A written finding that the decision serves the financial interests of pension members.
5. Public posting of the analysis and finding within 30 days after the purchase.

[Read the legislative brief &rarr;](/legislators/) or [ask your legislator to support the Integrity Act &rarr;](/take-action/).

</div>
