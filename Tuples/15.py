# Write a Python program to replace the last value of tuples in a list.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]


myList = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

l = list((i, j, 100) for i, j, k in myList)

print(l)
# [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

#/////////////////////////////////////////////////////////////////////////////

myList = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

l = list(el[:2] + (100,) for el in myList)

print(l)
# [(10, 20, 100), (40, 50, 100), (70, 80, 100)]