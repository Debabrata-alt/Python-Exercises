# Write a Python program to create the largest possible number using the elements of a given list of positive integers.
# Original list:
# [3, 40, 41, 43, 74, 9]
# Largest possible number using the elements of the said list of positive integers:
# 9744341403
# Original list:
# [10, 40, 20, 30, 50, 60]
# Largest possible number using the elements of the said list of positive integers:
# 605040302010
# Original list:
# [8, 4, 2, 9, 5, 6, 1, 0]
# Largest possible number using the elements of the said list of positive integers:
# 98654210

list1 = [3, 40, 41, 43, 74, 9]
list2 = [10, 40, 20, 30, 50, 60]
list3 = [8, 4, 2, 9, 5, 6, 1, 0]

def func(inp_list):
  return int("".join(sorted([e for el in inp_list for e in str(el)], reverse=True)))


print(func(list1)) # 9744443310
print(func(list2)) # 654321000000
print(func(list3)) # 98654210

