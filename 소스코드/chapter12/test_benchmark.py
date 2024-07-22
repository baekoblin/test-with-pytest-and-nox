import pytest

def some_function(*args, **kwargs):
    # 함수의 구현
    return "result"

def test_performance(benchmark):
    args = ()  # 테스트에 사용할 인수
    kwargs = {}  # 테스트에 사용할 키워드 인수
    expected = "result"  # 예상 결과

    result = benchmark(some_function, *args, **kwargs)
    assert result == expected
