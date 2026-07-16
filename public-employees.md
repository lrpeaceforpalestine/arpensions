---
layout: landing
title: "For Public Employees — The APERS Investment Record"
description: "What Arkansas public employees and retirees should know about the confirmed APERS purchase and the Board's stated authorization range."
permalink: /public-employees/
audience_nav: true
breadcrumb: "For Public Employees"
hero_band: pine
---

{% assign inv = site.data.investigation %}
{% assign apers = inv.agencies | where: "id", "apers" | first %}

## Your pension, your record

APERS's Investment Finance Subcommittee authorized a **{{ apers.authorization_display }}** range in May 2025. The reviewed transaction file documents a **{{ apers.measure_display }} purchase** on October 15, 2025.

The purchase is **{{ inv.transaction_figures.apers_below_minimum_difference.display }} below** the motion's stated minimum. The produced record does not resolve the operational or legal effect of that discrepancy, set an implementation deadline, or document an additional purchase through the record cutoff.

These records concern investment process and portfolio reporting. They do not show a change to earned-benefit formulas, payment schedules, or the legal obligation to pay benefits.

<div class="audience-fact-grid">
  <article><span class="evidence-status evidence-status--established">{{ apers.status }}</span><strong>{{ inv.metrics.confirmed_security_floor.display }}</strong><p>Statewide security floor, including APERS and Treasury.</p></article>
  <article><span class="evidence-status evidence-status--established">established</span><strong>{{ apers.measure }}</strong><p>Confirmed by the October 15 transaction record.</p></article>
  <article><span class="evidence-status evidence-status--authorization">authorization</span><strong>{{ apers.authorization_display }}</strong><p>The IFSC-authorized range is not the amount purchased.</p></article>
</div>

## What APERS's analytical file contains

The May 15 minutes document Jason Brady, acting as the Auditor's proxy on the APERS Board and Investment Finance Subcommittee, presenting the proposal and moving the authorization. Jim Hudson seconded it, and the motion carried without dissent.

In the reviewed authorization file, we identified no Callan sovereign-credit memorandum tied to the decision. APERS's chief investment officer later represented internally that he prepared nothing for the Board on the topic and believed the consultants had not either. That is a bounded finding about the selected written record, not proof that no oral discussion or unproduced work occurred.

{% include citation.html source_id="apers_authorization" %}
{% include citation.html source_id="apers_analysis_email" %}
{% include citation.html source_id="apers_purchase" %}

{% include evidence-boundary.html
  established="APERS approved the stated range and made the documented security purchase."
  unresolved="The effect of the below-minimum purchase and any later transaction outside the cutoff remain open."
  not_claimed="The site does not equate the authorization ceiling with holdings or infer a legal violation from the discrepancy alone."
%}

## What the Integrity Act would protect

{{ inv.legislation.full_summary }} It would leave the ultimate investment decision with APERS trustees.

## What public employees can do

1. **Read the primary pages.** Review the [signed authorization minutes](/documents/records/apers-authorization/) and [privacy-reviewed purchase record](/documents/records/apers-purchase/).
2. **Contact your legislators.** Use the external [District Finder](https://districtfinder.youraedi.com/) linked from the [Arkansas Legislature website](https://www.arkleg.state.ar.us/) and the fund-specific letter below. The address you enter goes to that service; the campaign does not receive it.
3. **Follow APERS meetings.** Use [apers.org](https://apers.org/) for current meeting information and ask for fund-specific holdings and analytical records.

<div class="letter-template letter-template--compact" markdown="1">
<button class="copy-letter-btn" type="button" aria-label="Copy public employee letter to clipboard">Copy</button>

Dear [Representative/Senator],

I am an Arkansas public employee or APERS member asking you to support the Pension Investment Integrity Act in the 2027 session. APERS records document a purchase of {{ apers.measure_display }} under a {{ apers.authorization_display }} authorization, while the reviewed authorization file contains no Callan sovereign-credit memorandum tied to the decision.

{{ inv.legislation.full_summary }} It is issuer-neutral and would not tell trustees what to buy or sell.

Please support a public investment record for public retirement money.

Sincerely,

[Name, city]

</div>

[Take action](/take-action/) · [Read the full evidence](/evidence/) · [Email Arkansans for Pension Integrity](mailto:info@arpensions.org)
