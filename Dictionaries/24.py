# Write a Python program to convert a list into a nested dictionary of keys.

numList = [1, 2, 3, 4]

myDict = {}

for el in numList[::-1]:
  myDict = {el: myDict}

print(myDict)
# {1: {2: {3: {4: {}}}}}