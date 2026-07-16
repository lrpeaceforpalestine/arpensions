"""Audit the campaign site for factual, editorial, accessibility, and build regressions."""

from __future__ import annotations

import argparse
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
LEGACY_TARGETS = ROOT / "_data" / "legacy_anchor_targets.yml"
TEXT_SUFFIXES = {".md", ".html", ".js", ".json", ".txt", ".csv", ".css", ".svg"}
SOURCE_SKIP_PARTS = {
    ".git",
    ".qa",
    "_data",
    "_internal",
    "_site",
    "node_modules",
    "scripts",
    "vendor",
}
SOURCE_SKIP_FILES = {"README.md", "CLAUDE.md", "LICENSE", "Gemfile.lock"}


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


def public_source_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        rel = path.relative_to(ROOT)
        if path.name in SOURCE_SKIP_FILES or any(part in SOURCE_SKIP_PARTS for part in rel.parts):
            continue
        files.append(path)
    return sorted(files)


def rendered_text_files(site: Path) -> list[Path]:
    return sorted(
        path for path in site.rglob("*") if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES
    )


def line_for(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def audit_regressions(audit: Audit, files: list[Path], *, rendered: bool) -> None:
    entries = yaml.safe_load(REGRESSIONS.read_text(encoding="utf-8"))["regressions"]
    for entry in entries:
        if entry.get("scope") == "rendered" and not rendered:
            continue
        pattern = re.compile(entry["pattern"], re.I | re.S)
        for path in files:
            text = path.read_text(encoding="utf-8")
            for match in pattern.finditer(text):
                try:
                    rel = path.relative_to(ROOT)
                except ValueError:
                    rel = path
                audit.fail(
                    f"{rel}:{line_for(text, match.start())}: regression {entry['id']}: {entry['note']}"
                )


def split_front_matter(path: Path) -> tuple[dict, str] | None:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\r?\n(.*?)\r?\n---\s*\r?\n", text, re.S)
    if not match:
        return None
    return yaml.safe_load(match.group(1)) or {}, text[match.end() :]


def content_files() -> list[Path]:
    files = [
        path
        for path in ROOT.iterdir()
        if path.is_file() and path.suffix.lower() in {".md", ".html"} and path.name not in SOURCE_SKIP_FILES
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
        if path != ROOT / "index.md" and path.name != "404.html" and not front.get("permalink"):
            audit.fail(f"{rel}: public content lacks an explicit permalink")
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


def audit_canonical(audit: Audit) -> dict:
    data = yaml.safe_load(CANONICAL.read_text(encoding="utf-8"))
    agencies = {agency["id"]: agency for agency in data["agencies"]}
    metrics = data["metrics"]

    floor = agencies["treasury"]["measure_millions"] + agencies["apers"]["measure_millions"]
    if metrics["confirmed_security_floor"]["value_millions"] != floor:
        audit.fail("canonical: completed-purchase floor must equal Treasury plus APERS")
    combined = floor + agencies["atrs"]["measure_millions"]
    if metrics["combined_tied_or_funded"]["value_millions"] != combined:
        audit.fail("canonical: combined purchase-and-funding figure is arithmetically inconsistent")
    ceiling = agencies["atrs"]["authorization_max_millions"] + agencies["apers"]["authorization_max_millions"]
    if metrics["pension_authorization_ceiling"]["value_millions"] != ceiling:
        audit.fail("canonical: pension authorization ceiling is arithmetically inconsistent")

    source_ids = set(data["sources"])
    allowed_status = set(data["status_labels"])
    allowed_route_status = set(data["event_status_labels"])
    for metric_id, metric in metrics.items():
        if metric["status"].replace(" ", "_") not in allowed_status:
            audit.fail(f"canonical: metric {metric_id} has unknown status {metric['status']!r}")
        for source_id in metric.get("source_ids", []):
            if source_id not in source_ids:
                audit.fail(f"canonical: metric {metric_id} references unknown source {source_id}")
    for agency in data["agencies"]:
        for source_id in agency.get("source_ids", []):
            if source_id not in source_ids:
                audit.fail(f"canonical: agency {agency['id']} references unknown source {source_id}")
    for event in data["timeline"]:
        source_id = event.get("source_id")
        if source_id and source_id not in source_ids:
            audit.fail(f"canonical: timeline event {event['id']} references unknown source {source_id}")
    for route in data["routes"]:
        if route["status"] not in allowed_route_status:
            audit.fail(f"canonical: route {route['id']} has unknown status {route['status']!r}")

    for source_id, source in data["sources"].items():
        missing = sorted({"title", "agency", "date", "locator"} - set(source))
        if missing:
            audit.fail(f"canonical: source {source_id} lacks {', '.join(missing)}")
        asset_url = source.get("asset_url")
        if asset_url and not (ROOT / asset_url.lstrip("/")).is_file():
            audit.fail(f"canonical: source {source_id} points to missing asset {asset_url}")
        record_url = source.get("record_url", "")
        if record_url.startswith("/documents/records/"):
            slug = record_url.removeprefix("/documents/records/").strip("/")
            if not (ROOT / "documents" / "records" / slug / "index.md").is_file():
                audit.fail(f"canonical: source {source_id} points to missing record page {record_url}")

    return data


def audit_source_contracts(audit: Audit) -> None:
    default = (ROOT / "_layouts" / "default.html").read_text(encoding="utf-8")
    nav = (ROOT / "_includes" / "nav.html").read_text(encoding="utf-8")
    head = (ROOT / "_includes" / "head.html").read_text(encoding="utf-8")
    css = "\n".join(path.read_text(encoding="utf-8") for path in (ROOT / "assets" / "css").glob("*.css"))
    js = "\n".join(path.read_text(encoding="utf-8") for path in (ROOT / "assets" / "js").rglob("*.js"))

    if 'href="#main-content"' not in default or 'id="main-content" tabindex="-1"' not in default:
        audit.fail("accessibility: skip link and focusable main target must remain paired")
    if "prefers-reduced-motion: reduce" not in css:
        audit.fail("accessibility: CSS lacks a reduced-motion mode")
    if ":focus-visible" not in css:
        audit.fail("accessibility: CSS lacks visible keyboard-focus rules")
    if "@media (max-width: 768px)" not in css or ".nav-toggle" not in css:
        audit.fail("responsive: mobile navigation styles are missing")
    if "html:not(.nav-js) .nav-links" not in css:
        audit.fail("accessibility: mobile navigation has no no-JavaScript fallback")
    if "nav-js" not in js or "e.key === 'Tab'" not in js or ".inert" not in js:
        audit.fail("accessibility: mobile navigation lacks progressive enhancement or focus containment")
    if "Avenir Next" not in css or "League Spartan" not in css or "family=League+Spartan" not in head:
        audit.fail("brand: the original Avenir/League Spartan type system is not intact")
    take_action_link = re.search(r'<a[^>]+href="\{\{ \'/take-action/\'[^>]+>(?:\s*)Take Action', nav)
    if not take_action_link or re.search(r'<a[^>]+href="\{\{ \'/take-action/\'[^>]+class="[^"]*(?:btn|cta)', nav):
        audit.fail("brand: the desktop Take Action navigation item must remain a normal nav link")

    if (ROOT / "assets" / "css" / "evidence-led.css").exists():
        audit.fail("editorial: the rejected evidence-led redesign stylesheet must not return")
    for endpoint in (ROOT / "assets" / "data" / "investigation.json", ROOT / "assets" / "data" / "current-facts.csv"):
        if endpoint.exists():
            audit.fail(f"editorial: internal research data must not be published at {endpoint.relative_to(ROOT)}")

    evidence = (ROOT / "evidence.md").read_text(encoding="utf-8")
    issue = (ROOT / "the-issue.md").read_text(encoding="utf-8")
    for token in ("scrollytelling: true", "charts: true", "apexcharts: true", 'class="scrolly"', 'id="exposure-chart"', 'id="decision-window-chart"'):
        if token not in evidence:
            audit.fail(f"interaction: Evidence is missing {token}")
    for token in ("d3sankey: true", 'id="influence-sankey"', 'class="visual-fallback"'):
        if token not in issue:
            audit.fail(f"interaction: The Issue is missing {token}")
    for asset in (
        "charts.js",
        "decision-window.js",
        "influence-sankey.js",
        "scrollytelling.js",
        "timeline-thread.js",
        "vendor/scrollama.min.js",
    ):
        if not (ROOT / "assets" / "js" / asset).is_file():
            audit.fail(f"interaction: missing restored JavaScript asset assets/js/{asset}")

    take_action = (ROOT / "take-action.md").read_text(encoding="utf-8")
    if "actionnetwork.org/widgets" not in take_action or "<noscript>" not in take_action:
        audit.fail("conversion: Take Action must retain the Action Network embed and no-JavaScript path")
    if "petition-fallback" not in take_action or "/privacy/" not in take_action:
        audit.fail("conversion: Take Action needs a visible direct petition path and privacy link")
    if "source=widget" in take_action or take_action.count("source=arpensions") < 2:
        audit.fail("conversion: Action Network attribution must use source=arpensions")


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
    targets = yaml.safe_load(LEGACY_TARGETS.read_text(encoding="utf-8"))
    for url, anchors in legacy.items():
        target = output_target(site, url)
        if target is None or target not in id_cache:
            audit.fail(f"public contract: legacy-anchor route is missing {url}")
            continue
        missing = sorted(set(anchors) - id_cache[target])
        if missing:
            audit.fail(f"public contract: {url} lacks legacy anchors: {', '.join(missing)}")
        mapping = targets.get(url, {})
        missing_mappings = sorted(set(anchors) - set(mapping))
        if missing_mappings:
            audit.fail(f"public contract: {url} lacks legacy target mappings: {', '.join(missing_mappings)}")


def audit_html(audit: Audit, site: Path, data: dict) -> None:
    pages = sorted(site.rglob("*.html"))
    if not pages:
        audit.fail(f"rendered site contains no HTML: {site}")
        return

    soup_cache: dict[Path, BeautifulSoup] = {}
    id_cache: dict[Path, set[str]] = {}
    for path in pages:
        raw = path.read_text(encoding="utf-8")
        soup = BeautifulSoup(raw, "html.parser")
        soup_cache[path] = soup
        ids = [tag.get("id") for tag in soup.find_all(id=True)]
        duplicates = sorted(item for item, count in Counter(ids).items() if count > 1)
        if duplicates:
            audit.fail(f"{path.relative_to(site)}: duplicate IDs: {', '.join(duplicates)}")
        id_cache[path] = set(ids)

        refresh = soup.find("meta", attrs={"http-equiv": re.compile("refresh", re.I)})
        canonical = soup.find("link", rel=lambda value: value and "canonical" in value)
        titles = soup.find_all("title")
        if len(titles) != 1:
            audit.fail(f"{path.relative_to(site)}: expected one title, found {len(titles)}")
        elif len(titles[0].get_text(strip=True)) > 120:
            audit.fail(f"{path.relative_to(site)}: title exceeds 120 characters")
        if not refresh:
            h1s = soup.find_all("h1")
            if len(h1s) != 1:
                audit.fail(f"{path.relative_to(site)}: expected one h1, found {len(h1s)}")
            levels = [int(tag.name[1]) for tag in soup.find_all(re.compile(r"^h[1-6]$"))]
            for previous, current in zip(levels, levels[1:]):
                if current > previous + 1:
                    audit.fail(f"{path.relative_to(site)}: heading jumps from h{previous} to h{current}")
            expected = "https://arpensions.org" + output_url(site, path)
            if not canonical or canonical.get("href") != expected:
                audit.fail(f"{path.relative_to(site)}: canonical URL does not match {expected}")
        elif not canonical or not str(canonical.get("href", "")).startswith("https://arpensions.org/"):
            audit.fail(f"{path.relative_to(site)}: redirect page lacks an absolute campaign canonical URL")

        visible_text = soup.get_text("\n")
        if re.search(r"(?:^|\n)\s*#{1,6}\s+\S", visible_text):
            audit.fail(f"{path.relative_to(site)}: literal Markdown heading leaked into rendered copy")
        for image in soup.find_all("img"):
            if not image.has_attr("alt"):
                audit.fail(f"{path.relative_to(site)}: image lacks alt text: {image.get('src')}")
        for labeled in soup.find_all(attrs={"aria-label": True}):
            if not str(labeled.get("aria-label", "")).strip():
                audit.fail(f"{path.relative_to(site)}: empty aria-label")

        for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
            try:
                json.loads(html.unescape(script.string or ""))
            except json.JSONDecodeError as exc:
                audit.fail(f"{path.relative_to(site)}: invalid JSON-LD: {exc}")

    audit_public_contract(audit, site, id_cache)

    for path, soup in soup_cache.items():
        current_url = output_url(site, path)
        for link in soup.find_all("a", href=True):
            href = str(link["href"]).strip()
            if not href or href.startswith(("mailto:", "tel:", "javascript:")):
                continue
            parsed = urlsplit(urljoin(current_url, href))
            if parsed.netloc and parsed.netloc not in {"arpensions.org", "www.arpensions.org"}:
                continue
            if parsed.scheme and parsed.scheme not in {"http", "https"}:
                continue
            target = path if not parsed.path else output_target(site, parsed.path)
            if target is None or not target.exists():
                audit.fail(f"{path.relative_to(site)}: broken internal link {href}")
                continue
            if parsed.fragment and target.suffix.lower() == ".html":
                if unquote(parsed.fragment) not in id_cache.get(target, set()):
                    audit.fail(f"{path.relative_to(site)}: missing anchor in {href}")

        asset_refs: list[tuple[str, str]] = []
        for tag in soup.find_all(["img", "script", "source"]):
            for attribute in ("src", "srcset"):
                value = str(tag.get(attribute, "")).strip()
                if not value:
                    continue
                values = [part.strip().split()[0] for part in value.split(",")] if attribute == "srcset" else [value]
                asset_refs.extend((tag.name, item) for item in values if item)
        for tag in soup.find_all("link", href=True):
            if set(tag.get("rel", [])) & {"stylesheet", "icon", "preload"}:
                asset_refs.append(("link", str(tag["href"])))
        for tag_name, reference in asset_refs:
            parsed = urlsplit(urljoin(current_url, reference))
            if parsed.scheme in {"data", "blob"}:
                continue
            if parsed.netloc and parsed.netloc not in {"arpensions.org", "www.arpensions.org"}:
                continue
            target = output_target(site, parsed.path)
            if target is None or not target.exists():
                audit.fail(f"{path.relative_to(site)}: broken {tag_name} asset {reference}")

    homepage = soup_cache[site / "index.html"]
    if "Arkansans for Pension Integrity" not in homepage.get_text(" "):
        audit.fail("homepage: campaign identity is missing")
    take_action = next((a for a in homepage.select(".nav-links a") if a.get_text(" ", strip=True) == "Take Action"), None)
    if not take_action or any(name in take_action.get("class", []) for name in ("btn-primary", "nav-cta", "cta")):
        audit.fail("homepage: Take Action must be an ordinary navigation link")
    home_raw = (site / "index.html").read_text(encoding="utf-8")
    for metric_id in ("confirmed_security_floor", "atrs_manager_funding", "treasury_conditional_payment"):
        display = data["metrics"][metric_id]["display"]
        if display not in home_raw and display.lstrip("+") not in home_raw:
            audit.fail(f"homepage: canonical figure {metric_id} ({display}) is missing")

    evidence = soup_cache.get(site / "evidence" / "index.html")
    if evidence:
        required = {
            ".scrolly": "scrollytelling",
            "#exposure-chart": "exposure chart",
            "#decision-window-chart": "decision timeline",
            ".timeline-wrapper": "event timeline",
        }
        for selector, label in required.items():
            if not evidence.select_one(selector):
                audit.fail(f"evidence: restored {label} is missing")
        scripts = " ".join(str(tag.get("src", "")) for tag in evidence.find_all("script"))
        for name in ("charts.js", "decision-window.js", "scrollytelling.js", "timeline-thread.js"):
            if name not in scripts:
                audit.fail(f"evidence: restored script {name} is missing")
        if not evidence.select_one("#exposure-chart") or not evidence.select_one(".issue-agency-table table"):
            audit.fail("evidence: exposure chart lacks its readable table")

    issue = soup_cache.get(site / "the-issue" / "index.html")
    if issue:
        if not issue.select_one("#influence-sankey"):
            audit.fail("the issue: restored route graphic is missing")
        scripts = " ".join(str(tag.get("src", "")) for tag in issue.find_all("script"))
        if "influence-sankey.js" not in scripts:
            audit.fail("the issue: restored route graphic script is missing")
        if not issue.select_one(".visual-fallback table"):
            audit.fail("the issue: route graphic lacks a readable table")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", type=Path, help="Rendered Jekyll site to audit")
    args = parser.parse_args()

    audit = Audit()
    source_files = public_source_files()
    audit_regressions(audit, source_files, rendered=False)
    audit_front_matter(audit)
    data = audit_canonical(audit)
    audit_source_contracts(audit)
    if args.site:
        site = args.site.resolve()
        audit_regressions(audit, rendered_text_files(site), rendered=True)
        audit_html(audit, site, data)
    audit.finish()


if __name__ == "__main__":
    main()
