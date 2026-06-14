#!/usr/bin/env python3
# Trade2Swing - Weekly Header Image Generator
#
# Renders a 1456x816 on-brand PNG header for a Substack post.
#
# How to use:
#   Option A - local Python (if you have Python + Pillow installed):
#       cd C:/Users/ssugu/OneDrive/Importantdocs/Claude/Projects/trade2swing
#       # edit the CONFIG block below
#       python make-header.py
#       # output lands at images/<output_filename>.png
#
#   Option B - have Claude run it in chat each Sunday:
#       Send Claude the new CONFIG values; Claude updates this file,
#       runs it in the sandbox, saves the PNG into your images/ folder.
#
# The script auto-detects fonts on Linux / macOS / Windows.
#
# To install Pillow locally (one-time):
#     py -m pip install pillow

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# ===========================================================
#  CONFIG -- edit this block each week, then run the script.
# ===========================================================
CONFIG = {
    "output":          "header-week-02-roundtrip.png",

    "pill_text":       "WEEK 02  *  MODEL BOOK ENTRY",
    "pill_dot_color":  "amber",

    "headline_line1":  "Round trip.",
    "headline_line2":  "The pattern.",

    "subhead_line1":   "How META, HOOD, and PLTR each went from",
    "subhead_line2":   "winners to flat -- and what the chart was saying.",

    "stat1_value":     "3",
    "stat1_label":     "NAMES",
    "stat1_color":     "white",

    "stat2_value":     "100%",
    "stat2_label":     "GIVE-BACK",
    "stat2_color":     "red",

    "stat3_value":     "Q3",
    "stat3_label":     "TURNING POINT",
    "stat3_color":     "amber",

    "chart_shape":     "round_trip",
    "chart_callout":   "Flat year",
}
# ===========================================================


W, H = 1456, 816

INK       = (14, 10, 31)
WHITE     = (255, 255, 255)
MUTE      = (165, 159, 196)
URL_GREY  = (123, 119, 144)
INDIGO    = (99, 102, 241)
VIOLET    = (139, 92, 246)
LAVENDER  = (196, 181, 253)
GREEN     = (16, 185, 129)
RED       = (239, 68, 68)
AMBER     = (251, 191, 36)
PANEL_GR  = (74, 70, 96)

DOT_COLORS  = {"green": GREEN, "amber": AMBER, "red": RED}
STAT_COLORS = {"white": WHITE, "green": GREEN, "red": RED, "amber": AMBER}


def find_font(candidates, size):
    paths = []
    for name in candidates:
        paths += [
            "/usr/share/fonts/truetype/dejavu/" + name,
            "C:/Windows/Fonts/" + name,
            "/System/Library/Fonts/" + name,
            "/System/Library/Fonts/Supplemental/" + name,
        ]
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()


F_BOLD   = ["DejaVuSans-Bold.ttf", "arialbd.ttf", "Arial-Bold.ttf",
            "Arial Bold.ttf", "Helvetica-Bold.ttf", "seguibl.ttf"]
F_REG    = ["DejaVuSans.ttf", "arial.ttf", "Arial.ttf", "Helvetica.ttc",
            "segoeui.ttf"]
F_ITALIC = ["DejaVuSans-Oblique.ttf", "ariali.ttf", "Arial Italic.ttf",
            "Helvetica-Oblique.ttf", "segoeuii.ttf"]

f_wm      = find_font(F_BOLD, 30)
f_pill    = find_font(F_BOLD, 16)
f_head    = find_font(F_BOLD, 100)
f_sub     = find_font(F_REG, 26)
f_stat    = find_font(F_BOLD, 52)
f_lbl     = find_font(F_BOLD, 14)
f_url     = find_font(F_REG, 16)
f_tag     = find_font(F_ITALIC, 16)
f_chart   = find_font(F_BOLD, 13)
f_callout = find_font(F_BOLD, 18)


