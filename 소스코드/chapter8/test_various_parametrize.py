# test_various_parametrize.py
import pytest

def idfn(fixture_value):
    return f"value={fixture_value}"

@pytest.mark.parametrize("x", range(3), ids=idfn)
def test_with_function_ids(x):
    assert x < 3

@pytest.mark.parametrize("x, y", [
    pytest.param(1, 2, id="one_plus_two"),
    pytest.param(3, 4, id="three_plus_four"),
])
def test_with_param(x, y):
    assert x + y in [3, 7]
