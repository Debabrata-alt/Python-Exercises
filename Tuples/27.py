# Write a Python program to convert a given list of tuples to a list of lists.
# Original list of tuples: [(1, 2), (2, 3), (3, 4)]
# Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
# Original list of tuples: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
# Convert the said list of tuples to a list of lists: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]

mylist1 = [(1, 2), (2, 3), (3, 4)]
myList2 = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]

def func(myList):
  #return list([el] for el in myList)
  return list([e for e in el] for el in myList)


print(func(mylist1))
# [[1, 2], [2, 3], [3, 4]]

print(func(myList2))
# [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]