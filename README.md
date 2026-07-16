# Arkansans for Pension Integrity

Public-facing Jekyll site for [arpensions.org](https://arpensions.org), an Arkansas public-records and legislative campaign.

## Editorial architecture

- `_data/investigation.yml` is the canonical public evidence model for amounts, statuses, cutoffs, bounded findings, timeline entries, and source locators.
- `_includes/` contains the evidence ledger, agency status, exposure, route, citation, and evidentiary-boundary components.
- `documents/records/` contains explanatory pages for privacy-reviewed source excerpts.
- `scripts/` contains local source-publication and audit utilities.
- `assets/documents/` contains selected publication excerpts and longstanding public document URLs.

Do not edit generated `_site` output. Run the repository checks before publishing.

## Stack

- Jekyll and GitHub Pages
- Pico CSS v2 plus campaign styles
- Progressive enhancement; charts and evidence remain comprehensible without JavaScript

## Contact

[info@arpensions.org](mailto:info@arpensions.org)

## License

See [LICENSE](LICENSE) for the mixed licensing of code, site content, government records, third-party assets, and campaign marks.
