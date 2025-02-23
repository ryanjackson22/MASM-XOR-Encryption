# xor_test.py

import unittest

from main import xor_encrypt

class MyTestCase(unittest.TestCase):
    def test_xor_encrypt(self):
        expected = '1(p1">5)'
        actual = xor_encrypt("Max Carney", 'P')
        self.assertEqual(actual, expected)

    def test_xor_decrypt(self):
        expected = "Max Carney"
        actual = xor_encrypt('1(p1">5)', 'P')
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
