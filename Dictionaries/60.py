# Write a Python program to combine two or more dictionaries, creating a list of values for each key.
# Sample Output:
# Original dictionaries:
# {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
# {'x': 300, 'y': 'Red', 'z': 600}
# Combined dictionaries, creating a list of values for each key:
# {'w': [50], 'x': [100, 300], 'y': ['Green', 'Red'], 'z': [400, 600]}

dict1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
dict2 = {'x': 300, 'y': 'Red', 'z': 600}

newDict = {}

for k, v in dict1.items():
  newDict.setdefault(k,[]).append(v)

for i, j in dict2.items():
  newDict.setdefault(i,[]).append(j)

print(newDict)
# {'w': [50], 'x': [100, 300], 'y': ['Green', 'Red'], 'z': [400, 600]}

#///////////////////////////////////////////////////////////////////////////////////////

dict1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
dict2 = {'x': 300, 'y': 'Red', 'z': 600}

for k, v in dict2.items():
  dict2[k] = [v]

for k, v in dict1.items():
  dict2.setdefault(k, []).append(v)

print(dict2)
# {'x': [300, 100], 'y': ['Red', 'Green'], 'z': [600, 400], 'w': [50]}


