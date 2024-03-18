# Write a Python program to find the first repeated word in a given string.


def func(string):
  list = [s for s in string.split() if string.split().count(s) > 1]
  return list[0] if len(list) >= 1 else None


print(func("ab ca bc ab")) # ab
print(func("ab ca bc ab ca ab bc")) # ab
print(func("ab ca bc ca cd bc")) # ca
print(func("ab ca bc")) # None