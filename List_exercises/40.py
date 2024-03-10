# Write a Python program to extract specified size of strings from a give list of string values.
# Original list:
# ['Python', 'list', 'exercises', 'practice', 'solution']
# length of the string to extract:
# 8
# After extracting strings of specified length from the said list:
# ['practice', 'solution']


org_list = ['Python', 'list', 'exercises', 'practice', 'solution']

new_list = [el for el in org_list if len(el) == 8]

print(new_list) 
# ['practice', 'solution']