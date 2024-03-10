# Write a Python program to create the smallest possible number using the elements of a given list of positive integers.
# Original list:
# [3, 40, 41, 43, 74, 9]
# Smallest possible number using the elements of the said list of positive integers:
# 3404143749
# Original list:
# [10, 40, 20, 30, 50, 60]
# Smallest possible number using the elements of the said list of positive integers:
# 102030405060
# Original list:
# [8, 4, 2, 9, 5, 6, 1, 0]
# Smallest possible number using the elements of the said list of positive integers:
# 01245689

list1 = [3, 40, 41, 43, 74, 9]
list2 = [10, 40, 20, 30, 50, 60]
list3 = [8, 4, 2, 9, 5, 6, 1, 0]

def func(inp_list):
  return int("".join(sorted([e for el in inp_list for e in str(el)])))


print(func(list1)) # 133444479
print(func(list2)) # 123456
print(func(list3)) # 1245689