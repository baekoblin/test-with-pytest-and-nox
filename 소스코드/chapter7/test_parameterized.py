import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (1, 2, 3),
    (2, 2, 4),
])
def test_addition(a, b, expected):
    assert a + b == expected

@pytest.mark.parametrize("a", [0, 1])
@pytest.mark.parametrize("b", [2, 3])
def test_param_combination(a, b):
    assert (a + b) in [2, 3, 4]

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


@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

def test_number(number):
    assert number in [1, 2, 3]

@pytest.mark.parametrize("input_str, expected", [
    ("hello", "HELLO"),
    ("world", "WORLD"),
    ("pytest", "PYTEST"),
])
def test_uppercase(input_str, expected):
    assert input_str.upper() == expected

@pytest.mark.parametrize("num, expected", [
    (0, True),
    (1, True),
    (-1, False),
])
def test_is_positive(num, expected):
    assert (num >= 0) == expected
