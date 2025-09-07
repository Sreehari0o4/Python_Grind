# CS50P Lecture 6 — File I/O (Solutions)

This folder contains my solutions for CS50P Lecture 6 (File I/O).

## Contents
- lines.py — Counts lines of code in a Python file (ignores blanks and comments)
- pizza.py — Prints a CSV as a table (uses tabulate)
- scourgify.py — Cleans “Last, First” names CSV into first/last/house columns
- shirt.py — Overlays a shirt image onto a photo (uses Pillow)

## Setup (Windows)
Install dependencies:
```bash
py -m pip install tabulate pillow
```

## Usage
- Count lines:
```bash
py lines.py program.py
```

- Tabulate CSV:
```bash
py pizza.py favorites.csv
```

- Clean names CSV:
```bash
py scourgify.py before.csv after.csv
```

- Apply shirt overlay:
```bash
py shirt.py input.jpg output.jpg
```

## Notes
- CSV write on Windows: open with newline="" to avoid extra blank lines.
- scourgify expects a header with columns including “name” and “house”; output header is first,last,house.
- shirt.py requires input/output to share the same extension; allowed: .jpg,