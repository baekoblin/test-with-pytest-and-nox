# test_basic_parametrize.py
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (1, 2, 3),
    (2, 2, 4),
])
def test_addition(a, b, expected):
    assert a + b == expected

@pytest.mark.parametrize("x, y, z", [
    (1, 2, 3),
    (4, 5, 9),
    (10, 20, 30),
])
def test_addition_multiple(x, y, z):
    assert x + y == z
