import pytest
from calculator import add, subtract, multiply, division


def test_add():
    assert add(2, 3) == 5
    assert add(0, 5) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 7) == 3

def test_multiply():
    assert multiply(4, 3) == 12

def test_division():
    assert division(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        division(10, 0)
    