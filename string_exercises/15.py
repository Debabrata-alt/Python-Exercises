# Write a Python program to get the last part of a string before a specified character.
# https://www.w3resource.com/python/exercises
# https://www.w3resource.com/python

def str_modify(str, char):
  # The rsplit() method splits a string into a list, starting from the right.
  str_list = str.rsplit(char, 1)
  return str_list[0]

new_str = str_modify("https://www.w3resource.com/python/exercises", "/")

print(new_str) # https://www.w3resource.com/python
