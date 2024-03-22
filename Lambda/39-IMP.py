# Write a Python program to find the nested list elements, which are present in another list using lambda.
# Original lists: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
# Intersection of said nested lists:
# [[12], [7, 11], [1, 5, 8]]

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
nestedList = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]

newList = [list(filter(lambda x: x in myList, el)) for el in nestedList]

print(newList)
# [[12], [7, 11], [1, 5, 8]]