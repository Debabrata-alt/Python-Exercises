# Write a Python program to unzip a list of tuples into individual lists.

myList = [(1, 2), (3, 4), (8, 9)]

l = list(zip(*myList))

print(l)
# [(1, 3, 8), (2, 4, 9)]