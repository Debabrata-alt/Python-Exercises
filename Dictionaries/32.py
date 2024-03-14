# Write a Python program to create a dictionary from two lists without losing duplicate values.
# Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# Expected Output: defaultdict(<class 'set'>, {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}})

list1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
list2 = [1, 2, 2, 3]

myDict = {}

for a, b in zip(list1, list2):
  myDict.update({a: {b}})

print(myDict)
# {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}}

#///////////////////////////////////////////////////////////////////////////////////////////

list1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
list2 = [1, 2, 2, 3]

myDict = {}

for a, b in zip(list1, list2):
  myDict[a] = {b}


print(myDict)
# {'Class-V': {1}, 'Class-VI': {2}, 'Class-VII': {2}, 'Class-VIII': {3}}

#////////////////////////////////////////////////////////////////////////////////////////////

list1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
list2 = [1, 2, 2, 3]

myDict = {}

l = list(zip(*(list1, list2)))

print(l)
# [('Class-V', 1), ('Class-VI', 2), ('Class-VII', 2), ('Class-VIII', 3)]