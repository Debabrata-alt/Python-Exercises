# A Python dictionary contains List as a value. Write a Python program to clear the list values in the said dictionary.
# Original Dictionary:
# {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# Clear the list values in the said dictionary:
# {'C1': [], 'C2': [], 'C3': []}

myDict = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}

def func(dictionary):
  for key in dictionary:
    dictionary[key] = []
  return dictionary

print(func(myDict))
# {'C1': [], 'C2': [], 'C3': []}

#/////////////////////////////////////////////////////////////////////////////////

myDict = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}

def func(dictionary):
  for key in dictionary:
    dictionary[key].clear()
  return dictionary

print(func(myDict))
# {'C1': [], 'C2': [], 'C3': []}

#/////////////////////////////////////////////////////////////////////////////////

myDict = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}

l = {k: v.clear() for k, v in myDict.items()}

print(l)
# {'C1': None, 'C2': None, 'C3': None}

#/////////////////////////////////////////////////////////////////////////////////

myDict = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}

l = {k: [] for k, v in myDict.items()}

print(l)
# {'C1': [], 'C2': [], 'C3': []}