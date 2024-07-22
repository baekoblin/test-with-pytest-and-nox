import pytest

def test_basic_assertion():
    assert 1 + 1 == 2
    assert 2 * 2 == 4
    assert 3 - 1 == 2

def test_comparison_assertion():
    assert 3 > 2
    assert 2 < 3
    assert 2 >= 2
    assert 2 <= 2

def test_membership_assertions():
    assert "h" in "hello"
    assert 3 in [1,2,3]

def test_exception_assertion():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_type_assertion():
    assert isinstance(123, int)
    assert isinstance("hello", str)

def test_float_comparison():
    assert 0.1 + 0.2 == pytest.approx(0.3)


def assert_is_even(number):
    assert number % 2 == 0, f"Expected {number} to be even"

def test_custum_assertion():
    assert_is_even(4)
    assert_is_even(5)

class CustomAssertions:
    @staticmethod
    def assert_is_positive(number):
        assert number > 0, f"Expected {number} to be positive"

    @staticmethod
    def assert_is_negative(number):
        assert number < 0, f"Expected {number} to be negative"

def test_custom_assertion_class():
    CustomAssertions.assert_is_positive(10)  # 통과
    CustomAssertions.assert_is_negative(-5)  # 통과
    CustomAssertions.assert_is_positive(-3)  # 실패, AssertionError 발생
