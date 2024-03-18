# Write a Python program to remove all characters except a specified character from a given string.
# Original string
# Python Exercises
# Remove all characters except P in the said string:
# P
# Original string
# google
# Remove all characters except g in the said string:
# gg
# Original string
# exercises
# Remove all characters except e in the said string:
# eee


def func(string, char):
  return "".join(s for s in string if s == char)


print(func("Python Exercises", "P")) # P
print(func("google", "g")) # gg
print(func("exercises", "e")) # eee