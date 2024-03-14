# Write a Python program to drop empty items from a given dictionary.
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

myDict = {'c1': 'Red', 'c2': 'Green', 'c3': None}

l = {key: value for key, value in myDict.items() if value != None}

print(l)
# {'c1': 'Red', 'c2': 'Green'}

#///////////////////////////////////////////////////////////////////////

myDict = {'c1': 'Red', 'c2': 'Green', 'c3': None}

l = {key: value for key, value in myDict.items() if value is not None}

print(l)
# {'c1': 'Red', 'c2': 'Green'}

