# test_xfail.py
import pytest

@pytest.mark.xfail(reason="known bug")
def test_known_bug():
    assert False
