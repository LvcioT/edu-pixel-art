from data import data
# from colorama import Fore, Back, Style
from termcolor import colored

# iterate over rows
for row in data:
    # iterate over chunks in the row
    for chunk in row:
        # check the color
        if chunk[1] == 'B':
            color = 'blue'
        elif chunk[1] == 'W':
            color = 'white'
        elif chunk[1] == 'G':
            color = 'green'
        elif chunk[1] == 'Y':
            color = 'yellow'
        elif chunk[1] == 'M':
            color = 'magenta'
        elif chunk[1] == 'R':
            color = 'red'
        elif chunk[1] == 'C':
            color = 'cyan'
        else:
            color = 'white'

        # print chunk in selected color
        for char in range(chunk[0]):
            print(colored('█', color), end='')

    # at the end of the row print a new line
    print('')
