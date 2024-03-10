# Write a Python program to find the item with the most occurrences in a given list.
# Original list:
# [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
# Item with maximum occurrences of the said list:
# 2

org_list = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]

def func(list):
  max_count = 0
  for el in list:
    count = list.count(el)
    if count > max_count:
      max_count = count
      max_tup = (el, max_count)
  return max_tup[0]

print(func(org_list)) # 2