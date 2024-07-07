# test_conditional_execution.py
import pytest
import sys
from dummy_database import connect_to_database

@pytest.mark.skipif(sys.platform == "win32", reason="does not run on Windows")
def test_not_on_windows():
    assert True
