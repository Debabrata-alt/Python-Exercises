# Write a Python program to find the maximum and minimum values in a given list of tuples using the lambda function.
# Original list with tuples:
# [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
# Maximum and minimum values of the said list of tuples:
# (74, 62)

myList = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]

maxi = max(myList, key=lambda el: el[1])
mini = min(myList, key=lambda el: el[1])

print(maxi)
# ('IX', 74)
print(mini)
# ('V', 62)

#///////////////////////////////////////////////////////////////////////////////////////////

myList = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]

maxi = max(map(lambda el: el[1], myList))

mini = min(map(lambda el: el[1], myList))

print(maxi)
# 74
print(mini)
# 62