# Write a Python program to split a given list into specified-sized chunks.
# Original list:
# [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# Split the said list into equal size 3
# [[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]
# Split the said list into equal size 4
# [[12, 45, 23, 67], [78, 90, 45, 32], [100, 76, 38, 62], [73, 29, 83]]
# Split the said list into equal size 5
# [[12, 45, 23, 67, 78], [90, 45, 32, 100, 76], [38, 62, 73, 29, 83]]


org_list = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]

def helper_func(inp_list, q, size):
  f_list = []
  t_list = []
  ind = 0
  for n in range(q):
    for i in range(size):
      t_list.append(inp_list[ind])
      ind += 1
    f_list.append(t_list)
    t_list = []
  return f_list


def func(inp_list, size):
  q, r = divmod(len(inp_list), size)
  if r == 0:
    f_list = helper_func(inp_list, q, size)
    return f_list
  else:
    f_list = helper_func(inp_list, q, size)
    return f_list + [inp_list[-r:]]


print(func(org_list, 3))
# [[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]

print(func(org_list, 4))
# [[12, 45, 23, 67], [78, 90, 45, 32], [100, 76, 38, 62], [73, 29, 83]]

print(func(org_list, 5))
# [[12, 45, 23, 67, 78], [90, 45, 32, 100, 76], [38, 62, 73, 29, 83]]