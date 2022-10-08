from jar import Jar
import pytest

def main():
      test_init()
      test_str()
      test_deposit()
      test_withdraw()

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    jar.size == 5

def test_withdraw():
    jar = Jar()
    jar.deposit(9)
    jar.withdraw(5)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.withdraw(10)
