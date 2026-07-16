---
layout: page
title: "Pension Investment Integrity Act — One-Page Brief"
description: "A printable summary of the issuer-neutral pension investment safeguards proposed for Arkansas's 2027 legislative session."
permalink: /legislators/one-page/
breadcrumb: "Integrity Act one-page brief"
hide_rule: true
hide_cta: true
mobile_cta_label: "Request a briefing"
mobile_cta_url: "mailto:info@arpensions.org?subject=Pension%20Investment%20Integrity%20Act%20briefing"
body_class: integrity-brief-page
---

{% assign inv = site.data.investigation %}
{% assign treasury = inv.agencies | where: "id", "treasury" | first %}
{% assign apers = inv.agencies | where: "id", "apers" | first %}

<p class="brief-download"><a class="btn-secondary" href="{{ inv.legislation.brief_pdf_url }}" download>Download the dated one-page PDF</a> <span>Version {{ inv.legislation.brief_version_date | date: "%B %-d, %Y" }}</span></p>

<div class="print-one-page" markdown="1">

<header class="print-only print-brief-heading" markdown="1">

<p class="print-brief-title">Pension Investment Integrity Act</p>

**2027 Arkansas legislative briefing · Arkansans for Pension Integrity**

</header>

**Campaign stage:** {{ inv.legislation.stage }} · **Bill number:** {{ inv.legislation.bill_number }} · **Prefiling opens:** {{ inv.legislation.prefiling_opens_display }} · **Ordinary retirement-bill deadline:** {{ inv.legislation.retirement_filing_deadline_display }}

## The principle

> **Public money deserves a public investment record.**

Arkansas records establish a **{{ inv.metrics.confirmed_security_floor.display }} security-level floor** across Treasury and APERS, plus **{{ inv.metrics.atrs_manager_funding.display }} funded to an ATRS manager mandate** whose underlying security holdings were not produced. The files contain manager-selection, implementation, marketability, and credit-related materials while leaving material questions about how sovereign-credit risk and portfolio fit were connected to each affirmative pension decision.

## The five safeguards

{% for provision in inv.legislation.provisions %}
{{ forloop.index }}. {{ provision }}.
{% endfor %}

{{ inv.legislation.full_summary }}

## What the proposal does—and does not do

- It creates a consistent, reviewable decision record for covered pension acquisitions.
- It is prospective and issuer-neutral.
- It leaves the ultimate buy, hold, or sell decision with trustees.
- It publishes the core decision record after acquisition while allowing only narrow, explained protection of legally confidential operational details.
- It does not convert authorization or manager funding into holdings.
- It does not reach the separately governed State Treasury.

## Legislative request

Request a drafting and source briefing before prefiling opens, preserve the five safeguards in bill text and fiscal review, and consider sponsoring the proposal for the 2027 regular session. The ordinary filing deadline for retirement legislation is {{ inv.legislation.retirement_filing_deadline_display }}; {{ inv.legislation.late_filing_rule | downcase }} [Official 2027 dates.]({{ inv.legislation.important_dates_url }})

**Briefing and source package:** [info@arpensions.org](mailto:info@arpensions.org?subject=Pension%20Investment%20Integrity%20Act%20briefing) · [arpensions.org/evidence](https://arpensions.org/evidence/)

<p class="print-instruction"><em>Use your browser's Print command to print or save this brief as a PDF.</em></p>

</div>
