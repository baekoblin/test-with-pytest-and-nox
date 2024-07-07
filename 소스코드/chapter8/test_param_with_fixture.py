# test_param_with_fixture.py
import pytest

@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

def test_number(number):
    assert number in [1, 2, 3]
