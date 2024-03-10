# Write a Python program to remove empty lists from a given list of lists.
# Original list:
# [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
# After deleting the empty lists from the said lists of lists
# ['Red', 'Green', [1, 2], 'Blue']

org_list = [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]

x = [el for el in org_list if el]

print(x) # ['Red', 'Green', [1, 2], 'Blue']

y = [el for el in org_list if not el]

print(y) # [[], [], [], [], []]