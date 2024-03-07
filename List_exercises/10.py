# Write a Python program to shuffle and print a specified list.

from random import shuffle

color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# Use the 'shuffle' function to randomly reorder the elements in the 'color' list
shuffle(color_list)

print(color_list)
# ['Red', 'Green', 'Black', 'Yellow', 'White', 'Pink']
