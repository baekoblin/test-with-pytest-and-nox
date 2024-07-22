import pytest 

def assert_is_even(number):
    assert number % 2 == 0, f"Expected {number} to be even, but got {number}"

def test_even_number():
    ''' this is my awesome test '''

    assert_is_even(4)  # 통과
    assert_is_even(5)  # 실패


class CustomAssertions:
    @staticmethod
    def assert_is_positive(number):
        assert number > 0, f"Expected {number} to be positive, but got {number}"

def test_positive_number():
    CustomAssertions.assert_is_positive(10)  # 통과
    CustomAssertions.assert_is_positive(-5)  # 실패


def is_feature_available():
    return False  # 조건에 따라 동적 판단

def test_dynamic_skip():
    if not is_feature_available():
        pytest.skip("Feature not available")
    assert True


def is_known_issue():
    return True  # 조건에 따라 동적 판단

def test_dynamic_xfail():
    if is_known_issue():
        pytest.xfail("Known issue")
    assert False


import logging

def test_logging():
    logger = logging.getLogger(__name__)
    logger.info("This is a log message")
    assert True
