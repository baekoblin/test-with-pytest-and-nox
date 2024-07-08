def pytest_addoption(parser):
    parser.addoption("--custom-option", action="store", default="default value", help="A custom option for Pytest")
    parser.addoption("--env", action="store", default="dev", help="Environment to run tests against")

def pytest_configure(config):
    env = config.getoption("--env")
    print(f"Running tests in {env} environment")
