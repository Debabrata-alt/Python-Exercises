# Write a Python program to get the unique values in a given list of lists.
# Original list:
# [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
# Unique values of the said list of lists:
# [0, 1, 2, 3, 4, 5, 7]
# Original list:
# [['h', 'g', 'l', 'k'], ['a', 'b', 'd', 'e', 'c'], ['j', 'i', 'y'], ['n', 'b', 'v', 'c'], ['x', 'z']]
# Unique values of the said list of lists:
# ['e', 'd', 'c', 'b', 'x', 'k', 'n', 'h', 'g', 'j', 'i', 'a', 'l', 'y', 'v', 'z']

list1 = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
list2 = [['h', 'g', 'l', 'k'], ['a', 'b', 'd', 'e', 'c'], ['j', 'i', 'y'], ['n', 'b', 'v', 'c'], ['x', 'z']]

def func(inp_list):
  # Flatten the List of lists
  flat_list = list(e for el in inp_list for e in el)
  # Remove duplicate values by converting the list to set
  my_set = set(flat_list)
  return list(my_set)


print(func(list1))
# [0, 1, 2, 3, 4, 5, 7]

print(func(list2))
# ['v', 'i', 'a', 'k', 'c', 'n', 'g', 'y', 'x', 'b', 'd', 'z', 'l', 'e', 'h', 'j']