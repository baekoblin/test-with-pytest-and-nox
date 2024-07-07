# test_skip.py
import pytest

@pytest.mark.skip(reason="not implemented yet")
def test_not_implemented():
    assert True
