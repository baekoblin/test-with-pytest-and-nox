# dummy_database.py
class DummyDB:
    def __init__(self):
        self.data = {}

    def connect(self):
        return self

    def close(self):
        pass

    def is_connected(self):
        return True

    def query(self, sql):
        if "SELECT" in sql:
            return [{"name": "Alice"}] if "Alice" in sql else None
        return None

    def insert(self, sql):
        self.data["Alice"] = "Inserted"
        print(f"Executed query: {sql}")

    def delete(self, sql):
        if "Alice" in self.data:
            del self.data["Alice"]
        print(f"Executed query: {sql}")

def connect_to_database():
    return DummyDB().connect()
