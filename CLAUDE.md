# arpensions.org repository guide

Live site: <https://arpensions.org>

## Non-negotiable editorial rules

- Lead with: “Public money deserves a public investment record.”
- Treat `_data/investigation.yml` as the authoritative public source for amounts, evidence states, cutoffs, source links, and bounded descriptions.
- Keep confirmed securities, manager funding, authorization ceilings, and processing-stage payments visually and verbally distinct.
- Describe produced analytical material affirmatively, then identify the unresolved decision-record question.
- Do not publish correction history, retired claims, internal audit commentary, or retrospective comparisons.
- Keep legal conclusions and causal claims bounded to the record.
- Use Arkansans for Pension Integrity and `info@arpensions.org`; do not add an individual biography.
- Do not describe the Equity Supplement as a distributed Citizens First Congress handout or infer the contents of the unavailable Equity Report.
- Preserve public routes, document URLs, the QR destination, and the Action Network embed.
- Never edit `_site`.

## Brand and accessibility

Preserve the pine, mint, jade, and banknote identity. The evidence ledger is the signature component. Maintain keyboard focus, dark mode, reduced-motion behavior, readable no-JavaScript fallbacks, accessible tables for visual evidence, and responsive layouts without horizontal overflow.

### Brand reference

- Pine `#013237`: headings, dark surfaces, footer, and core brand field.
- Pine deep `#002A2E`: dark-mode and layered dark surfaces.
- Ink `#152019`: primary text on light surfaces.
- White `#FFFFFF` and mint wash `#F2FAF1`: primary and secondary light surfaces.
- Mint pale `#E6F9E4` and mint `#C0E7BA`: text and highlights on dark surfaces.
- Jade `#48A46D`: fills, charts, and large graphic accents; do not use it for ordinary text on white.
- Jade deep `#1E7B47`: links and interactive text on light surfaces.
- Jade bright `#5FBF8B`: links and focus accents on dark surfaces.
- Campaign red `#B91C1C`: primary calls to action and alerts.
- Display type: League Spartan. Body type: Mulish. Data labels: IBM Plex Mono.
- Logo assets use the `api-badge*` family under `assets/images/`.

Brand primitives and semantic aliases live in `assets/css/main.css`; the evidence-led layer lives in `assets/css/evidence-led.css`. Keep the anti-FOUC colors in `_includes/head.html` and the theme values in `assets/js/theme-toggle.js` synchronized with those tokens. If the inline theme script changes, recompute its CSP hash.

## Public routes

- `/` — principle, evidence ledger, audience pathways, and Integrity Act entry point.
- `/the-issue/` — instrument, agency record, fiduciary principles, and proposed safeguards.
- `/evidence/` — canonical findings, agency status, analytical record, open questions, events, and sources.
- `/documents/` and `/documents/records/*/` — curated primary-record trail and exact locators.
- `/legislators/` — Pension Investment Integrity Act policy brief.
- `/take-action/` — Action Network petition, letter, meeting, volunteer, and sharing actions.
- `/about/`, `/press/`, `/methodology/`, `/news/`, and `/glossary/` — organization and research context.
- `/educators/` and `/public-employees/` — fund-specific audience pages.
- `/findings/` and `/key-figures/` — detailed findings and participant roles; preserve these public routes.

## Local development

```bash
bundle install
bundle exec jekyll serve
```

Install the audit dependencies separately:

```bash
python -m pip install -r requirements-dev.txt
```

The source-excerpt and social-asset generators are local publication tools, not deploy-time dependencies. `scripts/build_source_excerpts.py` defaults to the Windows investigation path and both generators prefer Windows system fonts; pass an explicit corpus root when using the excerpt generator elsewhere.

## Validation

Before publishing, run:

```bash
python scripts/audit_site.py
JEKYLL_ENV=production bundle exec jekyll build --trace
python scripts/audit_site.py --site _site
python scripts/verify_assets.py
```

The GitHub Actions workflow in `.github/workflows/site-audit.yml` repeats these gates on pull requests. It checks canonical-data arithmetic and references, regression language, front matter, headings, IDs, internal links and anchors, canonical URLs, JSON-LD, alt text, visualization fallbacks, QR payload, source PDFs, and the Open Graph asset.
