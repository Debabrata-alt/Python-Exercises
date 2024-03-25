# Write a Python program to sum recursion lists using recursion.
# Test Data: [1, 2, [3,4], [5,6]]
# Expected Result: 21

myList = [1, 2, [3,4], [5,6]]

def calc_sum(myList):
  total = 0
  for el in myList:
    if type(el) == type([]):
      total = total + calc_sum(el)
    else:
      total = total + el
  return total

print(calc_sum(myList)) # 21

#////////////////////////////////////////////////////////////////////

# NOTE: 

print(type([])) # <class 'list'>
print(type(list())) # <class 'list'>

print(type({})) # <class 'dict'>
print(type(dict())) # <class 'dict'>

print(type(set())) # <class 'set'>

print(type(5)) # <class 'int'>
print(type(5.2)) # <class 'float'>