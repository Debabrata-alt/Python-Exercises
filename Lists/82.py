# Write a Python program to get the index of the first element that is greater than a specified element.
# Original list:
# [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]
# Index of the first element which is greater than 73 in the said list:
# 4
# Index of the first element which is greater than 21 in the said list:
# 1
# Index of the first element which is greater than 80 in the said list:
# 5
# Index of the first element which is greater than 55 in the said list:
# 3

org_list = [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]

def func(inp_list, num):
  return [el for i, el in enumerate(inp_list) if el > num][0]


print(func(org_list, 73)) # 78
print(func(org_list, 21)) # 45
print(func(org_list, 80)) # 90
print(func(org_list, 55)) # 67

#//////////////////////////////////////////////////////////////

def func1(inp_list, num):
  return [i for i, el in enumerate(inp_list) if el > num][0]

print(func1(org_list, 73)) # 4
print(func1(org_list, 21)) # 1
print(func1(org_list, 80)) # 5
print(func1(org_list, 55)) # 3