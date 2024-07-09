# test_report.py

import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config._metadata['Project Name'] = 'My Project'
    config._metadata['Tester'] = 'John Doe'

def test_sample():
    assert True
