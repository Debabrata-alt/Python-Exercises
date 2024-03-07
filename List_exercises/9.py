# Write a Python program to print the numbers of a specified list after removing even numbers from it.

def func(list):
  return [el for el in list if el % 2 != 0]


print(func([7, 8, 120, 25, 44, 20, 27])) 
# [7, 25, 27]