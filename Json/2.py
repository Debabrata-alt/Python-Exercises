# Write a Python program to convert Python object to JSON data.

import json

python_obj = {
  "name": "David",
  "class":"I",
  "age": 6  
}

json_str = json.dumps(python_obj)

print(json_str)
# '{"name": "David", "class": "I", "age": 6}'