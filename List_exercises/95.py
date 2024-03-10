# Write a Python program to insert a specified element in a given list after every nth element.
# Original list:
# [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
# Insert 20 in said list after every 4 th element:
# [1, 3, 5, 7, 20, 9, 11, 0, 2, 20, 4, 6, 8, 10, 20, 8, 9, 0, 4, 20, 3, 0]
# Original list:
# ['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
# Insert Z in said list after every 3 th element:
# ['s', 'd', 'f', 'Z', 'j', 's', 'a', 'Z', 'j', 'd', 'f', 'Z', 'd']


list1 = [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]

list2 = ['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']


def func(inp_list, num, n):
  org_len_list = len(inp_list)
  last_len_list = 0
  i = n
  while last_len_list - org_len_list < n: 
    inp_list.insert(i, num)
    last_len_list = len(inp_list)
    i += n + 1
  return inp_list


print(func(list1, 20, 4))
# [1, 3, 5, 7, 20, 9, 11, 0, 2, 20, 4, 6, 8, 10, 20, 8, 9, 0, 4, 20, 3, 0]

print(func(list2, "z", 3 ))
# ['s', 'd', 'f', 'z', 'j', 's', 'a', 'z', 'j', 'd', 'f', 'z', 'd']