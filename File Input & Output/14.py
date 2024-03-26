# Write a Python program to read a random line from a file.

from random import choice

with open("demo.txt", mode="r") as f:
  # splitlines() method splits a string into a list. 
  # The splitting is done at line breaks ('\n').
  content = f.read().splitlines()
  rand_line = choice(content)

# One random line from the content of 'demo.txt' file will be printed each time
print(rand_line)