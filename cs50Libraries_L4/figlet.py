"""
Program Description:
This script renders user-inputted text in ASCII art using the pyfiglet library. 
It allows the user to specify a font via command-line arguments (-f or --font), 
or randomly selects a font if no font is specified. If an invalid font or incorrect 
usage is detected, the program exits with an error message.
Usage:
    python figlet.py                # Uses a random font
    python figlet.py -f <fontname>  # Uses the specified font
    python figlet.py --font <fontname>  # Uses the specified font
Prompts the user for input and prints the ASCII art representation of the input text.
"""

import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

if len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        fnt = sys.argv[2]
        fonts = figlet.getFonts()
        if fnt not in fonts:
            sys.exit("Invalid usage")
        figlet.setFont(font = fnt)
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    fonts = figlet.getFonts()
    fnt = random.choice(fonts)
    figlet.setFont(font = fnt)
else:
    sys.exit("Invalid usage")

word = input("Input: ")
print(figlet.renderText(word))