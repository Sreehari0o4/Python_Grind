"""
shirt.py
A command-line utility that overlays a shirt image ("shirt.png") onto another image provided by the user.
The program resizes and crops the input image to match the shirt's dimensions, then pastes the shirt image on top.
It ensures that the input and output file extensions are valid and match, and handles common errors such as missing files or arguments.
Usage:
    python shirt.py <input_image> <output_image>
Arguments:
    input_image   Path to the input image file (.jpg, .jpeg, .png)
    output_image  Path to the output image file (.jpg, .jpeg, .png)
Raises:
    SystemExit: If arguments are missing, files do not exist, or file extensions are invalid/mismatched.
"""

import sys
from pathlib import Path
from PIL import Image, ImageOps

def main():
    try:
        inp, out = sys.argv[1], sys.argv[2]
        ext_i = Path(inp).suffix.lower()
        ext_o = Path(out).suffix.lower()
        if ext_i not in [".jpeg",".png", ".jpg"]:
            sys.exit("Invalid input")
        if ext_o not in [".jpeg",".png", ".jpg"]:
            sys.exit("Invalid output")
        if ext_i != ext_o:
            sys.exit("Input and  output have different extensions")
        mimage = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        isize = shirt.size
        cropped = ImageOps.fit(mimage, isize, method = Image.Resampling.BICUBIC, bleed = 0.0, centering = (0.5, 0.5))
        cropped.paste(shirt,shirt)
        cropped.save(f"{out}")

    except IndexError:
        sys.exit("Too few command-line arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")

main()
