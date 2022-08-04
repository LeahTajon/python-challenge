"""
File: capital_indexes.py
Author: Leah Tajon

Challenge: Capital indexes

Assignment: Write a function named capital_indexes. The function takes a 
single parameter, which is a string. Your function should return a list of
all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list 
[0, 2, 4]
"""

def capital_indexes(letters):
    list_1 = []
    
    for count, values in enumerate(letters):
        if values.isupper():
            list_1.append(count)
    
    return list_1
    
result = capital_indexes("HeLlO")
print(result)
