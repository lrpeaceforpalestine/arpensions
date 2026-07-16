---
layout: record
title: "Treasury Settled-Position Record"
description: "A June 30, 2025 bondholder statement supporting the settled Treasury position and the derived floor after a later maturity."
permalink: /documents/records/treasury-holdings/
source_agency: "Arkansas State Treasury"
source_date: "2025-06-30"
source_file: "Israel Bondholder Statements_Redacted.pdf"
source_locator: "Physical PDF page 1"
publication_treatment: "Campaign crop omits recipient, barcode, account, and return-mail data; agency mask retained."
asset_url: /assets/documents/treasury-holdings-june-2025-cropped.pdf
---

{% assign inv = site.data.investigation %}
{% assign treasury = inv.agencies | where: "id", "treasury" | first %}

## What the statement establishes

The dated statement lists seven positions with a total current value of **{{ inv.transaction_figures.treasury_june_statement.display }}**. A separately documented February 1, 2026 maturity reduces the derived confirmed Treasury floor to **{{ treasury.measure }}**.

The May 2025 positions shown in this statement are also supported by a [settled purchase confirmation](/assets/documents/sovereign-bond-purchase-confirmation-may2025.pdf).

The February 2026 processing-stage payment is not included in the confirmed floor without later settlement or holdings evidence.

[Open the processing-stage record](/documents/records/treasury-processing-payment/) · [See the exposure ledger](/the-issue/#four-institutions-different-transaction-states)
