# Write a Python program to check if a set is a superset of another set.

set1 = {"apple", "mango"}
set2 = {"mango", "orange"}
set3 = {"mango"}

# 1. Using comparison operator (">=")

# if set1 is superset of set2

print(set1 >= set2) # False

# if set2 is superset of set1

print(set2 >= set3) # True

#///////////////////////////////////////////

# 2. using issuperset() method

# if set1 is superset of set2

print(set1.issuperset(set2)) # False

# if set2 is superset of set1

print(set2.issuperset(set3)) # True