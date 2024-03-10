# Write a Python program to reverse each list in a given list of lists.
# Original list of lists:
# [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# Reverse each list in the said list of lists:
# [[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9], [16, 15, 14, 13]]

org_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

x = [el[::-1] for el in org_list]

print(x)
# [[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9], [16, 15, 14, 13]]


#/////////////////////////////////////////////////////////////////////////////

# Difference between reverse() and [::-1]

# 1. reverse()

my_list = [1, 2, 3, 4]

my_list.reverse()

print(my_list) # [4, 3, 2, 1]

# 2. [::-1]

my_list = [1, 2, 3, 4]

new_list = my_list[::-1]

print(new_list) # [4, 3, 2, 1]
