# Write a Python program to find the difference between two lists including duplicate elements.
# Original lists:
# [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
# [1, 1, 2, 4, 5, 6]
# Difference between two said list including duplicate elements):
# [3, 3, 4, 7]

list1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
list2 = [1, 1, 2, 4, 5, 6]

for el in list2:
  list1.remove(el)

print(list1) # [3, 3, 4, 7]