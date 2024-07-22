# myplugin.py

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment to run tests against")

def pytest_configure(config):
    env = config.getoption("--env")
    print(f"Running tests in {env} environment")
