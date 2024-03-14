# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd

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