# Write a Python program to sort a list alphabetically in a dictionary.

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

newDict = {key: sorted(value) for key, value in num.items()}

print(newDict)
# {'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}