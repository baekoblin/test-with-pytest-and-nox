# test_boundary_conditions.py
import pytest

@pytest.mark.parametrize("num, expected", [
    (0, True),
    (1, True),
    (-1, False),
])
def test_is_positive(num, expected):
    assert (num >= 0) == expected
