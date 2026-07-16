---
layout: page
title: "What ATRS's $50 Million Funding Means"
description: "ATRS funded a manager account for the Israel Bonds strategy; the public account records do not list the individual securities."
permalink: /findings/oversight-gap/
breadcrumb: "Key Findings"
---

{% assign inv = site.data.investigation %}
{% assign atrs = inv.agencies | where: "id", "atrs" | first %}

ATRS took three distinct steps: it authorized **{{ atrs.authorization_display | replace: 'Up to', 'up to' }}**, hired Reams Asset Management, and later reported moving **{{ atrs.measure_display }}** into the manager account.

Those steps should not be collapsed into one claim about holdings.

## What the funding notice tells members

The December 29, 2025 Board update shows that ATRS transferred {{ atrs.measure_display }} to the Reams account created for the strategy. That is a real movement of public retirement money and an important measure of scale.

## What members still cannot see

The account documents released by ATRS do not list:

- the individual bonds purchased by Reams;
- the amount and date of each purchase;
- settlement records for those securities; or
- a later account statement showing the mix of cash and bonds.

Without those details, the accurate description is **{{ atrs.measure_display }} in manager-account funding**. It is not a published security-level holdings total.

## Why the distinction matters

Authorization, manager funding, and an individual security purchase answer different questions. Clear public reporting lets members follow the money without mistaking one step for another.

The Integrity Act focuses on the financial work behind a covered acquisition. Ongoing manager-account reporting is a related issue that pension boards can address through their own transparency policies.

[Read the ATRS manager-funding notice &rarr;]({{ inv.sources.atrs_funding.record_url }})
[See the full ATRS timeline &rarr;](/evidence/#how-the-decisions-unfolded)

---

[Back to Key Findings &rarr;](/findings/)
