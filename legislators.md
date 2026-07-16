---
layout: landing
title: "The Pension Investment Integrity Act — 2027 Policy Brief"
description: "Issuer-neutral safeguards for credit analysis, alternatives comparison, liquidity disclosure, fiduciary findings, and public posting."
permalink: /legislators/
audience_nav: true
breadcrumb: "Integrity Act"
hero_band: pine
---

{% assign inv = site.data.investigation %}

## Executive summary

Arkansas records establish a **{{ inv.metrics.confirmed_security_floor.display }} security-level floor** across the State Treasury and APERS. Separately, ATRS documented **{{ inv.metrics.atrs_manager_funding.display }} in funding to a manager mandate** whose security-level holdings were not produced. A further Treasury payment of {{ inv.metrics.treasury_conditional_payment.display }} remained marked “Processing By Bank” and is conditional.

The files contain manager-selection, implementation, marketability, and credit-related materials. They leave material questions about how sovereign-credit risk and portfolio fit were evaluated and connected to each affirmative investment decision.

The Pension Investment Integrity Act answers that procedural problem without directing an investment result. Citizens First Congress selected the proposal as a short-term priority for the 2027 Arkansas legislative session.

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

## The record before legislators

<div class="table-scroll" tabindex="0" role="region" aria-label="Arkansas investment measures and status">

| Institution or measure | Current record | Evidentiary status |
|---|---|---|
| State Treasury | {{ inv.agencies[0].measure }} | {{ inv.agencies[0].status }} |
| APERS | {{ inv.agencies[1].measure }} under {{ inv.agencies[1].authorization }} | {{ inv.agencies[1].status }} |
| ATRS | {{ inv.agencies[2].measure }}; underlying holdings not identified | {{ inv.agencies[2].status }} |
| Additional Treasury payment | {{ inv.metrics.treasury_conditional_payment.display }} at processing stage | {{ inv.metrics.treasury_conditional_payment.status }} |
| Pension authorization ceiling | {{ inv.metrics.pension_authorization_ceiling.display }} | Authorization, not holdings |

</div>

## What the Act does not do

- It does not order a pension system to buy, hold, or sell a security.
- It does not apply a political loyalty test.
- It does not convert an authorization ceiling or manager funding into a holdings number.
- It does not replace trustees, staff, or independent advisers.
- It does not reach the separately governed State Treasury; Treasury records provide context for the public-investment problem.

## Legislative ask

1. Sponsor and enact the Pension Investment Integrity Act in the 2027 regular session.
2. Hold an interim briefing on the existing analytical and transaction record.
3. Require the final bill and fiscal analysis to preserve the five issuer-neutral safeguards.

For a briefing or source package, contact **Arkansans for Pension Integrity** at [info@arpensions.org](mailto:info@arpensions.org?subject=Pension%20Investment%20Integrity%20Act%20briefing).

---

[Review the evidence](/evidence/) · [Browse selected primary records](/documents/) · [Download current facts from the press page](/press/)
