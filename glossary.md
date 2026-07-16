---
layout: page
title: "Glossary — Reading the Public Investment Record"
description: "Plain-language definitions for authorizations, manager funding, holdings, transaction states, marketability, and evidence labels."
permalink: /glossary/
---

{% assign inv = site.data.investigation %}

## Investment and transaction terms

**Authorization ceiling.** The maximum amount a board permits under a motion or resolution. It is not evidence that the amount was purchased, funded, or held.

**Manager mandate.** An account or assignment under which an external investment manager may implement a strategy within agreed guidelines.

**Manager funding.** Cash transferred into a manager account. It establishes funding of the mandate, not the account's underlying security holdings.

**Purchase.** A transaction for a specified security and amount. A purchase record should be distinguished from an order or payment instruction that remains in process.

**Settlement.** Completion of the transaction's cash-and-security exchange.

**Holdings statement.** A record of securities owned as of a stated date. It is a dated snapshot, not necessarily a complete transaction history.

**Processing-stage payment.** A payment instruction whose record does not show completed bank processing or resulting ownership. The site's additional Treasury {{ inv.metrics.treasury_conditional_payment.display }} is in this category.

## Security and portfolio terms

**Israel Bonds.** Securities issued by the State of Israel and offered in the United States through Development Corporation for Israel. The campaign names the instrument while applying issuer-neutral standards to the public fiduciary process.

**Sovereign debt.** Debt issued by a national government.

**Limited marketability.** Constraints on ordinary resale or exit. Aon's ATRS memorandum uses this concept, and the campaign treats the transfer and secondary-market terms as information trustees should receive in plain language.

**Credit risk.** The risk that an issuer's financial capacity or willingness to meet its obligations changes.

**Portfolio fit.** How an investment's expected risk, return, duration, liquidity, currency exposure, concentration, and role compare with the rest of a portfolio and available alternatives.

**Pecuniary factor.** Under Arkansas's Act 498 framework, a factor expected to have a material financial effect on risk or return.

## Evidence labels

| Label | Meaning |
|---|---|
{% for status in inv.status_labels %}| **{{ status[0] | replace: '_', ' ' }}** | {{ status[1] }} |
{% endfor %}

## Current amount vocabulary

- **{{ inv.metrics.confirmed_security_floor.display }} security-level floor:** Treasury {{ inv.agencies[0].measure }} plus APERS {{ inv.agencies[1].measure }}.
- **{{ inv.metrics.atrs_manager_funding.display }} funded mandate:** ATRS funding to Reams; underlying holdings unproduced.
- **{{ inv.metrics.combined_tied_or_funded.display }} securities plus funded mandate:** a transparent combination of different measures, not holdings.
- **{{ inv.metrics.pension_authorization_ceiling.display }} authorization ceiling:** ATRS plus APERS maximum authorizations, not holdings.

[See the ledger in context](/evidence/) · [Review selected records](/documents/)
