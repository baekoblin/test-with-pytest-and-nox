from my_project.my_module.example import Example, external_function
import pytest

def test_method_mock(mocker):
    # Example 클래스의 method 메서드를 모킹합니다.
    mock = mocker.patch('my_project.my_module.example.Example.method')
    mock.return_value = 'mocked!'

    instance = Example()
    assert instance.method() == 'mocked!'

def test_external_function_mock(mocker):
    # my_project.my_module.example 모듈 내의 external_function 함수를 모킹합니다.
    mock = mocker.patch('my_project.my_module.example.external_function')
    mock.return_value = 'mocked external!'

    # 실제 호출되는 함수는 모킹된 함수여야 합니다.
    from my_project.my_module.example import external_function
    assert external_function() == 'mocked external!'

def test_attribute_mock(mocker):
    # Example 클래스의 속성을 모킹합니다.
    instance = Example()
    mocker.patch.object(instance, 'attribute', 'mocked attribute')

    assert instance.attribute == 'mocked attribute'


def test_method_call_verification(mocker):
    mock = mocker.patch('my_project.my_module.example.Example.method')

    instance = Example()
    instance.method()

    # 메서드가 호출되었는지 확인합니다.
    mock.assert_called_once()


def test_multiple_return_values(mocker):
    mock = mocker.patch('my_project.my_module.example.Example.method')
    mock.side_effect = ['first call', 'second call']

    instance = Example()
    assert instance.method() == 'first call'
    assert instance.method() == 'second call'


def test_raise_exception(mocker):
    mock = mocker.patch('my_project.my_module.example.Example.method')
    mock.side_effect = Exception('mocked exception')

    instance = Example()
    with pytest.raises(Exception, match='mocked exception'):
        instance.method()