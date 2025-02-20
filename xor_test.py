import unittest

from main import xor_encrypt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        expected = '1(p1">5)'
        actual = xor_encrypt("Max Carney")
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
