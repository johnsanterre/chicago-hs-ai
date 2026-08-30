#!/usr/bin/env python3
"""Animated lesson videos: Python-drawn frames + Kokoro narration -> MP4.

Each scene is a draw function animated across the exact duration of its
narration line. Frames are drawn with Pillow, narration comes from Kokoro,
ffmpeg muxes. Run with the tts venv python (has kokoro, soundfile, numpy;
pillow installed 2026-08-30):

    /Users/john/Dropbox/_/tts/venv/bin/python make_videos.py chsai-ai-1
"""
import math, os, random, subprocess, sys
import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw, ImageFont

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = "/tmp/chsai-anim"
W, H, FPS = 1280, 720, 15
os.makedirs(WORK, exist_ok=True)
os.makedirs(f"{SITE}/video", exist_ok=True)

# Chicago palette
PAPER = (252, 251, 248); INK = (30, 37, 48); INK2 = (91, 101, 114)
NAVY = (23, 74, 108); STAR = (206, 58, 54); SKY = (179, 221, 242)
CARD = (255, 255, 255); HAIR = (227, 224, 216); GREEN = (27, 122, 69)

HN = "/System/Library/Fonts/HelveticaNeue.ttc"
MENLO = "/System/Library/Fonts/Menlo.ttc"
def F(size, bold=False, med=False):
    return ImageFont.truetype(HN, size, index=1 if bold else (10 if med else 0))
def FM(size):
    return ImageFont.truetype(MENLO, size, index=0)

def ease(t): return t * t * (3 - 2 * t)
def clamp01(x): return max(0.0, min(1.0, x))
def sub(t, a, b):  # progress of t within [a,b]
    return clamp01((t - a) / (b - a)) if b > a else 1.0

def chi_star(dr, cx, cy, r, fill):
    """Six-pointed Chicago-flag star."""
    pts = []
    for i in range(12):
        ang = math.pi / 6 * i - math.pi / 2
        rad = r if i % 2 == 0 else r * 0.5
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    dr.polygon(pts, fill=fill)

def frame_base(num, total):
    im = Image.new("RGB", (W, H), PAPER)
    dr = ImageDraw.Draw(im)
    dr.text((90, 26), "Chicago HS AI", font=F(22, bold=True), fill=NAVY)
    tw = dr.textlength("Chicago HS AI ", font=F(22, bold=True))
    chi_star(dr, 90 + tw + 12, 40, 11, STAR)
    dr.text((W - 90, 28), f"{num} / {total}", font=F(17), fill=INK2, anchor="ra")
    dr.rectangle([0, H - 10, W, H], fill=SKY)
    return im, dr

def kicker(dr, text, y=78):
    dr.text((90, y), text.upper(), font=F(19, bold=True), fill=STAR)

def type_text(dr, xy, text, t, font, fill, cursor=True):
    """Draw text typing on; t=1 means fully typed."""
    n = int(round(len(text) * clamp01(t)))
    shown = text[:n]
    dr.text(xy, shown, font=font, fill=fill)
    if cursor and 0 < t < 1:
        cw = dr.textlength(shown, font=font)
        dr.rectangle([xy[0] + cw + 3, xy[1] + 4, xy[0] + cw + 6,
                      xy[1] + font.size - 2], fill=STAR)
    return n >= len(text)

def wrap_type(dr, x, y, text, t, font, fill, maxw, lh):
    """Multiline typing within maxw; simple word wrap."""
    n = int(round(len(text) * clamp01(t)))
    words, line, yy = text[:n].split(" "), "", y
    for w_ in words:
        test = (line + " " + w_).strip()
        if dr.textlength(test, font=font) > maxw and line:
            dr.text((x, yy), line, font=font, fill=fill)
            yy += lh; line = w_
        else:
            line = test
    dr.text((x, yy), line, font=font, fill=fill)
    return yy

def bars_panel(dr, x, y, w, rows, title=None):
    """rows = [(word, pct01, style)] style: 'pick'|'' """
    if title:
        dr.text((x, y - 30), title.upper(), font=F(14, bold=True), fill=INK2)
    bh, gap = 30, 12
    for i, (word, p, style) in enumerate(rows):
        yy = y + i * (bh + gap)
        dr.text((x + 108, yy + bh / 2), word, font=F(19, med=True),
                fill=STAR if style == "pick" else INK, anchor="rm")
        dr.rounded_rectangle([x + 122, yy, x + w, yy + bh], 5, outline=HAIR,
                             width=2, fill=CARD)
        fw = (w - 122) * p
        if fw > 6:
            dr.rounded_rectangle([x + 122, yy, x + 122 + fw, yy + bh], 5,
                                 fill=STAR if style == "pick" else SKY)
        dr.text((x + w + 14, yy + bh / 2), f"{int(round(p*100))}%",
                font=F(16), fill=INK2, anchor="lm")

