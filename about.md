---
layout: page
title: "About Arkansans for Pension Integrity"
description: "An organization-led Arkansas campaign for public investment records, fiduciary process, and issuer-neutral pension safeguards."
permalink: /about/
header_image: /assets/images/about-highsmith-capitol-duotone-wide.jpg
header_image_alt: "Arkansas State Capitol in Little Rock, rendered in pine and mint tones."
mobile_cta_label: "Volunteer with the campaign"
mobile_cta_url: "/take-action/#volunteer"
---

{% assign inv = site.data.investigation %}
{% assign treasury = inv.agencies | where: "id", "treasury" | first %}
{% assign apers = inv.agencies | where: "id", "apers" | first %}
{% assign atrs = inv.agencies | where: "id", "atrs" | first %}

## Our principle

> **Public money deserves a public investment record.**

Arkansans for Pension Integrity is a grassroots campaign using public records, financial analysis, and Arkansas law to make public pension decisions easier to examine. The campaign is organization-led and can be reached at [info@arpensions.org](mailto:info@arpensions.org).

Arkansans for Pension Integrity continues campaign work begun under the name **Divest for AR Future**. The current legislative program is the issuer-neutral Pension Investment Integrity Act, which governs decision procedure rather than directing an investment outcome.

## What we do

<div class="approach-pillars" markdown="1">

**Review public records.** The current research baseline covers {{ inv.corpus.raw_files_display }} source files and {{ inv.corpus.pdf_pages_display }} PDF pages. We preserve agency productions, render every PDF page, and publish selected privacy-reviewed anchors with exact locators.

**Separate evidence states.** Authorizations, manager funding, payments in process, settled purchases, and holdings are different facts. The site labels them separately and treats absence findings as bounded to a defined production.

**Advance issuer-neutral procedure.** {{ inv.legislation.full_summary }} It would not prescribe an investment outcome.

**Build public participation.** Educators, public employees, retirees, legislators, journalists, and other Arkansans should be able to see and discuss the financial record governing public retirement money.

</div>

## Organizational accountability

Research, publication, legislative advocacy, and public contact are conducted under the organization name **Arkansans for Pension Integrity**. The site's factual account is tied to cited public records; interpretive claims and unresolved questions are labeled. A participant's politics, office, or organizational relationship is context, not a substitute for evidence of authority or causation.

To challenge a locator, submit an alternate reading, request an accessible record, or provide a source, email [info@arpensions.org](mailto:info@arpensions.org?subject=Source%20or%20editorial%20question). Include the page, claim, and supporting record when possible. The site presents the strongest verified account supported by the current evidence model.

Petition and contact-data practices are described in the [privacy notice](/privacy/).

## Campaign structure and coalition relationship

**Public responsibility.** Research, editorial decisions, legislative advocacy, and responses from this site are issued under the Arkansans for Pension Integrity name through its co-chair structure and organization-level contact. The campaign is not a pension system, broker-dealer, investment adviser, or government office.

**Coalition route.** Little Rock Peace for Palestine, a Citizens First Congress member organization, brought the Pension Investment Integrity Act into the coalition process with Arkansans for Pension Integrity leading the campaign work. {{ inv.legislation.cfc_status }} Priority status does not make Citizens First Congress responsible for this website's research or wording.

**Publication independence.** The site carries no advertising or paid placements. Claims are accepted, revised, or rejected according to the cited record and stated evidence boundaries, not a participant's office, affiliation, or political relationship.

**Name and strategy.** Divest for AR Future began the campaign work. Arkansans for Pension Integrity names the current organization and its issuer-neutral legislative program: a reviewable fiduciary procedure rather than a direction to buy, hold, sell, or divest from a particular security.

## Current evidence in one paragraph

Arkansas records establish a {{ inv.metrics.confirmed_security_floor.display }} security-level floor: Treasury's derived {{ treasury.measure }} plus APERS's {{ apers.measure }}. ATRS separately documented {{ atrs.measure }}. An additional Treasury {{ inv.metrics.treasury_conditional_payment.display }} payment remained at the processing stage. The produced files contain implementation, manager-selection, marketability, and credit-related materials while leaving material questions about how sovereign-credit risk and portfolio fit were connected to each affirmative investment decision.

## Frequently asked questions

<div class="faq-section" markdown="1">

### Is {{ inv.metrics.combined_tied_or_funded.display }} a holdings total?

No. It combines {{ inv.metrics.confirmed_security_floor.display }} in confirmed securities with {{ inv.metrics.atrs_manager_funding.display }} funded to an ATRS manager account. The underlying ATRS security holdings were not identified in the reviewed production.

### Is {{ inv.metrics.pension_authorization_ceiling.display }} the amount pension systems bought?

No. It is the combined maximum of two authorizations. APERS's confirmed purchase is {{ apers.measure }}; ATRS documented manager funding, not security-level holdings.

### What analytical material is in the record?

Aon provided substantive implementation and manager-selection advice to ATRS; Treasury produced a substantive internal credit overview; other materials address marketability and rating developments. The open question is how sovereign-credit risk and portfolio fit were evaluated and connected to each affirmative decision.

### Is the campaign asking pension funds to divest?

No. The legislative proposal requires a procedure and a public record. It does not direct a board to buy, hold, or sell a particular security.

### Are political relationships part of the investigation?

Yes, when documented. They provide context for access, advocacy, and information routes. The site does not treat chronology or political association as proof of investment causation.

### Can I review the source material?

Yes. Start with the [selected documents](/documents/), [evidence page](/evidence/), and [methodology](/methodology/). Contact [info@arpensions.org](mailto:info@arpensions.org?subject=Source%20question) for a locator or accessibility request.

</div>

## Contact

**Arkansans for Pension Integrity**<br>
[info@arpensions.org](mailto:info@arpensions.org)<br>
[arpensions.org](https://arpensions.org)
