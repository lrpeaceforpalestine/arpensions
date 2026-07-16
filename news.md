---
layout: page
title: "Campaign Updates"
description: "Dated milestones in the Arkansas public-investment investigation and the Pension Investment Integrity Act campaign."
permalink: /news/
---

{% assign inv = site.data.investigation %}
{% assign apers = inv.agencies | where: "id", "apers" | first %}
{% assign atrs = inv.agencies | where: "id", "atrs" | first %}

Each entry is a standalone account of the record or campaign milestone known at that date.

## 2026

### July 16 — PDF render gate completed

The investigation completed {{ inv.corpus.render_jobs_complete }} of {{ inv.corpus.render_jobs_total }} PDF render jobs covering {{ inv.corpus.pdf_pages_display }} pages in a {{ inv.corpus.raw_files_display }}-file raw corpus. The current evidence model distinguishes confirmed securities, manager funding, authorization ceilings, and processing-stage payments and supplies exact locators for the site's principal claims. [Read the methodology.](/methodology/)

### June 27 — 2027 coalition priority

{{ inv.legislation.cfc_status }} {{ inv.legislation.full_summary }} The proposal is issuer-neutral. [Read the policy brief.](/legislators/)

### May 18 — Six-system response record completed

The Arkansas Judicial Retirement System reported no records responsive to the request. With that response, the project had received responses from each of the six pension systems within the Act 498 definition used by the investigation. A no-records response is reported as a bounded agency response, not proof that no related record could exist in another custodian's files.

### April 20 — Broker-dealer records received

The Arkansas Securities Department supplied registration and historical regulatory records for the broker-dealer through which the securities are offered. The records inform questions about marketability, due diligence, and Arkansas's exclusive-agency language; they do not by themselves establish present disqualification, a statutory violation, or investment unsuitability. [Read the finding.](/findings/regulatory-record/)

### March 28 — ASHERS outreach record received

Selected ASHERS records document a DFA introduction and the sellers' pitch. No reply, authorization, or holding was identified in the reviewed production. The files do not establish an affirmative decline or the cause of the different observed outcome. [Read the ASHERS finding.](/findings/control-case/)

### February 27 — APERS transaction and governance production

The APERS production included meeting records and a large correspondence package. The reviewed file documents a {{ apers.measure_display }} purchase and signed minutes for a {{ apers.authorization_display }} authorization. [See APERS records.](/documents/#a-curated-source-trail)

### February 19 — Treasury payment-stage production

Treasury records document an additional {{ inv.metrics.treasury_conditional_payment.display }} payment instruction marked “Processing By Bank.” Without a completed bank status or resulting holdings record in the production, the amount remains conditional. [Read the record.](/documents/records/treasury-processing-payment/)

## 2025

### December 29 — ATRS mandate funding documented

An ATRS Board liquidity update documented {{ inv.metrics.atrs_manager_funding.display }} funded to the Scout/Reams mandate. The email does not identify the manager's security-level purchases or holdings. [Read the record.](/documents/records/atrs-manager-funding/)

### October 15 — APERS purchase documented

APERS's transaction file documents a {{ apers.measure }}. The purchase is below the authorization motion's stated minimum; the operational and legal effect remains unresolved. [Read the privacy-reviewed record.](/documents/records/apers-purchase/)

### June 2 — ATRS authorization adopted

ATRS adopted Resolution 2025-22, authorizing **{{ atrs.authorization_display | replace: 'Up to', 'up to' }}** and naming Reams as manager. Aon's packet memorandum provides implementation and manager-selection advice while expressly withholding an invest-or-not or individual-security recommendation. [Read pages 149–150.](/documents/records/atrs-aon-memo/)

### May 15 — APERS committee authorization adopted

Signed minutes document an APERS Investment Finance Subcommittee motion for **{{ apers.authorization_display }}**. Jason Brady presented and moved the proposal, Jim Hudson seconded it, and the motion carried without dissent. [Read the minutes.](/documents/records/apers-authorization/)

### Spring — Investigation launched

Arkansans for Pension Integrity began assembling agency records on public investments, governance, and fiduciary process. The project publishes selected privacy-reviewed anchors and keeps its legislative proposal focused on issuer-neutral procedure.
