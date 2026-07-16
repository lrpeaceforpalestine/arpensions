---
layout: page
title: "Pension Investment Integrity Act — One-Page Brief"
description: "A printable summary of the issuer-neutral pension investment safeguards proposed for Arkansas's 2027 legislative session."
permalink: /legislators/one-page/
breadcrumb: "Integrity Act one-page brief"
hide_rule: true
hide_cta: true
---

{% assign inv = site.data.investigation %}
{% assign treasury = inv.agencies | where: "id", "treasury" | first %}
{% assign apers = inv.agencies | where: "id", "apers" | first %}

<div class="print-one-page" markdown="1">

**Campaign stage:** {{ inv.legislation.stage }} · **Bill number:** {{ inv.legislation.bill_number }} · **Status verified:** {{ inv.legislation.status_verified | date: "%B %-d, %Y" }}

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
- It does not convert authorization or manager funding into holdings.
- It does not reach the separately governed State Treasury.

## Legislative request

Request a drafting and source briefing, preserve the five safeguards in bill text and fiscal review, and consider sponsoring the proposal for the 2027 regular session.

**Briefing and source package:** [info@arpensions.org](mailto:info@arpensions.org?subject=Pension%20Investment%20Integrity%20Act%20briefing) · [arpensions.org/evidence](https://arpensions.org/evidence/)

*Use your browser's Print command to print or save this brief as a PDF.*

</div>
