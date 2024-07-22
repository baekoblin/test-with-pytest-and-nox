import pytest

@pytest.mark.run(order=1)
def test_first():
    assert True

@pytest.mark.run(order=2)
def test_second():
    assert True
