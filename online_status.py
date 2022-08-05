"""
File: online_status.py
Author: Leah Tajon

Challenge: Online Status

Assignment: The aim of this challenge is, given a dictionary of people's
online status, to count the number of people who are online.

Write a function named online_count that takes one parameter.
The parameter is a dictionary that maps from strings of names
to the string "online" or "offline".

Your function should return the number of people who are online.
"""

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(dict):
    counter = 0
    for key, value in dict.items():
        if value == 'online':
            counter += 1
    return counter

count = online_count(statuses)
print(count)
