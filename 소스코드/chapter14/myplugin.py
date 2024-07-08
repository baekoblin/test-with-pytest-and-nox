# myplugin.py

import pytest

def pytest_addoption(parser):
    parser.addoption("--custom-option", action="store", default="default value", help="A custom option for Pytest")
    parser.addoption("--env", action="store", default="dev", help="Environment to run tests against")

def pytest_configure(config):
    custom_option = config.getoption("--custom-option")
    env = config.getoption("--env")
    print(f"Custom option value: {custom_option}")
    print(f"Running tests in {env} environment")

def pytest_collection_modifyitems(config, items):
    if config.getoption("--custom-option") == "skip":
        skip_marker = pytest.mark.skip(reason="Skipped by custom option")
        for item in items:
            item.add_marker(skip_marker)
