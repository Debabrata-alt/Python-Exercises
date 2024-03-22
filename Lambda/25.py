# Write a Python program to find a list with maximum and minimum length using lambda.
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])

myList = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

min_el = min(myList, key=len)

max_el = max(myList, key=len)

print(min_el) 
# [0]

print(max_el)
# [13, 15, 17]

min_length = min(len(el) for el in myList)

max_length = max(len(el) for el in myList)

print(min_length) # 1
print(max_length) # 3

#///////////////////////////////////////////////////////////////////

min_el = min(myList, key=lambda el: len(el))

max_el = max(myList, key=lambda el: len(el))

print(min_el) 
# [0]

print(max_el)
# [13, 15, 17]

#///////////////////////////////////////////////////////////////////

min_el = min(filter(lambda el: len(el), myList))

max_el = max(filter(lambda el: len(el), myList))

print(min_el)
# [0]

print(max_el)
# [13, 15, 17]