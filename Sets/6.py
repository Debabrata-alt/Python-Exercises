# Write a Python program to create a symmetric difference.

set1 = {'blue', 'green', 'red', 'black'}
set2 = {'yellow', 'blue', 'white', 'red'}

# Keep all, but not the duplicates
set3 = set1.symmetric_difference(set2)

print(set3) # {'white', 'green', 'black', 'yellow'}

set3 = set2.symmetric_difference(set1)

print(set3) # {'white', 'green', 'black', 'yellow'}

#//////////////////////////////

set1 = {1, 1, 2, 3, 4, 5}
set2 = {1, 5, 6, 7, 8, 9}

set3 = set1.symmetric_difference(set2)

print(set3) # {2, 3, 4, 6, 7, 8, 9}

set3 = set2.symmetric_difference(set1)

print(set3) # {2, 3, 4, 6, 7, 8, 9}

#///////////////////////////////////////////////////////////////////////////////////////////

# Using symmetric difference operator(^)

set1 = {'blue', 'green', 'red', 'black'}
set2 = {'yellow', 'blue', 'white', 'red'}

# Keep all, but not the duplicates
set3 = set1 ^ set2

print(set3) # {'black', 'green', 'yellow', 'white'}

set3 = set2 ^ set1

print(set3) # {'black', 'green', 'yellow', 'white'}

#//////////////////////////////

set1 = {1, 1, 2, 3, 4, 5}
set2 = {1, 5, 6, 7, 8, 9}

set3 = set1 ^ set2

print(set3) # {2, 3, 4, 6, 7, 8, 9}

set3 = set2 ^ set1

print(set3) # {2, 3, 4, 6, 7, 8, 9}