# Write a Python program to convert a given list of strings into a list of lists using the map function.

colors = ['Red', 'Green', 'Black', 'Orange']

new_colors = map(list, colors)

print(list(new_colors))
# [['R', 'e', 'd'], ['G', 'r', 'e', 'e', 'n'], ['B', 'l', 'a', 'c', 'k'], ['O', 'r', 'a', 'n', 'g', 'e']]

