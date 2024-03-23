# Write a Python program to add member(s) to a set.

# Create an empty set
color_set = set()

# Add only one item
color_set.add("yellow")

print(color_set) # {'yellow'}

# Add multiple items
color_set.update(["black", "white"])

print(color_set) # {'yellow', 'white', 'black'}