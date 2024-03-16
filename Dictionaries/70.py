# Write a Python program to create a flat list of all the keys in a flat dictionary.
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# Create a flat list of all the keys of the said flat dictionary:
# ['Theodore', 'Roxanne', 'Mathew', 'Betty']

myDict = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}

myList = list(myDict)

print(myList)
# ['Theodore', 'Roxanne', 'Mathew', 'Betty']