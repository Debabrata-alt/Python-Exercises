# Write a Python program to remove the last N number of elements from a given list.
# Original lists:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
# Remove the last 3 elements from the said list:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34]
# Remove the last 5 elements from the said list:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34]
# Remove the last 1 element from the said list:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3]


def func(n):
  inp_list = [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
  while n > 0:
    del inp_list[-n]
    n -= 1
  return inp_list

print(func(3))
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34]

print(func(5))
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34]

print(func(1))
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3]

#/////////////////////////////////////////////////////////////////////

def func(n):
  inp_list = [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
  return inp_list[:len(inp_list) - n]

print(func(3))
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34]

print(func(5))
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34]

print(func(1))
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3]
