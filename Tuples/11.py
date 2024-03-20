# Write a Python program to convert a tuple to a dictionary.

tuplex = ((2, "w"), (3, "r"))

myDict = dict((j, i) for i, j in tuplex)

print(myDict) # {'w': 2, 'r': 3}