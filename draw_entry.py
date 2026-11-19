#!/usr/bin/env python3
"""Draw the news-image-20261118 final infographic with code (PIL).

All text is drawn with fonts — no AI-generated text. Output: entry.png,
1024x1024, flat colours, PNG.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (246, 241, 227)
INK = (26, 26, 26)
MUTED = (74, 74, 66)
RULE = (26, 26, 26)
RED = (166, 28, 28)
BLUE = (29, 78, 137)
GREEN = (46, 107, 52)
AMBER = (138, 90, 0)
TEAL = (14, 107, 107)
CARD = (255, 252, 244)

FD = "/usr/share/fonts/truetype/noto/"
SERIF_BLACK = FD + "NotoSerif-Black.ttf"
SERIF_BOLD = FD + "NotoSerif-Bold.ttf"
SERIF = FD + "NotoSerif-Regular.ttf"
SANS_BOLD = FD + "NotoSans-Bold.ttf"
SANS = FD + "NotoSans-Regular.ttf"
SANS_BLACK = FD + "NotoSans-Black.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, xy, text, fnt, max_w, fill, leading):
    x, y = xy
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def tag(draw, x, y, text, color, fnt):
    pad_x, pad_y = 12, 6
    tw = draw.textlength(text, font=fnt)
    th = fnt.size
    draw.rounded_rectangle([x, y, x + tw + pad_x * 2, y + th + pad_y * 2],
                           radius=4, fill=color)
    draw.text((x + pad_x, y + pad_y - 1), text, font=fnt, fill=(255, 255, 255))
    return x + tw + pad_x * 2, y + th + pad_y * 2


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Outer border
    d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=8)

    # ---------- Masthead ----------
    mx = 44
    kicker_f = font(SANS_BOLD, 22)
    kicker = "T H E   W O R L D   I N   O N E   D A Y"
    d.text((mx, 30), kicker, font=kicker_f, fill=RED)
    d.line([(mx, 64), (W - mx, 64)], fill=RULE, width=3)

    date_f = font(SERIF_BLACK, 58)
    date = "Wednesday, November 18, 2026"
    d.text((mx, 74), date, font=date_f, fill=INK)

    sub_f = font(SERIF, 26)
    d.text((mx, 146), "Five stories that defined the day \u2014 as reported.",
           font=sub_f, fill=MUTED)
    d.line([(mx, 190), (W - mx, 190)], fill=RULE, width=3)
    d.line([(mx, 196), (W - mx, 196)], fill=RULE, width=1)

    # ---------- Lead story ----------
    lx, ly, lw = mx, 214, W - 2 * mx
    lead_h = 230
    d.rectangle([lx, ly, lx + lw, ly + lead_h], fill=CARD, outline=INK, width=2)
    d.rectangle([lx, ly, lx + 10, ly + lead_h], fill=RED)
    tx = lx + 30
    tag(d, tx, ly + 18, "MIDDLE EAST  \u00b7  LEAD STORY", RED, font(SANS_BOLD, 20))
    head_f = font(SERIF_BLACK, 42)
    y = draw_wrapped(d, (tx, ly + 56),
                     "U.S.\u2013Iran tanker war escalates in the Gulf",
                     head_f, lw - 60, INK, 48)
    body_f = font(SANS, 23)
    draw_wrapped(d, (tx, y + 8),
                 "U.S. forces destroyed five Iranian tankers, CENTCOM said, "
                 "after Iran's IRGC twice targeted U.S. warships. "
                 "Iran said it hit 10 ships near Hormuz; oil topped $100.",
                 body_f, lw - 60, MUTED, 30)

    # ---------- Two-column rows ----------
    gutter = 24
    col_w = (W - 2 * mx - gutter) // 2

    def block(x, y, h, color, tag_text, headline, body, icon):
        d.rectangle([x, y, x + col_w, y + h], fill=CARD, outline=INK, width=2)
        d.rectangle([x, y, x + col_w, y + 8], fill=color)
        tx = x + 24
        tag(d, tx, y + 20, tag_text, color, font(SANS_BOLD, 18))
        icon(d, x + col_w - 72, y + 18, color)
        hy = draw_wrapped(d, (tx, y + 56), headline,
                          font(SERIF_BOLD, 29), col_w - 48 - 64, INK, 35)
        draw_wrapped(d, (tx, hy + 4), body, font(SANS, 21),
                     col_w - 48, MUTED, 26)

    def icon_globe(d, x, y, color):
        d.ellipse([x, y, x + 48, y + 48], outline=color, width=4)
        d.ellipse([x + 15, y, x + 33, y + 48], outline=color, width=3)
        d.line([(x, y + 24), (x + 48, y + 24)], fill=color, width=3)

    def icon_sun(d, x, y, color):
        import math
        cx, cy, r = x + 24, y + 24, 14
        for ang in range(0, 360, 45):
            a = math.radians(ang)
            d.line([(cx + int(19 * math.cos(a)), cy + int(19 * math.sin(a))),
                    (cx + int(25 * math.cos(a)), cy + int(25 * math.sin(a)))],
                   fill=color, width=3)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)

    def icon_chip(d, x, y, color):
        d.rectangle([x + 8, y + 8, x + 40, y + 40], outline=color, width=4)
        d.rectangle([x + 18, y + 18, x + 30, y + 30], fill=color)
        for px in (16, 24, 32):
            d.line([(x + px, y), (x + px, y + 8)], fill=color, width=3)
            d.line([(x + px, y + 40), (x + px, y + 48)], fill=color, width=3)
            d.line([(x, y + px), (x + 8, y + px)], fill=color, width=3)
            d.line([(x + 40, y + px), (x + 48, y + px)], fill=color, width=3)

    def icon_spiral(d, x, y, color):
        for r in (22, 15, 8):
            d.arc([x + 24 - r, y + 24 - r, x + 24 + r, y + 24 + r],
                  start=20, end=290, fill=color, width=4)

    def icon_bars(d, x, y, color):
        for i, h in enumerate((16, 28, 40)):
            bx = x + 6 + i * 14
            d.rectangle([bx, y + 48 - h, bx + 9, y + 48], fill=color)

    row2_y, row_h = 460, 220
    block(mx, row2_y, row_h, BLUE, "ASIA  \u00b7  DIPLOMACY",
          "APEC opens in Shenzhen",
          "Trump met Marcos in Manila, then flew to China. A "
          "first-ever Trump\u2013Xi\u2013Putin meeting is confirmed for Thursday.",
          icon_globe)
    block(mx + col_w + gutter, row2_y, row_h, GREEN, "MARKETS  \u00b7  IPO",
          "Anthropic prices $83 IPO",
          "The AI firm priced its IPO at $83 a share, above its "
          "$70\u2013$78 range \u2014 an $81bn sale, the largest on record.",
          icon_bars)

    row3_y = 696
    block(mx, row3_y, row_h, AMBER, "MARKETS  \u00b7  TECH",
          "Nvidia tops $115bn quarter",
          "Revenue more than doubled to $115.8bn \u2014 but shares fell "
          "2.9% Wednesday to $150.96, a fifth straight loss.",
          icon_chip)
    block(mx + col_w + gutter, row3_y, row_h, TEAL, "INDIA  \u00b7  WEATHER",
          "Cyclone Akvan nears India",
          "India\u2019s weather office said Akvan turned severe "
          "Wednesday; landfall is forecast for Friday at 90\u2013100 km/h.",
          icon_spiral)

    # ---------- Footer ----------
    fy = 932
    d.line([(mx, fy), (W - mx, fy)], fill=RULE, width=2)
    foot_f = font(SANS, 18)
    d.text((mx, fy + 12),
           "Sources: U.S. Central Command \u00b7 Al Jazeera \u00b7 Reuters \u00b7 Bloomberg \u00b7 "
           "India Meteorological Dept. \u00b7 Nvidia \u00b7 Anthropic",
           font=foot_f, fill=MUTED)
    d.text((mx, fy + 36), "One image, one day. Claims are attributed to the "
           "sources that reported them.", font=foot_f, fill=MUTED)

    img.save("/home/hatch/workspace/makefun/news-image-entry/entry.png",
             optimize=True)
    print("saved")


if __name__ == "__main__":
    main()
