# Write a Python program to reverse strings in a given list of string values.
# Original lists:
# ['Red', 'Green', 'Blue', 'White', 'Black']
# Reverse strings of the said given list:
# ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']


org_list = ['Red', 'Green', 'Blue', 'White', 'Black']

x = [el[::-1] for el in org_list]

print(x)
# ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
