# CS50P Lecture 4 (Libraries) – Solutions

This folder contains my Python solutions for CS50P Lecture 4 (Libraries) exercises.

## Included (typical L4 set)
- adieu.py – Formats a farewell list with proper commas
- bitcoin.py – Fetches current Bitcoin price and multiplies by user-supplied amount
- emojize.py – Converts shortcode (e.g. :thumbsup:) to emoji using `emoji`
- professor.py – Little Professor math quiz (random sums, limited attempts)
- game.py – Number guessing game
- figlet.py – Renders text in ASCII art using the `pyfiglet` library

## Run
```bash
python filename.py
```
Some programs expect:
- Repeated input until EOF (Ctrl+D / Ctrl+Z+Enter on Windows)
- Command-line argument (e.g. bitcoin.py: amount of BTC)

## Notes
- Uses standard library (`random`, `sys`) plus third‑party libs (`requests`, `emoji`, `inflect`) where required.
- Prompts removed where CS50 tests expect no extra text.

## Environment
Python 3.11+ recommended. Install dependencies (if any):
```bash
pip install requests emoji inflect
```

## Purpose
Practice with:
- Third‑party libraries
- String formatting
- Input validation
- Loops and error handling