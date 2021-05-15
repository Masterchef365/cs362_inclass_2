#!/usr/bin/env python3
def word_count(s):
    if not isinstance(s, str):
        raise TypeError("Only strings can be passed to word_count")
    if not s:
        raise ValueError("Only non-empty strings can be passed to word_count")
    return len(s.split())

if __name__ == '__main__':
    s = input("Please enter a string: ")
    k = word_count(s)
    print(f"\"{s}\" has {k} words")
