# test_conditional_execution_with_marker.py
import pytest
from dummy_database import connect_to_database

@pytest.mark.skipif(not connect_to_database().is_connected(), reason="database not connected")
def test_database_connection():
    assert connect_to_database().is_connected()

# 더미 데이터베이스 연결 함수
class DummyDB:
    def is_connected(self):
        return True

def connect_to_database():
    return DummyDB()
