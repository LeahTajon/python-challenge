"""
File: type_check.py
Author: Leah Tajon

Challenge #5: Type check

Assignment: Write a function name only_ints that takes two
parameters. Your function should return True if both parameters
are integers, and False otherwise.
"""

def only_ints(num1, num2):
    if type(num1) == int and type(num2) == int:
        result = True
    else:
        result = False
    return result

ans = only_ints('a', 1)
print(ans)