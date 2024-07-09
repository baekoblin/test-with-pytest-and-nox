# test_assert_helpers.py

def assert_is_even(number):
    assert number % 2 == 0, f"Expected {number} to be even, but got {number}"

def test_even_number():
    assert_is_even(4)  # 통과
    assert_is_even(5)  # 실패

class CustomAssertions:
    @staticmethod
    def assert_is_positive(number):
        assert number > 0, f"Expected {number} to be positive, but got {number}"

def test_positive_number():
    CustomAssertions.assert_is_positive(10)  # 통과
    CustomAssertions.assert_is_positive(-5)  # 실패
