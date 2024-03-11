# Write a Python program to sum two or more lists. The lengths of the lists may be different.
# Original list:
# [[1, 2, 4], [2, 4, 4], [1, 2]]
# Sum said lists with different lengths:
# [4, 8, 8]
# Original list:
# [[1], [2, 4, 4], [1, 2], [4]]
# Sum said lists with different lengths:
# [8, 6, 4]

list1 = [[1, 2, 4], [2, 4, 4], [1, 2]]
list2 = [[1], [2, 4, 4], [1, 2], [4]]

def func(inp_list):
  return list(map(sum, inp_list))


print(func(list1)) 
# [7, 10, 3]

print(func(list2)) 
# [1, 10, 3, 4]

#///////////////////////////////////////////////////////////////////////////////////

list1 = [[1, 2, 4], [2, 4, 4], [1, 2]]
list2 = [[1], [2, 4, 4], [1, 2], [4]]

def func(inp_list):
  max_len = max(len(el) for el in inp_list)
  for el in inp_list:
    len_el = len(el)
    if len_el < max_len:
      index = inp_list.index(el)
      diff = max_len - len_el
      el += diff * [0]
      inp_list[index] = el
      
  return [sum(el) for el in zip(*inp_list)]


print(func(list1)) 
# [4, 8, 8]

print(func(list2)) 
# [8, 6, 4]
