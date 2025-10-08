#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Github: KairaBegudiri
GPL3
"""

import math
import random
import numpy as np
import time
import os
from PIL import Image, ImageDraw

def lerp(a, b, t): return a + t * (b - a)
def fade(t): return t * t * t * (t * (t * 6 - 15) + 10)

def value_noise_2d(x, y, perm):
    xi = int(math.floor(x)) & 255
    yi = int(math.floor(y)) & 255
    xf = x - math.floor(x)
    yf = y - math.floor(y)
    aa = perm[(perm[xi] + yi) & 255]
    ab = perm[(perm[xi] + yi + 1) & 255]
    ba = perm[(perm[xi + 1] + yi) & 255]
    bb = perm[(perm[xi + 1] + yi + 1) & 255]
    va = (aa & 255) / 255.0
    vb = (ab & 255) / 255.0
    vc = (ba & 255) / 255.0
    vd = (bb & 255) / 255.0
    u = fade(xf)
    v = fade(yf)
    x1 = lerp(va, vc, u)
    x2 = lerp(vb, vd, u)
    return lerp(x1, x2, v)

def fractal_noise(width, height, seed, scale=0.03, octaves=5, persistence=0.5, lacunarity=2.0, live=False):
    rnd = random.Random(seed)
    perm = list(range(256))
    rnd.shuffle(perm)
    perm += perm
    arr = np.zeros((height, width), dtype=float)
    max_amp = 0.0
    amplitude = 1.0
    frequency = 1.0
    for octave in range(octaves):
        for j in range(height):
            for i in range(width):
                x = i * scale * frequency
                y = j * scale * frequency
                arr[j,i] += value_noise_2d(x, y, perm) * amplitude
        max_amp += amplitude
        amplitude *= persistence
        frequency *= lacunarity

        if live: 
            os.system("clear")
            print(f"🌍 Noise is being created... Octave {octave+1}/{octaves}")
            show_ascii(arr / max_amp)
            time.sleep(0.5)

    arr /= max_amp
    arr = (arr - arr.min()) / (arr.max() - arr.min() + 1e-9)
    return arr

BIOME_TILES = [
    (0.00, '~'),
    (0.15, ','),
    (0.30, '"'),
    (0.45, '.'),
    (0.60, '^'),
    (0.78, 'A'),
    (0.90, '#'),
]

def height_to_tile(h):
    for thresh, ch in BIOME_TILES:
        if h < thresh:
            return ch
    return BIOME_TILES[-1][1]

def show_ascii(arr):
    for row in arr:
        print("".join(height_to_tile(v) for v in row))

def save_preview_image(arr, path='world_preview.png', cell=4):
    h, w = arr.shape
    img = Image.new('RGB', (w*cell, h*cell))
    draw = ImageDraw.Draw(img)
    for j in range(h):
        for i in range(w):
            v = arr[j,i]
            if v < 0.15: color = (10, 30, 140)
            elif v < 0.30: color = (50, 100, 200)
            elif v < 0.40: color = (240, 225, 140)
            elif v < 0.60: color = (50, 180, 60)
            elif v < 0.78: color = (120, 100, 60)
            elif v < 0.90: color = (120, 120, 120)
            else: color = (240, 240, 255)
            draw.rectangle([i*cell, j*cell, (i+1)*cell-1, (j+1)*cell-1], fill=color)
    img.save(path)
    return path

def demo(width=100, height=50, scale=0.04, octaves=6, live=True):
    seed = random.randint(0, 999999)
    print(f"🌱 Random seed: {seed}")
    arr = fractal_noise(width, height, seed, scale=scale, octaves=octaves, live=live)
    os.system("clear")
    print("🌏 Map:")
    show_ascii(arr)
    save_preview_image(arr)
    print("\n🖼️ PNG saved: world_preview.png")

if __name__ == "__main__":
    demo()
