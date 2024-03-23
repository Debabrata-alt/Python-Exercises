# Write a Python program to add two given lists and find the difference between them. Use the map() function.

list1 = [6, 5, 3, 9]
list2 = [0, 1, 7, 7]

def myFunc(x, y):
  return x + y, x - y

newList = list(map(myFunc, list1, list2))

print(newList)
# [(6, 6), (6, 4), (10, -4), (16, 2)]