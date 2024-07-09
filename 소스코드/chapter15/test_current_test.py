# test_current_test.py

import pytest

def pytest_runtest_setup(item):
    print(f"Running test: {item.nodeid}")

def test_sample():
    assert True
