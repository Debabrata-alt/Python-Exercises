# Write a Python program to find the difference between consecutive numbers in a given list.
# Original list:
# [1, 1, 3, 4, 4, 5, 6, 7]
# Difference between consecutive numbers of the said list:
# [0, 2, 1, 0, 1, 1, 1]
# Original list:
# [4, 5, 8, 9, 6, 10]
# Difference between consecutive numbers of the said list:
# [1, 3, 1, -3, 4]

list1 = [1, 1, 3, 4, 4, 5, 6, 7]
list2 = [4, 5, 8, 9, 6, 10]


def func(input_list):
  new_list = []
  for n in range(len(input_list) - 1):
    new_list.append(input_list[n + 1] - input_list[n])
  
  return new_list


print(func(list1))
# [0, 2, 1, 0, 1, 1, 1]

print(func(list2))
# [1, 3, 1, -3, 4]