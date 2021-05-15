#!/usr/bin/env python3
from word_count import word_count
import pytest

def test_word_count():
    assert(word_count("this is a duck") == 4)
    assert(word_count(" ") == 0)
    assert(word_count("this is not a duck") == 5)
    assert(word_count("One. Two. Three.") == 3)

def test_type():
    with pytest.raises(TypeError):
        word_count(2.)
    with pytest.raises(TypeError):
        word_count(8)

def test_empty():
    with pytest.raises(ValueError):
        word_count("")

