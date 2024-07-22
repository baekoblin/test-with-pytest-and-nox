# conftest.py

def pytest_addoption(parser):
    parser.addoption("--custom-option", action="store", default="default value", help="A custom option for Pytest")

pytest_plugins = ["myplugin"]
