#!/usr/bin/env python3

from data import data

colors = {
    'B': 34,
    'W': 37,
    'G': 32,
    'Y': 33,
    'M': 35,
    'R': 31,
    'C': 36,
}
reset = 0

# iterate over rows
for row in data:
    # iterate over chunks in the row
    for chunk in row:
        # print chunk in selected color
        color = colors.get(chunk[1], colors['W'])
        print(f'\033[{color}m', end='')
        for char in range(chunk[0]):
            print('█', end='')
        print(f'\033[{reset}m', end='')

    # at the end of the row print a new line
    print('')
