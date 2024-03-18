#  Write a Python program to check if a substring appears in a given list of string values.
# Original list:
# ['red', 'black', 'white', 'green', 'orange']
# Substring to search:
# ack
# Check if a substring presents in the said list of string values:
# True
# Substring to search:
# abc
# Check if a substring presents in the said list of string values:
# False

org_list = ['red', 'black', 'white', 'green', 'orange']

x = any(el for el in org_list if "ack" in el)

y = any(el for el in org_list if "abc" in el)

print(x) # True
print(y) # False
