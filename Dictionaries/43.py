# Write a Python program to convert string values of a given dictionary into integer/float datatypes.
# Original list:
# [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# String values of a given dictionary, into integer types:
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
# Original list:
# [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
# String values of a given dictionary, into float types:
# [{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]

myList = [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]

myDict = {}
newList = []

for el in myList:
  l = {k: int(v) for k, v in el.items()}
  newList.append(l)

print(newList) 
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]

#///////////////////////////////////////////////////////////////////////////////////

myList = [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]

x = [{k: int(v) for el in myList for k, v in el.items()}]

print(x)
# [{'x': 10, 'y': 20, 'z': 30, 'p': 40, 'q': 50, 'r': 60}]

#///////////////////////////////////////////////////////////////////////////////////

myList = [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]

y = [{k: int(v) for k, v in el.items()} for el in myList]

print(y)
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]

#///////////////////////////////////////////////////////////////////////////////////

thisList = [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]

p = [{k: float(v) for k, v in el.items()} for el in thisList]

print(p)
# [{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]

#/////////////////////////////////////////////////////////////////////////////////

nums_int = [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]

nums_float = [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]

def convert_to_int(lst):
  result = [dict([a, int(x)] for a, x in b.items()) for b in lst]
  return result

def convert_to_float(lst):
  result = [dict([a, float(x)] for a, x in b.items()) for b in lst]
  return result

print(convert_to_int(nums_int))
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]

print(convert_to_float(nums_float)) 
# [{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]

#/////////////////////////////////////////////////////////////////////////

nums_int = [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]

nums_float = [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]

def convert_to_int(lst):
  result = [dict((a, int(x)) for a, x in b.items()) for b in lst]
  return result

def convert_to_float(lst):
  result = [dict((a, float(x)) for a, x in b.items()) for b in lst]
  return result

print(convert_to_int(nums_int))
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]

print(convert_to_float(nums_float)) 
# [{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]