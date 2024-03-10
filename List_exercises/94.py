# Write a Python program to find common elements in a given list of lists.
# Original list:
# [[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]
# Common elements of the said list of lists:
# [2, 3]
# Original list:
# [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
# Common elements of the said list of lists:
# ['c']

org_list1 = [[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]

org_list2 = [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]

def common_list_of_lists(inp_list):
  # Use set intersection to find the common elements among the lists in 'lst'.
  temp = set(inp_list[0]).intersection(*inp_list)
  return list(temp)


print(common_list_of_lists(org_list1))
# [2, 3]

print(common_list_of_lists(org_list2))
# ['c']