#!/usr/bin/env python3
import unittest
from word_count import word_count

class WordCountTests(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(word_count("this is a duck"), 4)
        self.assertEqual(word_count(" "), 0)
        self.assertEqual(word_count("this is not a duck"), 5)
        self.assertEqual(word_count("One. Two. Three."), 3)

    def test_type(self):
        with self.assertRaises(TypeError):
            word_count(2.)
        with self.assertRaises(TypeError):
            word_count(8)

    def test_empty(self):
        with self.assertRaises(ValueError):
            word_count("")

if __name__ == '__main__':
    unittest.main()
