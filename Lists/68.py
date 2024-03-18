# Write a Python program to sum a specific column of a list in a given list of lists.
# Original list of lists:
# [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
# Sum: 1st column of the said list of lists:
# 12
# Sum: 2nd column of the said list of lists:
# 15
# Sum: 4th column of the said list of lists:
# 9

org_list = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]

def func(inp_list, index):
  return sum(el[index] for el in inp_list)

print(func(org_list, 0)) # 12
print(func(org_list, 1)) # 15
print(func(org_list, 3)) # 9