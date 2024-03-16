# Write a Python program to find the key of the maximum value in a dictionary.
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# Finds the key of the maximum and minimum value of the said dictionary:
# ('Roxanne', 'Theodore')

myDict = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}

def func(myDict):
  return max(myDict, key=myDict.get), min(myDict, key=myDict.get)

print(func(myDict))
# ('Roxanne', 'Theodore')

#////////////////////////////////////////////////////////////////

myDict = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}

def func(myDict):
  return max(myDict, key=lambda x: myDict[x]), min(myDict, key=lambda x: myDict[x])

print(func(myDict))
# ('Roxanne', 'Theodore')

#////////////////////////////////////////////////////////////////

myDict = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}

def func(myDict):
  return max(map(lambda x: myDict[x], myDict)), min(map(lambda x: myDict[x], myDict))

print(func(myDict))
# (22, 19)

#////////////////////////////////////////////////////////////////

myDict = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}

def func(myDict):
  sort_list = sorted(myDict, key=lambda x: myDict[x])
  return sort_list[-1], sort_list[0]

print(func(myDict))
# ('Roxanne', 'Theodore')