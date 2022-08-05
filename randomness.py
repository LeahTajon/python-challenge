"""
File: randomness.py
Author: Leah Tajon

Challenge #4: Randomness

Assignment: Define a function, random_number, that takes no parameters.
The function must generate a random integer between 1 and 100, both inclusive,
and return it.

Calling the function multiple times should (usually) return different numbers.
"""
import random

def random_number():
    num = random.randint(1,100)
    return num

number_1 = random_number()
number_2 = random_number()
number_3 = random_number()

print(number_1)
print(number_2)
print(number_3)

