# Write a Python program to sort a given list of lists by length and value.
# Original list:
# [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# Sort the list of lists by length and value:
# [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

org_list = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17, 19], [3, 5], [6], [6, 8], [12, 34, 10]]

def func(list):
  return sorted(sorted(list), key=len)

print(func(org_list))
# [[0], [2], [6], [0, 7], [1, 3], [3, 5], [6, 8], [9, 11], [12, 34, 10], [13, 15, 17, 19]]

#/////////////////////////////////////////////////////////////////////////////
# Explaining the above:

org_list = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17, 19], [3, 5], [6], [6, 8], [12, 34, 10]]

org_list.sort()

print(org_list)
# [[0], [0, 7], [1, 3], [2], [3, 5], [6], [6, 8], [9, 11], [12, 34, 10], [13, 15, 17, 19]]

org_list.sort(key=len)

print(org_list)
# [[0], [2], [6], [0, 7], [1, 3], [3, 5], [6, 8], [9, 11], [12, 34, 10], [13, 15, 17, 19]]

