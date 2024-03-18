# Write a Python program to compute average of two given lists.
# Original list:
# [1, 1, 3, 4, 4, 5, 6, 7]
# [0, 1, 2, 3, 4, 4, 5, 7, 8]
# Average of two lists:
# 3.823529411764706

list1 = [1, 1, 3, 4, 4, 5, 6, 7]
list2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]

def func(list1, list2):
  return (sum(list1)+ sum(list2)) / (len(list1) + len(list2))


print(func(list1, list2)) # 3.823529411764706