"""
File: anagrams.py
Author: Leah Tajon

Challenge #9: Anagrams

Assignment: Two strings are anagrams if you make one from
the other by rearranging the letters.

Write a function named is_anagram that takes two string as its
parameters. Your function should return True if the strings are
anagrams, and False otherwise.

For example, the call is_anagram("typhoon","opython") should return
True while the call is_anagram("Alice", "Bob") should return False.
"""

def is_anagram(a, b):
    sort_a = ''.join(sorted(a, key=str.lower))
    sort_b = ''.join(sorted(b, key=str.lower))

    if sort_a.lower() == sort_b.lower():
        return True
    return False
    
sort_1 = is_anagram("Typhoon","opython")
print(sort_1)
sort_2 = is_anagram("Alice","Bob")
print(sort_2)