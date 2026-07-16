---
layout: record
title: "Treasury Final-Maturity Cash-Flow Record"
description: "The produced cash-flow row documenting a $5 million final maturity posted in February 2026."
permalink: /documents/records/treasury-maturity/
source_agency: "Arkansas State Treasury"
source_date: "2026-02-02"
source_file: "2026 0202 IA- Non- MBS Cash Flow_Treasury Gen AGG- ISRAEL BONDS- PAR & MATURITY.xlsx"
source_locator: "Sheet1, row 14"
publication_treatment: "Campaign-typeset excerpt; account and security identifiers, coupon details, and unrelated formula or adjustment rows omitted."
asset_url: /assets/documents/treasury-final-maturity-excerpt.pdf
---

{% assign inv = site.data.investigation %}
{% assign treasury = inv.agencies | where: "id", "treasury" | first %}

## What the workbook establishes

The produced Treasury cash-flow workbook identifies a **Final Maturity** of **{{ inv.transaction_figures.treasury_february_maturity.display }}**, with a February 2, 2026 post date. The excerpt publishes the transaction type, security category, issuer description, post date, and amount from Sheet1, row 14.

The June 30, 2025 bondholder statement documents {{ inv.transaction_figures.treasury_june_statement.display }}. Subtracting this final maturity produces the derived **{{ treasury.measure }}** used in the site's confirmed security-level floor.

The separate February 2026 payment instruction is not added back to that floor because the produced report remained marked “Processing By Bank.”

{% include evidence-boundary.html
  established="The produced cash-flow record posts the documented final maturity."
  unresolved="Any later settled acquisition must be established through a completed transaction or holdings record."
  not_claimed="The processing-stage payment is not counted as a confirmed security holding."
%}

[Open the June 2025 settled-position record](/documents/records/treasury-holdings/) · [Open the processing-stage payment](/documents/records/treasury-processing-payment/) · [Review the amount ledger](/evidence/)
