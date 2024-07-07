# test_various_inputs.py
import pytest

@pytest.mark.parametrize("input_str, expected", [
    ("hello", "HELLO"),
    ("world", "WORLD"),
    ("pytest", "PYTEST"),
])
def test_uppercase(input_str, expected):
    assert input_str.upper() == expected
