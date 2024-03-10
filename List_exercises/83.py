# Write a Python program to get items from a given list with specific conditions.
# Original list:
# [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# Number of Items of the said list which are even and greater than 45
# 5

org_list = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]

def func(inp_list):
  return len([el for el in inp_list if el % 2 == 0 and el > 45])

print(func(org_list)) # 5