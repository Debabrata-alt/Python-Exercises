# Write a Python program to extract specified number of elements from a given list, which follows each other continuously.
# Original list:
# [1, 1, 3, 4, 4, 5, 6, 7]
# Extract 2 number of elements from the said list which follows each other continuously:
# [1, 4]
# Original lists:
# [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
# Extract 4 number of elements from the said list which follows each other continuously:
# [4]

from itertools import groupby

list1 = [1, 1, 3, 4, 4, 5, 6, 7]
list2 = [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]

mul_el_list1 = [key for (key, group) in groupby(list1) if len(list(group)) > 1]

mul_el_list2 = [key for (key, group) in groupby(list2) if len(list(group)) > 1]


print(mul_el_list1) # [1, 4]

print(mul_el_list2) # [4]