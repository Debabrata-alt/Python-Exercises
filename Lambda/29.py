# Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda.
# Original Matrix:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows
# [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
# Original Matrix:
# [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows
# [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]

list1 = [[2, 4, 5], [1, 2, 3], [1, 1, 3], [1, 1, 1]]
list2 = [[1, 2, 3], [-2, 4, -6], [1, -1, 1], [-3, 6, -5]]

def func(myList):
  return sorted(myList, key=sum)

print(func(list1))
# [[1, 1, 1], [1, 1, 3], [1, 2, 3], [2, 4, 5]]

print(func(list2))
# [[-2, 4, -6], [-3, 6, -5], [1, -1, 1], [1, 2, 3]]