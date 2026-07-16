---
layout: record
title: "APERS Confirmed Purchase Record"
description: "The October 15, 2025 transaction record documenting the confirmed APERS purchase."
permalink: /documents/records/apers-purchase/
source_agency: "Arkansas Public Employees Retirement System"
source_date: "2025-10-15"
source_file: "IB_FOIA_FINAL. 2.27.2026 Redacted.LMG.pdf"
source_locator: "Physical PDF page 6,925"
publication_treatment: "Campaign crop; transaction and account identifiers masked."
asset_url: /assets/documents/apers-purchase-record-page-6925-masked.pdf
---

{% assign inv = site.data.investigation %}
{% assign apers = inv.agencies | where: "id", "apers" | first %}

## What the record establishes

The page shows a purchase of **{{ apers.measure_display }}** dated October 15, 2025, with a beneficiary descriptor for the seller's wire-purchase account and a two-year bond CUSIP.

The amount is below the motion's stated range. The selected files do not resolve whether the purchase was intended as a first stage, the final amount, or an implementation requiring later Board treatment.

{% include evidence-boundary.html
  established="APERS made the documented security purchase."
  unresolved="The operational or legal effect of the purchase being below the stated minimum remains open."
  not_claimed="The authorization ceiling is not presented as purchased or held."
%}

[Read the signed authorization minutes](/documents/records/apers-authorization/) · [See APERS in the agency ledger](/evidence/#agency-apers)
