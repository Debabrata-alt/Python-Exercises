# Write a Python program to find nested list elements that are present in another list.
# Original lists:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
# Intersection of said nested lists:
# [[12], [7, 11], [1, 5, 8]]

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
list2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]

x = [[el for el in list if el in list1] for list in list2]

print(x) # [[12], [7, 11], [1, 5, 8]]

