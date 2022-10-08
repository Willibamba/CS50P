from fuel import gauge, convert
import pytest

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"

def test_convert():
    assert convert("2/3") == 67
    assert convert("1/4") == 25
    with pytest.raises(ValueError):
        convert("one/three")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")