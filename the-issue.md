---
layout: page
title: "The Issue — Public Money, Public Accountability"
description: "Arkansas directed $115 million into Israel Bonds purchases and an ATRS manager account. Pension members deserve the financial case behind those decisions."
permalink: /the-issue/
d3sankey: true
---

{% assign inv = site.data.investigation %}
{% assign treasury = inv.agencies | where: "id", "treasury" | first %}
{% assign apers = inv.agencies | where: "id", "apers" | first %}
{% assign atrs = inv.agencies | where: "id", "atrs" | first %}

<div class="issue-page" markdown="1">

<span class="section-label">The basic problem</span>

## Your retirement money should never run on trust alone

Arkansas agencies put **{{ inv.metrics.confirmed_security_floor.display }} into completed Israel Bonds purchases** and moved another **{{ inv.metrics.atrs_manager_funding.display }} into an ATRS manager account** created for the same strategy. That is {{ inv.metrics.combined_tied_or_funded.display }} across completed purchases and manager funding.

Pension members were left to piece together the financial case from motions, consultant pages, operational emails, and transaction records. A commitment this large should arrive with one usable written explanation of the credit risk, expected return, limited marketability, and reasonable alternatives.

That is the issue Arkansans for Pension Integrity is working to fix.

<div class="callout" markdown="1">

**Public money deserves a public investment record.** If a board believes an investment is financially sound, it should be able to show the analysis, the alternatives it considered, and the reason the decision serves pension members.

</div>

---

<span class="section-label">The investment</span>

## What makes Israel Bonds different?

Israel Bonds are sovereign debt issued by the State of Israel and sold directly through a specialized broker-dealer. The Arkansas investments at issue have no secondary market, so a pension plan generally holds them until maturity even when conditions change or a better opportunity appears.

That loss of flexibility makes credit, return, liquidity, and portfolio fit central to the decision.

A sound decision should answer four ordinary questions:

1. **Credit:** What could affect the issuer's ability to repay, and how was that risk priced?
2. **Return:** How does the expected return compare with other fixed-income choices available at the same time?
3. **Liquidity:** What does the plan give up by holding an investment that cannot be readily sold?
4. **Portfolio fit:** Why does this particular commitment serve the fund's overall strategy and the interests of its members?

A decision memo would answer all four questions in one place and connect them to each pension board's vote.

---

<span class="section-label">What Arkansas did</span>

## Three agencies, three different transactions

<div class="issue-agency-table issue-agency-table--fact-detail" markdown="1">

| Agency | Public money involved | What happened |
|---|---:|---|
| **State Treasury** | **{{ treasury.measure_display }}** | Completed purchases after accounting for a later maturity. Treasury operates outside the pension systems covered by the proposed Integrity Act. |
| **APERS** | **{{ apers.measure_display }} purchased** | Its Investment Finance Subcommittee authorized a $25&ndash;$50 million range; APERS later bought a two-year bond for {{ apers.measure_display }}. |
| **ATRS** | **{{ atrs.measure_display }} funded** | ATRS authorized {{ atrs.authorization_display | replace: 'Up to', 'up to' }}, hired Reams, and later moved {{ atrs.measure_display }} into the manager account. |

</div>

Treasury also initiated another **{{ inv.metrics.treasury_conditional_payment.display }} payment**. The February 17 bank report placed that instruction in a separate processing stage alongside the {{ inv.metrics.confirmed_security_floor.display }} in completed purchases.

Together, ATRS and APERS authorized **{{ inv.metrics.pension_authorization_ceiling.display }}**. The money that later moved was {{ apers.measure_display }} in an APERS purchase and {{ atrs.measure_display }} into the ATRS manager account.

---

<span class="section-label">The financial questions</span>

## What members were entitled to see

### Treasury: a hold recommendation, followed by another purchase

An internal Treasury overview dated October 8, 2024 summarized rating-agency downgrades and recommended holding the existing positions while scheduled maturities rolled off. Treasury settled a new {{ inv.transaction_figures.treasury_may_settled.display }} purchase in May 2025. The public trail jumps from a hold recommendation to a new purchase; Arkansans deserve the written reasoning that connected them.

### APERS: a $25&ndash;$50 million authorization and a $15 million purchase

APERS authorized a $25&ndash;$50 million range in May 2025 and later bought {{ apers.measure_display }}. A February 2026 email from its chief investment officer makes the transparency problem concrete and underscores the need for a standard written decision memo.

### ATRS: Aon chose the route; trustees chose the investment

Aon's June 2 memo compared managers, recommended Reams, and discussed the bonds' limited marketability. Its assignment centered on implementation and manager selection. Trustees retained responsibility for the sovereign-credit, return, liquidity, and portfolio case for the investment.

