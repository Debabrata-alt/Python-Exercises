# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd

myDict = {'1':['a','b'], '2':['c','d']}

result = [x + y for x in myDict["1"] for y in myDict["2"]]

print(result) 
# ['ac', 'ad', 'bc', 'bd']

#/////////////////////////////////////////////////////////////////////////////////////////

myDict = {'1':['a','b'], '2':['c','d']}

print(myDict.values()) # dict_values([['a', 'b'], ['c', 'd']])

myList = list(myDict.values()) 

print(myList) # [['a', 'b'], ['c', 'd']]

newList = [x + y for x in myList[0] for y in myList[1]]

print(newList)
# ['ac', 'ad', 'bc', 'bd']

#////////////////////////////////////////////////////////////////////////////////////////

myDict = {'1':['a','b'], '2':['c','d']}
result = []

list1 = myDict["1"]
list2 = myDict["2"]

for i in list1:
  for j in list2:
    result.append(i + j) 

print(result) # ['ac', 'ad', 'bc', 'bd']

#////////////////////////////////////////////////////////////////////////////////////////

from itertools import product

myDict = {'1':['a','b'], '2':['c','d']}

print(myDict[k] for k in sorted(myDict.keys()))
# <generator object <genexpr> at 0x00000260B6E43850>

print([myDict[k] for k in sorted(myDict.keys())])
# [['a', 'b'], ['c', 'd']]

print(*[myDict[k] for k in sorted(myDict.keys())])
# ['a', 'b'] ['c', 'd']


for combo in product(*[myDict[k] for k in sorted(myDict.keys())]):
  print(list(combo))
  # ['a', 'c']
  # ['a', 'd']
  # ['b', 'c']
  # ['b', 'd']  
  
  print("".join(combo))
  # ac
  # ad
  # bc
  # bd