# test_with_mock.py

import some_module  # 실제 모듈명을 사용하세요

def test_with_mock(mocker):
    mock = mocker.patch('some_module.Class.method')
    mock.return_value = 'mocked!'
    assert some_module.Class().method() == 'mocked!'
