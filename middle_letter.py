"""
File: middle_letter.py
Author: Leah Tajon

Challenge: Middle letter

Assignment: Write a function named mid that takes a string as its 
parameter. Your function should extract and return the middle letter.
If there is no middle letter, your function should return the empty
string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".
"""

def mid(letters):
    length = len(letters)
    half = length % 2
    
    if half == 0:
        result = ""
    elif half == 1:
        center = int(length / 2)
        result = letters[center]
    
    return result
       
middle_letter1 = mid("abc")
middle_letter2 = mid("aaaa")

print(middle_letter1)
print(middle_letter2)
