from plates import is_valid

def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("AAA222") == True
    assert is_valid("50") == False
    assert is_valid("C") == False
    assert is_valid("CS05") == False
    assert is_valid("AAA22A") == False
    assert is_valid("no.period space!") == False
