# Write a Python program to create a union of sets.

# 1. union() method

set1 = {'green', 'blue'}
set2 = {'blue', 'yellow'}

set3 = set1.union(set2)

print(set3) # {'yellow', 'green', 'blue'}

#/////////////////////////////////////////////////

set1 = {1, 2, 3, 4, 5}
set2 = {1, 5, 6, 7, 8, 9}

set3 = set1.union(set2)

print(set3) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

#//////////////////////////////////////////////////////////////////////////////////////////

# 2. union operator '|'

set1 = {'green', 'blue'}
set2 = {'blue', 'yellow'}

# Use the union operator '|' to combine 'set1' and 'set2' into 'set3':
set3 = set1 | set2

print(set3) # {'yellow', 'blue', 'green'}

#/////////////////////////////////////////////////

set1 = {1, 2, 3, 4, 5}
set2 = {1, 5, 6, 7, 8, 9}

# Use the union operator '|' to combine 'set1' and 'set2' into 'set3':
set3 = set1 | set2

print(set3) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

#//////////////////////////////////////////////////////////////////////////////////////////

# Union of more than 2 sets:

set1 = {1, 2, 3, 4, 5}
set2 = {1, 5, 6, 7, 8, 9}
set3 = {3, 4, 5, 9, 10}
set4 = {5, 7, 9, 10, 12, 14}

setn = set1.union(set2, set3)

print(setn) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

setn1 = set1.union(set2, set3, set4)

print(setn1) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14}