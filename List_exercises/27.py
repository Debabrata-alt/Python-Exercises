# Write a Python program to flatten a given nested list structure.
# Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# Flatten list:
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

original_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]

nested_list = list((original_list.index(el), el) for el in original_list if not isinstance(el, int) and len(el) > 1)

print(nested_list)
# [(2, [20, 30]), (5, [60, 70, 80]), (6, [90, 100, 110, 120])]

print(nested_list[0][1][1]) # 30

new_original_list = list(el for el in original_list if isinstance(el, int))

print(new_original_list) # [0, 10, 40, 50]