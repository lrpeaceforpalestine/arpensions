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

ATRS authorized {{ atrs.authorization_display | replace: 'Up to', 'up to' }} and later moved {{ atrs.measure_display }} into a manager account for an Israel Bonds strategy. APERS authorized a $25&ndash;$50 million range and later completed a {{ apers.measure_display }} purchase. The available files show implementation advice, signed motions, operational correspondence, and later transactions. They do not give members one decision-specific written comparison of credit risk, expected return, liquidity, and reasonable alternatives for each board's choice.

The **Pension Investment Integrity Act** would fill that procedural gap. It is prospective, issuer-neutral, and limited to covered pension purchases. It would not direct a trustee vote or govern the separately managed State Treasury.

Citizens First Congress selected pension investment integrity as a short-term priority for the 2027 legislative session on June 27, 2026.

## Key facts

<div class="issue-agency-table issue-agency-table--fact-detail" markdown="1">

| Fact | Current public account |
|---|---|
| **Completed purchases** | {{ inv.metrics.confirmed_security_floor.display }} total: {{ treasury.measure_display }} at Treasury and {{ apers.measure_display }} at APERS. |
| **ATRS manager funding** | {{ atrs.measure_display }} moved to the Reams account created for the strategy. The released account documents do not list individual bonds. |
| **Combined scale** | {{ inv.metrics.combined_tied_or_funded.display }} across completed purchases and manager funding—two different transaction types. |
| **Later Treasury payment** | {{ inv.metrics.treasury_conditional_payment.display }} shown as still processing by the bank; excluded from the completed total. |
| **Pension authorization ceiling** | {{ inv.metrics.pension_authorization_ceiling.display }} combined: ATRS up to $50M and APERS up to $50M. A ceiling is not a holdings figure. |
| **ATRS advice** | Aon compared implementation options, recommended Reams, and noted limited marketability. Aon did not advise whether ATRS should invest or which bond to buy. |
| **APERS Board material** | The chief investment officer wrote that he prepared no Board material on the topic and believed the consultants had not either. |
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

## Scope and guardrails

The proposal would apply to covered acquisitions by Arkansas pension benefit plans, including ATRS, APERS, ASHERS, ASPRS, AJRS, and LOPFI.

It would not:

- prescribe an investment outcome;
- name or disfavor a particular issuer;
- substitute the legislature's judgment for a trustee vote;
- apply retroactively to past transactions; or
- extend to the separately governed State Treasury.

## Why the Arkansas transactions make the case

**ATRS shows an implementation-versus-merits gap.** Aon helped choose the manager and structure the account. Its own scope statement left the invest-or-not decision with trustees. The Integrity Act would require the trustees' financial case to be written down.

**APERS shows why a decision memo matters.** The signed motion authorized a $25&ndash;$50 million range; the later purchase was {{ apers.measure_display }}. A concise memo would explain both the investment case and how the completed amount fit the authorization.

**Treasury shows the value of reconciling advice and action.** Treasury's internal overview recommended holding while maturities rolled off, followed months later by a new purchase. Treasury sits outside the bill, but the sequence illustrates why public financial reasoning matters.

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
