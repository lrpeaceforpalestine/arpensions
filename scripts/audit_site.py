"""Audit public source and rendered Jekyll output for evidence and HTML regressions."""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

import yaml
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "_data" / "investigation.yml"
REGRESSIONS = ROOT / "_internal" / "accuracy-regressions.yml"
PUBLIC_CONTRACT = ROOT / "_internal" / "public-contract.yml"
LEGACY_ANCHORS = ROOT / "_data" / "legacy_anchors.yml"
TEXT_SUFFIXES = {".md", ".html", ".yml", ".yaml", ".js", ".json", ".txt", ".csv", ".css", ".svg"}
SKIP_PARTS = {".git", ".qa", "_site", "_internal", "scripts", "vendor", "node_modules"}
SKIP_FILES = {"README.md", "CLAUDE.md", "LICENSE", "Gemfile.lock"}
CORE_AMOUNT = re.compile(r"\$(?:10|15|20|25|50|55|60|65|75|100|115|125)\s*(?:M\b|million\b)", re.I)
POSITIONAL_CANONICAL = re.compile(
    r"\b(?:inv|site\.data\.investigation)\.(?:agencies|timeline|routes)\[\d+\]"
)


class Audit:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def fail(self, message: str) -> None:
        self.errors.append(message)

    def finish(self) -> None:
        if self.errors:
            print(f"AUDIT FAILED: {len(self.errors)} finding(s)", file=sys.stderr)
            for error in self.errors:
                print(f"- {error}", file=sys.stderr)
            raise SystemExit(1)
        print("AUDIT PASSED")


def public_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        rel = path.relative_to(ROOT)
        if path.name in SKIP_FILES or any(part in SKIP_PARTS for part in rel.parts):
            continue
        files.append(path)
    return sorted(files)


