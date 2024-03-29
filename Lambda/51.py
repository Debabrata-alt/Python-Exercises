# Write a Python program to remove None values from a given list using the lambda function.
# Original list:
# [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
# Remove None value from the said list:
# [12, 0, 23, -55, 234, 89, 0, 6, -12]

myList = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]

newList = list(filter(lambda el: el is not None, myList))

print(newList)
# [12, 0, 23, -55, 234, 89, 0, 6, -12]

#////////////////////////////////////////////////////////////////////////////////

myList = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]

newList = list(filter(lambda el: el != None, myList))

print(newList)
# [12, 0, 23, -55, 234, 89, 0, 6, -12]