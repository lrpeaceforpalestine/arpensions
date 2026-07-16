---
layout: landing
title: "The Pension Investment Integrity Act — 2027 Policy Brief"
description: "Issuer-neutral safeguards for credit analysis, alternatives comparison, liquidity disclosure, fiduciary findings, and public posting."
permalink: /legislators/
audience_nav: true
breadcrumb: "Integrity Act"
hero_band: pine
mobile_cta_label: "Request a briefing"
mobile_cta_url: "mailto:info@arpensions.org?subject=Pension%20Investment%20Integrity%20Act%20briefing"
---

{% assign inv = site.data.investigation %}
{% assign treasury = inv.agencies | where: "id", "treasury" | first %}
{% assign apers = inv.agencies | where: "id", "apers" | first %}
{% assign atrs = inv.agencies | where: "id", "atrs" | first %}

## Executive summary

Arkansas records establish a **{{ inv.metrics.confirmed_security_floor.display }} security-level floor** across the State Treasury and APERS. Separately, ATRS documented **{{ inv.metrics.atrs_manager_funding.display }} in funding to a manager mandate** whose security-level holdings were not produced. A further Treasury payment of {{ inv.metrics.treasury_conditional_payment.display }} remained marked “Processing By Bank” and is conditional.

The files contain manager-selection, implementation, marketability, and credit-related materials. They leave material questions about how sovereign-credit risk and portfolio fit were evaluated and connected to each affirmative investment decision.

The Pension Investment Integrity Act answers that procedural problem without directing an investment result. {{ inv.legislation.cfc_status }}

## Proposal status

<div class="proposal-status-grid">
  <div><span>Campaign stage</span><strong>{{ inv.legislation.stage }}</strong></div>
  <div><span>Bill number</span><strong>{{ inv.legislation.bill_number }}</strong></div>
  <div><span>Sponsor status</span><strong>{{ inv.legislation.sponsor_status }}</strong></div>
  <div><span>Coalition status</span><strong>{{ inv.legislation.cfc_status_short }}</strong></div>
</div>

Status verified {{ inv.legislation.status_verified | date: "%B %-d, %Y" }}. The policy core is public here; legislative language, fiscal review, and a bill number will be linked when available. [Open the printable one-page brief](/legislators/one-page/) or [download the dated PDF]({{ inv.legislation.brief_pdf_url }}). The coalition-selection status is attributed to the campaign's convention record; Citizens First Congress describes the delegate process that creates its priority platform on its [official process page]({{ inv.legislation.cfc_process_url }}).

{% include legislative-window.html %}

{% include evidence-ledger.html %}

## What Arkansas law already provides

[Act 498 of 2023]({{ inv.legislation.act_498_url }}) requires covered pension fiduciaries to evaluate investments based on pecuniary factors—material financial effects on risk and return. The proposed Act gives that principle a consistent written procedure for acquisitions of non-tradable sovereign debt.

This proposal does not declare that an agency violated Act 498. It makes the future record clear enough for trustees, beneficiaries, and legislators to assess compliance without reconstructing it through FOIA.

## The five safeguards

<ol class="policy-steps">
{% for provision in inv.legislation.provisions %}
  <li><span>{{ forloop.index }}</span><p>{{ provision }}</p></li>
{% endfor %}
</ol>

The safeguards are **issuer-neutral**. They apply to the asset characteristics and the public fiduciary process, not to a particular country, seller, political position, or desired vote.

{{ inv.legislation.full_summary }}

### Publication without pre-trade disclosure

{{ inv.legislation.publication_boundary }} The intended public record would retain:

{% for field in inv.legislation.publication_public_fields %}
- {{ field }}.
{% endfor %}

## The record before legislators

<div class="table-scroll" tabindex="0" role="region" aria-label="Arkansas investment measures and status">

| Institution or measure | Current record | Evidentiary status |
|---|---|---|
| State Treasury | {{ treasury.measure }} | {{ treasury.status }} |
| APERS | {{ apers.measure }} under {{ apers.authorization }} | {{ apers.status }} |
| ATRS | {{ atrs.measure }}; underlying holdings not identified | {{ atrs.status }} |
| Additional Treasury payment | {{ inv.metrics.treasury_conditional_payment.display }} at processing stage | {{ inv.metrics.treasury_conditional_payment.status }} |
| Pension authorization ceiling | {{ inv.metrics.pension_authorization_ceiling.display }} | Authorization, not holdings |

</div>

## What the Act does not do

- It does not order a pension system to buy, hold, or sell a security.
- It does not apply a political loyalty test.
- It does not convert an authorization ceiling or manager funding into a holdings number.
- It does not replace trustees, staff, or independent advisers.
- It does not reach the separately governed State Treasury; Treasury records provide context for the public-investment problem.

## What legislative drafting must settle

The prefiling process must translate the policy core into administrable bill text. Drafting should make these points explicit without weakening the five safeguards:

- the covered-plan and covered-transaction definitions;
- any materiality threshold and narrowly stated operational exceptions;
- who receives, posts, and retains the required record;
- the covered-acquisition event that starts the 30-day publication clock and the treatment of staged transactions;
- narrow redaction standards that protect legally confidential operational details without hiding the required conclusions;
- the implementation date and treatment of transactions already in progress; and
- the fiscal and administrative note for affected systems.

For staff review, the campaign can provide exact source locators, the proposed process map, and a fund-by-fund evidence briefing. It will not ask a sponsor to rely on an authorization ceiling as if it were a holdings number.

## Legislative ask

1. **Potential sponsor:** request a bill-drafting meeting and carry the proposal in the 2027 regular session.
2. **Committee or caucus staff:** request a source briefing on the analytical and transaction record.
3. **All legislators:** preserve the five issuer-neutral safeguards through bill drafting and fiscal review.

For a briefing or source package, contact **Arkansans for Pension Integrity** at [info@arpensions.org](mailto:info@arpensions.org?subject=Pension%20Investment%20Integrity%20Act%20briefing).

---

[Review the evidence](/evidence/) · [Browse selected primary records](/documents/) · [Download the one-page PDF]({{ inv.legislation.brief_pdf_url }}) · [Download current facts](/assets/data/current-facts.csv)
