# Write a Python program to check if two given sets have no elements in common.

x = {1, 2, 3, 4}
y = {4, 5, 6, 7}
z = {8}

# check if 'x' and 'y' have no common elements
print(x.isdisjoint(y)) # False

# check if 'x' and 'z' have no common elements
print(z.isdisjoint(x)) # True

# check if 'y' and 'z' have no common elements
print(y.isdisjoint(z)) # True