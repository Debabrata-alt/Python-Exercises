# Write a Python program to remove consecutive (following each other continuously) duplicates (elements) from a given list.

# Import the 'groupby' function from the 'itertools' module
from itertools import groupby

def compress(list_nums):
  # Use 'groupby' to group consecutive duplicates and return the unique keys
  return [key for key, group in groupby(list_nums)] 

num_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

print(compress(num_list)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]