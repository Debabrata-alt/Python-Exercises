# Write a Python program to sort a given list of strings(numbers) numerically.
# Original list:
# ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
# Sort the said list of strings(numbers) numerically:
# [-500, -12, 0, 4, 7, 12, 45, 100, 200]

org_list = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']

x = sorted([int(i) for i in org_list])

print(x)
# [-500, -12, 0, 4, 7, 12, 45, 100, 200]