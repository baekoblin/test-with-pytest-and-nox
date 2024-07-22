# tests/test_example.py
from example import add
import pytest
def test_add():
    assert add(1, 2) == 3

def test_add2():
    assert add(2, 2) == 4


def test_with_mock(mocker):
    mock = mocker.patch('module.Class.method')
    mock.return_value = 'mocked!'
    assert module.Class().method() == 'mocked!'
