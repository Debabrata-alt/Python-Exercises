# Write a Python program to generate two strings from a given string. For the first string, use the characters that occur only once, and for the second, use the characters that occur multiple times in the said string.

from collections import OrderedDict

def func(string):
  first_string = "".join(s for s in string if string.count(s) == 1)
  second_string_testing = "".join(s for s in string if string.count(s) > 1)
  
  dict_unique_chars = OrderedDict.fromkeys(second_string_testing)
  second_string = "".join(dict_unique_chars.keys())
  
  return first_string, second_string


first_string, second_string = func("w3resource")
print(first_string) # w3souc
print(second_string) # re


first_string, second_string = func("aabbcceffgh")
print(first_string) # egh
print(second_string) # abcf