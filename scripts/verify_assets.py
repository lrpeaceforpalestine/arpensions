"""Verify the campaign QR payload, Open Graph dimensions, and source excerpts."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
from urllib.request import Request, urlopen

import fitz
import yaml
import zxingcpp
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_QR_PAYLOAD = "https://qr.generatorqr.com/3drm7MQpG"
EXPECTED_QR_DESTINATION = "https://arpensions.org"
ASSET_MANIFEST = ROOT / "_internal" / "source-assets.yml"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--live", action="store_true", help="Resolve the QR redirect over the network")
    args = parser.parse_args()

    errors: list[str] = []
    data = yaml.safe_load((ROOT / "_data" / "investigation.yml").read_text(encoding="utf-8"))
    manifest = yaml.safe_load(ASSET_MANIFEST.read_text(encoding="utf-8"))["sources"]

    og = Image.open(ROOT / "assets" / "images" / "og-default.png")
    if og.size != (1200, 630):
        errors.append(f"Open Graph image is {og.size}, expected 1200x630")

    for name in ("banknote-share.jpg", "banknote-share.webp"):
        image = Image.open(ROOT / "assets" / "images" / name)
        payloads = [result.text for result in zxingcpp.read_barcodes(image)]
        if EXPECTED_QR_PAYLOAD not in payloads:
            errors.append(f"{name} does not contain the preserved QR payload")

    for source_id, source in data["sources"].items():
        asset_url = source.get("asset_url")
        if not asset_url:
            continue
        path = ROOT / asset_url.lstrip("/")
        try:
            document = fitz.open(path)
            expected_pages = source.get("expected_pages")
            manifest_entry = manifest.get(source_id)
            if not manifest_entry:
                errors.append(f"{source_id} excerpt is missing from the source-asset manifest")
            elif manifest_entry.get("pages") != expected_pages:
                errors.append(f"{source_id} canonical and manifest page counts disagree")
            if len(document) != expected_pages:
                errors.append(f"{source_id} excerpt has {len(document)} pages; expected {expected_pages}")
            for page in document:
                if page.rect.width <= 0 or page.rect.height <= 0:
                    errors.append(f"{source_id} excerpt has an invalid page rectangle")
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            if manifest_entry and digest != manifest_entry.get("sha256"):
                errors.append(f"{source_id} excerpt hash differs from the visually reviewed artifact")
        except Exception as exc:  # pragma: no cover - diagnostic path
            errors.append(f"{source_id} excerpt is not a readable PDF: {exc}")

    asset_sources = {source_id for source_id, source in data["sources"].items() if source.get("asset_url")}
    unknown_manifest = sorted(set(manifest) - asset_sources)
    if unknown_manifest:
        errors.append(f"source-asset manifest contains unknown entries: {', '.join(unknown_manifest)}")

    if args.live:
        try:
            request = Request(
                EXPECTED_QR_PAYLOAD.rstrip("/") + "/go",
                headers={"User-Agent": "Mozilla/5.0 (compatible; arpensions asset audit)"},
            )
            with urlopen(request, timeout=15) as response:
                terminal = response.geturl().rstrip("/")
            if terminal != EXPECTED_QR_DESTINATION:
                errors.append(f"QR redirect resolves to {terminal}, expected {EXPECTED_QR_DESTINATION}")
        except Exception as exc:  # pragma: no cover - network diagnostic path
            errors.append(f"QR redirect could not be resolved: {exc}")

    if errors:
        raise SystemExit("ASSET AUDIT FAILED\n- " + "\n- ".join(errors))
    live_note = f" · destination={EXPECTED_QR_DESTINATION}" if args.live else ""
    print(f"ASSET AUDIT PASSED · QR={EXPECTED_QR_PAYLOAD}{live_note} · OG={og.size[0]}x{og.size[1]}")


if __name__ == "__main__":
    main()
