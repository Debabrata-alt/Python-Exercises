# Write a Python program to remove the K'th element from a given list, and print the updated list.

def func(list, position):
  list.pop(position)
  return list

print(func([1, 1, 2, 3, 4, 4, 5, 1], 3))
# [1, 1, 2, 4, 4, 5, 1]