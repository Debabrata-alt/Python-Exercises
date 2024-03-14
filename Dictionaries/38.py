# Write a Python program to filter the height and width of students, which are stored in a dictionary.
# Original Dictionary:
# {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# Height > 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}

myDict = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}

newList = list(filter(lambda x: myDict[x][0] >= 6 and myDict[x][1] >= 70, myDict))

print(newList) # ['Cierra Vega']

d = {key: value for key, value in myDict.items() if key in newList}

print(d) # {'Cierra Vega': (6.2, 70)}

#/////////////////////////////////////////////////////////////////////////////////

myDict = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}

newDict = {}

for key, value in myDict.items():
  if value[0] >= 6.0 and value[1] >= 70:
    newDict[key] = myDict[key]

print(newDict)
# {'Cierra Vega': (6.2, 70)}

#/////////////////////////////////////////////////////////////////////////////////

myDict = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}

newDict = {}

for key in myDict:
  if myDict[key][0] >= 6 and myDict[key][1] >= 70:
    newDict[key] = myDict[key]

print(newDict)
# {'Cierra Vega': (6.2, 70)}

#/////////////////////////////////////////////////////////////////////////////////

myDict = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}

def filter_data(students):
  result = {k: s for k, s in students.items() if s[0] >= 6.0 and s[1] >= 70}
  return result


print(filter_data(myDict))
# {'Cierra Vega': (6.2, 70)}
