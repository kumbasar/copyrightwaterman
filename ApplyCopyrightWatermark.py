#!/usr/bin/env python3

import glob
import os
import argparse

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

DEFAULT_COPYRIGHT_WATERMARK = '© Volkan Kumbasar'
DEFAULT_SHOW = 'store_true'
DEFAULT_INPUT_DIR = 'input'
DEFAULT_OUTPUT_DIR = 'output'
FONT = 'Fonts/Roboto-Black.ttf'
FONT_SIZE = 70


def copyright_apply(input_image_path, output_image_path, text, show):
    
    photo = Image.open(input_image_path)

    w, h = photo.size

    drawing = ImageDraw.Draw(photo)

    font = ImageFont.truetype(FONT, FONT_SIZE)

    text_w, text_h = drawing.textsize(text + " ", font)
    pos = w - text_w, (h - text_h) - 50

    c_text = Image.new('RGB', (text_w, (text_h)))
    drawing = ImageDraw.Draw(c_text)

    drawing.text((0,0), text, fill='#ffffff', font=font)
    c_text.putalpha(100)
  
    photo.paste(c_text, pos, c_text)
    if show:
        photo.show()
    photo.save(output_image_path)


parser = argparse.ArgumentParser(
                    formatter_class = argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-w", "--watermark", help = "Set copyright text", type = str,
                    default = DEFAULT_COPYRIGHT_WATERMARK)
parser.add_argument("-s", "--show", help = "Show watermarked image", action = DEFAULT_SHOW)
parser.add_argument("-o", "--output", help = "Output directory", type = str,
                    default = DEFAULT_OUTPUT_DIR)
parser.add_argument("-i", "--input", help = "Input directory", type = str,
                    default = DEFAULT_INPUT_DIR)

args = parser.parse_args()

photos = glob.glob(args.input + "/*.*")

if not os.path.exists(args.output):
    os.makedirs(args.output)

for photo in photos: 
    out = photo.replace(args.input, args.output)
    copyright_apply(photo, out, args.watermark, args.show)