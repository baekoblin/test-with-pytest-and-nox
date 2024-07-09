# conftest.py

import pytest

def pytest_configure(config):
    if not hasattr(config, '_metadata'):
        config._metadata = {}
    config._metadata['Project Name'] = 'My Project'
    config._metadata['Tester'] = 'John Doe'
