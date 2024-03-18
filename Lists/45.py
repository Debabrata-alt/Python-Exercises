# Write a Python program to extract a specified column from a given nested list.
# Original Nested list:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Extract 1st column:
# [1, 2, 1]
# Original Nested list:
# [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# Extract 3rd column:
# [3, -5, 1]

list1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
list2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

def func(list, index):
  return [el[index] for el in list]


print(func(list1, 0)) # [1, 2, 1]
print(func(list2, 2)) # [3, -5, 1]