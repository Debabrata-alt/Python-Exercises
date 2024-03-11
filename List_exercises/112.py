# Write a Python program to remove all values except integer values from a given array of mixed values.
# Original list: [34.67, 12, -94.89, 'Python', 0, 'C#']
# After removing all the values except integer values from the said array of mixed values: [12, 0]

org_list = [34.67, 12, -94.89, 'Python', 0, 'C#']

x = list(el for el in org_list if isinstance(el, int))

print(x) # [12, 0]

#////////////////////////////////////////////////////////

org_list = [34.67, 12, -94.89, 'Python', 0, 'C#']

x = list(el for el in org_list if type(el) is int)

print(x) # [12, 0]