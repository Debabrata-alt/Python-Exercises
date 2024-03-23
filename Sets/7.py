# Write a Python program to check if a set is a subset of another set.

set1 = {"apple", "mango"}
set2 = {"mango", "orange"}
set3 = {"mango"}

# Check if 'set1' is a subset of 'set2' using both comparison operators ("<=") and issubset() method.

# 1. using "<=" operator (comparison operator)

# if 'set1' is a subset of 'set2'

print(set1 <= set2) # False

# 2. using issubset() method

print(set1.issubset(set2)) # False

#////////////////////////////////////////////////////////////

# if 'set2' is a subset of 'set3'

print(set2 <= set3) # False

print(set2.issubset(set3)) # False

#////////////////////////////////////////////////////////////

# if 'set3' is a subset of 'set2'

print(set3 <= set2) # True

print(set3.issubset(set2)) # True