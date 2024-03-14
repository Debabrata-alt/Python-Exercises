# Write a Python program to check if a dictionary is empty or not.

# Create an empty dictionary 'my_dict'.
my_dict = {}

# Check if the dictionary is empty by evaluating its boolean value.
# The 'bool()' function returns False for an empty dictionary, so if it's not empty, the condition is True.
if not bool(my_dict):
  # Print a message indicating that the dictionary is empty.
  print("Dictionary is empty")

# Dictionary is empty