[Read the full, plain-language account and source documents &rarr;](/evidence/)

---

<div class="influence-flow-section" data-aos="fade-up" markdown="1">

<span class="section-label">The route through state government</span>

## How the proposal moved

Seller outreach, public-office coordination, board roles, and later agency actions appear across the same chain of events. The interactive map brings those connections together. Hover a line, or tap a node on a touch screen, to see the relationship.

<div class="influence-sankey-container">
  <div id="influence-sankey"></div>
</div>

<div class="sankey-legend" aria-hidden="true">
  <span class="sankey-legend-item"><span class="sankey-legend-dot" data-category="seller"></span>Seller</span>
  <span class="sankey-legend-item"><span class="sankey-legend-dot" data-category="office"></span>Public office</span>
  <span class="sankey-legend-item"><span class="sankey-legend-dot" data-category="route"></span>Outreach route</span>
  <span class="sankey-legend-item"><span class="sankey-legend-dot" data-category="agency"></span>Agency</span>
  <span class="sankey-legend-item"><span class="sankey-legend-dot" data-category="action"></span>Later action</span>
</div>

<details class="visual-fallback" markdown="1">
  <summary>Read the connections as a table</summary>

| From | To | What the documents show |
|---|---|---|
| Israel Bonds representatives | April 2025 itinerary | Seller representatives appear on the April 14&ndash;15 itinerary. |
| Auditor of State office | DFA and pension contacts | The office helped coordinate introductions and scheduling. |
| Auditor or proxy | APERS and ATRS | The Auditor held ex-officio board seats and used a proxy in board settings. |
| Jason Brady | APERS proposal | Brady presented the proposal and moved for the APERS authorization. |
| Agency decisions | Later transactions | Treasury and APERS completed purchases; ATRS later funded the Reams manager account. |
| ASHERS introduction | ASHERS | DFA opened the door to a seller presentation; ASHERS later reported zero holdings and zero purchases. |

</details>

<p class="influence-flow-note">The map traces the proposal through public offices, formal board roles, and later agency actions. Financial responsibility remained with each institution's decision-makers.</p>

</div>

---

<div class="issue-red-flags" markdown="1">

<span class="section-label">The standard</span>

## Arkansas law already puts pension members first

Arkansas pension trustees must act solely in the interest of members and beneficiaries. State law also requires investment evaluations to rest on pecuniary factors—factors expected to have a material effect on financial risk or return.

Those duties are the right starting point. The Integrity Act would turn them into a clear public procedure for covered sovereign-debt purchases.

The surrounding record makes transparency especially important:

**The investment was promoted through political channels.** Public officials celebrated Israel Bonds as an expression of support for Israel. The Auditor of State's office coordinated outreach, participated through board designees, and promoted the strategy publicly. That convergence makes a written financial case essential.

**The agencies took different paths.** APERS made a direct purchase. ATRS hired a manager. ASHERS received the seller's presentation and later reported zero holdings and zero purchases. The contrast shows the value of a common written process.

**The public trail is built from fragments.** ATRS shows how a manager was chosen. APERS shows the motion and later purchase. Treasury shows both a credit warning and later transactions. A decision memo would connect those fragments into a concise financial explanation.

</div>

<div class="issue-principle" markdown="1">

<span class="section-label">The solution</span>

## The Pension Investment Integrity Act

The Integrity Act would establish the same basic process for any covered purchase of non-tradable sovereign debt, regardless of issuer. It would require pension staff or an independent adviser to put the financial case in writing, compare reasonable alternatives, explain liquidity limits, and connect the decision to members' financial interests.

The proposal is designed around five protections:

- **Trustee authority:** pension boards keep the final investment decision.
- **Issuer neutrality:** the same rule applies to every covered sovereign issuer.
- **Prospective application:** the procedure governs future covered purchases.
- **Pension scope:** the bill covers Arkansas pension systems under a common standard.
- **Public accountability:** the financial analysis becomes public within 30 days after the purchase.

</div>

<div class="issue-demands" markdown="1">

## What we're asking for

1. **Pass the Pension Investment Integrity Act in 2027.** Require written credit, alternatives, liquidity, and fiduciary analysis for covered pension purchases.
2. **Use legislative oversight now.** Ask the Joint Committee on Public Retirement and Social Security Programs to examine how current procedures apply Arkansas's pecuniary-factors standard.
3. **Publish the work.** Pension boards can make decision-specific financial analysis public even before legislation requires it.

[Read the legislative brief &rarr;](/legislators/) or [take action &rarr;](/take-action/).

</div>

</div>
