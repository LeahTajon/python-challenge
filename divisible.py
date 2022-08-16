"""
File: divisible.py
Author: Leah Tajon

Challenge # 12: Divisible by 3

Assignment: Define a function named div_3 that returns True if its
single integer parameters is divisible by 3 and False otherwise.
"""

def div_3(num):
    pass
    
    divisible = num % 3

    if divisible == 0:
        return True
    else:
        return False

result_1  = div_3(6)
print(result_1)

result_2  = div_3(5)
print(result_2)
