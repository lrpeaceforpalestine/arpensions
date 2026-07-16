---
layout: page
title: "Methodology — Render-Aware Public-Records Review"
description: "How Arkansans for Pension Integrity reviews source files, rendered PDF pages, transaction states, and bounded absence findings."
permalink: /methodology/
breadcrumb: "Methodology"
---

{% assign inv = site.data.investigation %}

## Research baseline

The current investigation baseline covers **{{ inv.corpus.raw_files_display }} raw files** and **{{ inv.corpus.pdf_pages_display }} PDF pages**. All {{ inv.corpus.render_jobs_total }} corpus render jobs are complete. The transaction-record cutoff used for the site's amount ledger is {{ inv.record_cutoff | date: "%B %-d, %Y" }}; the render-aware review was completed {{ inv.review_completed | date: "%B %-d, %Y" }}.

## Source preservation

Agency productions are retained as received. File hashes, paths, page counts, duplicates, variants, and extraction outputs are tracked separately. Publication excerpts are derivative copies; privacy masking never changes the preserved source.

## Text and visual review

PDF text extraction is a locator aid, not a substitute for seeing the page. The review process combines:

1. file inventory, hashing, and duplicate or variant reconciliation;
2. native text extraction and OCR where useful;
3. full-page rendering at readable resolution;
4. visual inspection of pages classified as blank, empty, image-only, low-text, or relevant to an absence finding;
5. comparison of cited page numbers with the rendered original; and
6. propagation of supported facts and boundaries into the site's evidence model.

This method is essential for pages whose substantive content is carried as vectors, images, overlays, or other elements ordinary extraction does not recover.

## Transaction states

The site distinguishes authorization, manager funding, payment processing, settlement, and security ownership. One state does not automatically prove the next.

- A board authorization is a ceiling or permission.
- Manager funding documents cash transferred to an investment account.
- A payment marked processing documents an operational step.
- Settlement evidence documents a completed transaction.
- A holdings statement documents a position as of its stated date.

Amounts on the site are assigned to these states in [`_data/investigation.yml`](https://github.com/divestforARfuture/arpensions.org/blob/main/_data/investigation.yml), the canonical public evidence model.

## Bounded absence findings

An absence claim identifies its searched corpus, record type, custodian, date range, and method. “Not identified in the reviewed production” does not mean a record never existed, an oral discussion never occurred, or no responsive material exists elsewhere.

Audio transcripts and OCR are treated as search indices. A no-match result is reported as no identified topic match, not proof of exhaustive silence.

## Evidence labels

| Label | Use |
|---|---|
{% for status in inv.status_labels %}| **{{ status[0] | replace: '_', ' ' }}** | {{ status[1] }} |
{% endfor %}

## Privacy and publication

Before an excerpt is hosted, it is checked for account data, transaction and user identifiers, direct contact information, signatures where unnecessary, and operational details. Campaign masks are disclosed on the record page. Page crops preserve enough context to verify the finding while omitting unrelated sensitive material.

## Interpretation

The project separates chronology from causation, organizational context from investment authority, and legal questions from adjudicated conclusions. Political advocacy and institutional relationships are reported when documented; claims about motive, control, statutory application, or investment merit are made only when the record supports them and are otherwise labeled interpretive or unresolved.

## Reproduce or question a finding

Use the [selected document trail](/documents/) and exact locators on each record page. For a source question, alternate reading, or accessibility request, contact [info@arpensions.org](mailto:info@arpensions.org?subject=Methodology%20or%20source%20question).