def token_chips(dr, x, y, tokens, maxw, font, lh=52):
    """Draw tokens as sky chips, wrapping; returns (x,y) after last chip."""
    cx, cy = x, y
    for tk in tokens:
        tw = dr.textlength(tk, font=font)
        pad = 8 if tk not in (",", ".") else 2
        wpx = tw + pad * 2
        if cx + wpx > x + maxw:
            cx, cy = x, cy + lh
        if tk not in (",", "."):
            dr.rounded_rectangle([cx, cy - 4, cx + wpx, cy + font.size + 6], 6,
                                 fill=SKY)
        dr.text((cx + pad, cy), tk, font=font, fill=INK)
        cx += wpx + 8
    return cx, cy

# ---------------------------------------------------------------- scenes

def s1_title(dr, t, rng):
    kicker(dr, "How AI works · Lesson 1")
    if t > 0.02:
        a = ease(sub(t, 0.02, 0.22))
        col = tuple(int(PAPER[i] + (NAVY[i] - PAPER[i]) * a) for i in range(3))
        dr.text((90, 130), "The prediction machine", font=F(64, bold=True), fill=col)
    dr.text((90, 260), "One trick, at colossal scale:", font=F(34), fill=INK)
    type_text(dr, (90, 330), "predict what comes next.", sub(t, 0.3, 0.72),
              F(52, bold=True), STAR)
    if t > 0.8:
        rows = [("next", 0.72, "pick"), ("after", 0.14, ""), ("soon", 0.09, "")]
        bars_panel(dr, 700, 470, 420, rows, title="the model's bets, every step")

def s2_phone(dr, t, rng):
    kicker(dr, "You already use one")
    dr.text((90, 118), "The suggestion bar is a tiny language model.",
            font=F(30, med=True), fill=INK)
    # phone
    px, py, pw, ph = 160, 190, 340, 450
    dr.rounded_rectangle([px, py, px + pw, py + ph], 34, fill=CARD,
                         outline=INK, width=5)
    dr.rounded_rectangle([px + 130, py + 14, px + pw - 130, py + 26], 6, fill=HAIR)
    # message being typed
    msg = "see you at the"
    words = ["game", "after", "school"]
    # timeline: type msg (0..0.3), suggest+pick 'game' (0.3..0.55), append (0.55..),
    # suggest2 pick 'after' (0.65..0.85), append 'school' quickly
    typed = msg
    tt = sub(t, 0.04, 0.30)
    shown = msg[:int(round(len(msg) * tt))]
    extra = []
    if t > 0.52: extra.append("game")
    if t > 0.82: extra.append("after")
    full = shown + (" " + " ".join(extra) if extra else "")
    dr.rounded_rectangle([px + 22, py + 60, px + pw - 22, py + 150], 12,
                         fill=PAPER, outline=HAIR, width=2)
    wrap_type(dr, px + 34, py + 74, full, 1, F(22), INK, pw - 70, 30)
    # suggestion bar
    sugg = None
    if 0.32 < t < 0.55: sugg = (["game", "park", "gym"], 0)
    elif 0.60 < t < 0.85: sugg = (["after", "tomorrow", "?"], 0)
    sy = py + 175
    if sugg:
        opts, hot = sugg
        cx = px + 22
        for i, o in enumerate(opts):
            ow = dr.textlength(o, font=F(20, med=True)) + 26
            hotnow = i == hot and (t % 0.14) > 0.05
            dr.rounded_rectangle([cx, sy, cx + ow, sy + 40], 9,
                                 fill=SKY if hotnow else PAPER,
                                 outline=NAVY if hotnow else HAIR, width=2)
            dr.text((cx + 13, sy + 8), o, font=F(20, med=True), fill=NAVY)
            cx += ow + 10
    # keyboard hint rows
    for r in range(3):
        for c in range(9 - r):
            kx = px + 26 + c * 32 + r * 16
            ky = py + 240 + r * 46
            dr.rounded_rectangle([kx, ky, kx + 26, ky + 38], 5, fill=PAPER,
                                 outline=HAIR, width=2)
    lines = [(0.35, "It reads your last few words"),
             (0.62, "and bets on the next one."),
             (0.88, "Now scale it up a million times.")]
    yy = 300
    for at, ln in lines:
        if t > at:
            dr.text((580, yy), ln, font=F(31, med=True),
                    fill=NAVY if at > 0.8 else INK)
        yy += 62

