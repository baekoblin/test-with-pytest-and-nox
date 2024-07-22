import unittest

class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(2 - 1, 1)

class TestExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setup for the class")

    @classmethod
    def tearDownClass(cls):
        print("Teardown for the class")

    def setUp(self):
        print("Setup for a test")

    def tearDown(self):
        print("Teardown for a test")

    def test_case1(self):
        self.assertTrue(True)

    def test_case2(self):
        self.assertTrue(True)

# Method 1: Running tests directly with unittest.main()
def run_directly():
    print("Running directly with unittest.main()")
    unittest.main()

# Method 2: Running tests with a custom test suite
def run_with_suite():
    print("Running with a custom test suite")
    suite = unittest.TestSuite()
    suite.addTest(TestMathOperations('test_addition'))
    suite.addTest(TestMathOperations('test_subtraction'))
    runner = unittest.TextTestRunner()
    runner.run(suite)

# Method 3: Running tests with TestLoader
def run_with_loader():
    print("Running with TestLoader")
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestMathOperations)
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    # Uncomment one of the following lines to run the corresponding method

    # Method 1
    run_directly()

    # Method 2
    run_with_suite()

    # Method 3
    run_with_loader()