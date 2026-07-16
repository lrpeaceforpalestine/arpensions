"""Build privacy-reviewed publication excerpts from the preserved investigation corpus.

The source corpus is external to this website repository and remains unchanged.
Run locally with PyMuPDF, Pillow, and BeautifulSoup installed.
"""

from __future__ import annotations

import argparse
import email
import os
from email import policy
from email.utils import getaddresses, parseaddr
from pathlib import Path
from textwrap import wrap

import fitz
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from PIL import Image, ImageDraw, ImageFont


DEFAULT_CORPUS = Path(os.environ.get("ISRAEL_BONDS_CORPUS", r"D:\israel-bonds-wiki"))
DEFAULT_OUTPUT = Path(__file__).resolve().parents[1] / "assets" / "documents"
PINE = "#013237"
INK = "#152019"
MINT = "#E6F9E4"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    name = "arialbd.ttf" if bold else "arial.ttf"
    path = Path(r"C:\Windows\Fonts") / name
    if path.exists():
        return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def render_page(
    source: Path,
    page_number: int,
    *,
    clip: tuple[float, float, float, float] | None = None,
    masks: tuple[tuple[float, float, float, float], ...] = (),
    dpi: int = 180,
) -> Image.Image:
    """Render a physical PDF page and irreversibly apply publication masks."""
    document = fitz.open(source)
    page = document[page_number - 1]
    page_clip = fitz.Rect(clip) if clip else page.rect
    scale = dpi / 72
    pixmap = page.get_pixmap(matrix=fitz.Matrix(scale, scale), clip=page_clip, alpha=False)
    image = Image.frombytes("RGB", (pixmap.width, pixmap.height), pixmap.samples)
    draw = ImageDraw.Draw(image)
    for x0, y0, x1, y1 in masks:
        box = (
            round((x0 - page_clip.x0) * scale),
            round((y0 - page_clip.y0) * scale),
            round((x1 - page_clip.x0) * scale),
            round((y1 - page_clip.y0) * scale),
        )
        draw.rectangle(box, fill="black")
    document.close()
    return image


def add_provenance(image: Image.Image, source_label: str, masking: str) -> Image.Image:
    footer_height = 104
    canvas = Image.new("RGB", (image.width, image.height + footer_height), "white")
    canvas.paste(image, (0, 0))
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((0, image.height, image.width, image.height + 7), fill=PINE)
    draw.text((24, image.height + 20), source_label, fill=INK, font=font(16, bold=True))
    draw.text((24, image.height + 54), masking, fill=PINE, font=font(15))
    return canvas


