# Write a Python program to remove item(s) from a given set.

# Create a set 'num_set' with the elements 0, 1, 3, 4, and 5 using a list:
num_set = set([0, 1, 3, 4, 5])

print(num_set) # {0, 1, 3, 4, 5}

# Remove and return the first element from 'num_set' using the 'pop' method:
first_element = num_set.pop()

print(first_element) # 0

print(num_set) # {1, 3, 4, 5}

# Remove an element from 'num_set' if it is present in the set:
num_set.discard(3)

print(num_set) # {1, 4, 5}