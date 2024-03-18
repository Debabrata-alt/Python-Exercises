# Write a Python program to remove a specified column from a given nested list.
# Original Nested list:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# After removing 1st column:
# [[2, 3], [4, 5], [1, 1]]
# Original Nested list:
# [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# After removing 3rd column:
# [[1, 2], [-2, 4], [1, -1]]

list1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
list2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

def func(list, index):
  new_list = []
  for el in list:
    el.pop(index)
    # del el[index]
    new_list.append(el)
  return new_list


print(func(list1, 0))
# [[2, 3], [4, 5], [1, 1]]

print(func(list2, 2))
# [[1, 2], [-2, 4], [1, -1]]