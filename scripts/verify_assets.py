"""Verify the campaign QR payload, Open Graph dimensions, and source excerpts."""

from __future__ import annotations

from pathlib import Path

import fitz
import yaml
import zxingcpp
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_QR_PAYLOAD = "https://qr.generatorqr.com/3drm7MQpG"


def main() -> None:
    errors: list[str] = []
    data = yaml.safe_load((ROOT / "_data" / "investigation.yml").read_text(encoding="utf-8"))

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
            if len(document) < 1:
                errors.append(f"{source_id} excerpt has no pages")
            for page in document:
                if page.rect.width <= 0 or page.rect.height <= 0:
                    errors.append(f"{source_id} excerpt has an invalid page rectangle")
        except Exception as exc:  # pragma: no cover - diagnostic path
            errors.append(f"{source_id} excerpt is not a readable PDF: {exc}")

    if errors:
        raise SystemExit("ASSET AUDIT FAILED\n- " + "\n- ".join(errors))
    print(f"ASSET AUDIT PASSED · QR={EXPECTED_QR_PAYLOAD} · OG={og.size[0]}x{og.size[1]}")


if __name__ == "__main__":
    main()
