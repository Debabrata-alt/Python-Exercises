# Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
# Original arrays:
# [-1, 2, -3, 5, 7, 8, 9, -10]
# Rearrange positive and negative numbers of the said array:
# [2, 5, 7, 8, 9, -10, -3, -1]

myList = [-1, 2, -3, 5, 7, 8, 9, -10]

result = sorted(myList, key=lambda i: 0 if i == 0 else -1 / i) 

print(result)
# [2, 5, 7, 8, 9, -10, -3, -1]

#///////////////////////////////////////////////////////////////////////////////////////

myList = [-1, 2, -3, 5, 7, 8, 9, -10]

func = lambda x: sorted(x, reverse=True)

print(func(myList))
# [9, 8, 7, 5, 2, -1, -3, -10]



