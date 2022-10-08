from project import add, multiply, subtract, divide
import pytest

# Unit tests on funstions from project.py

def test_add():
    with pytest.raises(TypeError):
        assert add("2 + 2")

def test_multiply():
    with pytest.raises(TypeError):
        assert multiply("4 * 4")

def test_substract():
    with pytest.raises(TypeError):
        assert subtract("4 - 2")

def test_divide():
    with pytest.raises(TypeError):
        assert divide("4 * 4")