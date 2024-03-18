# 1. Write a Python program to sum all the items in a list.

list = [1, 2, -8]

print(sum(list)) # -5

#/////////////////////////////////////////////////////////////////////////////////////////////

# 2. Write a Python program to multiply all the items in a list.

def func(list):
  total = 1
  for el in list:
    total *= el
  return total

print(func([1, 2, -8])) # -16

