# Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.
# Original list:
# [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}

colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

def grouping_dictionary(l):
  newDict = {}
  
  for k, v in l:
    newDict.setdefault(k, []).append(v)
  
  return newDict


print(grouping_dictionary(colors))
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}

#//////////////////////////////////////////////////////////////////////////////////

myList = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

newlist = []
myDict = {}

for el in myList:
  if el[0] in myDict:
    myDict[el[0]] = myDict[el[0]] +  [el[1]]
  else:
    myDict[el[0]] = [el[1]]

print(myDict)
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
