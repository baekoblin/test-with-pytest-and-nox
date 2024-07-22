from unittest.mock import MagicMock

magic = MagicMock()
magic.__str__.return_value = "MagicMock"
print(str(magic))  # 출력: MagicMock

mock = MagicMock()
mock.method(1, 2, 3)
mock.method.assert_called_with(1, 2, 3)
mock.method.assert_called_once_with(1, 2, 3)
# mock.method.assert_not_called()  # AssertionError 발생
