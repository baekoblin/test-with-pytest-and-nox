# test_marker_basic.py
import pytest
import time

@pytest.mark.slow
def test_slow_function():
    time.sleep(5)
    assert True
