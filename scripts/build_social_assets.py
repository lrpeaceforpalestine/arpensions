"""Generate social preview assets from the canonical investigation data."""

from __future__ import annotations

import math
from pathlib import Path

import yaml
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "_data" / "investigation.yml"
OUTPUT = ROOT / "assets" / "images" / "og-default.png"

PINE = "#013237"
PINE_2 = "#074750"
MINT = "#E6F9E4"
MINT_2 = "#C0E7BA"
JADE = "#48A46D"
GOLD = "#EAB85D"
INK = "#152019"
WHITE = "#FFFFFF"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    name = "arialbd.ttf" if bold else "arial.ttf"
    path = Path(r"C:\Windows\Fonts") / name
    if path.exists():
        return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def text(draw: ImageDraw.ImageDraw, xy: tuple[int, int], value: str, size: int, color: str, bold: bool = False) -> None:
    draw.text(xy, value, fill=color, font=font(size, bold=bold))


def ledger_row(draw: ImageDraw.ImageDraw, y: int, amount: str, status: str, label: str, accent: str) -> None:
    draw.rounded_rectangle((742, y, 1122, y + 112), radius=12, fill=WHITE, outline=MINT_2, width=2)
    draw.rectangle((742, y, 750, y + 112), fill=accent)
    text(draw, (774, y + 15), status.upper(), 16, accent, bold=True)
    text(draw, (774, y + 41), amount, 42, PINE, bold=True)
    text(draw, (930, y + 57), label, 19, INK)


def main() -> None:
    data = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    metrics = data["metrics"]
    canvas = Image.new("RGB", (1200, 630), PINE)
    draw = ImageDraw.Draw(canvas)

    # Quiet guilloche field, echoing the campaign's banknote identity.
    for i in range(18):
        points = []
        for x in range(-20, 1221, 8):
            y = 40 + i * 32 + 11 * math.sin((x / 58) + i * 0.72)
            points.append((x, y))
        draw.line(points, fill=PINE_2, width=2)

    draw.rounded_rectangle((26, 26, 1174, 604), radius=24, outline=MINT_2, width=3)
    draw.rounded_rectangle((50, 50, 700, 580), radius=16, fill=PINE, outline=JADE, width=2)

    badge = Image.open(ROOT / "assets" / "images" / "api-badge-512.png").convert("RGBA")
    badge.thumbnail((86, 86))
    canvas.paste(badge, (82, 82), badge)
    text(draw, (188, 90), "ARKANSANS FOR", 19, MINT_2, bold=True)
    text(draw, (188, 120), "PENSION INTEGRITY", 25, WHITE, bold=True)

    headline = ["PUBLIC MONEY", "DESERVES A PUBLIC", "INVESTMENT RECORD."]
    for line, y in zip(headline, (220, 286, 352)):
        text(draw, (82, y), line, 52, WHITE, bold=True)

    text(draw, (84, 472), "Evidence-led. Issuer-neutral. Built from public records.", 22, MINT_2)
    text(draw, (84, 526), "arpensions.org", 26, WHITE, bold=True)

    draw.rounded_rectangle((720, 50, 1150, 580), radius=16, fill=MINT, outline=JADE, width=2)
    text(draw, (752, 80), "ARKANSAS PUBLIC", 18, PINE_2, bold=True)
    text(draw, (752, 108), "INVESTMENT LEDGER", 26, PINE, bold=True)
    text(draw, (752, 145), f"Evidence baseline · {data['updated_at']}", 15, PINE_2)

    ledger_row(
        draw,
        190,
        metrics["confirmed_security_floor"]["display"],
        metrics["confirmed_security_floor"]["status"],
        "confirmed securities",
        JADE,
    )
    ledger_row(
        draw,
        316,
        metrics["atrs_manager_funding"]["display"],
        metrics["atrs_manager_funding"]["status"],
        "ATRS manager funding",
        PINE_2,
    )
    ledger_row(
        draw,
        442,
        metrics["treasury_conditional_payment"]["display"],
        metrics["treasury_conditional_payment"]["status"],
        "payment in process",
        GOLD,
    )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(OUTPUT, format="PNG", optimize=True)


if __name__ == "__main__":
    main()
