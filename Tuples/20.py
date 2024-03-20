# Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
# Original Tuple:
# (4, 3, 2, 2, -1, 18)
# Product - multiplying all the numbers of the said tuple: -864
# Original Tuple:
# (2, 4, 8, 8, 3, 2, 9)
# Product - multiplying all the numbers of the said tuple: 27648

tuplex1 = (4, 3, 2, 2, -1, 18)
tuplex2 = (2, 4, 8, 8, 3, 2, 9)

def func(inp_tup):
  product = 1
  for el in inp_tup:
    product *= el
  return product


print(func(tuplex1)) # -864
print(func(tuplex2)) # 27648

#//////////////////////////////////////////////////////////////////////////////////

from functools import reduce

tuplex1 = (4, 3, 2, 2, -1, 18)
tuplex2 = (2, 4, 8, 8, 3, 2, 9)

def func(inp_tup):
  return reduce(lambda x, y: x * y, inp_tup, 1)


print(func(tuplex1)) # -864
print(func(tuplex2)) # 27648

#//////////////////////////////////////////////////////////////////////////////////

from functools import reduce

tuplex1 = (4, 3, 2, 2, -1, 18)
tuplex2 = (2, 4, 8, 8, 3, 2, 9)

def func(inp_tup):
  # initial value is not mandatory here.
  return reduce(lambda x, y: x * y, inp_tup)


print(func(tuplex1)) # -864
print(func(tuplex2)) # 27648



