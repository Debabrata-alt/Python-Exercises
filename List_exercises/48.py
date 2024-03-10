# Write a Python program to check whether a specified list is sorted or not.
# Original list:
# [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
# Is the said list is sorted!
# True
# Original list:
# [1, 2, 4, 6, 8, 10, 14, 12, 16, 17]
# Is the said list is sorted!
# False

list1 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
list2 = [1, 2, 4, 6, 8, 10, 14, 12, 16, 17]

def func(list):
  return all(list[n] <= list[n + 1] for n in range(len(list) - 1))


print(func(list1)) # True
print(func(list2)) # False