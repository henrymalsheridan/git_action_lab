import unittest

class TestSimple(unittest.TestCase):
    def test_pass(self):
        """This is a simple test that just passes."""
        print("Hello world from the test!")
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()