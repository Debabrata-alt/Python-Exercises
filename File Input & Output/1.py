# Write a Python program to store dictionary data in a JSON file.

# Original dictionary:
# {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}

import json

myDict = {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName': 'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'}, {'firstName': 'Regine', 'lastName': 'Agtarap'}]}


with open("demo9.txt", mode="w") as f:
  f.write(json.dumps(myDict, indent=4, sort_keys=True))


#///////////////////////////////////////////////////////////////////////////////

# json.dumps() serializes (converts) an object to a JSON formatted string.
# <sort_keys = True> helps to maintain the order of the key-value pairs in a dictionary. 
# By <sort_keys = True>, we ensure that json.dumps() will always yield the same string for the same dictionary.
# If <indent> is a non-negative integer, then JSON array elements and object members will be pretty-printed with that indent level.