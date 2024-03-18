# Write a Python program to insert an element in a given list after every nth position.
# Original list:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# Insert a in the said list after 2 nd element:
# [1, 2, 'a', 3, 4, 'a', 5, 6, 'a', 7, 8, 'a', 9, 0]
# Insert b in the said list after 4 th element:
# [1, 2, 3, 4, 'b', 5, 6, 7, 8, 'b', 9, 0]


def func(char, position):
  org_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
  for i in range(position, len(org_list), position):
    org_list.insert(i, char)
  return org_list


print(func("a", 2)) 
# [1, 2, 'a', 3, 'a', 4, 'a', 5, 'a', 6, 7, 8, 9, 0]

print(func("b", 4))
# [1, 2, 3, 4, 'b', 5, 6, 7, 'b', 8, 9, 0]