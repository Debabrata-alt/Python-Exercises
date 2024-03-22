# Write a Python program to sort a given list of lists by length and value using lambda.
# Original list:
# [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# Sort the list of lists by length and value:
# [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

myList = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]

# Sort 'myList' based on two criteria:
# 1. First, sort by the length of each sublist (ascending order).
# 2. If the lengths are equal, sort lexicographically by the sublist elements themselves.

sort_list = sorted(myList, key=lambda el: (len(el), el))

print(sort_list)
# [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]