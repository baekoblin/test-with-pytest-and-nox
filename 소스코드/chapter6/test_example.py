import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_database():
    db = MagicMock()
    db.query.return_value = [{'id': 1, 'name': 'Alice'}]
    yield db

def test_database_query(mock_database):
    db = mock_database
    result = db.query("SELECT * FROM users")
    assert result is not None
    assert result[0]['name'] == 'Alice'

@pytest.fixture
def mock_user(mock_database):
    db = mock_database
    user = MagicMock()
    user.id = 1
    user.name = 'Alice'
    yield user

def test_user_creation(mock_database, mock_user):
    db = mock_database
    user = mock_user
    result = db.query(f"SELECT * FROM users WHERE id = {user.id}")
    assert result is not None
    assert result[0]['name'] == 'Alice'

import os

@pytest.fixture(autouse=True)
def setup_environment():
    # 환경 변수 설정
    os.environ['APP_ENV'] = 'test'
    yield
    # 환경 변수 정리
    os.environ.pop('APP_ENV')

import random

@pytest.fixture
def random_number():
    return random.randint(1, 100)

def test_random_number(random_number):
    assert 1 <= random_number <= 100

@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

def test_number(number):
    assert number in [1, 2, 3]


def test_database_insert(mock_database):
    db = mock_database
    db.insert("INSERT INTO users (name) VALUES ('Alice')")
    result = db.query("SELECT * FROM users WHERE name = 'Alice'")
    assert result is not None
    assert result[0]['name'] == 'Alice'


import requests
from unittest.mock import MagicMock

@pytest.fixture(scope="module")
def mock_server():
    server = MagicMock()
    server.get.return_value = MagicMock(status_code=200, text='Hello, World!')
    yield server

def test_homepage(mock_server):
    server = mock_server
    response = server.get("<http://localhost:8000>")
    assert response.status_code == 200
    assert response.text == 'Hello, World!'
