# # conftest.py

# import pytest

# def pytest_configure(config):
#     if not hasattr(config, 'metadata'):
#         config.metadata = {}
#     config.metadata['Project Name'] = 'My Project'
#     config.metadata['Tester'] = 'John Doe'


# conftest.py

# import pytest

# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     if not hasattr(config, 'metadata'):
#         config.metadata = {}
#     config.metadata['Project Name'] = 'My Project'
#     config.metadata['Tester'] = 'John Doe'


# # conftest.py


# def pytest_runtest_setup(item):
#     print(f"Running test: {item.nodeid}")