def make_background():
    img = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(img, "RGBA")
    for y in range(H):
        t = y / H
        r = int(14 + (26 - 14) * t)
        g = int(10 + (19 - 10) * t)
        b = int(31 + (56 - 31) * t)
        d.line([(0, y), (W, y)], fill=(r, g, b))
    for cx, cy, R, col, amax in [
        (int(W * 0.85), int(H * 0.18), 600, VIOLET, 85),
        (int(W * 0.12), int(H * 0.92), 500, INDIGO, 70),
    ]:
        glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        gd = ImageDraw.Draw(glow)
        for r in range(R, 0, -8):
            a = int(amax * (1 - r/R))
            gd.ellipse([cx-r, cy-r, cx+r, cy+r], fill=col + (a,))
        glow = glow.filter(ImageFilter.GaussianBlur(40))
        img.paste(glow, (0, 0), glow)
    grid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grid)
    for x in range(0, W, 64):
        gd.line([(x, 0), (x, H)], fill=(255, 255, 255, 12))
    for y in range(0, H, 64):
        gd.line([(0, y), (W, y)], fill=(255, 255, 255, 12))
    img.paste(grid, (0, 0), grid)
    return img


def draw_brand(img):
    d = ImageDraw.Draw(img, "RGBA")
    d.rounded_rectangle([80, 70, 124, 114], radius=10, fill=INDIGO)
    d.rounded_rectangle([90, 98, 95, 108], radius=2, fill=(255,255,255,140))
    d.rounded_rectangle([99, 92, 104, 108], radius=2, fill=(255,255,255,200))
    d.rounded_rectangle([108, 84, 113, 108], radius=2, fill=(255,255,255,255))
    d.line([(91, 96), (101, 89), (108, 92), (116, 80)], fill=WHITE, width=3)
    d.text((140, 78), "Trade2Swing", fill=WHITE, font=f_wm)


def draw_pill(img, text, dot_color="green"):
    d = ImageDraw.Draw(img, "RGBA")
    tw = d.textbbox((0, 0), text, font=f_pill)[2]
    pill_w = max(280, tw + 64)
    d.rounded_rectangle([80, 200, 80+pill_w, 244], radius=22,
                        fill=VIOLET + (38,), outline=VIOLET + (170,), width=1)
    d.ellipse([98, 217, 108, 227], fill=DOT_COLORS.get(dot_color, GREEN))
    d.text((118, 213), text, fill=LAVENDER, font=f_pill)


def draw_headline(img, line1, line2):
    d = ImageDraw.Draw(img, "RGBA")
    if line1:
        d.text((80, 290), line1, fill=WHITE, font=f_head)
    if not line2:
        return
    bbox = d.textbbox((0, 0), line2, font=f_head)
    tw = bbox[2] - bbox[0]
    grad = Image.new("RGBA", (tw + 20, 110), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grad)
    for x in range(tw + 20):
        t = x / (tw + 20)
        if t < 0.55:
            u = t / 0.55
            r = int(167 + (196-167)*u); g = int(139 + (181-139)*u); b = int(250 + (253-250)*u)
        else:
            u = (t - 0.55) / 0.45
            r = int(196 + (129-196)*u); g = int(181 + (140-181)*u); b = int(253 + (248-253)*u)
        gd.line([(x, 0), (x, 110)], fill=(r, g, b, 255))
    mask = Image.new("L", (tw + 20, 110), 0)
    md = ImageDraw.Draw(mask)
    md.text((0, 0), line2, fill=255, font=f_head)
    img.paste(grad, (80, 395), mask)


def draw_subhead(img, line1, line2):
    d = ImageDraw.Draw(img, "RGBA")
    if line1: d.text((80, 535), line1, fill=MUTE, font=f_sub)
    if line2: d.text((80, 572), line2, fill=MUTE, font=f_sub)


def draw_stats(img, stats):
    d = ImageDraw.Draw(img, "RGBA")
    SY = 660
    xs = [80, 240, 460]
    for x, (val, lbl, col) in zip(xs, stats):
        if not val: continue
        color = STAT_COLORS.get(col, WHITE)
        d.text((x, SY), val, fill=color, font=f_stat)
        if lbl:
            d.text((x, SY + 62), lbl, fill=MUTE, font=f_lbl)


def draw_bottom(img):
    d = ImageDraw.Draw(img, "RGBA")
    d.text((80, 778), "trade2swing.com", fill=URL_GREY, font=f_url)
    tag = "Trade by the chart, not the news."
    tw = d.textbbox((0, 0), tag, font=f_tag)[2]
    d.text((W-80-tw, 778), tag, fill=URL_GREY, font=f_tag)


