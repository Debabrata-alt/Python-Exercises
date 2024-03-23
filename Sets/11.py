# Write a Python program that uses frozensets.
# Note: Frozensets behave just like sets except they are immutable.

# Create a frozenset 'x' with elements [1, 2, 3, 4, 5].
x = frozenset([1, 2, 3, 4, 5])

# Create a frozenset 'y' with elements [3, 4, 5, 6, 7].
y = frozenset([3, 4, 5, 6, 7])

# Use the 'isdisjoint()' method to check if 'x' and 'y' have no common elements and print the result.
# Return True if the sets have no elements in common with each other.
print(x.isdisjoint(y)) # False

# Use the 'difference()' method to find the elements in 'x' that are not in 'y' and print the result.
# Return a new frozenset with elements in 'x' that are not in 'y'.
print(x.difference(y)) # frozenset({1, 2})

# Create a new frozenset with elements that are a union of 'x' and 'y' and print the result.
# This combines elements from both 'x' and 'y'.
print(x | y) 
# frozenset({1, 2, 3, 4, 5, 6, 7})
