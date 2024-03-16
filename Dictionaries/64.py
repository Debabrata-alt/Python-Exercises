# Write a Python program to invert a dictionary with unique hashable values.
# Original dictionary:
# students = {'Theodore': 10, 'Mathew': 11,'Roxanne': 9}
# Sample Output:
# (swap keys and values of the dictionary)
# {10: 'Theodore', 11: 'Mathew', 9: 'Roxanne'}

students = {'Theodore': 10, 'Mathew': 11,'Roxanne': 9}

l = {value: key for key, value in students.items()}

print(l)
# {10: 'Theodore', 11: 'Mathew', 9: 'Roxanne'}