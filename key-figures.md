---
layout: page
title: "Key Participants and Institutions"
description: "The public offices, pension systems, advisers, managers, sellers, and officials documented in the Arkansas investment record."
permalink: /key-figures/
breadcrumb: "Key Figures"
---

{% assign inv = site.data.investigation %}
{% assign treasury = inv.agencies | where: "id", "treasury" | first %}
{% assign apers = inv.agencies | where: "id", "apers" | first %}
{% assign atrs = inv.agencies | where: "id", "atrs" | first %}

This page describes roles shown in the public record. Appearance in a chronology or correspondence network does not establish control, motive, or decision causation.

## Pension systems and advisers

<div class="findings-grid" markdown="1">

<article class="finding-card" markdown="1">

### Arkansas Teacher Retirement System

ATRS authorized {{ atrs.authorization_display | replace: 'Up to', 'up to' }}, selected Reams as manager, and documented {{ atrs.measure_display }} in manager funding. Executive Director **Mark White** administered the proposal; **Aon Hewitt Investment Consulting** advised on implementation and manager selection; **Reams Asset Management** received the mandate. Security-level holdings were not identified in the reviewed production.

</article>

<article class="finding-card" markdown="1">

### Arkansas Public Employees Retirement System

APERS's Investment Finance Subcommittee adopted a {{ apers.authorization_display }} range, and APERS later recorded a {{ apers.measure_display }} purchase. Executive Director **Amy Fecher** and Chief Investment Officer **Carlos Borromeo** appear in the governance and implementation record. The reviewed authorization file contains no Callan sovereign-credit memorandum tied to the decision.

</article>

<article class="finding-card" markdown="1">

### Arkansas State Treasury

Treasury records establish a security-level floor of {{ treasury.measure_display }} after a documented maturity. An **unattributed internal Treasury overview** dated October 8, 2024 recommends HOLD and surveillance. Senior Investment Officer **Steve Pulley** placed the later {{ inv.transaction_figures.treasury_may_settled.display }} order; the reviewed files contain no identified written reconciliation with the recommendation.

</article>

</div>

## Public-office and governance roles

**Dennis Milligan, Auditor of State.** The Auditor is an ex-officio ATRS trustee. Records document Milligan's advocacy and his office's role in scheduling, correspondence, and promotion. The Auditor does not manage pension assets or serve as pension investment staff.

**Jason Brady, Chief Deputy Auditor.** ATRS records identify Brady as Milligan's designee; APERS minutes identify him as the Auditor's proxy on the Board and Investment Finance Subcommittee. He presented and moved the APERS authorization and appears in scheduling, correspondence, and promotion records.

**Jim Hudson and Andy Babbitt, Department of Finance and Administration.** DFA records support a confirmed encounter in the April 2025 itinerary and an introduction of the sellers to ASHERS. The selected ASHERS records show the pitch and no identified adoption.

## Seller, manager, and network

**Development Corporation for Israel.** The registered broker-dealer through which Israel Bonds are offered in the United States. Its representatives, including **Lawrence Berman** and **Brad Young**, appear in Treasury, pension, DFA, and Auditor-office records.

**Reams Asset Management.** The manager selected by ATRS to implement the mandate. The production documents the management structure and funding, but not the account's security-level holdings.

**State Financial Officers Foundation.** A national network appearing in event, newsletter, speech, and contact-facilitation records. Those records establish context and relationships, not direction of a pension allocation or control over Arkansas decision-makers.

{% include evidence-boundary.html
  established="The records identify formal roles, communications, scheduled or reported encounters, and institution-specific decisions."
  unresolved="The influence of any one person, office, meeting, or network on a board's independent decision remains open unless a record expressly establishes it."
  not_claimed="Frequency of appearance and chronological proximity are not treated as causal measures."
%}

[See the agency ledger](/evidence/#agency-by-agency) · [Read the detailed findings](/findings/) · [Review the documented routes](/evidence/#events-and-routes)
