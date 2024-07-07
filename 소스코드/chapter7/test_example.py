# test_example.py
import pytest
import os
import random
import requests
from dummy_database import connect_to_database, create_user, delete_user
from dummy_server import start_web_server

@pytest.fixture
def setup_database():
    db = connect_to_database()
    yield db
    db.close()

def test_database_query(setup_database):
    db = setup_database
    result = db.query("SELECT * FROM users")
    assert result is not None

@pytest.fixture
def setup_user(setup_database):
    db = setup_database
    user = create_user(db)
    yield user
    delete_user(db, user)

def test_user_creation(setup_database, setup_user):
    db = setup_database
    user = setup_user
    result = db.query(f"SELECT * FROM users WHERE id = {user['id']}")
    assert result is not None

@pytest.fixture(scope="module")
def setup_environment():
    os.environ['APP_ENV'] = 'test'
    yield
    os.environ.pop('APP_ENV')

@pytest.fixture(autouse=True)
def setup_autouse_environment():
    os.environ['APP_ENV'] = 'test'
    yield
    os.environ.pop('APP_ENV')

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

@pytest.fixture(scope="module")
def start_server():
    server = start_web_server()
    yield server
    server.stop()

def test_homepage(start_server):
    response = requests.get("http://localhost:8000")
    assert response.status_code == 200
