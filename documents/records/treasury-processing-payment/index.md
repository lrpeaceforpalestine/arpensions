---
layout: record
title: "Treasury Processing-Stage Payment"
description: "The February 17, 2026 outgoing payment report marked ‘Processing By Bank.’"
permalink: /documents/records/treasury-processing-payment/
source_agency: "Arkansas State Treasury"
source_date: "2026-02-17"
source_file: "Wire Confirm 2-17-26_Redacted.pdf"
source_locator: "Physical PDF page 1"
publication_treatment: "Campaign crop; requester and transaction identifiers masked; agency masks retained."
asset_url: /assets/documents/treasury-processing-payment-masked.pdf
---

{% assign inv = site.data.investigation %}

## What the report establishes

The outgoing payment report shows a **{{ inv.metrics.treasury_conditional_payment.display }}** instruction for an Israel Jubilee bond and a status of **“Processing By Bank.”** The amount, intended instrument, and operational approval stage are documented.

The reviewed production does not include a completed bank status, seller acceptance, book-entry registration, or a resulting holdings statement. The additional amount therefore remains conditional.

{% include evidence-boundary.html
  established="The payment instruction reached the processing stage."
  unresolved="Settlement and resulting beneficial ownership are not documented in the reviewed production."
  not_claimed="The payment instruction is not included in the confirmed security-level floor."
%}

[Open the confirmed Treasury position](/documents/records/treasury-holdings/) · [Read the transaction-state methodology](/methodology/#transaction-states)
