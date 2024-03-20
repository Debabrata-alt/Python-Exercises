# Write a Python program to convert a list of tuples into a dictionary.

myList = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]

myDict = {}

for i, j in myList:
  myDict.setdefault(i, []).append(j)

print(myDict)
# {'x': [1, 2, 3], 'y': [1, 2], 'z': [1]}

#//////////////////////////////////////////////////////////////////////////////////////////

# NOTE:

print(list(zip(*myList)))
# [('x', 'x', 'x', 'y', 'y', 'z'), (1, 2, 3, 1, 2, 1)]
