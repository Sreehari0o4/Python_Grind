from twttr import shorten

def test_lower():
    assert shorten("there are four people") == "thr r fr ppl"
    assert shorten("shape of you") == "shp f y"

def test_upper():
    assert shorten("THERE ARE FOUR PEOPLE") == "THR R FR PPL"
    assert shorten("SHAPE OF YOU") == "SHP F Y"

def test_mixed():
    assert shorten("There Are Four People") == "Thr r Fr Ppl"
    assert shorten("Shape Of You") == "Shp f Y"

def test_numbers():
    assert shorten("CS50 2025") == "CS50 2025"
    assert shorten("A1E2I3O4U5") == "12345"

def test_punctuation():
    assert shorten("Hello, world!") == "Hll, wrld!"
    assert shorten("What's up?") == "Wht's p?"
    assert shorten("Twttr!!!???") == "Twttr!!!???"
