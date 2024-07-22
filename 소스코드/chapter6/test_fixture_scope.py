
# test_fixture_scope.py

import pytest
from unittest.mock import MagicMock

# fixture 정의
@pytest.fixture(scope="function")
def sample_function_scope_fixture():
    print("\\nSetup: function scope fixture")
    yield
    print("Teardown: function scope fixture")

@pytest.fixture(scope="class")
def sample_class_scope_fixture():
    print("\\nSetup: class scope fixture")
    yield
    print("Teardown: class scope fixture")

@pytest.fixture(scope="module")
def sample_module_scope_fixture():
    print("\\nSetup: module scope fixture")
    yield
    print("Teardown: module scope fixture")

@pytest.fixture(scope="session")
def sample_session_scope_fixture():
    print("\\nSetup: session scope fixture")
    yield
    print("Teardown: session scope fixture")

# fixture 적용 예제
def test_example_function_scope(sample_function_scope_fixture):
    print("Executing test_example_function_scope")

class TestExampleClass:
    def test_example_class_scope_1(self, sample_class_scope_fixture):
        print("Executing test_example_class_scope_1")

    def test_example_class_scope_2(self, sample_class_scope_fixture):
        print("Executing test_example_class_scope_2")

def test_example_module_scope(sample_module_scope_fixture):
    print("Executing test_example_module_scope")

def test_example_session_scope(sample_session_scope_fixture):
    print("Executing test_example_session_scope")

