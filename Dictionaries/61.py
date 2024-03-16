# Write a Python program to group the elements of a given list based on the given function.
# Sample Output:
# Original list & function:
# [7, 23, 3.2, 3.3, 8.4] Function name: floor:
# Group the elements of the said list based on the given function:
# {7: [7], 23: [23], 3: [3.2, 3.3], 8: [8.4]}
# Original list & function:
# ['Red', 'Green', 'Black', 'White', 'Pink'] Function name: len:
# Group the elements of the said list based on the given function:
# {3: ['Red'], 5: ['Green', 'Black', 'White'], 4: ['Pink']}

from math import floor

list1 = [7, 23, 3.2, 3.3, 8.4]
list2 = ['Red', 'Green', 'Black', 'White', 'Pink']

myDict1 = {}
myDict2 = {}

for el in list1:
  myDict1.setdefault(floor(el), []).append(el)

print(myDict1)
# {7: [7], 23: [23], 3: [3.2, 3.3], 8: [8.4]}

for el in list2:
  myDict2.setdefault(len(el), []).append(el)

print(myDict2)
# {3: ['Red'], 5: ['Green', 'Black', 'White'], 4: ['Pink']}

#///////////////////////////////////////////////////////////////////////////////////////

myList = [7, 23, 3.2, 3.3, 8.4]

myDict = {}

for el in myList:
  if type(el) == int:
    myDict.setdefault(el, []).append(el)
  elif type(el) == float:
    myDict.setdefault(int(el), []).append(el)

print(myDict)
# {7: [7], 23: [23], 3: [3.2, 3.3], 8: [8.4]}

#/////////////////////////////////////////////////////////////////////////////////////////

myList = [7, 23, 3.2, 3.3, 8.4]

myDict = {}

for el in myList:
  if not isinstance(el, int):
    myDict.setdefault(int(el), []).append(el)
  else:
    myDict.setdefault(el, []).append(el)

print(myDict)
# {7: [7], 23: [23], 3: [3.2, 3.3], 8: [8.4]}