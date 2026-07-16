"""Audit public source and rendered Jekyll output for evidence and HTML regressions."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "_data" / "investigation.yml"
REGRESSIONS = ROOT / "_internal" / "accuracy-regressions.yml"
TEXT_SUFFIXES = {".md", ".html", ".yml", ".yaml", ".js", ".json", ".txt", ".css", ".svg"}
SKIP_PARTS = {".git", ".qa", "_site", "_internal", "scripts", "vendor", "node_modules"}
SKIP_FILES = {"README.md", "CLAUDE.md", "LICENSE", "Gemfile.lock"}
CORE_AMOUNT = re.compile(r"\$(?:10|15|20|25|50|55|60|65|75|100|115|125)\s*(?:M\b|million\b)", re.I)


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

    take_action = (ROOT / "take-action.md").read_text(encoding="utf-8")
    if "actionnetwork.org/widgets" not in take_action or "<noscript>" not in take_action:
        audit.fail("accessibility: Take Action must retain the Action Network embed and no-JavaScript path")


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
    for agency in data["agencies"]:
        normalized = agency["status"].replace(" ", "_")
        if normalized not in allowed_status:
            audit.fail(f"canonical: agency {agency['id']} has unknown status {agency['status']!r}")
    for event in data["timeline"]:
        normalized = event["status"].replace(" ", "_")
        if normalized not in allowed_status:
            audit.fail(f"canonical: timeline event {event['id']} has unknown status {event['status']!r}")
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

    investigation_json = (ROOT / "assets" / "data" / "investigation.json").read_text(encoding="utf-8")
    if "site.data.investigation | jsonify" not in investigation_json:
        audit.fail("canonical: generated JSON endpoint does not derive from investigation.yml")
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
            canonical = soup.find("link", rel=lambda value: value and "canonical" in value)
            if not canonical or not str(canonical.get("href", "")).startswith("https://arpensions.org"):
                audit.fail(f"{path.relative_to(site)}: missing absolute canonical URL")

        for image in soup.find_all("img"):
            if not image.has_attr("alt"):
                audit.fail(f"{path.relative_to(site)}: image lacks alt attribute: {image.get('src')}")
        for labeled in soup.find_all(attrs={"aria-label": True}):
            if not str(labeled.get("aria-label", "")).strip():
                audit.fail(f"{path.relative_to(site)}: empty aria-label")

        for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
            try:
                json.loads(html.unescape(script.string or ""))
            except json.JSONDecodeError as exc:
                audit.fail(f"{path.relative_to(site)}: invalid JSON-LD: {exc}")

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

    for path, soup in soup_cache.items():
        for link in soup.find_all("a", href=True):
            href = str(link["href"]).strip()
            if not href or href.startswith(("mailto:", "tel:", "javascript:")):
                continue
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc:
                continue
            if parsed.path and not parsed.path.startswith("/"):
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

    homepage = (site / "index.html").read_text(encoding="utf-8")
    for metric_id in ("confirmed_security_floor", "atrs_manager_funding", "treasury_conditional_payment"):
        display = data["metrics"][metric_id]["display"]
        if display not in homepage:
            audit.fail(f"rendered homepage lacks canonical metric {metric_id}: {display}")
    if "og-default.png" not in homepage:
        audit.fail("rendered homepage does not use the replacement Open Graph image")


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
