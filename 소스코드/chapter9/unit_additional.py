import unittest
from unittest.mock import patch
import requests

class TestExceptionHandling(unittest.TestCase):

    def test_raise_exception(self):
        with self.assertRaises(ValueError):
            raise ValueError("This is a ValueError")


def get_github_user(username):
    response = requests.get(f"<https://api.github.com/users/{username}>")
    return response.json()

class TestGitHubAPI(unittest.TestCase):

    @patch('requests.get')
    def test_get_github_user(self, mock_get):
        mock_get.return_value.json.return_value = {"login": "octocat"}
        user = get_github_user("octocat")
        self.assertEqual(user["login"], "octocat")

if __name__ == '__main__':
    unittest.main()
