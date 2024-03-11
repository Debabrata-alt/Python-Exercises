# Write a Python program to calculate the maximum and minimum sum of a sublist in a given list of lists.
# Original list:
# [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
# Maximum sum of sub list of the said list of lists:
# [2, 3, 5, 4]
# Minimum sum of sub list of the said list of lists:
# [1, 2, 1, 2]


org_list = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]

max_sum_tup = max((sum(el), el) for el in org_list)

min_sum_tup = min((sum(el), el) for el in org_list)

print(max_sum_tup) # (14, [2, 3, 5, 4])
print(min_sum_tup) # (6, [1, 2, 1, 2])

print(f"Sublist that has maximum sum = {max_sum_tup[1]}")
# Sublist that has maximum sum = [2, 3, 5, 4]

print(f"Sublist that has minimum sum = {min_sum_tup[1]}")
# Sublist that has minimum sum = [1, 2, 1, 2]