def s3_build(dr, t, rng):
    kicker(dr, "Watch an answer get built")
    # user bubble
    dr.rounded_rectangle([90, 120, 560, 180], 14, fill=SKY)
    dr.text((112, 136), "Why is the sky blue?", font=F(24, med=True), fill=NAVY)
    toks = ["Sunlight", "scatters", "in", "the", "air", ",", "and", "blue",
            "scatters", "the", "most", "."]
    cands = [
        [("Sunlight", .58), ("Because", .22), ("The", .12)],
        [("scatters", .44), ("bounces", .3), ("bends", .14)],
        [("in", .62), ("through", .2), ("around", .1)],
        [("the", .87), ("our", .08), ("thin", .03)],
        [("air", .7), ("sky", .18), ("wind", .06)],
        [(",", .55), (".", .3), ("and", .1)],
        [("and", .5), ("so", .27), ("but", .13)],
        [("blue", .66), ("short", .2), ("that", .08)],
        [("scatters", .48), ("bends", .26), ("wins", .12)],
        [("the", .84), ("far", .09), ("out", .05)],
        [("most", .77), ("hardest", .13), ("widest", .06)],
        [(".", .81), ("!", .11), (",", .05)],
    ]
    n = len(toks)
    prog = sub(t, 0.12, 0.88) * n
    done = int(prog)
    # assistant bubble with tokens so far
    dr.rounded_rectangle([90, 215, 700, 380], 14, fill=CARD, outline=HAIR, width=3)
    token_chips(dr, 116, 244, toks[:done], 560, F(26))
    # candidates panel for the token being chosen
    idx = min(done, n - 1)
    if t < 0.94:
        rows = [(w if w not in (",", ".") else ("comma" if w == "," else "period"),
                 p, "pick" if j == 0 else "") for j, (w, p) in enumerate(cands[idx])]
        bars_panel(dr, 760, 200, 400, rows, title="top bets for the next piece")
    if t > 0.9:
        dr.text((90, 470), "The answer did not exist until it was written.",
                font=F(33, bold=True), fill=NAVY)
        dr.text((90, 530), "Each piece: the most plausible next piece.",
                font=F(26), fill=INK2)

def s4_nodb(dr, t, rng):
    kicker(dr, "The fact to hold on to")
    # database cylinder
    cx, cy, rw, rh, bh = 280, 300, 130, 42, 200
    a = ease(sub(t, 0.05, 0.25))
    if a > 0:
        col = tuple(int(PAPER[i] + (INK2[i] - PAPER[i]) * a) for i in range(3))
        dr.ellipse([cx - rw, cy + bh - rh, cx + rw, cy + bh + rh], outline=col, width=6)
        dr.rectangle([cx - rw, cy, cx + rw, cy + bh], fill=PAPER)
        dr.line([cx - rw, cy, cx - rw, cy + bh], fill=col, width=6)
        dr.line([cx + rw, cy, cx + rw, cy + bh], fill=col, width=6)
        dr.ellipse([cx - rw, cy - rh, cx + rw, cy + rh], fill=PAPER, outline=col, width=6)
        for k in (0.45, 0.75):
            dr.arc([cx - rw, cy + bh * k - rh, cx + rw, cy + bh * k + rh],
                   0, 180, fill=col, width=5)
    # red X
    xp = ease(sub(t, 0.3, 0.5))
    if xp > 0:
        x0, y0, x1, y1 = cx - 170, cy - 120, cx + 170, cy + bh + 90
        dr.line([x0, y0, x0 + (x1 - x0) * xp, y0 + (y1 - y0) * xp], fill=STAR, width=16)
    xp2 = ease(sub(t, 0.45, 0.65))
    if xp2 > 0:
        x0, y0, x1, y1 = cx + 170, cy - 120, cx - 170, cy + bh + 90
        dr.line([x0, y0, x0 + (x1 - x0) * xp2, y0 + (y1 - y0) * xp2], fill=STAR, width=16)
    type_text(dr, (560, 250), "There is no", sub(t, 0.3, 0.5), F(58, bold=True), INK)
    type_text(dr, (560, 330), "database inside.", sub(t, 0.5, 0.72), F(58, bold=True), STAR)
    if t > 0.8:
        dr.text((560, 440), "It read the internet once, learned the", font=F(27), fill=INK2)
        dr.text((560, 480), "patterns — and now it writes plausible text.", font=F(27), fill=INK2)

