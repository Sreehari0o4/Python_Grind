from bank import value

def test_hello():
    assert value("Hello, my dear") == 0
    assert value("hello") == 0
    assert value("   hello , world") == 0

def test_h():
    assert value("h") == 20
    assert value("hai") == 20
    assert value("  how are you?") == 20

def test_other():
    assert value("Whats, Up!!") == 100
    assert value("sorry") == 100
    assert value("4 is a number") == 100