def chart_panel(img):
    CX0, CY0, CW, CH = 800, 200, 576, 430
    d = ImageDraw.Draw(img, "RGBA")
    d.rounded_rectangle([CX0, CY0, CX0+CW, CY0+CH], radius=18,
                        fill=(255, 255, 255, 8),
                        outline=(255, 255, 255, 20), width=1)
    for y in (100, 180, 260, 340):
        d.line([(CX0+30, CY0+y), (CX0+CW-30, CY0+y)], fill=(255, 255, 255, 15))
    return CX0, CY0, CW, CH


def chart_ftd_lockout(img, callout="+467%"):
    CX0, CY0, _, _ = chart_panel(img)
    d = ImageDraw.Draw(img, "RGBA")
    pre = [(300,34),(290,40),(295,38),(285,48),(300,35),
           (310,30),(305,32),(315,28),(320,26),(310,32)]
    for i, (top, h) in enumerate(pre):
        x, y = CX0+40+i*20, CY0+top
        d.rectangle([x, y, x+8, y+h], fill=PANEL_GR)
    ftd_x = CX0 + 252
    for dy in range(40, 380, 10):
        d.line([(ftd_x, CY0+dy), (ftd_x, CY0+dy+6)], fill=AMBER, width=3)
    d.rounded_rectangle([ftd_x+8, CY0+55, ftd_x+68, CY0+81], radius=6, fill=AMBER)
    d.text((ftd_x+18, CY0+58), "FTD", fill=INK, font=f_chart)
    post = [(295,40),(265,50),(230,50),(200,45),(170,42),(140,40),(115,38),
            (92,36),(75,32),(60,30),(48,28),(40,26),(35,22)]
    pts = []
    for i, (top, h) in enumerate(post):
        x, y = CX0+270+i*20, CY0+top
        d.rectangle([x, y, x+8, y+h], fill=GREEN)
        pts.append((x+4, y+h/2))
    for i in range(len(pts)-1):
        d.line([pts[i], pts[i+1]], fill=GREEN + (180,), width=3)
    co_x, co_y = CX0+420, CY0+80
    d.rounded_rectangle([co_x, co_y, co_x+120, co_y+38], radius=19, fill=GREEN)
    ctw = d.textbbox((0,0), callout, font=f_callout)[2]
    d.text((co_x+(120-ctw)//2, co_y+8), callout, fill=WHITE, font=f_callout)
    d.text((CX0+40, CY0+400), "PRE-FTD: SIDEWAYS BASE", fill=URL_GREY, font=f_lbl)
    d.text((CX0+320, CY0+400), "POST-FTD: LOCK-OUT RALLY", fill=GREEN, font=f_lbl)


def chart_round_trip(img, callout="Flat year"):
    CX0, CY0, CW, CH = chart_panel(img)
    d = ImageDraw.Draw(img, "RGBA")
    base = [(310,28),(305,30),(300,34)]
    for i, (top, h) in enumerate(base):
        x, y = CX0+40+i*18, CY0+top
        d.rectangle([x, y, x+8, y+h], fill=PANEL_GR)
    rise = [(295,30),(265,38),(230,42),(195,42),(160,40),(125,38),(95,34),(72,30)]
    rise_pts = []
    for i, (top, h) in enumerate(rise):
        x, y = CX0+100+i*24, CY0+top
        d.rectangle([x, y, x+8, y+h], fill=GREEN)
        rise_pts.append((x+4, y+h/2))
    peak_x = rise_pts[-1][0]
    d.line([(peak_x, CY0+40), (peak_x, CY0+95)], fill=(255,255,255,140), width=2)
    d.rounded_rectangle([peak_x-30, CY0+55, peak_x+50, CY0+85], radius=15, fill=GREEN)
    d.text((peak_x-15, CY0+62), "PEAK", fill=WHITE, font=f_chart)
    fall = [(85,30),(115,38),(145,42),(180,42),(215,40),(245,42),(275,38),(300,32)]
    fall_pts = []
    for i, (top, h) in enumerate(fall):
        x, y = CX0+300+i*24, CY0+top
        d.rectangle([x, y, x+8, y+h], fill=RED)
        fall_pts.append((x+4, y+h/2))
    for i in range(len(rise_pts)-1):
        d.line([rise_pts[i], rise_pts[i+1]], fill=GREEN + (180,), width=2)
    d.line([rise_pts[-1], fall_pts[0]], fill=(255,255,255,140), width=2)
    for i in range(len(fall_pts)-1):
        d.line([fall_pts[i], fall_pts[i+1]], fill=RED + (180,), width=2)
    co_x, co_y = CX0 + CW - 170, CY0 + CH - 110
    d.rounded_rectangle([co_x, co_y, co_x+140, co_y+44], radius=22, fill=PANEL_GR)
    cw = d.textbbox((0,0), callout, font=f_callout)[2]
    d.text((co_x + (140-cw)//2, co_y+11), callout, fill=WHITE, font=f_callout)
    d.text((CX0+40, CY0+400), "UP MOVE: WINS", fill=GREEN, font=f_lbl)
    d.text((CX0+320, CY0+400), "DOWN MOVE: GAVE BACK", fill=RED, font=f_lbl)


def chart_base_breakout(img, callout="Breakout"):
    CX0, CY0, CW, CH = chart_panel(img)
    d = ImageDraw.Draw(img, "RGBA")
    base = [(290,32),(280,38),(295,30),(285,40),(300,34),(290,36),
            (305,30),(295,32),(285,36),(300,32),(295,30),(290,34)]
    for i, (top, h) in enumerate(base):
        x, y = CX0+40+i*22, CY0+top
        d.rectangle([x, y, x+8, y+h], fill=PANEL_GR)
    pivot_x = CX0 + 320
    d.line([(CX0+30, CY0+260), (pivot_x, CY0+260)], fill=(255,255,255,80), width=1)
    bo = [(255,40),(220,42),(180,42),(140,40),(108,36),(80,32),(60,28)]
    pts = []
    for i, (top, h) in enumerate(bo):
        x, y = pivot_x+i*30, CY0+top
        d.rectangle([x, y, x+10, y+h], fill=GREEN)
        pts.append((x+5, y+h/2))
    for i in range(len(pts)-1):
        d.line([pts[i], pts[i+1]], fill=GREEN + (180,), width=3)
    co_x, co_y = CX0+420, CY0+80
    cw = d.textbbox((0,0), callout, font=f_callout)[2]
    d.rounded_rectangle([co_x, co_y, co_x+cw+40, co_y+38], radius=19, fill=GREEN)
    d.text((co_x+20, co_y+8), callout, fill=WHITE, font=f_callout)
    d.text((CX0+40, CY0+400), "BASE: VOLATILITY CONTRACTION", fill=URL_GREY, font=f_lbl)
    d.text((CX0+340, CY0+400), "BREAKOUT: VOLUME CONFIRM", fill=GREEN, font=f_lbl)


CHART_SHAPES = {
    "ftd_lockout":    chart_ftd_lockout,
    "round_trip":     chart_round_trip,
    "base_breakout":  chart_base_breakout,
}


def main(config=None):
    cfg = config or CONFIG
    img = make_background()
    draw_brand(img)
    draw_pill(img, cfg["pill_text"], cfg.get("pill_dot_color", "green"))
    draw_headline(img, cfg.get("headline_line1", ""), cfg.get("headline_line2", ""))
    draw_subhead(img, cfg.get("subhead_line1"), cfg.get("subhead_line2"))
    draw_stats(img, [
        (cfg.get("stat1_value"), cfg.get("stat1_label"), cfg.get("stat1_color", "white")),
        (cfg.get("stat2_value"), cfg.get("stat2_label"), cfg.get("stat2_color", "white")),
        (cfg.get("stat3_value"), cfg.get("stat3_label"), cfg.get("stat3_color", "white")),
    ])
    draw_bottom(img)
    shape_fn = CHART_SHAPES.get(cfg.get("chart_shape", "ftd_lockout"))
    if shape_fn:
        shape_fn(img, cfg.get("chart_callout", ""))
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, cfg["output"])
    img.save(out_path, "PNG", optimize=True)
    print("wrote " + out_path + " (" + str(img.size[0]) + "x" + str(img.size[1]) + ")")
    return out_path


if __name__ == "__main__":
    main()
