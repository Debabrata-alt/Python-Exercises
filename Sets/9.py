# Write a Python program to create a shallow copy of sets.

# Note : Shallow copy is a bit-wise copy of an object. A new object is created that has an exact copy of the values in the original object.

set1 = {"Red", "Green"}

# Create a shallow copy of 'set1' and store it in 'set2'.
set2 = set1.copy()

print(set2) # {'Green', 'Red'}

#///////////////////////////////////////////////////////////

# set.copy() => shallow copy