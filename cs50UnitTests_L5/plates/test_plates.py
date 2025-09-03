from plates import is_valid

def test_valid():
    assert is_valid("aa") == True
    assert is_valid("aaa222") == True
    assert is_valid("CS50") == True

def test_invalid():
    assert is_valid("AAA22A") == False
    assert is_valid("CS05") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("23") == False
