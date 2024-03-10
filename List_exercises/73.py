# Write a Python program to find the maximum and minimum values in a given list within a specified index range.
# Original list:
# [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
# Index range:
# 3 to 8
# Maximum and minimum values of the said given list within index range:
# (5, 0)

org_list = [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]

def func(list, start_range, end_range):
  return max(list[start_range: end_range + 1]), min(list[start_range: end_range + 1])


print(func(org_list, 3, 8)) # (5, 0)