# test_data_operations.py
import unittest
import pytest

@pytest.fixture
def setup_data():
    return {"key": "value"}

class TestDataOperations(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def _inject_fixtures(self, setup_data):
        self.data = setup_data

    def test_data_existence(self):
        self.assertIn("key", self.data)
        self.assertEqual(self.data["key"], "value")

# 필요할 경우, unittest.main()을 추가하여 unittest로도 실행 가능하게 설정
if __name__ == '__main__':
    unittest.main()
