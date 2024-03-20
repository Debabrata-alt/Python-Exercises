# Write a Python program to remove an empty tuple(s) from a list of tuples.
# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

myList = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

l = [el for el in myList if el]

print(l)
# [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']


x = [el for el in myList if not el]

print(x)
# [(), ()]

#////////////////////////////////////////////////////////

# NOTE:
# tuple == False means tuple is empty [tuple = ()]