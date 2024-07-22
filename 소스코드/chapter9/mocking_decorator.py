import unittest
from unittest.mock import patch

def get_data():
    return "Real Data"

class TestPatch(unittest.TestCase):

    @patch('__main__.get_data', return_value="Mock Data")
    def test_get_data(self, mock_get_data):
        self.assertEqual(get_data(), "Mock Data")

if __name__ == '__main__':
    unittest.main()