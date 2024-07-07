# test_parametrize_with_marker.py
import pytest

@pytest.mark.parametrize("x, y, result", [
    (1, 2, 3),
    pytest.param(1, 1, 3, marks=pytest.mark.xfail),
])
def test_addition(x, y, result):
    assert x + y == result
