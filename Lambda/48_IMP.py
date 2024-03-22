# Write a Python program to count the occurrences of items in a given list using lambda.
# Original list:
# [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
# Count the occurrences of the items in the said list:
# {3: 4, 4: 2, 5: 3, 8: 2, 0: 2, 1: 1, 2: 2}

myList = [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]

newDict = dict(map(lambda el: (el, myList.count(el)), myList))

print(newDict)
# {3: 4, 4: 2, 5: 3, 8: 2, 0: 2, 1: 1, 2: 2}