# Write a Python program to transform a dictionary into a list of tuples.
# Sample Output:
# Original Dictionary:
# {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# Convert the said dictionary to a list of tuples:
# [('Red', 1), ('Green', 3), ('White', 5), ('Black', 2), ('Pink', 4)]

myDict = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}

l = list((k, v) for k, v in myDict.items())

print(l)
# [('Red', 1), ('Green', 3), ('White', 5), ('Black', 2), ('Pink', 4)]