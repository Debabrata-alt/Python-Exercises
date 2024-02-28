# Write a Python program to remove the nth index character from a nonempty string.

import random

# string = input("Enter the string: ")
string = "Python"
random_char = random.choice(string)
index = string.index(random_char)
new_string = ""

for char in string:
  if char == random_char:
    char = ""
  new_string += char

print(new_string)
