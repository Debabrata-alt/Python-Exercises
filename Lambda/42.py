# Write a Python program to multiply all the numbers in a given list using lambda.
# Original list:
# [4, 3, 2, 2, -1, 18]
# Multiply all the numbers of the said list: -864
# Original list:
# [2, 4, 8, 8, 3, 2, 9]
# Multiply all the numbers of the said list: 27648

from functools import reduce

list1 = [4, 3, 2, 2, -1, 18]
list2 = [2, 4, 8, 8, 3, 2, 9]

def func(inp_list):
  return reduce(lambda x, y: x * y, inp_list, 1)

print(func(list1)) # -864
print(func(list2)) # 27648

#///////////////////////////////////////////////////////////////////////

list1 = [4, 3, 2, 2, -1, 18]
list2 = [2, 4, 8, 8, 3, 2, 9]

def func(inp_list):
  # initial is optional here
  return reduce(lambda x, y: x * y, inp_list)

print(func(list1)) # -864
print(func(list2)) # 27648