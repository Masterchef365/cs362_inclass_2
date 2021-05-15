#!/usr/bin/env python3
def is_palindrome(s):
    if not isinstance(s, str):
        raise TypeError("Only strings can be passed to is_palindrome")
    if not s:
        raise ValueError("Only non-empty strings can be passed to is_palindrome")
    return all([s[i] == s[-(i+1)] for i in range(len(s) // 2)])


if __name__ == '__main__':
    s = input("Please enter a string: ")
    if is_palindrome(s):
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")
