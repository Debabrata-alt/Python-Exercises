# Write a Python program to find the index of an item in a tuple.

tuplex = ('i', 'n', 'd', 'e', 'x', ' ', 't', 'u', 'p', 'l', 'e')

# Get the index of the first occurrence of the character "p" in the 'tuplex' tuple
index = tuplex.index("p")
# Print the index value
print(index) # 8

# Define the index from which you want to start searching for the character "p" (index 5)
index = tuplex.index("p", 5)
# Print the index value
print(index) # 8

# Define a segment of the 'tuplex' tuple (from index 3 to 6) within which you want to search for the character "e"
index = tuplex.index("e", 3, 6)
# Print the index value
print(index) # 3

# Attempt to find the index of the character "y," which does not exist in the 'tuplex' tuple
# This will raise a "ValueError" exception because the item is not in the tuple
index = tuplex.index("y") 
