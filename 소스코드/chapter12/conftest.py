import pytest

@pytest.fixture
def env(request):
    return request.config.getoption("--env")

pytest_plugins = ["myplugin"]
