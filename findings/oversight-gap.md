---
layout: page
title: "ATRS Mandate Funding and the Holdings Record"
description: "ATRS documented funding to the Reams manager mandate; the produced files do not identify the mandate's security-level holdings."
permalink: /findings/oversight-gap/
breadcrumb: "Key Findings"
---

{% assign inv = site.data.investigation %}
{% assign atrs = inv.agencies | where: "id", "atrs" | first %}

ATRS's public record distinguishes two events that should not be collapsed into one number: authorization and funding of a managed account on one hand, and the manager's security-level transactions on the other.

## Authorization and implementation

Resolution 2025-22 authorized **{{ atrs.authorization_display | replace: 'Up to', 'up to' }}** for an Israel Bonds-associated mandate and selected Reams as manager. The September 2025 management agreement and November amendment describe a separate-account structure, a private-placement target, and an acknowledgement of illiquidity.

On December 29, 2025, an ATRS Board update documented **{{ atrs.measure_display }} in funding to the Scout/Reams mandate**. This establishes that ATRS transferred the authorized capital to the manager account. It does not, by itself, identify which securities Reams acquired, in what amounts, or on what dates.

[Read the ATRS funding record](/documents/records/atrs-manager-funding/).

## What the production does not identify

Within the reviewed ATRS production, we did not identify:

- security-level purchase confirmations for the mandate;
- an inventory of securities held in the account;
- settlement dates or a deployment schedule; or
- a reconciliation between the account's funding and its underlying positions.

“Unproduced” is a boundary on this corpus. It does not establish the account's cash balance or immediate security deployment.

{% include search-boundary.html boundary_id="atrs_holdings" %}

## The December meeting record

Searches of locally generated transcripts for the December 1, 2025 ATRS Investment Committee and Board meetings found no topic match for Israel Bonds, Reams, Scout, Jubilee, or Resolution 2025-22. The same meetings included substantive discussion of private credit.

Transcript search is useful as a locator method, but it is not proof of exhaustive oral silence. The audio finding therefore remains a bounded absence finding: **no identified topic match in the reviewed transcripts**, not a claim that no relevant words were spoken or no oversight occurred elsewhere.

{% include search-boundary.html boundary_id="atrs_audio" %}

{% include evidence-boundary.html
  established="The documented amount was funded to the Reams manager mandate."
  unresolved="The produced files do not identify the mandate's security-level purchases, holdings, settlement dates, or deployment pace."
  not_claimed="Manager funding is not presented as a security holding or as proof of a single capital purchase."
%}

## What the Integrity Act would add

{{ inv.legislation.full_summary }} Continuing holdings transparency may require separate reporting rules, but the Act would make the pre-acquisition financial basis and liquidity terms available on a defined publication schedule.

---

- [Back to Key Findings](/findings/)
- [See the amount ledger](/key-figures/)
- [Read the Integrity Act proposal](/legislators/)
