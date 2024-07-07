# test_combined.py
import unittest
import pytest

class TestMathOperations(unittest.TestCase):

    @pytest.mark.slow
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(2 - 1, 1)
