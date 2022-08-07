"""
File: counting_syllable.py
Author: Leah Tajon

Challenge #8: Counting syllables

Assignment: Define a function named 'count' that takes a 
single parameter. The parameter is a string. The string will
contain a single word divided into syllables by hypens, such as these:

"ho-tel"
"cat"
"met-a-phor"
"ter-min-a-tor"

Your function should count the number of syllables and return it.
For example, the call count("ho-tel") should return 2.
"""

def count(word):
    counter = word.count('-') + 1
    return counter

counter1 = count("ho-tel")
print(counter1)
counter2 = count("cat")
print(counter2)
counter3 = count("met-a-phor")
print(counter3)