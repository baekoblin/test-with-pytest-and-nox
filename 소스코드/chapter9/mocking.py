from unittest.mock import Mock

mock = Mock()
mock.method.return_value = 3
print(mock.method())  # 출력: 3

mock.method_with_exception.side_effect = Exception("Error")
try:
    mock.method_with_exception()
except Exception as e:
    print(e)  # 출력: Error

