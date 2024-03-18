# Write a Python program to find the first repeated character in a given string.

def func(string):
  list = [s for s in string if string.count(s) > 1]
  return list[0] if len(list) >=1 else None

print(func("abcdabcd")) # a

print(func("abcd")) # None