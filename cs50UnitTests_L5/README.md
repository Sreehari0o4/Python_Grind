# CS50P Lecture 5 – Unit Tests (L5)

This folder contains my solutions and accompanying `pytest` tests for CS50P Lecture 5 (Unit Tests) problem set.

## Layout
```
cs50UnitTests_L5/
  bank/
    bank.py        # value(greeting) implementation
    test_bank.py   # tests for greeting value rules
  fuel/
    fuel.py        # convert(fraction) -> int percent, gauge(percent) -> string
    test_fuel.py   # tests for valid parsing, errors, and gauge edge cases
  plates/
    plates.py      # is_valid(plate) vanity plate validation
    test_plates.py # tests for length, format, digits placement, leading zero, punctuation
  twttr/
    twttr.py       # shorten(text) removes vowels only
    test_twttr.py  # tests preserving digits/punctuation & case handling
```

## Goals Covered
- Designing pure functions for easier testing
- Using `pytest` assertions and `pytest.raises` for exception checks
- Edge case coverage (boundary values, invalid input formats)
- Avoiding false positives by testing negative scenarios

## Running Tests
From repository root or this folder:
```bash
python -m pytest
```
Run a single module:
```bash
python -m pytest fuel/test_fuel.py
```
Show verbose output:
```bash
python -m pytest -v
```
Stop after first failure:
```bash
python -m pytest -x
```

## Test Highlights
- `bank`: Ensures correct integer returns (0 / 20 / 100), case-insensitive, ignores leading spaces, rejects mid-string "hello" as start.
- `fuel`: Confirms correct rounding, raises `ValueError` for invalid fractions or numerator>denominator, `ZeroDivisionError` for zero denominator, gauge edge outputs `E` (<=1%) and `F` (>=99%).
- `plates`: Validates length (2–6), first two letters, digits only at end, no leading zero in digit sequence, no punctuation/symbols.
- `twttr`: Verifies vowels (a e i o u in both cases) removed only; preserves digits, punctuation, other characters.

## Adding More Tests
1. Create a new folder with your module and a `test_*.py` file.
2. Import the target functions (pure functions preferred).
3. Add descriptive test function names (`test_...`).
4. Cover both success and failure paths.

## Tips
- Keep logic out of `main()` so tests import functions without executing I/O.
- Prefer small focused tests over one large multi-assert test.
- Run `python -m pytest -q` for quicker feedback.

## Dependencies
- Python 3.11+
- `pytest` (install with: `pip install pytest`)

---
Feel free to extend with coverage reports (`pip install pytest-cov`) later:
```bash
python -m pytest --cov=. --cov-report=term-missing
```
