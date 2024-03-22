# Write a Python program to remove all elements from a given list present in another list using lambda.
# Original lists:
# list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2: [2, 4, 6, 8]
# Remove all elements from 'list1' present in 'list2:
# [1, 3, 5, 7, 9, 10]

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

newList = list(filter(lambda el: el not in [2, 4, 6, 8], list1))

print(newList)
# [1, 3, 5, 7, 9, 10]


