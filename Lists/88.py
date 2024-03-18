# Write a Python program to display vertically each element of a given list, list of lists.
# Original list:
# ['a', 'b', 'c', 'd', 'e', 'f']
# Display each element vertically of the said list:
# a
# b
# c
# d
# e
# f
# Original list:
# [[1, 2, 5], [4, 5, 8], [7, 3, 6]]
# Display each element vertically of the said list of lists:
# 1 4 7
# 2 5 3
# 5 8 6


org_list1 = ['a', 'b', 'c', 'd', 'e', 'f']
org_list2 = [[1, 2, 5], [4, 5, 8], [7, 3, 6]]

def func(*args):
  print(args) 
  # 1. ('a', 'b', 'c', 'd', 'e', 'f')
  # 2. ([1, 2, 5], [4, 5, 8], [7, 3, 6])
  
  for arg in args:
    print(arg)


func(*org_list1)
# a
# b
# c
# d
# e
# f

func(*org_list2)
# [1, 2, 5]
# [4, 5, 8]
# [7, 3, 6]

#////////////////////////////////////////////////////////////////////////////////

nums = [[1, 2, 5], [4, 5, 8], [7, 3, 6]]

# NOTE: * is unpacaking operator. (Each element will be unpacked from the list).
# Unpacking the list = [1, 2, 5] [4, 5, 8] [4, 5, 8]
# print(*nums) => [1, 2, 5] [4, 5, 8] [7, 3, 6]

for a, b, c in zip(*nums):
  print(a, b, c)
  
  # 1 4 7
  # 2 5 3
  # 5 8 6