"""
File: flatten.py
Author: Leah Tajon

Challenge # 10:  Flatten a List

Assignment: Write a function that takes a list of lists and flattens it
into one-dimensional list. 

Name your function flatten. It should take a single parameter and return a
list.
"""

def flatten(a_list):
    result = []
    for sub_list in a_list:
        for item in sub_list:
            result.append(item)
    return result

flat = flatten([[1, 2], [3, 4]])
print(flat)