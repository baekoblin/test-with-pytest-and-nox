import unittest

class TestMathOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(2 - 1, 1)

import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)


import pytest
import unittest

@pytest.fixture
def setup_data():
    return {"key": "value"}

class TestDataOperations(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def inject_fixtures(self, setup_data):
        self.setup_data = setup_data

    def test_data_existence(self):
        self.assertIn("key", self.setup_data)
        self.assertEqual(self.setup_data["key"], "value")


import unittest
from unittest.mock import MagicMock

class TestDatabaseOperations(unittest.TestCase):

    def test_database_insert(self):
        db = MagicMock()
        db.insert.return_value = True
        self.assertTrue(db.insert("INSERT INTO users (name) VALUES ('Alice')"))

    def test_database_query(self):
        db = MagicMock()
        db.query.return_value = [{'id': 1, 'name': 'Alice'}]
        result = db.query("SELECT * FROM users WHERE name = 'Alice'")
        self.assertIsNotNone(result)
        self.assertEqual(result[0]['name'], 'Alice')

if __name__ == '__main__':
    unittest.main()