def s5_flex(dr, t, rng):
    kicker(dr, "Why it can do anything")
    cards = [
        ("A POEM", ["The lake keeps every color", "the sky has thrown away —"], F(28, med=True), INK, False),
        ("A BUSINESS PLAN", ["Q3 goal: launch the tutoring app", "in two Chicago high schools."], F(28, med=True), INK, False),
        ("WORKING CODE", ["for student in roster:", "    send_reminder(student)"], FM(26), NAVY, True),
    ]
    seg = sub(t, 0.04, 0.9) * 3
    i = min(int(seg), 2)
    local = seg - i
    label, lines, fnt, col, mono = cards[i]
    dr.rounded_rectangle([200, 150, 1080, 420], 18, fill=CARD, outline=HAIR, width=3)
    dr.text((240, 185), label, font=F(20, bold=True), fill=STAR)
    yy = 245
    for j, ln in enumerate(lines):
        share = clamp01(local * 2 - j)
        type_text(dr, (240, yy), ln, share, fnt, col, cursor=(share < 1))
        yy += 62
    dr.text((W / 2, 520), "All just text to continue.", font=F(40, bold=True),
            fill=NAVY, anchor="ma")
    dr.text((W / 2, 585), "One trick covers all of it.", font=F(28), fill=INK2,
            anchor="ma")

def s6_wrong(dr, t, rng):
    kicker(dr, "Why it can be wrong")
    pairs = [
        (95, "The Willis Tower is", "1,451 feet tall.", True),
        (660, "The Willis Tower has", "121 floors.", False),
    ]
    for x, l1, l2, truth in pairs:
        dr.rounded_rectangle([x, 130, x + 525, 330], 16, fill=CARD,
                             outline=HAIR, width=3)
        tt = sub(t, 0.08, 0.42)
        type_text(dr, (x + 36, 170), l1, clamp01(tt * 2), F(31, med=True), INK,
                  cursor=False)
        type_text(dr, (x + 36, 225), l2, clamp01(tt * 2 - 1), F(31, med=True), INK,
                  cursor=False)
        if t > (0.55 if truth else 0.68):
            mark_col = GREEN if truth else STAR
            mx, my = x + 460, 275
            if truth:
                dr.line([mx - 20, my, mx - 5, my + 18], fill=mark_col, width=10)
                dr.line([mx - 5, my + 18, mx + 28, my - 22], fill=mark_col, width=10)
            else:
                dr.line([mx - 20, my - 20, mx + 20, my + 20], fill=mark_col, width=10)
                dr.line([mx + 20, my - 20, mx - 20, my + 20], fill=mark_col, width=10)
                dr.text((x + 36, 285), "(it has 110)", font=F(20), fill=INK2)
    if t > 0.8:
        dr.text((W / 2, 430), "Same machine. Same trick. Same confident tone.",
                font=F(36, bold=True), fill=NAVY, anchor="ma")
        dr.text((W / 2, 495), "Confident and correct are not the same thing.",
                font=F(28), fill=STAR, anchor="ma")

def s7_random(dr, t, rng):
    kicker(dr, "Same question, twice")
    dr.text((90, 120), "The best thing about Chicago is…", font=F(34, bold=True),
            fill=INK)
    runs = [
        ("RUN 1", "…the lake in summer, when the whole city moves outside.", 0.1, 0.42),
        ("RUN 2", "…the food from every corner of the world.", 0.5, 0.78),
    ]
    yy = 200
    for label, txt, a, b in runs:
        if t > a:
            dr.rounded_rectangle([90, yy, 900, yy + 96], 14, fill=CARD,
                                 outline=HAIR, width=3)
            dr.text((116, yy + 14), label, font=F(16, bold=True), fill=STAR)
            wrap_type(dr, 116, yy + 44, txt, sub(t, a, b), F(25, med=True), INK,
                      740, 34)
        yy += 130
    # randomness dial
    cx, cy, r = 1075, 320, 92
    dr.arc([cx - r, cy - r, cx + r, cy + r], 150, 390, fill=HAIR, width=14)
    wob = math.sin(t * math.tau * 2.2) * 0.5 + 0.5
    ang = math.radians(150 + 240 * (0.35 + 0.4 * wob))
    dr.line([cx, cy, cx + (r - 22) * math.cos(ang), cy + (r - 22) * math.sin(ang)],
            fill=STAR, width=10)
    dr.ellipse([cx - 10, cy - 10, cx + 10, cy + 10], fill=NAVY)
    dr.text((cx, cy + r + 16), "RANDOMNESS", font=F(15, bold=True), fill=INK2,
            anchor="ma")
    if t > 0.82:
        dr.text((90, 490), "On purpose. Neither is “the” answer.",
                font=F(33, bold=True), fill=NAVY)
        dr.text((90, 550), "Now go into the lesson and catch it predicting.",
                font=F(27), fill=INK2)

