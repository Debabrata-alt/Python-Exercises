# Write a Python program to calculate the product of a given list of numbers using lambda.
# list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Product of the said list numbers:
# 3628800
# list2: [2.2, 4.12, 6.6, 8.1, 8.3]
# Product of the said list numbers:
# 4021.8599520000007

from functools import reduce

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2.2, 4.12, 6.6, 8.1, 8.3]

def func(inp_List):
  return reduce(lambda x, y: x * y, inp_List, 1)


print(func(list1)) # 3628800
print(func(list2)) # 4021.8599520000007

#///////////////////////////////////////////////////////////////////////

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2.2, 4.12, 6.6, 8.1, 8.3]

def func(inp_List):
  # initial is optional here
  return reduce(lambda x, y: x * y, inp_List)


print(func(list1)) # 3628800
print(func(list2)) # 4021.8599520000007