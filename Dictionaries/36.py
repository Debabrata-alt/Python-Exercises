# Write a Python program to filter a dictionary based on values.
# Original Dictionary:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}

myDict = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}

l = {key: value for key, value in myDict.items() if value > 170}

print(l)
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}

#/////////////////////////////////////////////////////////////////////////////////////

myDict = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}

newDict = {}

myList = list(filter(lambda x: myDict[x] > 170, myDict))

print(myList) # ['Cierra Vega', 'Alden Cantrell', 'Pierre Cox']

for e in myList:
  if e in myDict:
    newDict[e] = myDict[e]

print(newDict)
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}




