from numb3rs import validate

# Running tests on ip validation function in numb3rs.py
def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("cat") == False
    assert validate("1.512.512.0") == False
    assert validate("1000.21.255.255") == False
    assert validate("108") == False

