"""
File: min_max.py
Author: Leah Tajon

Challenge # 11: min-maxing

Assignment: Define a function named largest_difference that takes
a list of numbers as its only parameter.

Your function should compute and return the difference between
the largest and smallest number in the list.
"""

def largest_difference(a_list):
    pass
    smallest = min(a_list)
    largest = max(a_list)

    difference = largest - smallest

    return difference

result = largest_difference([1, 2, 3])
print(result)