# Write a Python program to find the index position and value of the maximum and minimum values in a given list of numbers using lambda.
# Original list:
# [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
# Index position and value of the maximum value of the said list:
# (5, 89)
# Index position and value of the minimum value of the said list:
# (3, 10.11)

myList = [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]

maxi = lambda lst: (lst.index(max(lst)), max(lst))

mini = lambda lst: (lst.index(min(lst)), min(lst))

print(maxi(myList))
# (5, 89)
print(mini(myList))
# (3, 10.11)

#/////////////////////////////////////////////////////////////////////////////////////////

# Using enumerate(), max(), min()

myList = [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]

maxi = max(enumerate(myList), key=lambda x: x[1])

mini = min(enumerate(myList), key=lambda x: x[1])

print(maxi)
# (5, 89)
print(mini)
# (3, 10.11)