def save_pdf(images: list[Image.Image], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    first, *rest = [image.convert("RGB") for image in images]
    first.save(destination, "PDF", resolution=180, save_all=True, append_images=rest)


def source_excerpt(
    source: Path,
    pages: list[int],
    destination: Path,
    *,
    clips: dict[int, tuple[float, float, float, float]] | None = None,
    masks: dict[int, tuple[tuple[float, float, float, float], ...]] | None = None,
    masking_note: str = "Campaign excerpt; no campaign masking applied.",
) -> None:
    clips = clips or {}
    masks = masks or {}
    rendered: list[Image.Image] = []
    for physical_page in pages:
        image = render_page(
            source,
            physical_page,
            clip=clips.get(physical_page),
            masks=masks.get(physical_page, ()),
        )
        rendered.append(
            add_provenance(
                image,
                f"Source: {source.name} · physical PDF page {physical_page}",
                masking_note,
            )
        )
    save_pdf(rendered, destination)


def funding_email_excerpt(source: Path, destination: Path) -> None:
    message = email.message_from_bytes(source.read_bytes(), policy=policy.default)
    html = message.get_body(preferencelist=("html",))
    body = BeautifulSoup(html.get_content(), "html.parser").get_text(" ", strip=True)
    marker = "December payments since the last Board update"
    start = body.index(marker)
    end = body.index("Please let me know", start)
    excerpt = body[start:end].strip()

    width, height = 1275, 1650
    page = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(page)
    draw.rectangle((0, 0, width, 20), fill=PINE)
    draw.text((78, 72), "ATRS BOARD UPDATE · LIQUIDITY", fill=PINE, font=font(34, bold=True))
    draw.text((78, 142), "Publication excerpt from an agency-produced email", fill=INK, font=font(22))

    from_name = parseaddr(str(message["From"]))[0]
    to_names = ", ".join(name for name, _ in getaddresses([str(message["To"])]))
    cc_names = ", ".join(name for name, _ in getaddresses([str(message["Cc"])]))
    metadata = [
        f"From: {from_name}",
        f"To: {to_names}",
        f"Cc: {cc_names}",
        f"Date: {message['Date']}",
        f"Subject: {str(message['Subject']).replace(chr(0), '').strip()}",
    ]
    y = 230
    for line in metadata:
        draw.text((78, y), line, fill=INK, font=font(21))
        y += 40

    draw.rectangle((78, y + 22, width - 78, y + 29), fill=MINT)
    y += 90
    for paragraph in excerpt.split(". "):
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        if not paragraph.endswith("."):
            paragraph += "."
        for line in wrap(paragraph, width=84):
            draw.text((92, y), line, fill=INK, font=font(24))
            y += 38
        y += 24

    draw.rectangle((0, height - 150, width, height), fill=PINE)
    draw.text(
        (78, height - 118),
        f"Source: {source.name} · email body · produced by the Auditor of State",
        fill="white",
        font=font(18, bold=True),
    )
    draw.text(
        (78, height - 76),
        "Campaign typeset excerpt; recipient addresses and unrelated notice text omitted.",
        fill=MINT,
        font=font(18),
    )
    save_pdf([page], destination)


def treasury_maturity_excerpt(source: Path, destination: Path) -> None:
    """Typeset the publication-safe fields from the produced cash-flow workbook."""
    workbook = load_workbook(source, data_only=True, read_only=True)
    sheet = workbook["Sheet1"]
    transaction_type = sheet["B14"].value
    security_type = sheet["C14"].value
    description = sheet["D14"].value
    post_date = sheet["G14"].value
    amount = sheet["H14"].value
    report_period = sheet["B4"].value

    if transaction_type != "Final Maturity" or amount != 5_000_000:
        raise ValueError("Treasury maturity source no longer matches the reviewed row 14 record")

    width, height = 1275, 1650
    page = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(page)
    draw.rectangle((0, 0, width, 20), fill=PINE)
    draw.text((78, 72), "TREASURY FINAL-MATURITY RECORD", fill=PINE, font=font(34, bold=True))
    draw.text((78, 142), "Publication excerpt from an agency-produced cash-flow workbook", fill=INK, font=font(22))

    metadata = [
        ("Report", "IA-Non-MBS Cash Flow"),
        ("Projected cash-flow period", str(report_period)),
        ("Source locator", "Sheet1 · row 14"),
    ]
    y = 240
    for label, value in metadata:
        draw.text((78, y), label.upper(), fill=PINE, font=font(16, bold=True))
        draw.text((390, y - 4), value, fill=INK, font=font(23))
        y += 64

    y += 45
    draw.rounded_rectangle((78, y, width - 78, y + 520), radius=18, fill="#F2FAF1", outline=PINE, width=3)
    rows = [
        ("Transaction type", transaction_type),
        ("Security category", security_type),
        ("Description", description.title()),
        ("Post date", post_date.strftime("%B %-d, %Y") if os.name != "nt" else post_date.strftime("%B %#d, %Y")),
        ("Amount", f"${amount:,.0f}"),
    ]
    row_y = y + 54
    for label, value in rows:
        draw.text((118, row_y), label.upper(), fill=PINE, font=font(17, bold=True))
        value_font = font(30 if label == "Amount" else 25, bold=label == "Amount")
        draw.text((440, row_y - 8), str(value), fill=INK, font=value_font)
        row_y += 88

    note_y = y + 600
    draw.text((78, note_y), "PUBLICATION TREATMENT", fill=PINE, font=font(17, bold=True))
    note = (
        "Campaign-typeset excerpt. Account identifiers, the security identifier, "
        "coupon details, and unrelated formula or adjustment rows are omitted."
    )
    for line in wrap(note, width=90):
        note_y += 38
        draw.text((78, note_y), line, fill=INK, font=font(22))

    draw.rectangle((0, height - 170, width, height), fill=PINE)
    source_lines = wrap(f"Source: {source.name}", width=105)
    footer_y = height - 138
    for line in source_lines:
        draw.text((78, footer_y), line, fill="white", font=font(16, bold=True))
        footer_y += 29
    draw.text(
        (78, height - 56),
        "Exact locator: Sheet1, row 14 · produced by the Arkansas State Treasury",
        fill=MINT,
        font=font(17),
    )
    save_pdf([page], destination)


def build(corpus: Path, output: Path) -> None:
    atrs_packet = corpus / "raw/atrs/FOIA Response 7-3-25/06-02-25_BOT_Packet.pdf"
    apers_minutes = corpus / "raw/apers/FOIA Response 2-27-26/Minutes_IFC_05.15.25.pdf"
    apers_package = corpus / "raw/apers/FOIA Response 2-27-26/IB_FOIA_FINAL. 2.27.2026 Redacted.LMG.pdf"
    treasury_hold = corpus / "raw/treasury/FOIA Response 9-23-25/Israel Internal Credit overview 10-8-24.pdf"
    treasury_statement = corpus / "raw/treasury/FOIA Response 9-23-25/Israel Bondholder Statements_Redacted.pdf"
    treasury_wire = corpus / "raw/treasury/FOIA Response 2-19-26/Wire Confirm 2-17-26_Redacted.pdf"
    treasury_maturity = corpus / (
        "raw/treasury/FOIA Response 2-19-26/"
        "2026 0202 IA- Non- MBS Cash Flow_Treasury Gen AGG- ISRAEL BONDS- PAR & MATURITY.xlsx"
    )
    funding_email = corpus / (
        "raw/auditor/FOIA Response 3-3-26/Responsive Documents/"
        "Jason.Brady@auditor.ar.gov/Top-of-Information-Store/Inbox/ATRS Board Update-Liquidity.eml"
    )

    for path in (
        atrs_packet,
        apers_minutes,
        apers_package,
        treasury_hold,
        treasury_statement,
        treasury_wire,
        treasury_maturity,
        funding_email,
    ):
        if not path.exists():
            raise FileNotFoundError(path)

    source_excerpt(atrs_packet, [149, 150], output / "atrs-aon-memo-pages-149-150.pdf")
    source_excerpt(atrs_packet, [151, 152], output / "atrs-resolution-2025-22-pages-151-152.pdf")
    source_excerpt(apers_minutes, [4], output / "apers-authorization-minutes-page-4.pdf")
    source_excerpt(
        apers_package,
        [6925],
        output / "apers-purchase-record-page-6925-masked.pdf",
        clips={6925: (58, 42, 565, 208)},
        masks={
            6925: (
                (68, 68, 315, 89),
                (160, 121, 214, 141),
                (160, 136, 229, 156),
            )
        },
        masking_note="Campaign crop; transaction and account identifiers masked.",
    )
    source_excerpt(
        apers_package,
        [3081],
        output / "apers-analysis-email-page-3081-masked.pdf",
        clips={3081: (54, 54, 582, 326)},
        masks={3081: ((326, 251, 580, 326),)},
        masking_note="Campaign crop; direct contact information masked; quoted request omitted.",
    )
    source_excerpt(treasury_hold, [1, 2], output / "treasury-internal-credit-overview.pdf")
    source_excerpt(
        treasury_statement,
        [1],
        output / "treasury-holdings-june-2025-cropped.pdf",
        clips={1: (12, 272, 602, 665)},
        masking_note="Campaign crop omits recipient, barcode, account, and return-mail data; agency mask retained.",
    )
    source_excerpt(
        treasury_wire,
        [1],
        output / "treasury-processing-payment-masked.pdf",
        clips={1: (20, 18, 592, 472)},
        masks={1: ((62, 60, 148, 76), (152, 166, 238, 183))},
        masking_note="Campaign crop; requester and transaction identifiers masked; agency masks retained.",
    )
    treasury_maturity_excerpt(treasury_maturity, output / "treasury-final-maturity-excerpt.pdf")
    funding_email_excerpt(funding_email, output / "atrs-manager-funding-email-excerpt.pdf")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    build(args.corpus.resolve(), args.output.resolve())


if __name__ == "__main__":
    main()
