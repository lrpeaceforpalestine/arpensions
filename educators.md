---
layout: landing
title: "For Educators — The ATRS Investment Record"
description: "What Arkansas educators and retirees should know about the ATRS Reams mandate and the security-level records that remain unproduced."
permalink: /educators/
audience_nav: true
breadcrumb: "For Educators"
hero_band: pine
---

{% assign inv = site.data.investigation %}
{% assign atrs = inv.agencies | where: "id", "atrs" | first %}

## Your pension, your record

ATRS authorized **{{ atrs.authorization_display | replace: 'Up to', 'up to' }}** for an Israel Bonds-associated mandate in June 2025. A December Board update documents funding of **{{ atrs.measure_display }}** to Reams. The produced files do not identify the manager account's security-level purchases, holdings, settlement dates, or deployment pace.

That distinction matters: money transferred to an investment manager is not the same measure as securities shown in a holdings statement.

These records concern investment process and portfolio reporting. They do not show a change to earned-benefit formulas, payment schedules, or the legal obligation to pay benefits.

<div class="audience-fact-grid">
  <article><span class="evidence-status evidence-status--funded-mandate">{{ atrs.status }}</span><strong>{{ inv.metrics.atrs_manager_funding.display }}</strong><p>Transferred to the Reams mandate.</p></article>
  <article><span class="evidence-status evidence-status--unproduced">unproduced</span><strong>Holdings detail</strong><p>No security-level inventory was identified in the reviewed ATRS production.</p></article>
  <article><span class="evidence-status evidence-status--authorization">authorization</span><strong>{{ inv.metrics.pension_authorization_ceiling.display }}</strong><p>Combined ATRS and APERS ceiling; not a holdings total.</p></article>
</div>

## What ATRS's analytical file contains

Aon's two-page June 2 memorandum contains substantive implementation and manager-selection advice. Page 149 compares BlackRock and Reams, recommends Reams, and notes limited marketability. Page 150 says Aon is not recommending whether ATRS should invest or buy an individual security.

The production also contains an S&P downgrade report elsewhere. The files do not establish that trustees received or relied on it for Resolution 2025-22, and they do not identify a written analysis connecting sovereign-credit risk, liquidity, expected return, and portfolio fit to the affirmative authorization.

{% include citation.html source_id="atrs_aon" %}

{% include evidence-boundary.html
  established="ATRS authorized the mandate, Aon advised on implementation and manager selection, and ATRS funded the documented amount to Reams."
  unresolved="The produced record does not identify the mandate's underlying holdings or a merits analysis connected to the authorization."
  not_claimed="The record does not establish that every dollar funded was immediately invested in Israel Bonds or that trustees violated law."
%}

## What the Integrity Act would protect

{{ inv.legislation.full_summary }} The proposal would not tell ATRS what to buy or sell.

## What educators can do

1. **Read the primary pages.** Start with the [Aon memorandum](/documents/records/atrs-aon-memo/) and [ATRS funding record](/documents/records/atrs-manager-funding/).
2. **Ask your legislators to support the Integrity Act.** Use the [Arkansas Legislature's external District Finder](https://districtfinder.youraedi.com/) and the fund-specific letter below. The address you enter goes to that service; the campaign does not receive it.
3. **Follow ATRS meetings.** Check the [ATRS calendar](https://www.artrs.gov/calendar) and ask how manager funding, underlying holdings, credit risk, and liquidity are reported to trustees and members.

<div class="letter-template letter-template--compact" markdown="1">
<button class="copy-letter-btn" type="button" aria-label="Copy educator letter to clipboard">Copy</button>

Dear [Representative/Senator],

I am an Arkansas educator or ATRS member asking you to support the Pension Investment Integrity Act in the 2027 session. ATRS records document {{ inv.metrics.atrs_manager_funding.display }} funded to a manager mandate, while the produced files do not identify the mandate's underlying security holdings or a written sovereign-credit and portfolio-fit analysis tied to the authorization.

{{ inv.legislation.full_summary }} It would not direct trustees to buy or sell a particular investment.

Please support a public investment record for public retirement money.

Sincerely,

[Name, city]

</div>

[Take action](/take-action/) · [Read the full evidence](/evidence/) · [Email Arkansans for Pension Integrity](mailto:info@arpensions.org)
