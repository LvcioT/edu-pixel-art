from collections.abc import Iterator
from itertools import chain, zip_longest

RESET = 0


def _background_code(color_code: int) -> int:
    if 30 <= color_code <= 37 or 90 <= color_code <= 97:
        return color_code + 10
    raise ValueError(f'ANSI color code {color_code} cannot be used as a background')


def _pixel_codes(row: list[tuple[int, str]], colors: dict[str, int]) -> Iterator[int]:
    return chain.from_iterable(
        (colors[color_name] for _ in range(count))
        for count, color_name in row
    )


def render_art(colors: dict[str, int], rows: list[list[tuple[int, str]]]) -> None:
    background_codes = {
        color_code: _background_code(color_code)
        for color_code in set(colors.values())
    }

    for row_index in range(0, len(rows), 2):
        top_row = _pixel_codes(rows[row_index], colors)
        bottom_row = (
            _pixel_codes(rows[row_index + 1], colors)
            if row_index + 1 < len(rows)
            else iter(())
        )

        for top_color, bottom_color in zip_longest(top_row, bottom_row):
            if top_color is None:
                print(f'\033[{bottom_color};49m▄', end='')
            elif bottom_color is None:
                print(f'\033[{top_color};49m▀', end='')
            else:
                print(
                    f'\033[{top_color};{background_codes[bottom_color]}m▀',
                    end='',
                )
        print(f'\033[{RESET}m')