def line_for(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def audit_regressions(audit: Audit, files: list[Path]) -> None:
    entries = yaml.safe_load(REGRESSIONS.read_text(encoding="utf-8"))["regressions"]
    compiled = [(entry, re.compile(entry["pattern"], re.I | re.S)) for entry in entries]
    for path in files:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        for entry, pattern in compiled:
            for match in pattern.finditer(text):
                audit.fail(f"{rel}:{line_for(text, match.start())}: regression {entry['id']}: {entry['note']}")


def audit_core_amount_sources(audit: Audit, files: list[Path]) -> None:
    """Repeated investigative figures must be emitted from the canonical data model."""
    for path in files:
        if path == CANONICAL:
            continue
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        for match in CORE_AMOUNT.finditer(text):
            audit.fail(
                f"{rel}:{line_for(text, match.start())}: hardcoded core amount {match.group(0)!r}; "
                "render it from site.data.investigation"
            )
        for match in POSITIONAL_CANONICAL.finditer(text):
            audit.fail(
                f"{rel}:{line_for(text, match.start())}: positional canonical lookup {match.group(0)!r}; "
                "select canonical entries by a stable id or named field"
            )


def split_front_matter(path: Path) -> tuple[dict, str] | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return None
    match = re.match(r"^---\s*\r?\n(.*?)\r?\n---\s*\r?\n", text, re.S)
    if not match:
        return None
    data = yaml.safe_load(match.group(1)) or {}
    return data, text[match.end() :]


def content_files() -> list[Path]:
    files = [
        path
        for path in ROOT.iterdir()
        if path.is_file() and path.suffix.lower() in {".md", ".html"} and path.name not in SKIP_FILES
    ]
    files.extend((ROOT / "findings").rglob("*.md"))
    files.extend((ROOT / "documents").rglob("*.md"))
    files.append(ROOT / "assets" / "documents" / "index.html")
    return sorted(set(files))


def audit_front_matter(audit: Audit) -> None:
    for path in content_files():
        rel = path.relative_to(ROOT)
        parsed = split_front_matter(path)
        if parsed is None:
            audit.fail(f"{rel}: missing or malformed front matter")
            continue
        front, _ = parsed
        if "layout" not in front:
            audit.fail(f"{rel}: front matter lacks layout")
        if front.get("layout") is not None and not front.get("title"):
            audit.fail(f"{rel}: rendered page lacks title")
        if path.name != "index.md" or path.parent != ROOT:
            if not front.get("permalink") and path.name != "404.html":
                audit.fail(f"{rel}: public content lacks explicit permalink")
        if "documents" in rel.parts and "records" in rel.parts:
            required = {
                "source_agency",
                "source_date",
                "source_file",
                "source_locator",
                "publication_treatment",
                "asset_url",
            }
            missing = sorted(required - set(front))
            if missing:
                audit.fail(f"{rel}: source record lacks {', '.join(missing)}")


def audit_accessibility_contracts(audit: Audit) -> None:
    layout = (ROOT / "_layouts" / "default.html").read_text(encoding="utf-8")
    if 'href="#main-content"' not in layout or 'id="main-content" tabindex="-1"' not in layout:
        audit.fail("accessibility: skip link and focusable main target must remain paired")

    css = "\n".join(
        path.read_text(encoding="utf-8") for path in sorted((ROOT / "assets" / "css").glob("*.css"))
    )
    if "prefers-reduced-motion: reduce" not in css:
        audit.fail("accessibility: CSS lacks a reduced-motion mode")
    if ":focus-visible" not in css:
        audit.fail("accessibility: CSS lacks visible keyboard-focus rules")
    if re.search(r"\.container-prose\s+table\s*\{[^}]*display\s*:\s*block", css, re.S):
        audit.fail("accessibility: prose tables must not use display:block")

    take_action = (ROOT / "take-action.md").read_text(encoding="utf-8")
    if "actionnetwork.org/widgets" not in take_action or "<noscript>" not in take_action:
        audit.fail("accessibility: Take Action must retain the Action Network embed and no-JavaScript path")
    if "petition-fallback" not in take_action or "/privacy/" not in take_action:
        audit.fail("accessibility: Take Action needs an always-visible petition fallback and privacy link")
    if "source=widget" in take_action or take_action.count("source=arpensions") < 2:
        audit.fail("conversion: Action Network attribution must consistently use source=arpensions")

    privacy = (ROOT / "privacy.md").read_text(encoding="utf-8")
    if "districtfinder.youraedi.com" not in privacy or "not to this website" not in privacy:
        audit.fail("privacy: the external address-based District Finder needs a clear data boundary")
    if "linked from the [Arkansas Legislature's Legislators page]" not in take_action or "does not receive it" not in take_action:
        audit.fail("privacy: Take Action must identify the District Finder and the campaign data boundary")

    nav_js = (ROOT / "assets" / "js" / "nav.js").read_text(encoding="utf-8")
    if "nav-js" not in nav_js or "e.key === 'Tab'" not in nav_js or ".inert" not in nav_js:
        audit.fail("accessibility: mobile navigation lacks progressive enhancement or focus containment")
    if ".nav-js .nav-links" not in css:
        audit.fail("accessibility: mobile navigation has no no-JavaScript CSS fallback")

    toc_js = (ROOT / "assets" / "js" / "evidence-toc.js").read_text(encoding="utf-8")
    if "toc-js" not in toc_js or ".toc-js .evidence-toc-list" not in css:
        audit.fail("accessibility: evidence TOC lacks a no-JavaScript fallback")


def audit_canonical(audit: Audit) -> dict:
    data = yaml.safe_load(CANONICAL.read_text(encoding="utf-8"))
    agencies = {agency["id"]: agency for agency in data["agencies"]}
    metrics = data["metrics"]

    expected_floor = agencies["treasury"]["measure_millions"] + agencies["apers"]["measure_millions"]
    if metrics["confirmed_security_floor"]["value_millions"] != expected_floor:
        audit.fail("canonical: confirmed security floor does not equal Treasury plus APERS")
    expected_combined = expected_floor + agencies["atrs"]["measure_millions"]
    if metrics["combined_tied_or_funded"]["value_millions"] != expected_combined:
        audit.fail("canonical: combined tied-or-funded measure is arithmetically inconsistent")
    expected_ceiling = agencies["atrs"]["authorization_max_millions"] + agencies["apers"]["authorization_max_millions"]
    if metrics["pension_authorization_ceiling"]["value_millions"] != expected_ceiling:
        audit.fail("canonical: pension authorization ceiling is arithmetically inconsistent")
    if data["corpus"]["render_jobs_complete"] != data["corpus"]["render_jobs_total"]:
        audit.fail("canonical: render review is not complete")

    allowed_status = set(data["status_labels"])
    source_ids = set(data["sources"])
    for metric_id, metric in metrics.items():
        normalized = metric["status"].replace(" ", "_")
        if normalized not in allowed_status:
            audit.fail(f"canonical: metric {metric_id} has unknown status {metric['status']!r}")
        for source_id in metric.get("source_ids", []):
            if source_id not in source_ids:
                audit.fail(f"canonical: metric {metric_id} references unknown source {source_id}")
    for agency in data["agencies"]:
        normalized = agency["status"].replace(" ", "_")
        if normalized not in allowed_status:
            audit.fail(f"canonical: agency {agency['id']} has unknown status {agency['status']!r}")
        if not agency.get("authority_label"):
            audit.fail(f"canonical: agency {agency['id']} lacks an authorization/target label")
        for source_id in agency.get("source_ids", []):
            if source_id not in source_ids:
                audit.fail(f"canonical: agency {agency['id']} references unknown source {source_id}")
    for event in data["timeline"]:
        normalized = event["status"].replace(" ", "_")
        if normalized not in allowed_status:
            audit.fail(f"canonical: timeline event {event['id']} has unknown status {event['status']!r}")
        source_id = event.get("source_id")
        if source_id and source_id not in source_ids:
            audit.fail(f"canonical: timeline event {event['id']} references unknown source {source_id}")
    allowed_event_status = set(data["event_status_labels"])
    for route in data["routes"]:
        if route["status"] not in allowed_event_status:
            audit.fail(f"canonical: route {route['id']} has unknown event status {route['status']!r}")

    for source_id, source in data["sources"].items():
        asset_url = source.get("asset_url")
        if asset_url and not (ROOT / asset_url.lstrip("/")).is_file():
            audit.fail(f"canonical: source {source_id} points to missing asset {asset_url}")
        record_url = source.get("record_url", "")
        if record_url.startswith("/documents/records/"):
            slug = record_url.removeprefix("/documents/records/").strip("/")
            if not (ROOT / "documents" / "records" / slug / "index.md").is_file():
                audit.fail(f"canonical: source {source_id} points to missing record page {record_url}")

    timeline = {event["id"]: event for event in data["timeline"]}
    if timeline.get("atrs_authorization", {}).get("source_id") != "atrs_resolution":
        audit.fail("canonical: ATRS authorization timeline event must cite the signed resolution")
    floor_sources = set(metrics["confirmed_security_floor"].get("source_ids", []))
    if "treasury_maturity" not in floor_sources:
        audit.fail("canonical: confirmed floor must cite the subtractive Treasury maturity")

    legislation = data["legislation"]
    if "Before acquisition" not in legislation.get("full_summary", ""):
        audit.fail("canonical: policy summary must identify the pre-acquisition safeguards")
    if "within 30 days" not in legislation.get("full_summary", ""):
        audit.fail("canonical: policy summary must identify the post-acquisition publication deadline")

    terminology = yaml.safe_load((ROOT / "_data" / "terminology.yml").read_text(encoding="utf-8"))
    terminology_consumers = "\n".join(
        (ROOT / name).read_text(encoding="utf-8")
        for name in ("the-issue.md", "press.md", "_includes/jsonld.html")
    )
    if "site.data.terminology" not in terminology_consumers or not terminology.get("instrument_formal"):
        audit.fail("canonical: terminology model is not consumed by public pages")

    investigation_json = (ROOT / "assets" / "data" / "investigation.json").read_text(encoding="utf-8")
    if "site.data.investigation | jsonify" not in investigation_json:
        audit.fail("canonical: generated JSON endpoint does not derive from investigation.yml")
    facts_csv = (ROOT / "assets" / "data" / "current-facts.csv").read_text(encoding="utf-8")
    if "site.data.investigation.metrics" not in facts_csv:
        audit.fail("canonical: downloadable facts CSV does not derive from investigation.yml")
    return data


def output_target(site: Path, url_path: str) -> Path | None:
    path = unquote(url_path)
    if path == "/":
        return site / "index.html"
    candidate = site / path.lstrip("/")
    if path.endswith("/"):
        return candidate / "index.html"
    if candidate.is_file():
        return candidate
    if candidate.suffix == "":
        html_candidate = candidate.with_suffix(".html")
        if html_candidate.is_file():
            return html_candidate
        index_candidate = candidate / "index.html"
        if index_candidate.is_file():
            return index_candidate
    return None


def output_url(site: Path, path: Path) -> str:
    rel = path.relative_to(site).as_posix()
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel.removesuffix("index.html")
    return "/" + rel


def audit_public_contract(audit: Audit, site: Path, id_cache: dict[Path, set[str]]) -> None:
    contract = yaml.safe_load(PUBLIC_CONTRACT.read_text(encoding="utf-8"))
    for url in contract["routes"]:
        target = output_target(site, url)
        if target is None or not target.is_file():
            audit.fail(f"public contract: missing historical route {url}")
    for url in contract["downloads"]:
        target = output_target(site, url)
        if target is None or not target.is_file():
            audit.fail(f"public contract: missing historical download {url}")

    legacy = yaml.safe_load(LEGACY_ANCHORS.read_text(encoding="utf-8"))
    for url, anchors in legacy.items():
        target = output_target(site, url)
        if target is None or target not in id_cache:
            audit.fail(f"public contract: legacy-anchor route is missing {url}")
            continue
        missing = sorted(set(anchors) - id_cache[target])
        if missing:
            audit.fail(f"public contract: {url} lacks legacy anchors: {', '.join(missing)}")


def audit_html(audit: Audit, site: Path, data: dict) -> None:
    pages = sorted(site.rglob("*.html"))
    if not pages:
        audit.fail(f"rendered site contains no HTML: {site}")
        return

    soup_cache: dict[Path, BeautifulSoup] = {}
    id_cache: dict[Path, set[str]] = {}
    for path in pages:
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
        soup_cache[path] = soup
        ids = [tag.get("id") for tag in soup.find_all(id=True)]
        duplicates = sorted(item for item, count in Counter(ids).items() if count > 1)
        if duplicates:
            audit.fail(f"{path.relative_to(site)}: duplicate IDs: {', '.join(duplicates)}")
        id_cache[path] = set(ids)

        refresh = soup.find("meta", attrs={"http-equiv": re.compile("refresh", re.I)})
        canonical = soup.find("link", rel=lambda value: value and "canonical" in value)
        if not refresh:
            h1s = soup.find_all("h1")
            if len(h1s) != 1:
                audit.fail(f"{path.relative_to(site)}: expected one h1, found {len(h1s)}")
            heading_levels = [int(tag.name[1]) for tag in soup.find_all(re.compile(r"^h[1-6]$"))]
            for previous, current in zip(heading_levels, heading_levels[1:]):
                if current > previous + 1:
                    audit.fail(
                        f"{path.relative_to(site)}: heading level jumps from h{previous} to h{current}"
                    )
            expected_canonical = "https://arpensions.org" + output_url(site, path)
            if not canonical or str(canonical.get("href", "")) != expected_canonical:
                audit.fail(
                    f"{path.relative_to(site)}: canonical is {canonical.get('href') if canonical else None!r}, "
                    f"expected {expected_canonical!r}"
                )
        elif not canonical or not str(canonical.get("href", "")).startswith("https://arpensions.org/"):
            audit.fail(f"{path.relative_to(site)}: redirect page lacks an absolute canonical URL")

        for image in soup.find_all("img"):
            if not image.has_attr("alt"):
                audit.fail(f"{path.relative_to(site)}: image lacks alt attribute: {image.get('src')}")
        for labeled in soup.find_all(attrs={"aria-label": True}):
            if not str(labeled.get("aria-label", "")).strip():
                audit.fail(f"{path.relative_to(site)}: empty aria-label")

        jsonld_objects: list[dict] = []
        for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
            try:
                parsed_jsonld = json.loads(html.unescape(script.string or ""))
                if isinstance(parsed_jsonld, dict):
                    jsonld_objects.append(parsed_jsonld)
            except json.JSONDecodeError as exc:
                audit.fail(f"{path.relative_to(site)}: invalid JSON-LD: {exc}")
        if output_url(site, path) == "/":
            organizations = [item for item in jsonld_objects if item.get("@id") == "https://arpensions.org/#organization"]
            if not organizations or organizations[0].get("@type") != "Organization":
                audit.fail("homepage: organization JSON-LD must use the generic Organization type")

        for chart in soup.select("[data-investigation-chart]"):
            table = chart.find("table")
            if table is None:
                audit.fail(f"{path.relative_to(site)}: evidence chart lacks an HTML table fallback")
            elif table.has_attr("hidden") or table.get("aria-hidden") == "true":
                audit.fail(f"{path.relative_to(site)}: evidence chart table fallback is hidden")
        for route in soup.select(".route-map"):
            table = route.find("table")
            if table is None:
                audit.fail(f"{path.relative_to(site)}: route visualization lacks an HTML table fallback")
            elif table.has_attr("hidden") or table.get("aria-hidden") == "true":
                audit.fail(f"{path.relative_to(site)}: route visualization table fallback is hidden")

    audit_public_contract(audit, site, id_cache)

    for path, soup in soup_cache.items():
        current_url = output_url(site, path)
        for link in soup.find_all("a", href=True):
            href = str(link["href"]).strip()
            if not href or href.startswith(("mailto:", "tel:", "javascript:")):
                continue
            parsed = urlsplit(urljoin(current_url, href))
            if parsed.scheme and parsed.scheme not in {"http", "https"}:
                continue
            if parsed.netloc and parsed.netloc not in {"arpensions.org", "www.arpensions.org"}:
                continue
            target = path if not parsed.path else output_target(site, parsed.path)
            if target is None or not target.exists():
                audit.fail(f"{path.relative_to(site)}: broken internal link {href}")
                continue
            if parsed.fragment:
                if target.suffix.lower() != ".html":
                    continue
                if target not in soup_cache:
                    soup_cache[target] = BeautifulSoup(target.read_text(encoding="utf-8"), "html.parser")
                    id_cache[target] = {tag.get("id") for tag in soup_cache[target].find_all(id=True)}
                if unquote(parsed.fragment) not in id_cache[target]:
                    audit.fail(f"{path.relative_to(site)}: missing anchor in {href}")

        asset_refs: list[tuple[str, str]] = []
        for tag in soup.find_all(["img", "script", "source"]):
            for attribute in ("src", "srcset"):
                value = str(tag.get(attribute, "")).strip()
                if not value:
                    continue
                if attribute == "srcset":
                    values = [part.strip().split()[0] for part in value.split(",") if part.strip()]
                else:
                    values = [value]
                asset_refs.extend((tag.name, item) for item in values)
        for tag in soup.find_all("link", href=True):
            rel_values = set(tag.get("rel", []))
            if rel_values & {"stylesheet", "icon", "preload"}:
                asset_refs.append(("link", str(tag["href"])))

        for tag_name, reference in asset_refs:
            parsed = urlsplit(urljoin(current_url, reference))
            if parsed.scheme in {"data", "blob"}:
                continue
            if parsed.netloc and parsed.netloc not in {"arpensions.org", "www.arpensions.org"}:
                continue
            if parsed.scheme and parsed.scheme not in {"http", "https"}:
                continue
            target = output_target(site, parsed.path)
            if target is None or not target.exists():
                audit.fail(f"{path.relative_to(site)}: broken {tag_name} asset {reference}")

    homepage = (site / "index.html").read_text(encoding="utf-8")
    for metric_id in ("confirmed_security_floor", "atrs_manager_funding", "treasury_conditional_payment"):
        display = data["metrics"][metric_id]["display"]
        if display not in homepage:
            audit.fail(f"rendered homepage lacks canonical metric {metric_id}: {display}")
    if "og-default.png" not in homepage:
        audit.fail("rendered homepage does not use the replacement Open Graph image")

    rendered_json_path = site / "assets" / "data" / "investigation.json"
    try:
        rendered_data = json.loads(rendered_json_path.read_text(encoding="utf-8"))
        if rendered_data != data:
            audit.fail("rendered investigation.json does not exactly match investigation.yml")
    except (OSError, json.JSONDecodeError) as exc:
        audit.fail(f"rendered investigation.json is unreadable: {exc}")

    rendered_csv_path = site / "assets" / "data" / "current-facts.csv"
    try:
        with rendered_csv_path.open(encoding="utf-8", newline="") as handle:
            rows = {row["measure"]: row for row in csv.DictReader(handle)}
        for metric_id, metric in data["metrics"].items():
            row = rows.get(metric_id)
            if not row or row.get("value") != metric["display"] or row.get("status") != metric["status"]:
                audit.fail(f"rendered current-facts.csv is inconsistent for {metric_id}")
    except (OSError, KeyError, csv.Error) as exc:
        audit.fail(f"rendered current-facts.csv is unreadable: {exc}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", type=Path, help="Rendered Jekyll site to audit")
    args = parser.parse_args()

    audit = Audit()
    files = public_text_files()
    audit_regressions(audit, files)
    audit_core_amount_sources(audit, files)
    audit_front_matter(audit)
    audit_accessibility_contracts(audit)
    data = audit_canonical(audit)
    if args.site:
        audit_html(audit, args.site.resolve(), data)
    audit.finish()


if __name__ == "__main__":
    main()
