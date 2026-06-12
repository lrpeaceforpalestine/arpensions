# Arkansans for Pension Integrity (API) — Campaign Website

> **Live site:** [arpensions.org](https://arpensions.org)

This is the public-facing campaign website for Arkansans for Pension Integrity, a grassroots Arkansas initiative investigating state pension fund investments in non-marketable foreign sovereign debt.

## Quick Reference

| Item | Value |
|------|-------|
| Domain | arpensions.org |
| Stack | Jekyll + GitHub Pages + Pico CSS v2 |
| Email | info@arpensions.org |
| Organization | Arkansans for Pension Integrity (API) |
| Tagline | Your money. Zero analysis. |

## Site Structure

```
/                    # Home (hero + stats + pathway cards)
/the-issue/          # Core fiduciary argument
/evidence/           # FOIA findings + timeline
/key-figures/        # Profiles of key officials, orgs, and relationship patterns
/documents/          # FOIA document archive
/educators/          # ATRS-specific content
/public-employees/   # APERS-specific content
/legislators/        # Integrity Act + 2027 session
/press/              # Press kit + media resources
/take-action/        # CTAs by time commitment
/about/              # FAQ + campaign info
/news/               # Updates + coverage
/methodology/        # Research methodology
/glossary/           # Investment profile + terminology
```

## Brand System

**Colors (green "money" system — June 2026 redesign, from Payne Moussa's design suite):**
- Pine: `#013237` (brand dark — headings, links-hover, footer, hero, dark-mode bg)
- Ink: `#152019` (body text on light)
- White: `#FFFFFF` (page background, light mode)
- Mint wash: `#F2FAF1` (light surfaces — bands, cards); mint pale `#E6F9E4` (text on dark, highlights); mint `#C0E7BA`
- Jade: `#48A46D` (fills, charts, large display ONLY — 3.1:1 on white, never text)
- Jade deep: `#1E7B47` (links + interactive on light, 5.3:1); jade bright `#5FBF8B` (links on dark)
- Campaign red: `#B91C1C` (CTAs, alerts, key findings — unchanged)
- Secondary text: `#3F4F46`; muted text: `#5C6B62` (green-tinted neutrals, AA on white + mint wash)
- Borders: `#DCE8DC` light / `#14555C` dark

**Typography (unchanged):**
- Display: Cormorant Garamond (h1, h2)
- Body: Source Serif 4 (prose)
- UI/nav: Inter (sans-serif)
- Data/mono: IBM Plex Mono

**Logo:** "api" badge — lowercase League Spartan Bold glyph outlines (SIL OFL, extracted via fonttools) set in a simplified Arkansas keystone. Working render of Payne Moussa's concept pending her final design suite. Variants: `api-badge.svg` (pine fill, mint monogram — light surfaces), `api-badge-dark.svg` (mint keyline — dark surfaces), `api-badge-512.png` (raster for structured data), `apple-touch-icon.png` (180px, pine tile), `favicon.svg`/`favicon.ico`.

**CSS custom properties:** Brand primitives are `--api-pine`, `--api-ink`, `--api-white`, `--api-mint*`, `--api-jade*`, `--api-red`, `--api-gray` in `main.css :root`; semantic tokens use `--bg-*`, `--text-*`, `--accent`, `--border-*`, `--link-*` prefixes and cascade from the primitives. Legacy navy/gold-era primitive names (`--api-navy`, `--api-gold`, `--api-cream`, `--api-charcoal`, `--api-slate`, `--api-forest`) are aliased to green values for backwards compatibility — do not use them in new code. The anti-FOUC critical CSS in `_includes/head.html` and `syncBrowserTheme()` in `theme-toggle.js` hardcode the token values and must be kept in sync with `main.css`; the inline FOUC script is CSP-hashed (recompute the sha256 in the CSP meta when editing it).

## Development

**Local build:**
```bash
bundle install
bundle exec jekyll serve
```

**Key files:**
- `_config.yml` — site configuration
- `_includes/` — nav, footer, head, components
- `_layouts/` — default, page, post, landing
- `assets/css/main.css` — core styles (~71KB, `--art-*` tokens)
- `assets/css/elegant.css` — design layer (~33KB)
- `assets/js/` — nav, theme toggle, animations

## Content Guidelines

1. **Fiduciary-first framing** — financial merit and legal standards, not political arguments
2. **Source everything** — every factual claim must trace to a FOIA document
3. **Issuer-neutral language** — all campaign-voice content uses financial terminology ("non-marketable foreign sovereign debt," "non-tradable sovereign bonds," "the bonds under investigation") rather than naming the bond issuer. Official quotes stay verbatim with "From the public record:" prefix. The glossary page (`/glossary/`) explains the approach and provides the financial profile. See `REFRAME-INSTRUCTIONS.md` for the complete terminology table.
4. **No BDS self-identification** — this is a transparency and accountability campaign
5. **Current data only** — keep stats updated (ATRS: $23.7B, ~84% funded; APERS: $11.58B, ~83% funded)
6. **Corpus state** — 1,227 total documents (1,044 active after dedup) from the producing-docs agencies (Treasury, ATRS, APERS, ASHERS, Auditor); 12 FOIA requests across 4 rounds to 8 state entities (six pension systems covered by Act 498 plus Treasury and Auditor of State); AJRS Round 4 filed May 8, 2026 and acknowledged by Richmond Giles (APERS Staff Attorney handling both pension systems' legal); production extended to May 15, 2026

## Accessibility

- WCAG AA compliance target
- Skip links, semantic HTML, ARIA labels
- Dark mode support with opacity-based logo crossfade
- Keyboard navigation
- Focus indicators
- `prefers-reduced-motion` respected for all transitions
- `aria-hidden` managed dynamically on inactive logo variants

## About the Campaign

Arkansans for Pension Integrity (API) is a grassroots Arkansas campaign for pension transparency and fiduciary accountability. The campaign focuses on passing the Pension Investment Integrity Act in the 2027 Arkansas legislative session.

---

## Audit Log — March 27, 2026

### PR #2: Critical structural fixes

**CRITICAL-1 — Nav HTML/CSS mismatch:** `nav.html` had been restructured with CSS classes that had zero definitions. Reverted to reference site structure with ART brand changes only.

**CRITICAL-2 — Dark mode broken:** Theme toggle button missing `id` attribute + localStorage key mismatch (`art-theme` vs `d4arf-theme`). Both fixed.

**MEDIUM — robots.txt:** Restored OAI-SearchBot and PerplexityBot allow rules.

**LOW:** Removed unused d4arf-logo PNG files.

### PR #3: Logo replacement

Replaced hand-drawn geometric SVG with Cormorant Garamond Medium (500) glyph outlines extracted via fonttools. Red underline bar height set to 55 units (renders ~2px at nav size). Trailing newlines added to all files.

### PR #4: Theme polish + CSS rename

**Logo crossfade:** Changed from `display:none/block` to `opacity:0/1` with absolute positioning. Eliminates layout shift during toggle and between-page logo flash.

**Anti-FOUC inline style:** Expanded to cover logo stacking, pointer-events, and explicit opacity values.

**CSS rename:** Full `--d4arf-*` → `--art-*` custom property rename across all 5 CSS files.

**JS improvements:** `prefers-reduced-motion` guard skips `theme-transition` class entirely. `updateLogoAria()` manages `aria-hidden` on inactive logo. Uses `removeAttribute` (not `"false"`).

**Print URL:** Set to `arpensions.org`.

### PR #5: Final comment cleanup

Renamed "D4ARF" → "ART" in source code comments: `charts.js` line 2, `network.css` line 3, `network.js` line 2.

#### Known remaining items

All previously tracked items (og-default.png branding, favicon.ico branding) resolved as of March 29, 2026.
