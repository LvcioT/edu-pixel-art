#!/usr/bin/env python3

import argparse
from pathlib import Path

from art_parser import load_art
from renderer import render_art


def main():
    parser = argparse.ArgumentParser(description='Render pixel art from a text file.')
    parser.add_argument('filename', type=Path, help='path to the pixel-art text file')
    args = parser.parse_args()

    try:
        colors, data = load_art(args.filename)
        render_art(colors, data)
    except (OSError, ValueError) as error:
        parser.error(str(error))


if __name__ == '__main__':
    main()
