# test_param_combination.py
import pytest

@pytest.mark.parametrize("a", [0, 1])
@pytest.mark.parametrize("b", [2, 3])
def test_param_combination(a, b):
    assert (a + b) in [2, 3, 4]
