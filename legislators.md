---
layout: landing
title: "Policy Brief — Pension Investment Integrity Act"
description: "A concise legislative brief on issuer-neutral safeguards for covered Arkansas pension purchases of non-tradable sovereign debt."
permalink: /legislators/
audience_nav: true
breadcrumb: "For Legislators"
hero_band: pine
---

{% assign inv = site.data.investigation %}
{% assign treasury = inv.agencies | where: "id", "treasury" | first %}
{% assign apers = inv.agencies | where: "id", "apers" | first %}
{% assign atrs = inv.agencies | where: "id", "atrs" | first %}

## Executive summary

Arkansas pension boards need a clear, consistent process for covered purchases of non-tradable sovereign debt.

ATRS authorized {{ atrs.authorization_display | replace: 'Up to', 'up to' }} and later moved {{ atrs.measure_display }} into a manager account for an Israel Bonds strategy. APERS authorized a $25&ndash;$50 million range and later completed a {{ apers.measure_display }} purchase. Pension members are currently left to reconstruct the financial case from implementation advice, signed motions, operational correspondence, and transaction records.

The **Pension Investment Integrity Act** would create the missing public procedure. It is prospective, issuer-neutral, focused on covered pension purchases, and built around trustee authority.

Citizens First Congress selected pension investment integrity as a short-term priority for the 2027 legislative session on June 27, 2026.

## Key facts

<div class="issue-agency-table issue-agency-table--fact-detail" markdown="1">

| Fact | Current public account |
|---|---|
| **Completed purchases** | {{ inv.metrics.confirmed_security_floor.display }} total: {{ treasury.measure_display }} at Treasury and {{ apers.measure_display }} at APERS. |
| **ATRS manager funding** | {{ atrs.measure_display }} moved to the Reams account created for the strategy; ATRS members are waiting for security-level public reporting. |
| **Combined scale** | {{ inv.metrics.combined_tied_or_funded.display }} across completed purchases and manager funding—two different transaction types. |
| **Later Treasury payment** | {{ inv.metrics.treasury_conditional_payment.display }} shown at the bank-processing stage, separate from completed purchases. |
| **Pension authorization ceiling** | {{ inv.metrics.pension_authorization_ceiling.display }} combined: ATRS up to $50M and APERS up to $50M; later activity appears in the rows above. |
| **ATRS advice** | Aon compared implementation options, recommended Reams, and noted limited marketability. Trustees carried the investment decision. |
| **APERS decision memo** | The chief investment officer's February 2026 email reinforces the need for a standard written financial case. |
| **Treasury credit record** | An October 2024 internal overview recommended holding existing positions; a later {{ inv.transaction_figures.treasury_may_settled.display }} purchase settled in May 2025. |

</div>

## Why existing law needs a usable procedure

Arkansas law already requires pension trustees to act for members and beneficiaries and to evaluate investments on pecuniary factors—financial considerations expected to affect risk or return. The prudent-investor framework likewise requires care, skill, and attention to the portfolio as a whole.

Those standards state the duty. The Integrity Act would make the work behind a covered decision visible and consistent.

Non-tradable sovereign debt presents a specific governance challenge: the investment cannot be readily sold, so the fund gives up normal market liquidity and price discovery. A short written analysis is a reasonable safeguard before public retirement money is tied up until maturity.

## The Pension Investment Integrity Act

Before a covered acquisition, the proposal would require pension staff or an independent adviser to prepare:

1. **A written credit analysis** addressing repayment risk and material credit developments.
2. **An alternatives comparison** covering expected return, risk, and liquidity against reasonable fixed-income choices.
3. **A liquidity disclosure** explaining transfer restrictions and the absence of a secondary market.
4. **A fiduciary determination** connecting the decision to members' financial interests and the portfolio as a whole.
5. **Public posting after the purchase** within 30 days, with a written reason for any lawful redaction.

## Scope and design

The proposal would apply to covered acquisitions by Arkansas pension benefit plans, including ATRS, APERS, ASHERS, ASPRS, AJRS, and LOPFI.

The bill uses a focused design:

- **Covered plans:** Arkansas pension benefit plans, including ATRS, APERS, ASHERS, ASPRS, AJRS, and LOPFI.
- **Prospective rule:** future covered acquisitions follow the same procedure.
- **Issuer neutrality:** every covered sovereign issuer receives the same treatment.
- **Trustee authority:** pension boards keep the final investment decision.
- **Existing Treasury structure:** the separately governed State Treasury continues under its current framework.

## Why the Arkansas transactions make the case

**ATRS shows the division between implementation and investment judgment.** Aon helped choose the manager and structure the account. Trustees owned the merits decision. The Integrity Act would require their financial case to be written down.

**APERS shows why a decision memo matters.** The signed motion authorized a $25&ndash;$50 million range; the later purchase was {{ apers.measure_display }}. A concise memo would explain both the investment case and how the completed amount fit the authorization.

**Treasury shows the value of reconciling advice and action.** Treasury's internal overview recommended holding while maturities rolled off, followed months later by a new purchase. That sequence illustrates why public financial reasoning matters across government.

## Suggested questions for agencies

- What written analysis did the decision-maker rely on?
- Who prepared it, and what was that person's role?
- Which alternatives were compared on return, credit, and liquidity?
- How were transfer restrictions valued?
- Where can members read the final fiduciary determination?

## Legislative ask

Sponsor and support the Pension Investment Integrity Act in the 2027 regular session, and request an interim review by the Joint Committee on Public Retirement and Social Security Programs.

[Read the source documents &rarr;](/documents/)

[See the public explainer &rarr;](/evidence/)
[Contact Arkansans for Pension Integrity](mailto:info@arpensions.org)
