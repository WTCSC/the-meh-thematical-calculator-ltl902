import pytest
from meh_thematical_calc import add, subtract, multiply, divide, power, errors

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(0.00000000000000000000000000000000000000000000000000001, 0.00000000000000000000000000000000000000000000000000002) == 0.00000000000000000000000000000000000000000000000000003
    assert add(-1000, 500) == -500
    assert add(10000, 2500) == 12500
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 0) == 0
def test_divide():
    assert divide(6, 3) == 2
    assert divide(-4, 2) == -2
    assert divide(5, 1) == 5
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(3, 2) == 9
