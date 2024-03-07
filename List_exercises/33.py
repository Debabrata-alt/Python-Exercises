# Write a Python program to count the number of sublists that contain a particular element.
# Original list:
# [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
# Count 1 in the said list:
# 3
# Count 7 in the said list:
# 2
# Original list:
# [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
# Count 'A' in the said list:
# 3
# Count 'E' in the said list:
# 1

def func(list, num):
  count = 0
  for el in list:
    if num in el:
      count += 1
  return count

print(func([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1)) # 3

print(func([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 7)) # 2

print(func([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']], 'A')) # 3

print(func([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']], 'E')) # 1