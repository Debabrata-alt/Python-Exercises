# Write a Python program to compute the sum of digits of each number in a given list.
# Original list:
# [10, 2, 56]
# Sum of digits of each number of the said list of integers:
# 14
# Original list:
# [10, 20, 4, 5, 'b', 70, 'a']
# Sum of digits of each number of the said list of integers:
# 19
# Original list:
# [10, 20, -4, 5, -70]
# Sum of digits of each number of the said list of integers:
# 19

list1 = [10, 2, 56]
list2 = [10, 20, 4, 5, 'b', 70, 'a']
list3 = [10, 20, -4, 5, -70]

def calculate(input_list):
  return sum(int(e) for el in input_list for e in str(el) if e.isdigit())


print(calculate(list1)) # 14
print(calculate(list2)) # 19
print(calculate(list3)) # 19