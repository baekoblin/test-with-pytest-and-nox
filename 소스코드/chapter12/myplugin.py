# myplugin.py
import pytest

def pytest_addoption(parser):
    parser.addoption("--custom-option", action="store", default="default value", help="A custom option for Pytest")

def pytest_configure(config):
    custom_option = config.getoption("--custom-option")
    print(f"Custom option value: {custom_option}")

def pytest_collection_modifyitems(config, items):
    if config.getoption("--custom-option") == "skip":
        skip_marker = pytest.mark.skip(reason="Skipped by custom option")
        for item in items:
            item.add_marker(skip_marker)
