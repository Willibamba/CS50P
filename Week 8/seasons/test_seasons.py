from seasons import convert

# Test runs
def test_convert():
    assert convert("1999-09-20") == "Twelve million, one hundred nineteen thousand forty minutes"
    