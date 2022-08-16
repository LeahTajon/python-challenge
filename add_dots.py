"""
File: add_dots.py
Author: Leah Tajon

Challenge #7: Adding and removing dots

Assignment: Write a function named add_dots that takes a string
and adds "." in between each letter. For example, calling add_dots("test")
should return the string "t.e.s.t"

Then, below the add_dots function, write another function named
remove_dots that removes all dots from a string. For example, calling
remove_dots("t.e.s.t") should return "test".

If both functions are correct, calling remove_dots(add_dots(string))
should return back the original string for any string.

(You may assume that the input to add_dots does not itself contain
any dots.)
"""

def add_dots(word):
    new_word = '.'
    return new_word.join(word)

def remove_dots(word):
    new_word = word.replace('.','')
    return new_word

ans1 = add_dots("test")
print(ans1)
ans2 = remove_dots("t.e.s.t")
print(ans2)

ans3 = remove_dots(add_dots("test"))
print(ans3)