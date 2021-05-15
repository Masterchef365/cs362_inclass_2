#!/usr/bin/env python3
from palindrome import is_palindrome
import pytest

def test_palindrome():
    assert(is_palindrome("safdasffsadfas"))
    assert(not is_palindrome("safdasffsadfaq"))
    assert(not is_palindrome("safdasfqsadfas"))
    assert(is_palindrome("s"))
    assert(is_palindrome("asa"))
    assert(not is_palindrome("sa"))

def test_type():
    with pytest.raises(TypeError):
        is_palindrome(2.)
    with pytest.raises(TypeError):
        is_palindrome(8)

def test_empty():
    with pytest.raises(ValueError):
        is_palindrome("")

