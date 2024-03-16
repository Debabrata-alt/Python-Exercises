# Write a Python program to find all keys in a dictionary that have the given value.
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# Find all keys in the said dictionary that have the specified value:
# ['Roxanne', 'Betty']

myDict = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}

l = [k for k, v in myDict.items() if v == 20]

print(l)
# ['Roxanne', 'Betty']