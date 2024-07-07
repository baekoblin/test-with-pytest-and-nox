# dummy_database.py
class DummyDatabase:
    def __init__(self):
        self.data = {}

    def connect(self):
        print("Database connected")
        return self

    def close(self):
        print("Database closed")

    def query(self, sql):
        if sql == "SELECT * FROM users":
            return [{"id": 1, "name": "Alice"}]
        return None

    def insert(self, sql):
        print(f"Executed query: {sql}")

def connect_to_database():
    db = DummyDatabase()
    return db.connect()

def create_user(db=None):
    return {"id": 1, "name": "Alice"}

def delete_user(db, user):
    print(f"User {user['name']} deleted")
