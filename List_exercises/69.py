# How to flatten a nested list?

org_list = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]

def func(list):
  # return [el for sublist in list for el in sublist]
  return [e for el in list for e in el]


print(func(org_list)) 
# [1, 2, 3, 2, 4, 5, 6, 2, 7, 8, 9, 5]