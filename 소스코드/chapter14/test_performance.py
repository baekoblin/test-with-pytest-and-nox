# test_performance.py

def some_function(*args, **kwargs):
    # 테스트할 실제 함수를 여기에 정의하세요
    return True

def test_performance(benchmark):
    result = benchmark(some_function)
    assert result == True
