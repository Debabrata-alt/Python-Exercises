# Write a Python program to generate two strings from a given string. For the first string, use the characters that occur only once, and for the second, use the characters that occur multiple times in the said string.

from collections import OrderedDict

def func(string):
  uniq_chars = "".join(s for s in string if string.count(s) == 1)
  mul_chars = "".join(s for s in string if string.count(s) > 1)
  
  print(uniq_chars) # w3souc, egh
  print(mul_chars) # rere, aabbccff
  
  # consecutive characters are excluded in the Orderdict keys
  dict_mul_chars = OrderedDict.fromkeys(mul_chars)
  
  print(dict_mul_chars)
  # (1) OrderedDict({'r': None, 'e': None})
  # (2) OrderedDict({'a': None, 'b': None, 'c': None, 'f': None})
  
  mul_chars_final = "".join(dict_mul_chars.keys())
  
  return uniq_chars, mul_chars_final


uniq_chars, mul_chars = func("w3resource")
print(uniq_chars) # w3souc
print(mul_chars) # re

uniq_chars, mul_chars = func("aabbcceffgh")
print(uniq_chars) # egh
print(mul_chars) # abcf
