# Write a Python program to find the dimension of a given matrix.
# Original list:
# [[1, 2], [2, 4]]
# Dimension of the said matrix:
# (2, 2)
# Original list:
# [[0, 1, 2], [2, 4, 5]]
# Dimension of the said matrix:
# (2, 3)
# Original list:
# [[0, 1, 2], [2, 4, 5], [2, 3, 4]]
# Dimension of the said matrix:
# (3, 3)

list1 = [[1, 2], [2, 4]]
list2 = [[0, 1, 2], [2, 4, 5]]
list3 = [[0, 1, 2], [2, 4, 5], [2, 3, 4]]

def func(inp_list):
  return len(inp_list), len(inp_list[0])


print(func(list1)) # (2, 2)
print(func(list2)) # (2, 3)
print(func(list3)) # (3, 3)