LESSONS = {
"chsai-ai-1": [
 (s1_title, "Welcome to How AI Works. This whole video is about one idea: a language model does one thing. It reads everything so far, and predicts what comes next. That single trick, done at colossal scale, is the machine you're about to master."),
 (s2_phone, "You already use a language model every day. The suggestion bar on your phone's keyboard reads your last few words and guesses the next one. A modern AI is that idea, scaled up around a million times, and trained on a gigantic slice of everything humans have written."),
 (s3_build, "When an AI answers you, watch closely: the words arrive one piece at a time. That's not a loading animation. At every step the model holds ranked bets on what comes next, draws one, and commits. The answer is literally being written into existence — it did not exist anywhere until the moment it was generated."),
 (s4_nodb, "Here is the fact to tattoo on your brain: there is no database inside. The model isn't looking your question up. It read the internet once, learned the patterns, and now it writes plausible text. Everything good and everything dangerous about AI comes from that."),
 (s5_flex, "This explains the flexibility. A poem, a business plan, an apology, working Python code — to the model, they're all just text to continue. One trick covers all of it. That's why the same machine helps with homework and writes software."),
 (s6_wrong, "It also explains the danger. A false sentence can be perfectly plausible. The machine that writes truths and the machine that writes mistakes are the same machine, running the same trick, in the same confident tone. Remember that every time an answer sounds sure of itself."),
 (s7_random, "One more consequence. Ask the same question twice and you'll often get two different answers. There's a little on-purpose randomness in how the model picks among good next words — it keeps the writing fresh. It's not moody. It's designed that way. Now go into the lesson and catch it predicting."),
],
}

def narrate(pipe, text, out_wav, pad=0.45):
    chunks = [a for _, _, a in pipe(text, voice="af_heart")]
    audio = np.concatenate(chunks)
    audio = np.concatenate([audio, np.zeros(int(24000 * pad), dtype=audio.dtype)])
    sf.write(out_wav, audio, 24000)
    return len(audio) / 24000

def build(slug):
    from kokoro import KPipeline
    pipe = KPipeline(lang_code="a")
    scenes = LESSONS[slug]
    total = len(scenes)
    wavs, durs = [], []
    for i, (_, say) in enumerate(scenes, 1):
        wav = f"{WORK}/{slug}-{i}.wav"
        d = narrate(pipe, say, wav)
        wavs.append(wav); durs.append(d)
        print(f"  narration {i}/{total}: {d:.1f}s", flush=True)
    fdir = f"{WORK}/{slug}-frames"
    os.makedirs(fdir, exist_ok=True)
    for old in os.listdir(fdir): os.remove(f"{fdir}/{old}")
    n = 0
    for i, ((fn, _), d) in enumerate(zip(scenes, durs), 1):
        nf = int(round(d * FPS))
        rng = random.Random(i * 7919)
        for k in range(nf):
            t = (k + 0.5) / nf
            im, dr = frame_base(i, total)
            fn(dr, t, rng)
            im.save(f"{fdir}/f{n:05d}.png")
            n += 1
        print(f"  scene {i}: {nf} frames", flush=True)
    allaudio = np.concatenate([sf.read(w)[0] for w in wavs])
    concat = f"{WORK}/{slug}-all.wav"
    sf.write(concat, allaudio, 24000)
    out = f"{SITE}/video/{slug}-watch.mp4"
    subprocess.run(["ffmpeg", "-y", "-framerate", str(FPS), "-i", f"{fdir}/f%05d.png",
                    "-i", concat, "-c:v", "libx264", "-pix_fmt", "yuv420p",
                    "-r", "30", "-c:a", "aac", "-b:a", "96k", "-shortest", out],
                   capture_output=True, check=True)
    print(f"{out}  ({sum(durs)/60:.1f} min, {n} frames)", flush=True)

if __name__ == "__main__":
    slug = sys.argv[1] if len(sys.argv) > 1 else "chsai-ai-1"
    build(slug)
