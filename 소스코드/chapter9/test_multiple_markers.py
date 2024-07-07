import pytest
from dummy_database import connect_to_database

@pytest.mark.slow
@pytest.mark.database
def test_database_function():
    db = connect_to_database()
    assert db.is_connected()

# 더미 데이터베이스 연결 함수
def connect_to_database():
    class DummyDB:
        def is_connected(self):
            return True
    return DummyDB()