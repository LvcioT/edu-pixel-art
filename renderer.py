from collections.abc import Iterator
from itertools import chain, zip_longest

RESET = 0

_BASE_COLORS = (
    (0, 0, 0),
    (128, 0, 0),
    (0, 128, 0),
    (128, 128, 0),
    (0, 0, 128),
    (128, 0, 128),
    (0, 128, 128),
    (192, 192, 192),
    (128, 128, 128),
    (255, 0, 0),
    (0, 255, 0),
    (255, 255, 0),
    (0, 0, 255),
    (255, 0, 255),
    (0, 255, 255),
    (255, 255, 255),
)


def _pixel_codes(row: list[tuple[int, str]], colors: dict[str, int]) -> Iterator[int]:
    return chain.from_iterable(
        (colors[color_name] for _ in range(count))
        for count, color_name in row
    )


def _palette_rgb(index: int) -> tuple[int, int, int]:
    if index < 16:
        return _BASE_COLORS[index]
    if index < 232:
        levels = (0, 95, 135, 175, 215, 255)
        value = index - 16
        return (
            levels[value // 36],
            levels[value // 6 % 6],
            levels[value % 6],
        )
    gray = 8 + (index - 232) * 10
    return gray, gray, gray


def _print_palette_cell(index: int) -> None:
    red, green, blue = _palette_rgb(index)
    brightness = 0.299 * red + 0.587 * green + 0.114 * blue
    foreground = 0 if brightness >= 128 else 15
    print(
        f'\033[48;5;{index};38;5;{foreground}m{index:3}\033[{RESET}m',
        end=' ',
    )


def print_palette() -> None:
    print('Standard colors (0-15):')
    for row in range(2):
        for index in range(row * 8, row * 8 + 8):
            _print_palette_cell(index)
        print()

    levels = (0, 95, 135, 175, 215, 255)
    print('\nColor cube (green and blue rows, red columns):')
    print(f'{"Green":>5} {"Blue":>5} ' + ''.join(f'{red:>4}' for red in levels))
    for green_step, green in enumerate(levels):
        for blue_step, blue in enumerate(levels):
            print(f'{green:>5} {blue:>5} ', end='')
            for red_step in range(6):
                index = 16 + 36 * red_step + 6 * green_step + blue_step
                _print_palette_cell(index)
            print()

    print('\nGrayscale (232-255):')
    for row in range(2):
        for index in range(232 + row * 12, 232 + (row + 1) * 12):
            _print_palette_cell(index)
        print()


def render_art(colors: dict[str, int], rows: list[list[tuple[int, str]]]) -> None:
    for row_index in range(0, len(rows), 2):
        top_row = _pixel_codes(rows[row_index], colors)
        bottom_row = (
            _pixel_codes(rows[row_index + 1], colors)
            if row_index + 1 < len(rows)
            else iter(())
        )

        for top_color, bottom_color in zip_longest(top_row, bottom_row):
            if top_color is None:
                print(f'\033[38;5;{bottom_color};49m▄', end='')
            elif bottom_color is None:
                print(f'\033[38;5;{top_color};49m▀', end='')
            else:
                print(
                    f'\033[38;5;{top_color};48;5;{bottom_color}m▀',
                    end='',
                )
        print(f'\033[{RESET}m')
