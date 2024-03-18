# Write a Python program to find the minimum and maximum value for each tuple position in a given list of tuples.
# Original list:
# [(2, 3), (2, 4), (0, 6), (7, 1)]
# Maximum value for each tuple position in the said list of tuples:
# [7, 6]
# Minimum value for each tuple position in the said list of tuples:
# [0, 1]

my_list = [(2, 3), (2, 4), (0, 6), (7, 1)]

max_vals = [max(list(el[0] for el in my_list)), max(list(el[1] for el in my_list))]

print(max_vals) # [7, 6]

min_vals = [min(list(el[0] for el in my_list)), min(list(el[1] for el in my_list))]

print(min_vals) # [0, 1]