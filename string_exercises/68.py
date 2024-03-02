# Write a Python program to remove repeated consecutive characters and replace them with single letters and print a updated string.
# Sample Data:
# ("Red Green White") -> "Red Gren White"
# ("aabbbcdeffff") -> "abcdef"
# ("Yellowwooddoor") -> "Yelowodor"

from itertools import groupby

def func(string):
  unique_chars_list = []
  
  for (key, group) in groupby(string):
    unique_chars_list.append(key)
  
  return "".join(el for el in unique_chars_list)


print(func("Red Green White")) # Red Gren White
print(func("aabbbcdeffff")) # abcdef
print(func("Yellowwooddoor")) # Yelowodor