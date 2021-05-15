#!/usr/bin/env python3
import unittest
from palindrome import is_palindrome

class PalindromeTests(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("safdasffsadfas"))
        self.assertFalse(is_palindrome("safdasffsadfaq"))
        self.assertFalse(is_palindrome("safdasfqsadfas"))
        self.assertTrue(is_palindrome("s"))
        self.assertTrue(is_palindrome("asa"))
        self.assertFalse(is_palindrome("sa"))

    def test_type(self):
        with self.assertRaises(TypeError):
            is_palindrome(2.)
        with self.assertRaises(TypeError):
            is_palindrome(8)

    def test_empty(self):
        with self.assertRaises(ValueError):
            is_palindrome("")

if __name__ == '__main__':
    unittest.main()
