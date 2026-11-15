# -*- coding: utf-8 -*-
"""JUN'S TOUR mobile brochure — web asset builder.

Source photos live in the workspace (documents/…); this script writes the
optimised set into the GitHub Pages repo folder so the site stays light.

usage:  python3 sites/junstour/tools/build_assets.py
"""
import os
from PIL import Image, ImageOps

WS = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
SRC_A = os.path.join(WS, 'documents/laos-brochure-premium/assets/src')
SRC_B = os.path.join(WS, 'documents/mobile-itinerary-laos/assets')
LOGO = os.path.join(WS, 'documents/laos-brochure-premium/assets')
OUT = os.path.join(WS, 'sites/junstour/laos-2027-01/assets')
IMG = os.path.join(OUT, 'img')
os.makedirs(IMG, exist_ok=True)

# key, source path, (width, height) of the delivered crop, focus (cx, cy in 0..1), quality
JOBS = [
    # hero — portrait crop so the phone shows a tall, composed image
    ('hero',            f'{SRC_A}/bridge_hut_sunset.jpg', (1080, 1620), (0.42, 0.62), 84),
    ('karst-fog',       f'{SRC_A}/karst_fog.jpg',         (1000, 750),  (0.50, 0.50), 82),
    ('that-luang',      f'{SRC_B}/that_luang.jpg',        (1000, 664),  (0.50, 0.50), 84),
    ('haw-phra-kaew',   f'{SRC_B}/haw_phra_kaew.jpg',     (860, 860),   (0.50, 0.42), 82),
    ('tubing',          f'{SRC_A}/tubing_hi.jpg',         (1000, 667),  (0.50, 0.50), 82),
    ('kayak',           f'{SRC_A}/kayak_hi.jpg',          (1000, 667),  (0.50, 0.50), 82),
    ('mist',            f'{SRC_A}/mist_golden.jpg',       (1000, 667),  (0.50, 0.50), 82),
    ('paddy-bbq',       f'{SRC_A}/paddy_sunset.jpg',      (1000, 620),  (0.50, 0.55), 84),
    ('patuxai',         f'{SRC_B}/patuxai.jpg',           (1000, 750),  (0.50, 0.50), 84),
    ('buddha-park',     f'{SRC_B}/buddha_park.jpg',       (900, 1125),  (0.50, 0.50), 82),
    ('nam-song',        f'{SRC_B}/nam_song.jpg',          (1000, 563),  (0.50, 0.55), 84),
    ('karst-pano',      f'{SRC_A}/karst_pano_golden.jpg', (1000, 460),  (0.50, 0.55), 84),
    ('wat-si-saket',    f'{SRC_B}/wat_si_saket.jpg',      (900, 675),   (0.50, 0.50), 84),
    ('karst-sunrise',   f'{SRC_A}/karst_sunrise.jpg',     (1000, 563),  (0.50, 0.55), 84),
]


def crop_focus(im, ratio, focus):
    """Crop to `ratio` (w/h) as large as possible around the focus point."""
    w, h = im.size
    if w / h > ratio:
        cw, ch = int(h * ratio), h
    else:
        cw, ch = w, int(w / ratio)
    cx, cy = focus[0] * w, focus[1] * h
    left = min(max(0, cx - cw / 2), w - cw)
    top = min(max(0, cy - ch / 2), h - ch)
    return im.crop((int(left), int(top), int(left + cw), int(top + ch)))


def save(im, path, quality):
    im.convert('RGB').save(path, 'JPEG', quality=quality, optimize=True,
                           progressive=True, subsampling='4:2:0')
    kb = os.path.getsize(path) / 1024
    print(f'  {os.path.basename(path):24s} {im.size[0]}x{im.size[1]:<5d} {kb:6.0f} KB')
    return kb


total = 0
print('photos →', IMG)
for key, src, size, focus, q in JOBS:
    im = Image.open(src)
    im = ImageOps.exif_transpose(im)
    ratio = size[0] / size[1]
    im = crop_focus(im, ratio, focus)
    im = im.resize(size, Image.LANCZOS)
    total += save(im, f'{IMG}/{key}.jpg', q)

# Open Graph card — 1200x630, composed so the mountains and the walkway both read
og = Image.open(f'{SRC_A}/bridge_hut_sunset.jpg')
og = ImageOps.exif_transpose(og)
og = crop_focus(og, 1200 / 630, (0.50, 0.56)).resize((1200, 630), Image.LANCZOS)
total += save(og, f'{OUT}/og.jpg', 86)

# logos (transparent PNG, already colour variants)
for name in ('logo_white', 'logo_navy', 'logo_gold'):
    src = f'{LOGO}/{name}.png'
    dst_im = Image.open(src)
    dst_im.save(f'{OUT}/{name}.png', optimize=True)
    kb = os.path.getsize(f'{OUT}/{name}.png') / 1024
    total += kb
    print(f'  {name}.png{"":14s} {dst_im.size[0]}x{dst_im.size[1]:<5d} {kb:6.0f} KB')

print(f'total {total/1024:.2f} MB')
