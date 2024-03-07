# Write a Python program to pack consecutive duplicates of a given list of elements into sublists.
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After packing consecutive duplicates of the said list elements into sublists:
# [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]

from itertools import groupby

my_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

for key, group in groupby(my_list):
  print(key, list(group))
  
  # 0 [0, 0]
  # 1 [1]
  # 2 [2]
  # 3 [3]
  # 4 [4, 4]
  # 5 [5]
  # 6 [6, 6, 6]
  # 7 [7]
  # 8 [8]
  # 9 [9]
  # 4 [4, 4]

#/////////////////////////////////////////////////////////////////

my_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

def func(this_list):
  return [list(group) for key, group in groupby(this_list)]

print(func(my_list)) # [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]