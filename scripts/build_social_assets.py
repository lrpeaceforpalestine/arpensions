"""Generate the campaign's default social preview image."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "images" / "og-default.png"

PINE = "#013237"
PINE_DEEP = "#001E22"
PINE_LIGHT = "#074750"
MINT = "#E6F9E4"
MINT_SOFT = "#C0E7BA"
JADE = "#5FBF8B"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    filename = "arialbd.ttf" if bold else "arial.ttf"
    path = Path(r"C:\Windows\Fonts") / filename
    if path.exists():
        return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def draw_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    value: str,
    size: int,
    color: str,
    *,
    bold: bool = False,
    spacing: int = 4,
) -> None:
    draw.multiline_text(xy, value, fill=color, font=font(size, bold), spacing=spacing)


def main() -> None:
    canvas = Image.new("RGB", (1200, 630), PINE_DEEP)
    draw = ImageDraw.Draw(canvas)

    # Banknote-like linework echoes the existing campaign identity without
    # turning the preview into a data card.
    for row in range(28):
        points = []
        for x in range(-40, 1241, 8):
            y = 20 + row * 23 + 10 * math.sin((x / 62) + row * 0.55)
            points.append((x, y))
        draw.line(points, fill=PINE_LIGHT, width=1)

    draw.rounded_rectangle((34, 34, 1166, 596), radius=24, fill=PINE, outline=JADE, width=3)
    draw.line((74, 168, 1126, 168), fill=MINT_SOFT, width=1)

    badge = Image.open(ROOT / "assets" / "images" / "api-badge-512.png").convert("RGBA")
    badge.thumbnail((92, 92))
    canvas.paste(badge, (76, 64), badge)

    draw_text(draw, (190, 79), "ARKANSANS FOR", 24, MINT_SOFT, bold=True)
    draw_text(draw, (190, 113), "PENSION INTEGRITY", 32, MINT, bold=True)

    draw_text(
        draw,
        (78, 222),
        "PUBLIC MONEY DESERVES\nA PUBLIC INVESTMENT\nRECORD.",
        58,
        MINT,
        bold=True,
        spacing=9,
    )

    draw_text(draw, (82, 487), "They're messing with your money.", 25, JADE, bold=False)
    draw_text(draw, (82, 540), "ARPENSIONS.ORG", 22, MINT_SOFT, bold=True)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(OUTPUT, format="PNG", optimize=True)


if __name__ == "__main__":
    main()
