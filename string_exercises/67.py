# Write a Python program to extract numbers from a given string.
# Sample Output:
# Original string: red 12 black 45 green
# Extract numbers from the said string: [12, 45]


def func(string):
  return [int(el) for el in string.split() if el.isdigit()]


print(func("red 12 black 45 green")) # [12, 45]