# Write a Python program to calculate the sum of the numbers in a list between the indices of a specified range.
# Original list:
# [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
# Range: 8, 10
# Sum of the specified range:
# 29

org_list = [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
sum = 0

for n in range(8, 11):
  sum += org_list[n]

print(sum) # 29