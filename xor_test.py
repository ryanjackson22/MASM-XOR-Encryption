# xor_test.py

import unittest

from main import xor_encrypt, xor_encrypt_key


class MyTestCase(unittest.TestCase):
    def test_xor_encrypt(self):
        expected = '1(p1">5)'
        actual = xor_encrypt("Max Carney", 'P')
        self.assertEqual(actual, expected)

    def test_xor_decrypt(self):
        expected = "Max Carney"
        actual = xor_encrypt('1(p1">5)', 'P')
        self.assertEqual(actual, expected)

    def test_xor_encrypt_key(self):
        expected = '1(p1">5)'
        actual = xor_encrypt_key("Max Carney", "PPPPPPPPPP")
        self.assertEqual(actual, expected)

    def test_xor_decrypt_key(self):
        expected = "Max Carney"
        actual = xor_encrypt_key('1(p1">5)', "PPPPPPPPPP")
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
