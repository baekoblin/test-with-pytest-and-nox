# test_grouping.py
import pytest
from dummy_database import connect_to_database

@pytest.mark.database
def test_database_insert():
    db = connect_to_database()
    db.insert("INSERT INTO users (name) VALUES ('Alice')")
    result = db.query("SELECT * FROM users WHERE name = 'Alice'")
    assert result is not None

@pytest.mark.database
def test_database_delete():
    db = connect_to_database()
    db.delete("DELETE FROM users WHERE name = 'Alice'")
    result = db.query("SELECT * FROM users WHERE name = 'Alice'")
    assert result is None

# 더미 데이터베이스 연결 함수
class DummyDB:
    def __init__(self):
        self.data = {}

    def connect(self):
        return self

    def query(self, sql):
        if "SELECT" in sql:
            return [{"name": "Alice"}] if "Alice" in sql else None
        return None

    def insert(self, sql):
        print(f"Executed query: {sql}")

    def delete(self, sql):
        print(f"Executed query: {sql}")

def connect_to_database():
    return DummyDB().connect()
