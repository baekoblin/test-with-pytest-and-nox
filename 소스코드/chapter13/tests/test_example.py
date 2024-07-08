import pytest

@pytest.mark.slow
def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 3 == 2

@pytest.mark.run(order=1)
def test_first():
    assert True

@pytest.mark.run(order=2)
def test_second():
    assert True
