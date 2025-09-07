"""
Program Details:
----------------
This script counts the number of non-blank, non-comment lines in a given Python (.py) file.
It expects exactly one command-line argument: the filename of the Python file to analyze.
Usage:
    python lines.py <filename.py>
Features:
- Checks for correct number of command-line arguments.
- Ensures the provided file has a '.py' extension.
- Ignores blank lines and lines starting with '#' (comments).
- Handles file not found and argument errors gracefully.
Exits with an error message if:
- Too many or too few command-line arguments are provided.
- The file does not have a '.py' extension.
- The specified file does not exist.
"""

import sys


def main():
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        fname = sys.argv[1]
        if not fname.endswith('py'):
            sys.exit("Not a python file")
        with open(f"{fname}","r") as file:
            lines = file.readlines()
            count = 0
            for line in lines:
                line = line.strip()
                if line == '' or line.startswith('#'):
                    continue
                else:
                    count+=1
            print(count)
    except IndexError:
        sys.exit("Too few command-line arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")

main()