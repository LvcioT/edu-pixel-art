#!/usr/bin/env python3

import argparse
from pathlib import Path

from art_parser import load_art
from renderer import print_palette, render_art


def main():
    parser = argparse.ArgumentParser(
        description='Render pixel art or print the xterm-256 color palette.'
    )
    parser.add_argument(
        'filename',
        type=Path,
        nargs='?',
        help='path to the pixel-art text file',
    )
    parser.add_argument(
        '--palette',
        action='store_true',
        help='print the xterm-256 color palette',
    )
    args = parser.parse_args()

    if args.palette:
        if args.filename is not None:
            parser.error('filename cannot be used with --palette')
        print_palette()
        return
    if args.filename is None:
        parser.error('filename is required unless --palette is used')

    try:
        colors: dict[str, int]
        data: list[list[tuple[int, str]]]
        colors, data = load_art(args.filename)
        render_art(colors, data)
    except (OSError, ValueError) as error:
        parser.error(str(error))


if __name__ == '__main__':
    main()
