# Write a Python program to select an item randomly from a list.

# Import the 'random' module, which provides functions for generating random values
import random

color_list = ['Red', 'Blue', 'Green', 'White', 'Black']

# Use the 'random.choice' function to select and print a random color from the 'color_list'.

print(random.choice(color_list)) # Red

# Use the 'random.sample' function to select and print multiple random colors from the 'color_list'. Here we are printing 2 random colors.

print(random.sample(color_list, 2)) # ['Blue', 'Black']
