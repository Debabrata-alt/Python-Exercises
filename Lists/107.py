# Write a Python program to compute the average of the n-th element in a given list of lists with different lengths.
# Original list:
# [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
# Average of n-th elements in the said list of lists with different lengths:
# [4.8, 5.8, 6.8, 8.0, 11.0]

org_list = [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]

def func(inp_list):
  max_len = max(len(el) for el in inp_list)
  for el in inp_list:
    len_el = len(el)
    if len_el < max_len:
      index = inp_list.index(el)
      diff = max_len - len_el
      el += diff * [0]
      inp_list[index] = el
      
  zip_list = list(zip(*inp_list))
  zip_mod_list = list(tuple(e for e in el if e != 0) for el in zip_list[1:])
  zip_list[1:] = zip_mod_list
  avg_list = list(sum(el)/len(el) for el in zip_list)
  return avg_list


print(func(org_list))
# [4.8, 5.8, 6.8, 8.0, 11.0]