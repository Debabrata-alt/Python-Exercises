# Write a Python program to convert JSON data to Python object.

import json

json_str = '{"Name":"David", "Class":"I", "Age":6 }'

py_obj = json.loads(json_str)

print(py_obj)
# {'Name': 'David', 'Class': 'I', 'Age': 6}

print(py_obj["Name"]) # David
print(py_obj["Class"]) # I
print(py_obj["Age"]) # 6
