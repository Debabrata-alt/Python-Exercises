# Write a Python program to move spaces to the front of a given string.


def func(string):
  string_without_spaces = "".join(s for s in string if s != " ")
  difference = len(string) - len(string_without_spaces)
  return (" " * difference) + string_without_spaces


print(func("w3resource .  com  "))  # "     w3resource.com"

print(func("   w3resource.com  "))  # "     w3resource.com"